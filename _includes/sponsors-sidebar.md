{%- for group in site.data.sponsors %}
**{{ group.name }}**  
{% for sponsor in group.members %}
{%- if group.text_only %}
<div style="text-align: left; font-size: 16px; color: darkred;">{{ sponsor.name }} {{ sponsor.text }}</div>
{%- elsif group.image_only %}
[![{{ sponsor.name }} logo]({{ sponsor.logo }}){: width="{{ group.image_width | default: '200px' }}"}]({{ sponsor.url }})
{%- else %}
<span style="font-size: 16px;">**{{ sponsor.name }}**</span>
{% for logo in sponsor.logos %}
![{{ sponsor.name }} logo]({{ logo }}){: width="{{ sponsor.image_width | default: '200px' }}"} 
{% endfor %}
{%- endif %}
{%- endfor %}

&nbsp;

{% endfor %}