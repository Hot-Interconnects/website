---
# title: Committees
---
<!-- <div style="max-width: 850px; margin: 0 auto; text-align: center">
  <div style="text-align: center; font-size: 30px">
    <a href="attendee_instructions.html" style="color:white; background-color: red">Click here to REGISTER or JOIN the event!</a><br><br>
  </div>
</div> -->


<br>

<div style="text-align: center; font-size: 30px">
    <strong>HotI 2025 has concluded. Watch the recordings of all HotI 2025 sessions and talks on <a href="https://www.youtube.com/watch?v=b-ByJQDyWBU&list=PLBM5Lly_T4yRGBFgforeMTDpjasC_PV7r"> YouTube</a>!</strong>
    <a href="https://www.youtube.com/watch?v=b-ByJQDyWBU&list=PLBM5Lly_T4yRGBFgforeMTDpjasC_PV7r" target="_blank"> <img src="{{ '/assets/img/logo_youtube.png' | relative_url }}" alt="YouTube Logo" style="width: 50px; height: auto; vertical-align: middle;"></a>
</div>

<br>


<div class="oc-container">
  <p style="text-align: center; margin-bottom: 20px;"> Contact us: <a href="mailto:info@hoti.org">info@hoti.org</a> </p>
  
  {% assign positions = site.data.oc | map: "position" | uniq %}
  {% for position in positions %}
    <!-- Position Header -->
    {% assign members = site.data.oc | where: "position", position %}
    {% assign group_email = members.first.email %}
    
    <div class="position-header">
      <span class="header-line"></span>
      <div class="position-info">
        <span class="position-title">{{ position }}</span>
        {% if group_email %}
          <a class="position-email" href="mailto:{{ group_email }}">{{ group_email }}</a>
        {% endif %}
      </div>
      <span class="header-line"></span>
    </div>

    <!-- Members Grid -->
    <div class="members-grid">
      {% for member in members %}
        <div class="member-card">
          <div class="member-photo">
            <img src="{{ member.image | default: '/assets/img/headshot_placeholder.png' | relative_url }}" alt="{{ member.name }}">
          </div>
          <div class="member-details">
            <div class="member-name">{{ member.name }}</div>
            <div class="member-affiliation">
              {% if member.url %}
                <a href="{{ member.url }}">{{ member.affiliation }}</a>
              {% else %}
                {{ member.affiliation }}
              {% endif %}
            </div>
          </div>
        </div>
      {% endfor %}
    </div>
  {% endfor %}
</div>

<span></span>

<!-- TPC Members Table -->
<!-- <div class="tpc-table">
  <table>
  <thead>
    <tr>
    <th colspan="2"> Technical Program Committee​ </th>
    </tr>
  </thead>
      {% assign members = site.data.pc %}
      {% for member in members %}
        <tr>
          <td class="name">{{ member.name }}</td>
          <td class="name">{{ member.affiliation }}</td>
        </tr>
      {% endfor %}
  </table>
</div>  -->

<div class="oc-container">
  <div class="position-header">
    <span class="header-line"></span>
    <div class="position-info">
      <span class="position-title">Steering Committee</span>
    </div>
    <span class="header-line"></span>
  </div>

  <div class="members-grid">
    {% assign members = site.data.sc %}
    {% for member in members %}
      <div class="member-card">
        <div class="member-details">
          <div class="member-name">{{ member.name }}</div>
          <div class="member-affiliation">
            {% if member.url %}
              <a href="{{ member.url }}">{{ member.affiliation }}</a>
            {% else %}
              {{ member.affiliation }}
            {% endif %}
          </div>
        </div>
      </div>
    {% endfor %}
  </div>
</div> 

<style>
/* .tpc-table table {
  width: 100%;
  border-collapse: collapse;
  margin: 1em 0;
  text-align: center;
} */
.tpc-table {
  max-width: 900px;
  margin: 0 auto;
}

.tpc-table table {
  width: 100%;
  border-collapse: collapse;
  margin: 1em 0;
}

.tpc-table th {
  background-color: #f2f2f2;
  font-weight: bold;
  padding: 0.5em;
  text-align: center;
}

.tpc-table td {
  width: 50.00%; /* Two columns per row */
  text-align: left;
  padding: 0.5em;
  border-bottom: 1px solid #ddd;
}

.tpc-table h2 {
  text-align: left;
}
</style>



<style>
.oc-container {
  max-width: 900px;
  margin: 0 auto;
}

.position-header {
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 2em 0 1em 0;
}

.header-line {
  flex-grow: 1;
  height: 2px;
  background-color: #ddd;
}

.position-info {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin: 0 1em; /* Space between text/email block and lines */
}

.position-title {
  padding: 0.3em 0.8em;
  background-color: #f2f2f2; /* Gray highlight as requested */
  font-weight: bold;
  font-size: 1.2em;
  color: #333;
  border-radius: 4px;
  white-space: nowrap;
}

.position-email {
  margin-top: 5px;
  font-size: 0.9em;
  color: #2f7d95;
  text-decoration: none;
}

.position-email:hover {
  text-decoration: underline;
}

.members-grid {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 30px;
  margin-bottom: 2em;
}

.member-card {
  width: 220px;
  text-align: center;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.member-photo img {
  width: 150px;
  height: 150px;
  border-radius: 4px; /* Slightly rounded corners */
  object-fit: cover;
  margin-bottom: 15px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
  border: 1px solid #eee;
}

.member-name {
  font-weight: 700;
  font-size: 1.1em;
  margin-bottom: 4px;
}

.member-affiliation {
  font-style: italic;
  font-size: 0.95em;
  color: #666;
  line-height: 1.3;
}

.member-email {
  margin-top: 6px;
  font-size: 0.85em;
}

.oc-container a {
  color: inherit;
  text-decoration: none;
}

.oc-container a:hover {
  text-decoration: underline;
}
</style>



