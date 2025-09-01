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
    <strong>HotI 2025 has concluded. All presentations are now available <a href="https://www.youtube.com/watch?v=b-ByJQDyWBU&list=PLBM5Lly_T4yRGBFgforeMTDpjasC_PV7r"> here</a>!</strong>
</div>

<br>


<div class="committee-table">
  <p> Contact us: info@hoti.org </p>
  <table>
    <thead>
      <tr>
        <th>Position</th>
        <th>Name</th>
        <th>Affiliation</th>
      </tr>
    </thead>
    <tbody>
    {% assign positions = site.data.oc | map: "position" | uniq %}
    {% for position in positions %}
      {% assign members = site.data.oc | where: "position", position %}
      {% for member in members %}
<tr>
  {% if forloop.first %}
    <td class="position" rowspan="{{ members.size }}">
      {% if member.email %}
        {{position}}<br>
        <a class="email" href="mailto:{{ member.email }}">
          {{ member.email }}
        </a>
      {% else %}
        {{ position }}
      {% endif %}
    </td>
  {% endif %}
  <td class="name">{{ member.name }}</td>
  <td class="affiliation">
    {% if member.url %}
      <a href="{{ member.url }}">{{ member.affiliation }}</a>
    {% else %}
      {{ member.affiliation }}
    {% endif %}
  </td>
</tr>




      {% endfor %}
    {% endfor %}
    </tbody>
  </table>
</div>

<span></span>

<!-- TPC Members Table -->
<div class="tpc-table">
  <table>
  <thead>
    <tr>
    <th colspan="2"> Technical Program Committee​ </th>
    </tr>
  </thead>
    <!-- <tbody> -->
      {% assign members = site.data.pc %}
      {% for member in members %}
        <!-- {% if forloop.index0 == 0 or forloop.index0 | modulo: 3 == 0 %}<tr>{% endif %} -->
        <tr>
          <td class="name">{{ member.name }}</td>
          <td class="name">{{ member.affiliation }}</td>
        </tr>
        <!-- {% if forloop.index0 | modulo: 3 == 2 or forloop.last %}</tr>{% endif %} -->
      {% endfor %}
    <!-- </tbody> -->
  </table>
</div> 

<div class="tpc-table">
  <table>
  <thead>
    <tr>
    <th colspan="2"> Steering Committee​ </th>
    </tr>
  </thead>
    <!-- <tbody> -->
      {% assign members = site.data.sc %}
      {% for member in members %}
        <!-- {% if forloop.index0 == 0 or forloop.index0 | modulo: 3 == 0 %}<tr>{% endif %} -->
        <tr>
          <td class="name">{{ member.name }}</td>
          <td class="name">{{ member.affiliation }}</td>
        </tr>
        <!-- {% if forloop.index0 | modulo: 3 == 2 or forloop.last %}</tr>{% endif %} -->
      {% endfor %}
    <!-- </tbody> -->
  </table>
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

.committee-table {
  max-width: 900px;
  margin: 0 auto;
}

.committee-table table {
  width: 100%;
  border-collapse: collapse;
  margin: 1em 0;
}

.committee-table th,
.committee-table td {
  padding: 0.5em 1em;
  text-align: left;
  border-bottom: 1px solid #ddd;
}

.committee-table th {
  font-weight: bold;
  border-bottom: 2px solid #333;
}

.committee-table .position {
  font-weight: 500;
}

.committee-table .affiliation {
  font-style: italic;
  color: #666;
}

.committee-table .position a {
  color: #2f7d95;            /* make it blue */
  text-decoration: underline;  /* force the underline */
  
  /* optional hover tweak */
  &:hover {
    opacity: 0.8;
  }
}


.committee-table a {
  color: inherit;
  text-decoration: none;
}

.committee-table a:hover {
  text-decoration: underline;
}
</style>


