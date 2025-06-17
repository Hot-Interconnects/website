{%- for outer_group in site.data.sponsors %}
<div style="text-align: center;"><strong>{{ outer_group.name }}</strong></div>
{% for sponsor_tier in outer_group.members %}
<div style="text-align: center;">
  <span style="font-size: 18px;"><strong>{{ sponsor_tier.name }}</strong></span>
  <div class="logo-list-container" style="line-height: 0;">
    {% for logo_item in sponsor_tier.logos %}
    {%- assign current_logo_margin = logo_item.custom_spacing | default: "3px 0" -%}
    <a href="{{ logo_item.url }}" target="_blank" rel="noopener noreferrer" style="display: inline-block; 
                                margin: {{ current_logo_margin }}; 
                                text-decoration: none;">
      <img src="{{ logo_item.img | relative_url }}"
        alt="{{ sponsor_tier.name }} Sponsor Logo: {{ logo_item.url | split: '//' | last | split: '/' | first }}"
        width="{{ logo_item.image_width | default: '120px' }}" style="vertical-align: middle; border: none; ">
    </a>
    {% endfor %}
  </div>
</div>
{% endfor %}

&nbsp;
{% endfor %}