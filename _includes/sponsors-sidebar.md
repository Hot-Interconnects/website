{%- for group in site.data.sponsors %}
<div class="sidebar-sponsors">
  <h3>{{ group.name }}</h3>
  {% for sponsor in group.members %}
    <div class="sponsor-group">
      {%- if sponsor.name %}
      <h4 style="margin-bottom: 5px;">{{ sponsor.name }}</h4>
      {%- endif %}
      
      <div class="sponsor-logos" style="display: flex; flex-wrap: wrap; gap: 10px; align-items: center;">
        {% for logo in sponsor.logos %}
          <a href="{{ logo.url }}" target="_blank" rel="noopener noreferrer">
            <img src="{{ logo.img | relative_url }}" alt="{{ sponsor.name }} logo" style="width: {{ logo.image_width | default: '150px' }}; max-width: 100%; height: auto; margin-bottom: 10px;">
          </a>
        {% endfor %}
      </div>
    </div>
  {% endfor %}
</div>
{% endfor %}