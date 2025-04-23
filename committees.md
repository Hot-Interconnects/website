---
# title: Committees
---


<div class="committee-table">
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
          <td class="position" rowspan="{{ members.size }}">{{ position }}</td>
          {% endif %}
          <td class="name">
            {% if member.email %}
              <a href="mailto:{{ member.email }}">{{ member.name }}</a>
            {% else %}
              {{ member.name }}
            {% endif %}
          </td>
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

.committee-table a {
  color: inherit;
  text-decoration: none;
}

.committee-table a:hover {
  text-decoration: underline;
}
</style>


