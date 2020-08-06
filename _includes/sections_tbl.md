| Time | Title | Presenters |
| --- | ------- | ---------- |
{%- for section in include.content %}
| {{ section.time }} | {{ section.title }} | {{ section.presenters }}{% if section.presenters and section.affiliation %}, {% endif %}{{ section.affiliation }} |
  {%- if section.subsections %}
      {%- for talk in section.subsections %}
| | {{ talk.title }}
        {%- if include.showpdf == true and talk.pdf -%}
[{{ site.icons.pdf-file }}](/assets/program/{{ include.progtype }}/{{ talk.pdf }})
        {%- endif -%}
        {%- if include.showvid == true and talk.video -%}
[{{ site.icons.video-file }}]({{ talk.video }})
        {%- endif -%}
        {%- if talk.slack -%}
[{{ site.icons.slack }}]({{ talk.slack }})
        {%- endif -%}
| {{ talk.presenters }}{% if talk.presenters and talk.affiliation %}, {% endif %}{{talk.affiliation }} |
      {%- endfor %}
  {%- endif %}
{%- endfor %}
