---
# title: Archive
---
## HOTI Archive

<ul>
{% for year in site.data.archive %}
<li>{{ year.name }} | <a href="{{ year.ieee_url }}">IEEE Digital Library</a> | <a href="{{ year.website_url }}">Website</a></li>
{%- endfor %}
</ul>