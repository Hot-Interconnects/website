## Archive Slack Conversations using slackdump

### 1. Install slackdump
```bash
brew install slackdump
```
Slackdump is open-source; you can also build it from source if you're not on macOS. See the [Slackdump repo](https://github.com/rusq/slackdump) for other install options.

### 2. Export the channel 
```bash
slackdump export https://hoti.slack.com/archives/C0BQ9G9ULHJ
```
Note `C0BQ9G9ULHJ` is unique to channels.   

This produces a `.zip` file containing the exported conversation.

### 3. Convert the export to HTML
```bash
python3 slack_to_html.py <exported_zip_file>.zip
```
This generates a single, self-contained `.html` file named after the channel, with the full conversation and threaded replies — ready to drop into the site. 