---
# title: Home
---
<br>

<div style="max-width: 850px; margin: 0 auto; text-align: center">
    <div style="text-align: center; font-size: 30px">
    <a href="attendee_instructions.html" style="color:white; background-color: red">Click here to REGISTER or JOIN the event!</a><br><br>
    <a href="program.html" style="color:white; background-color: red">Click here to VIEW HotI'26 Program</a><br><br>
    <strong>Welcome to the 33rd iteration of the IEEE Hot Interconnects symposium. </strong>
    <strong>HotI’2026 will be held virtually.</strong> <br><br>
    <strong>2026 Conference Theme<br>
    Scale-Up, Scale-Out, Scale-Across: Do they really differ?</strong>
    </div>

    <div style="max-width: 850px; margin: 0 auto; text-align: justify; font-size: 18px; padding-top: 10px;">
    Complex high-capacity training and disaggregated inference workloads are being scaled-across multiple sites, blurring the lines between contemporary scale-out and scale-up interconnection stacks. All the classical issues, such as jitter, bursts, flow/congestion, long-tail latencies, etc., are amplified over long distances, requiring deliberate interventions across the full interconnection stack: algorithms, operational tools, communication frameworks, and network fabrics. This edition of Hot Interconnects will explore these interventions behind operationalizing interconnects over long, short, and shorter distances.
    </div>

</div>

<br>




{% comment %}
{% include reg-open.md %}
{% endcomment %}

<!-- <div style="text-align: center; font-size: 30px">
<strong>2025 Conference Theme<br>
Interconnect Software: You can't touch it but you need it</strong>
</div> -->



## HotI33 (2026) Overview

IEEE Hot Interconnects is the premier international forum for researchers and developers of state of the art hardware and software architectures and implementations for interconnection networks of all scales, ranging from multi-core on-chip interconnects to those within systems, clusters, and data centers. Leaders in industry and academia attend the conference to interact with individuals at the forefront of this field.

Our objective is to address the data center networking and the supercomputing communities. We hope you can join us and benefit not only by the content but also by the prime networking opportunities this event always offers.

<!-- 
## Keynotes

<table class="keynote-table" style="width:100%; border-collapse: collapse; table-layout: fixed;">
  <tbody>
    
    <tr>
      <td style="width:33.33%; text-align:center; padding:10px; border:none;">
        <img src="{{ '/assets/img/GiladShainer.png' | relative_url }}" alt="Gilad Shainer" style="width:100%; max-width:250px;">
      </td>
      <td style="width:33.33%; text-align:center; padding:10px; border:none;">
        <img src="{{ '/assets/img/Omar_Headshot.jpg' | relative_url }}" alt="Omar Baldonado" style="width:100%; max-width:250px;">
      </td>
      <td style="width:33.33%; text-align:center; padding:10px; border:none;">
        <img src="{{ '/assets/img/riaz_bilal_ciena_headshot_1.jpg' | relative_url }}" alt="Bilal Riaz" style="width:100%; max-width:250px;">
      </td>
    </tr>
   
    <tr>
      <td style="width:33.33%; text-align:center; padding:0px; border:none; font-size: 1.3em;">Gilad Shainer</td>
      <td style="width:33.33%; text-align:center; padding:0px; border:none; font-size: 1.3em;">Omar Baldonado</td>
      <td style="width:33.33%; text-align:center; padding:0px; border:none; font-size: 1.3em;">Bilal Riaz</td>
    </tr>
   
    <tr>
      <td class="keynote-affiliation" style="width:33.33%; vertical-align:top; text-align:center; font-size: 1em;">
        Senior Vice President Marketing at NVIDIA
      </td>
      <td class="keynote-affiliation" style="width:33.33%; vertical-align:top; text-align:center; font-size: 1em;">
        Senior Director of Networking at Meta
      </td>
      <td class="keynote-affiliation" style="width:33.33%; vertical-align:top; text-align:center; font-size: 1em;">
        Senior Director of Product Line Management and Head of Interconnect Strategy, Ciena
      </td>
    </tr>
   
    <tr>
      <td class="keynote-title" style="width:33.33%; vertical-align:top; text-align:center; font-size: 1.3em;">
        <strong> Networking Innovations for Gigascale AI Systems</strong> <br> <a href="keynotes-gilad.html">[details]</a>
      </td>
      <td class="keynote-title" style="width:33.33%; vertical-align:top; text-align:center; font-size: 1.3em;">
        <strong>Lessons from networking Meta's gigawatt-scale AI fleet</strong> <br> <a href="keynotes-omar.html">[details]</a>
      </td>
      <td class="keynote-title" style="width:33.33%; vertical-align:top; text-align:center; font-size: 1.3em;">
        <strong>The Future of AI Interconnects: Open Approaches to High‑Performance AI Infrastructure</strong> <br> <a href="keynotes-Bilal.html">[details]</a>
      </td>
    </tr>
  </tbody>
</table> -->



## Keynote Speakers

<style>
/* Keynote speakers — the SAME card + subgrid pattern as the Lightning and
   Sponsor tiers below, so every speaker gets their OWN red rule (one per
   column, separated by the column gap) instead of one continuous line across
   the row. Each card borrows the tier's rows via subgrid, so the affiliation
   row is as tall as the longest affiliation and all three rules start on the
   same line. Styling is local to this page (does not rely on main.scss). */
.keynote-tier {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-template-rows: repeat(4, auto);   /* image · name · affiliation · title */
  column-gap: 1.75em;
  row-gap: 0;
  max-width: 1020px;
  margin: 0 auto 3.5em;
}
.keynote-card {
  grid-row: 1 / span 4;
  display: grid;
  grid-template-rows: subgrid;
  grid-template-columns: minmax(0, 1fr);
  text-align: center;
  /* Each column is a third of the viewport — narrower on a phone than single
     title words like "High-Performance" or "Interconnects:" — so hyphenate and
     break long words to keep them inside the card. */
  min-width: 0;
  hyphens: auto;
  overflow-wrap: break-word;
}
/* Source images are 300x300; shown square at equal size in equal columns. */
.keynote-card img {
  width: 100%;
  max-width: 250px;
  aspect-ratio: 1 / 1;
  object-fit: cover;
  object-position: top;
  display: block;
  margin: 0 auto 0.9em;
}
.keynote-name {
  font-size: 1.3em;
  line-height: 1.3;
  text-wrap: balance;
}
.keynote-affiliation {
  font-size: 1em;
  line-height: 1.45;
  opacity: 0.75;
  margin-top: 0.35em;
  text-wrap: balance;
}
/* Red rule splitting "who is speaking" from "what they're speaking about". It
   lives on the title row, which the subgrid shares across all three cards, so
   the rules line up by construction. */
.keynote-title {
  font-size: 1.3em;
  line-height: 1.4;
  margin-top: 0.9em;
  padding-top: 0.7em;
  border-top: 3px solid #cc0000;
  text-wrap: balance;
}
@media (max-width: 700px) {
  .keynote-tier { column-gap: 0.75em; }
  .keynote-title { padding-top: 0.5em; border-top-width: 2px; }
}
</style>

<div class="keynote-tier">

  <div class="keynote-card">
    <img src="{{ '/assets/img/GiladShainer.png' | relative_url }}" alt="Gilad Shainer">
    <div class="keynote-name">Gilad Shainer</div>
    <div class="keynote-affiliation">Senior Vice President Marketing at NVIDIA</div>
    <div class="keynote-title"><strong> Networking Innovations for Gigascale AI Systems</strong> <br> <a href="keynotes-gilad.html">[details]</a></div>
  </div>

  <div class="keynote-card">
    <img src="{{ '/assets/img/Omar_Headshot.jpg' | relative_url }}" alt="Omar Baldonado">
    <div class="keynote-name">Omar Baldonado</div>
    <div class="keynote-affiliation">Senior Director of Networking at Meta</div>
    <div class="keynote-title"><strong>Lessons from networking Meta's gigawatt-scale AI fleet</strong> <br> <a href="keynotes-omar.html">[details]</a></div>
  </div>

  <div class="keynote-card">
    <img src="{{ '/assets/img/riaz_bilal_ciena_headshot_1.jpg' | relative_url }}" alt="Bilal Riaz">
    <div class="keynote-name">Bilal Riaz</div>
    <div class="keynote-affiliation">Senior Director of Product Line Management and Head of Interconnect Strategy, Ciena</div>
    <div class="keynote-title"><strong>The Future of AI Interconnects: Open Approaches to High-Performance AI Infrastructure</strong> <br> <a href="keynotes-Bilal.html">[details]</a></div>
  </div>

</div>


## Panel
<table style="width: 100%; border-collapse: collapse; border: none;">
  <tbody>
    <tr style="vertical-align: top; text-align: left;  font-size: 1.5em;">
      <td style="width: 60%; padding: 10px; border: none;">
        <large><strong>Title: Interconnects at the Edge Data Center: What are the roles of Scale-Up, Scale-Out, and Scale-Across now? </strong></large>  <br>
        Moderator: Timothy Crawford, Managing Director at KeyBanc Capital Markets <br>
        <small>Abstract: Inference is moving in a big way from the Core to the Edge, in the form of Edge data centers (and smaller things at the edge), whether operated by Neoclouds, specialized operators, industries, or enterprises. How do the interconnects within and between these Edge data centers differ from those of the Core? Where do the constraints of power and latency influence the architectures and technologies for Scale-Up, Scale-Out, and Scale-Across? When do they operate cooperatively versus standalone? When is the connection to the Core considered Scale-Across or just the WAN? In this panel we will examine this critical, emerging venue for interconnects and learn what it can tell us about these classifications and applicable technologies. <a href="highlight-panel.html"> [details]</a></small>
      </td>
    </tr>
  </tbody>
</table>

## Lightning Session
The week before OFC (the Optical Fiber Communication Conference) held in Los Angeles in March, four new Multi-Source Agreements (MSAs) were announced. Each is designed to accelerate design choices for some aspect of the AI data center, ideally in a way that serves the needs of the operator customers. They are not intended to give any vendor an advantage over the others but are meant to speed deployment by getting the suppliers (sources) to agree on some not-very-controversial aspects of these solutions. For each MSA, we have asked one of the founding companies to speak and to explain what problem the MSA is solving, why all the existing standards bodies and consortia are not solving that problem, what the MSA promises to actually produce, how the MSA will avoid stifling innovation, and how companies can join the MSA.
- OCI MSA, focusing on the optical compute interface; speaker: [Drew Alduino] (Meta)
- Open CPX MSA, focusing on open-socket NPO and CPO; speaker: [Ryan Yu](https://www.linkedin.com/in/rangchenyu/) (TeraHop) 
- SDM4 MCF MSA, focusing on multi-core fiber; speaker: [Gabe Sudduth](https://www.linkedin.com/in/gabriel-sudduth/) (Corning)
- XPO MSA, focusing on extreme pluggable optics; speaker: [Sunil Priyadarshi](https://www.linkedin.com/in/sunilpriyadarshi) (Arista)




## Last Year's Proceedings (HotI32 (2025))

Available at [IEEE here](https://ieeexplore.ieee.org/xpl/conhome/11244728/proceeding).

Watch the recordings of all sessions and talks on [YouTube](https://www.youtube.com/watch?v=b-ByJQDyWBU&list=PLBM5Lly_T4yRGBFgforeMTDpjasC_PV7r).

## Last Year's Publications (HotI32 (2025))

<!-- <div style="text-align: left">
    <img src="{{ '/assets/img/hoti_ieeeMicro.jpg' | relative_url }}" alt="HotI31" style="width: 20%; max-width: 800px; height: auto;">
</div> -->
Available at [IEEE Micro](https://ieeexplore.ieee.org/xpl/tocresult.jsp?isnumber=10989057&punumber=40).
