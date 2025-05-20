{%- for group in site.data.sponsors %}
<div style="text-align: center;"><strong>{{ group.name }}</strong></div>
{% for sponsor in group.members %}
{%- if group.text_only %}
<div style="text-align: center; font-size: 16px; color: darkred;">{{ sponsor.name }} {{ sponsor.text }}</div>
{%- elsif group.image_only %}
<p style="text-align: center;">
  <a href="{{ sponsor.url }}">
    <img src="{{ sponsor.logo }}" alt="{{ sponsor.name }} logo" width="{{ group.image_width | default: '200px' }}">
  </a>
</p>
{%- else %}
<div style="text-align: center;">
  <span style="font-size: 16px;"><strong>{{ sponsor.name }}</strong></span>
  {% for logo in sponsor.logos %}
  <p style="text-align: center;">
    <a href="{{ logo.url }}">
      <img src="{{ logo.img }}" alt="{{ sponsor.name }} logo" width="{{ logo.image_width | sponsor.image_width | group.image_width ｜ default: '100px' }}">
    </a>
  </p>
  {% endfor %}
</div>
{%- endif %}
{%- endfor %}

&nbsp;

{% endfor %}