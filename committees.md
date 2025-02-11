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


