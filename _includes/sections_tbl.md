| Time | Title | Presenters |
| --- | ------- | ---------- |
{%- for section in include.content %}
| {{ section.time }} | {{ section.title }} {% if section.abstract %} <br><br> **Abstract**: {{section.abstract}} {% endif %} | {% for presenter in section.presenters %} {{ presenter.name }} {{ presenter.affiliation }} {% if presenter.logo %} ({{ presenter.logo }}) {% endif %} {% endfor %} |
  {%- if section.subsections %}
      {%- for talk in section.subsections %}
| | {{ talk.title }}
        {%- if include.showpdf == true and talk.pdf -%}
[{{ site.data.icons.pdf-file }}](/assets/program/{{ include.progtype }}/{{ talk.pdf }})
        {%- endif -%}
        {%- if include.showvid == true and talk.video -%}
[{{ site.data.icons.video-file }}]({{ talk.video }})
        {%- endif -%}
        {%- if talk.slack -%}
[{{ site.data.icons.slack }}]({{ talk.slack }})
        {%- endif -%}
|{% for presenter in talk.presenters %} {{ presenter.name }} ({{presenter.affiliation }}),{% endfor %} |
      {%- endfor %}
  {%- endif %}
{%- endfor %}
