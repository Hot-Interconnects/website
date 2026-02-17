{%- for group in site.data.sponsors %}
<div class="sidebar-sponsors">
  <h3>{{ group.name }}</h3>
  {% for sponsor in group.members %}
    <div class="sponsor-group">
      {%- if sponsor.name %}
      <h4 style="margin-bottom: 5px;">{{ sponsor.name }}{% if sponsor.total_slots %} <span style="font-size: 0.75em; font-weight: normal; color: #999;">({{ sponsor.total_slots }} slots)</span>{% endif %}</h4>
      {%- endif %}
      
      <div class="sponsor-logos" style="display: flex; flex-wrap: wrap; gap: 10px; align-items: center;">
        {% for logo in sponsor.logos %}
          <a href="{{ logo.url }}" target="_blank" rel="noopener noreferrer">
            <img src="{{ logo.img | relative_url }}" alt="{{ sponsor.name }} logo" style="width: {{ logo.image_width | default: '150px' }}; max-width: 100%; height: auto; margin-bottom: 10px;">
          </a>
        {% endfor %}
        {% if sponsor.available_slots %}
          {% if sponsor.name == "Diamond" %}{% assign slot_logo_width = "130px" %}{% elsif sponsor.name == "Platinum" %}{% assign slot_logo_width = "105px" %}{% else %}{% assign slot_logo_width = "85px" %}{% endif %}
          {% for i in (1..sponsor.available_slots) %}
            <a href="sponsors.html" title="Available {{ sponsor.name }} slot – become a sponsor!" style="text-decoration: none;">
              <img src="{{ '/assets/img/hoti_logo.png' | relative_url }}" alt="Available slot" style="width: {{ slot_logo_width }}; max-width: 100%; height: auto; margin-bottom: 10px; opacity: 0.15; filter: grayscale(100%);">
            </a>
          {% endfor %}
        {% endif %}
      </div>
    </div>
  {% endfor %}
</div>
{% endfor %}