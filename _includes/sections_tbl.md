| Time | Title | Presenters |
| --- | ------- | ---------- |
{%- for section in include.content %}
| {{ section.time }} | {{ section.title }} | {{ section.presenters }}{% if section.affiliation %}, {% endif %}{{ section.affiliation }} |
  {%- if section.subsections %}
      {%- for talk in section.subsections %}
| | {{ talk.title }}
{%- if include.showpdf == true and talk.pdf -%}
[<i class="fa fa-file-pdf fa-fw" aria-hidden="true"></i>](/assets/program/{{ include.progtype }}/{{ talk.pdf }})
{%- endif -%}
{%- if include.showvid == true and talk.video -%}
[<i class="fas fa-video" aria-hidden="true"></i>]({{ talk.video }})
{%- endif -%}
{%- if talk.slack -%}
[<i class="fab fa-slack fa-fw" aria-hidden="true"></i>]({{ talk.slack }})
{%- endif -%}
| {% if talk.presenters %} {{ talk.presenters }}, {{talk.affiliation }} {% endif %} |
      {%- endfor %}
  {%- endif %}
{%- endfor %}
