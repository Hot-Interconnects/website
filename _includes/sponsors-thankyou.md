## Thank You Sponsors!

{%- for group in site.data.sponsors %}
{%- for sponsor in group.members %}
![{{ sponsor.name }} logo]({{ sponsor.logo }})
{%- endfor %}
{%- endfor %}
