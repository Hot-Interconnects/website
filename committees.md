---
title: Committees
---

## Organizing Committee

| Position | Name | Affiliation |
| -------- | ---- | ----------- |
{%- for member in site.data.oc %}
| {% if member.email %}[{{ member.position }}](mailto:{{ member.email }}){% else %}{{ member.position }}{% endif %} | {{ member.name }} | 
{%- if member.url %}[_{{ member.affiliation }}_]({{ member.url }}){% else %}{{ member.affiliation }}{% endif %} |
{%- endfor %}

{% comment %}
## Program Committee

| Name | Affiliation |
| ---- | ----------- |
{%- for member in site.data.pc %}
| {{ member.name }} | [_{{ member.affiliation }}_]({{ member.url }}) |
{%- endfor %}
{% endcomment %}
