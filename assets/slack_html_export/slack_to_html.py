#!/usr/bin/env python3
"""
slack_to_html.py

Reads a Slack export ZIP (the format produced by Slackdump's `export` command,
or Slack's own official export) and renders one static, self-contained HTML
file per channel found inside it. Images that were captured in the export's
`__uploads/` folder are embedded as base64 data URIs, so the resulting HTML
needs no external files and can be dropped straight into a Jekyll site
(e.g. under `_pages/` or linked to from a post).

Usage:
    python3 slack_to_html.py path/to/export.zip -o output_dir

If -o is omitted, files are written to ./slack_html_export/
"""

import argparse
import base64
import html
import json
import mimetypes
import re
import sys
import zipfile
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from tempfile import TemporaryDirectory

# Files/dirs in a Slack export that are metadata, not channel message folders.
NON_CHANNEL_FILES = {
    "channels.json", "groups.json", "mpims.json", "dms.json",
    "users.json", "integration_logs.json",
}
NON_CHANNEL_DIRS = {"__uploads"}

# A small mapping from common :emoji_shortcode: names to unicode, used both
# for reactions and for inline ":shortcode:" text in messages. Unrecognised
# shortcodes are left as ":name:" rather than guessed at.
EMOJI_MAP = {
    "+1": "\U0001F44D", "thumbsup": "\U0001F44D",
    "-1": "\U0001F44E", "thumbsdown": "\U0001F44E",
    "smile": "\U0001F604", "smiley": "\U0001F603", "grinning": "\U0001F600",
    "joy": "\U0001F602", "laughing": "\U0001F606",
    "heart": "\u2764\uFE0F", "heart_eyes": "\U0001F60D",
    "clap": "\U0001F44F", "raised_hands": "\U0001F64C",
    "pray": "\U0001F64F", "wave": "\U0001F44B",
    "white_check_mark": "\u2705", "heavy_check_mark": "\u2714\uFE0F",
    "eyes": "\U0001F440", "fire": "\U0001F525", "tada": "\U0001F389",
    "rocket": "\U0001F680", "thinking_face": "\U0001F914",
    "slightly_smiling_face": "\U0001F642", "wink": "\U0001F609",
    "100": "\U0001F4AF",
}


def emoji(name: str) -> str:
    return EMOJI_MAP.get(name, f":{name}:")


# ---------------------------------------------------------------------------
# mrkdwn (Slack's markdown-ish format) -> HTML
# ---------------------------------------------------------------------------

def render_mrkdwn(text: str, users: dict, channels: dict) -> str:
    if not text:
        return ""

    text = html.escape(text, quote=False)

    # Code blocks first, so nothing inside them gets touched further.
    code_blocks = []

    def stash_code_block(m):
        code_blocks.append(m.group(1))
        return f"\x00CODEBLOCK{len(code_blocks) - 1}\x00"

    text = re.sub(r"```(.+?)```", stash_code_block, text, flags=re.DOTALL)

    inline_code = []

    def stash_inline_code(m):
        inline_code.append(m.group(1))
        return f"\x00INLINECODE{len(inline_code) - 1}\x00"

    text = re.sub(r"`([^`\n]+?)`", stash_inline_code, text)

    # User mentions: <@U12345> or <@U12345|displayname>
    def user_mention(m):
        uid = m.group(1)
        label = users.get(uid, uid)
        return f'<span class="mention">@{html.escape(label)}</span>'

    text = re.sub(r"&lt;@([A-Z0-9]+)(?:\|[^&]*)?&gt;", user_mention, text)

    # Channel mentions: <#C12345|name> or <#C12345>
    def channel_mention(m):
        cid, name = m.group(1), m.group(2)
        label = name or channels.get(cid, cid)
        return f'<span class="mention">#{html.escape(label)}</span>'

    text = re.sub(r"&lt;#([A-Z0-9]+)(?:\|([^&]*))?&gt;", channel_mention, text)

    # Special mentions like <!here>, <!channel>, <!everyone>
    text = re.sub(
        r"&lt;!(here|channel|everyone)&gt;",
        lambda m: f'<span class="mention">@{m.group(1)}</span>',
        text,
    )

    # Links: <http://foo|label> or <http://foo>
    def link(m):
        url, label = m.group(1), m.group(2)
        display = label if label else url
        return f'<a href="{html.escape(url)}" target="_blank" rel="noopener">{html.escape(display)}</a>'

    text = re.sub(r"&lt;(https?://[^|&]+)(?:\|([^&]*))?&gt;", link, text)

    # Bold: *text*
    text = re.sub(r"(?<!\w)\*([^\*\n]+?)\*(?!\w)", r"<strong>\1</strong>", text)
    # Italic: _text_
    text = re.sub(r"(?<!\w)_([^_\n]+?)_(?!\w)", r"<em>\1</em>", text)
    # Strikethrough: ~text~
    text = re.sub(r"(?<!\w)~([^~\n]+?)~(?!\w)", r"<del>\1</del>", text)

    # Emoji shortcodes :name:
    text = re.sub(r":([a-zA-Z0-9_+\-]+):", lambda m: emoji(m.group(1)), text)

    # Blockquotes: lines starting with &gt;
    lines = text.split("\n")
    out_lines = []
    for line in lines:
        if line.startswith("&gt; "):
            out_lines.append(f"<blockquote>{line[5:]}</blockquote>")
        elif line.startswith("&gt;"):
            out_lines.append(f"<blockquote>{line[4:]}</blockquote>")
        else:
            out_lines.append(line)
    text = "<br>\n".join(out_lines)

    # Restore stashed code
    for i, code in enumerate(inline_code):
        text = text.replace(f"\x00INLINECODE{i}\x00", f"<code>{code}</code>")
    for i, code in enumerate(code_blocks):
        text = text.replace(f"\x00CODEBLOCK{i}\x00", f"<pre><code>{code.strip()}</code></pre>")

    return text


# ---------------------------------------------------------------------------
# Data loading
# ---------------------------------------------------------------------------

def load_users(root: Path) -> dict:
    """id -> best display name"""
    users_file = root / "users.json"
    mapping = {}
    if users_file.exists():
        data = json.loads(users_file.read_text(encoding="utf-8"))
        for u in data:
            profile = u.get("profile", {}) or {}
            name = (
                profile.get("display_name")
                or profile.get("real_name")
                or u.get("real_name")
                or u.get("name")
                or u.get("id")
            )
            mapping[u["id"]] = name
    return mapping


def load_channels(root: Path) -> dict:
    """id -> channel name, across channels/groups/mpims/dms"""
    mapping = {}
    for fname in ("channels.json", "groups.json", "mpims.json"):
        f = root / fname
        if f.exists():
            try:
                data = json.loads(f.read_text(encoding="utf-8"))
            except json.JSONDecodeError:
                continue
            for c in data:
                mapping[c["id"]] = c.get("name") or c.get("name_normalized") or c["id"]
    return mapping


def find_channel_dirs(root: Path) -> list:
    dirs = []
    for p in sorted(root.iterdir()):
        if p.is_dir() and p.name not in NON_CHANNEL_DIRS:
            if list(p.glob("*.json")):
                dirs.append(p)
    return dirs


def load_channel_messages(channel_dir: Path) -> list:
    messages = []
    for day_file in sorted(channel_dir.glob("*.json")):
        try:
            data = json.loads(day_file.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            continue
        messages.extend(data)
    messages.sort(key=lambda m: float(m.get("ts", 0)))
    return messages


def build_uploads_index(root: Path) -> dict:
    """file id -> local path, for embedding as base64"""
    idx = {}
    uploads_dir = root / "__uploads"
    if uploads_dir.exists():
        for sub in uploads_dir.iterdir():
            if sub.is_dir():
                for f in sub.iterdir():
                    if f.is_file():
                        idx[sub.name] = f
    return idx


def file_to_data_uri(path: Path) -> str:
    mime, _ = mimetypes.guess_type(str(path))
    mime = mime or "application/octet-stream"
    data = base64.b64encode(path.read_bytes()).decode("ascii")
    return f"data:{mime};base64,{data}"


# ---------------------------------------------------------------------------
# Threading
# ---------------------------------------------------------------------------

def organize_threads(messages: list) -> list:
    """
    Returns a list of top-level entries in chronological order, each either
    a plain message dict, or a dict augmented with a "_replies" list of
    reply message dicts (also chronological).
    """
    by_ts = {m["ts"]: m for m in messages if "ts" in m}
    replies_by_parent = defaultdict(list)
    top_level = []

    for m in messages:
        ts = m.get("ts")
        thread_ts = m.get("thread_ts")
        if thread_ts and thread_ts != ts:
            replies_by_parent[thread_ts].append(m)
        else:
            top_level.append(m)

    # Attach replies; if a reply's parent ts isn't in top_level (edge case
    # where the parent fell outside the exported date range), promote the
    # reply to top-level so nothing is silently dropped.
    top_level_ts = {m.get("ts") for m in top_level}
    for parent_ts, replies in replies_by_parent.items():
        if parent_ts in top_level_ts:
            for m in top_level:
                if m.get("ts") == parent_ts:
                    m["_replies"] = sorted(replies, key=lambda r: float(r["ts"]))
                    break
        else:
            top_level.extend(replies)

    top_level.sort(key=lambda m: float(m.get("ts", 0)))
    return top_level


# ---------------------------------------------------------------------------
# Rendering
# ---------------------------------------------------------------------------

PAGE_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<style>
  :root {{
    --bg: #ffffff;
    --text: #1d1c1d;
    --muted: #616061;
    --border: #e8e8e8;
    --mention-bg: #e8f5fa;
    --mention-text: #1264a3;
    --code-bg: #f6f6f6;
    --thread-border: #dddddd;
  }}
  * {{ box-sizing: border-box; }}
  body {{
    margin: 0;
    padding: 2rem 1rem 4rem;
    background: var(--bg);
    color: var(--text);
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
    font-size: 15px;
    line-height: 1.46668;
  }}
  .archive-header {{
    max-width: 760px;
    margin: 0 auto 2rem;
    padding-bottom: 1rem;
    border-bottom: 2px solid var(--border);
  }}
  .archive-header h1 {{
    margin: 0 0 0.25rem;
    font-size: 1.6rem;
  }}
  .archive-header .meta {{
    color: var(--muted);
    font-size: 0.9rem;
  }}
  .conversation {{
    max-width: 760px;
    margin: 0 auto;
  }}
  .message {{
    display: flex;
    gap: 0.75rem;
    padding: 0.35rem 0.5rem;
    border-radius: 6px;
  }}
  .message:hover {{
    background: #f8f8f8;
  }}
  .avatar {{
    flex: 0 0 auto;
    width: 36px;
    height: 36px;
    border-radius: 6px;
    background: #ccc;
    display: flex;
    align-items: center;
    justify-content: center;
    color: white;
    font-weight: 700;
    font-size: 0.95rem;
  }}
  .msg-body {{
    flex: 1 1 auto;
    min-width: 0;
  }}
  .msg-header {{
    display: flex;
    align-items: baseline;
    gap: 0.5rem;
    flex-wrap: wrap;
  }}
  .username {{
    font-weight: 900;
  }}
  .timestamp {{
    color: var(--muted);
    font-size: 0.75rem;
  }}
  .msg-text {{
    white-space: normal;
    word-wrap: break-word;
  }}
  .msg-text pre {{
    background: var(--code-bg);
    padding: 0.5rem;
    border-radius: 4px;
    overflow-x: auto;
  }}
  .msg-text code {{
    background: var(--code-bg);
    padding: 0.1rem 0.3rem;
    border-radius: 3px;
    font-family: SFMono-Regular, Consolas, "Liberation Mono", Menlo, monospace;
    font-size: 0.9em;
  }}
  .msg-text blockquote {{
    margin: 0.25rem 0;
    padding-left: 0.75rem;
    border-left: 3px solid #ddd;
    color: var(--muted);
  }}
  .mention {{
    background: var(--mention-bg);
    color: var(--mention-text);
    padding: 0 0.2rem;
    border-radius: 3px;
    font-weight: 600;
  }}
  .system-message {{
    color: var(--muted);
    font-size: 0.85rem;
    font-style: italic;
    padding: 0.25rem 0.5rem 0.25rem 3.25rem;
  }}
  .attachment img {{
    max-width: 100%;
    max-height: 400px;
    border-radius: 6px;
    margin-top: 0.4rem;
    border: 1px solid var(--border);
    display: block;
  }}
  .reactions {{
    margin-top: 0.35rem;
    display: flex;
    gap: 0.35rem;
    flex-wrap: wrap;
  }}
  .reaction {{
    background: #eef7fb;
    border: 1px solid #cfe6f2;
    border-radius: 12px;
    padding: 0.05rem 0.5rem;
    font-size: 0.85rem;
  }}
  .thread {{
    margin: 0.5rem 0 0.25rem 1.5rem;
    padding-left: 0.75rem;
    border-left: 3px solid var(--thread-border);
  }}
  .thread-label {{
    color: var(--muted);
    font-size: 0.8rem;
    font-weight: 600;
    margin-bottom: 0.25rem;
  }}
  hr.day-divider {{
    max-width: 760px;
    margin: 1.75rem auto;
    border: none;
    border-top: 1px solid var(--border);
    position: relative;
  }}
  .day-label {{
    max-width: 760px;
    margin: 1.75rem auto 0.5rem;
    text-align: center;
    color: var(--muted);
    font-size: 0.8rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.03em;
  }}
</style>
</head>
<body>
<div class="archive-header">
  <h1>{title}</h1>
  <div class="meta">{subtitle}</div>
</div>
<div class="conversation">
{body}
</div>
</body>
</html>
"""

AVATAR_COLORS = [
    "#7C3AED", "#DB2777", "#DC2626", "#D97706", "#059669",
    "#0891B2", "#2563EB", "#4F46E5", "#65A30D", "#C026D3",
]


def color_for(uid: str) -> str:
    if not uid:
        return "#999999"
    return AVATAR_COLORS[sum(map(ord, uid)) % len(AVATAR_COLORS)]


def format_ts(ts: str, with_date=False) -> str:
    try:
        dt = datetime.fromtimestamp(float(ts))
    except (ValueError, TypeError):
        return ""
    if with_date:
        return dt.strftime("%b %-d, %Y %-I:%M %p") if hasattr(dt, "strftime") else str(dt)
    return dt.strftime("%-I:%M %p")


def day_key(ts: str) -> str:
    try:
        return datetime.fromtimestamp(float(ts)).strftime("%Y-%m-%d")
    except (ValueError, TypeError):
        return ""


def day_label(ts: str) -> str:
    try:
        return datetime.fromtimestamp(float(ts)).strftime("%A, %B %-d, %Y")
    except (ValueError, TypeError):
        return ""


def render_attachments(msg: dict, uploads_index: dict) -> str:
    out = []
    for f in msg.get("files", []) or []:
        fid = f.get("id")
        name = html.escape(f.get("name") or "attachment")
        mimetype = f.get("mimetype", "")
        local_path = uploads_index.get(fid)
        if local_path and mimetype.startswith("image/"):
            try:
                uri = file_to_data_uri(local_path)
                out.append(f'<div class="attachment"><img src="{uri}" alt="{name}"></div>')
                continue
            except OSError:
                pass
        # Fallback: link out to whatever URL the export recorded.
        url = f.get("url_private") or f.get("permalink") or "#"
        out.append(f'<div class="attachment"><a href="{html.escape(url)}" target="_blank">{name}</a></div>')
    return "\n".join(out)


def render_reactions(msg: dict) -> str:
    reactions = msg.get("reactions") or []
    if not reactions:
        return ""
    items = "".join(
        f'<span class="reaction">{emoji(r["name"])} {r.get("count", len(r.get("users", [])))}</span>'
        for r in reactions
    )
    return f'<div class="reactions">{items}</div>'


def render_message(msg: dict, users: dict, channels: dict, uploads_index: dict, show_avatar=True) -> str:
    uid = msg.get("user") or msg.get("bot_id") or ""
    name = users.get(uid, msg.get("username") or uid or "Unknown")
    initial = (name[:1] or "?").upper()
    ts = msg.get("ts", "0")
    time_str = format_ts(ts)
    text_html = render_mrkdwn(msg.get("text", ""), users, channels)
    attachments_html = render_attachments(msg, uploads_index)
    reactions_html = render_reactions(msg)

    avatar_html = (
        f'<div class="avatar" style="background:{color_for(uid)}">{html.escape(initial)}</div>'
        if show_avatar else '<div class="avatar" style="visibility:hidden"></div>'
    )

    return f"""<div class="message">
  {avatar_html}
  <div class="msg-body">
    <div class="msg-header">
      <span class="username">{html.escape(name)}</span>
      <span class="timestamp">{time_str}</span>
    </div>
    <div class="msg-text">{text_html}</div>
    {attachments_html}
    {reactions_html}
  </div>
</div>"""


def render_system_message(msg: dict, users: dict) -> str:
    uid = msg.get("user", "")
    name = users.get(uid, uid)
    subtype = msg.get("subtype", "")
    if subtype == "channel_join":
        text = f"{name} joined the channel"
    elif subtype == "channel_leave":
        text = f"{name} left the channel"
    elif subtype == "channel_name":
        old = msg.get("old_name", "")
        new = msg.get("name", "")
        text = f"{name} renamed the channel from \"{old}\" to \"{new}\""
    elif subtype == "channel_topic":
        text = f"{name} set the channel topic to: {msg.get('topic', '')}"
    elif subtype == "channel_purpose":
        text = f"{name} set the channel purpose to: {msg.get('purpose', '')}"
    else:
        text = msg.get("text", "") or subtype
    return f'<div class="system-message">{html.escape(text)}</div>'


SYSTEM_SUBTYPES = {
    "channel_join", "channel_leave", "channel_name",
    "channel_topic", "channel_purpose", "channel_archive", "channel_unarchive",
}


def render_channel(channel_name: str, messages: list, users: dict, channels: dict, uploads_index: dict) -> str:
    top_level = organize_threads(messages)
    body_parts = []
    current_day = None

    for msg in top_level:
        ts = msg.get("ts", "0")
        d = day_key(ts)
        if d != current_day:
            body_parts.append(f'<div class="day-label">{day_label(ts)}</div><hr class="day-divider">')
            current_day = d

        subtype = msg.get("subtype")
        if subtype in SYSTEM_SUBTYPES:
            body_parts.append(render_system_message(msg, users))
            continue

        body_parts.append(render_message(msg, users, channels, uploads_index))

        replies = msg.get("_replies", [])
        if replies:
            thread_html = [f'<div class="thread"><div class="thread-label">{len(replies)} repl{"y" if len(replies) == 1 else "ies"}</div>']
            for r in replies:
                thread_html.append(render_message(r, users, channels, uploads_index, show_avatar=True))
            thread_html.append("</div>")
            body_parts.append("\n".join(thread_html))

    body = "\n".join(body_parts)
    first_ts = messages[0]["ts"] if messages else None
    last_ts = messages[-1]["ts"] if messages else None
    subtitle = ""
    if first_ts and last_ts:
        subtitle = f"Archived conversation &middot; {format_ts(first_ts, with_date=True)} &ndash; {format_ts(last_ts, with_date=True)} &middot; {len(messages)} messages"

    return PAGE_TEMPLATE.format(
        title=html.escape(channel_name),
        subtitle=subtitle,
        body=body,
    )


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Convert a Slack export ZIP to static HTML.")
    parser.add_argument("zip_path", help="Path to the Slackdump/Slack export .zip file")
    parser.add_argument("-o", "--output-dir", default="slack_html_export",
                         help="Directory to write the HTML file(s) into (default: ./slack_html_export)")
    args = parser.parse_args()

    zip_path = Path(args.zip_path)
    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    with TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)
        with zipfile.ZipFile(zip_path) as zf:
            zf.extractall(tmp_path)

        users = load_users(tmp_path)
        channels = load_channels(tmp_path)
        uploads_index = build_uploads_index(tmp_path)

        channel_dirs = find_channel_dirs(tmp_path)
        if not channel_dirs:
            print("No channel message folders found in this export.", file=sys.stderr)
            sys.exit(1)

        for channel_dir in channel_dirs:
            messages = load_channel_messages(channel_dir)
            if not messages:
                continue
            channel_name = channels.get(channel_dir.name, channel_dir.name)
            html_out = render_channel(channel_name, messages, users, channels, uploads_index)
            out_file = out_dir / f"{channel_dir.name}.html"
            out_file.write_text(html_out, encoding="utf-8")
            print(f"Wrote {out_file} ({len(messages)} messages)")


if __name__ == "__main__":
    main()
