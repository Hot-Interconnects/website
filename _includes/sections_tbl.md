| Time | Title | Presenters |
| --- | ------- | ---------- |
{%- for section in include.content %}
| {{ section.time }} | {{ section.title }} | {% for presenter in section.presenters %} {{ presenter.name }}, {{ presenter.affiliation }} {% endfor %} |
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
|{% for presenter in talk.presenters %} {{ presenter.name }} ({{presenter.affiliation }}),{% endfor %} |
      {%- endfor %}
  {%- endif %}
{%- endfor %}
