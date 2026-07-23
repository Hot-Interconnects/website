---

---
<div style="max-width: 850px; margin: 0 auto; text-align: center">
  <div style="text-align: center; font-size: 30px">
    <a href="attendee_instructions.html" style="color:white; background-color: red">Click here to REGISTER or JOIN the event!</a><br><br>
  </div>
</div>

<!-- <div style="text-align: center; font-size: 30px">
    <strong>HotI 2025 has concluded. Watch the recordings of all HotI 2025 sessions and talks on <a href="https://www.youtube.com/watch?v=b-ByJQDyWBU&list=PLBM5Lly_T4yRGBFgforeMTDpjasC_PV7r"> YouTube</a>!</strong>
    <a href="https://www.youtube.com/watch?v=b-ByJQDyWBU&list=PLBM5Lly_T4yRGBFgforeMTDpjasC_PV7r" target="_blank"> <img src="{{ '/assets/img/logo_youtube.png' | relative_url }}" alt="YouTube Logo" style="width: 50px; height: auto; vertical-align: middle;"></a>
</div> -->


## Keynote Speakers

<table class="keynote-table" style="width:100%; border-collapse: collapse; table-layout: fixed;">
  <tbody>
    <!-- Row: photos -->
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
    <!-- Row: names -->
    <tr>
      <td style="width:33.33%; text-align:center; padding:0px; border:none; font-size: 1.3em;">Gilad Shainer</td>
      <td style="width:33.33%; text-align:center; padding:0px; border:none; font-size: 1.3em;">Omar Baldonado</td>
      <td style="width:33.33%; text-align:center; padding:0px; border:none; font-size: 1.3em;">Bilal Riaz</td>
    </tr>
    <!-- Row: affiliations -->
    <tr>
      <td style="width:33.33%; vertical-align:top; text-align:center; padding:0px; border:none; font-size: 1em;">
        Senior Vice President Marketing at NVIDIA
      </td>
      <td style="width:33.33%; vertical-align:top; text-align:center; padding:0px; border:none; font-size: 1em;">
        Senior Director of Networking at Meta
      </td>
      <td style="width:33.33%; vertical-align:top; text-align:center; padding:0px; border:none; font-size: 1em;">
        Senior Director of Product Line Management and Head of Interconnect Strategy, Ciena
      </td>
    </tr>
    <!-- Row: titles + details link -->
    <tr>
      <td style="width:33.33%; vertical-align:top; text-align:center; padding:5px; border:none; font-size: 1.3em;">
        <strong> Networking Innovations for Gigascale AI Systems</strong> <br> <a href="keynotes-gilad.html">[details]</a>
      </td>
      <td style="width:33.33%; vertical-align:top; text-align:center; padding:5px; border:none; font-size: 1.3em;">
        <strong>Lessons from networking Meta's gigawatt-scale AI fleet</strong> <br> <a href="keynotes-omar.html">[details]</a>
      </td>
      <td style="width:33.33%; vertical-align:top; text-align:center; padding:5px; border:none; font-size: 1.3em;">
        <strong>The Future of AI Interconnects: Open Approaches to High-Performance AI Infrastructure</strong> <br> <a href="keynotes-Bilal.html">[details]</a>
      </td>
    </tr>
  </tbody>
</table>


## Panel

<table style="width: 100%; border-collapse: collapse; border: none;">
  <tbody>
    <tr style="vertical-align: top; text-align: left;  font-size: 1.3em;">
      <td style="width: 60%; padding: 10px; border: none; text-align: justify;">
        <large><strong>Title: Interconnects at the Edge Data Center: What are the roles of Scale-Up, Scale-Out, and Scale-Across now? </strong></large>  <br>
        Moderator: Timothy Crawford, Managing Director at KeyBanc Capital Markets <br>
        Abstract: Inference is moving in a big way from the Core to the Edge, in the form of Edge data centers (and smaller things at the edge), whether operated by Neoclouds, specialized operators, industries, or enterprises. How do the interconnects within and between these Edge data centers differ from those of the Core? Where do the constraints of power and latency influence the architectures and technologies for Scale-Up, Scale-Out, and Scale-Across? When do they operate cooperatively versus standalone? When is the connection to the Core considered Scale-Across or just the WAN? In this panel we will examine this critical, emerging venue for interconnects and learn what it can tell us about these classifications and applicable technologies. <a href="highlight-panel.html"> [details]</a>
      </td>
    </tr>
  </tbody>
</table>

<style>
.panelist-tier {
  display: grid;
  grid-template-columns: repeat(6, 1fr);
  column-gap: 1.75em;
  row-gap: 3em;
  max-width: 1020px;
  margin: 0 auto 3.5em;
}
.panelist-card {
  grid-column: span 2;          /* 6 cols / span 2 => 3 across */
  display: flex;
  flex-direction: column;
  text-align: center;
  min-width: 0;
  overflow-wrap: break-word;
}
/* Center the trailing pair on row 2 */
.panelist-card.offset-a { grid-column: 2 / span 2; }
.panelist-card.offset-b { grid-column: 4 / span 2; }

.panelist-card img {
  width: 100%;
  max-width: 165px;
  aspect-ratio: 1 / 1;
  object-fit: cover;
  object-position: top;
  display: block;
  margin: 0 auto 0.9em;
}
.panelist-name {
  font-size: 1.15em;
  line-height: 1.3;
  text-wrap: balance;
}
.panelist-affiliation {
  font-size: 0.9em;
  line-height: 1.45;
  opacity: 0.75;
  margin-top: 0.35em;
  text-wrap: balance;
}

.panelist-role {
  font-size: 0.78em;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  opacity: 0.6;
  margin-bottom: 0.3em;
}

/* Stays 3-across at every width — cards scale down rather than reflow. */
@media (max-width: 560px) {
  .panelist-tier { column-gap: 0.75em; row-gap: 2.5em; }
}
</style>

<div class="panelist-tier">

  <div class="panelist-card">
    <img src="{{ '/assets/img/Tim_Crawford.jpg' | relative_url }}" alt="Timothy Crawford">
    <div class="panelist-role">Moderator</div>
    <div class="panelist-name">Timothy Crawford</div>
    <div class="panelist-affiliation">Managing Director, KeyBanc Capital Markets</div>
  </div>

  <div class="panelist-card">
    <img src="{{ 'assets/img/Inder_Monga_panelist.jpeg' | relative_url }}" alt="Inder Monga">
    <div class="panelist-name">Inder Monga</div>
    <div class="panelist-affiliation">Director of Berkeley Lab’s Scientific Networking Division and Executive Director of Energy Sciences Network (ESnet)</div>
  </div>

  <div class="panelist-card">
    <img src="{{ 'assets/img/Yosuke_Aragane_panelist.jpeg' | relative_url }}" alt="Yosuke Aragane">
    <div class="panelist-name">Yosuke Aragane</div>
    <div class="panelist-affiliation">Vice President, IOWN Development Office, NTT</div>
  </div>

  <div class="panelist-card">
    <img src="{{ 'assets/img/Tanner_Ryan_panelist.jpeg' | relative_url }}" alt="Tanner Ryan">
    <div class="panelist-name">Tanner Ryan</div>
    <div class="panelist-affiliation">Network Engineer at Cloudflare</div>
  </div>

  <div class="panelist-card">
    <img src="{{ 'assets/img/Marc_Austin_panelist.jpeg' | relative_url }}" alt="Marc Austin">
    <div class="panelist-name">Marc Austin</div>
    <div class="panelist-affiliation">CEO and Founder - Hedgehog</div>
  </div>

  <div class="panelist-card">
    <img src="{{ 'assets/img/Ofer_Shapiro_panelist.jpeg' | relative_url }}" alt="Ofer Shapiro">
    <div class="panelist-name">Ofer Shapiro</div>
    <div class="panelist-affiliation">Investor</div>
  </div>

</div>

## Lightning Session

<style>
.lightning-intro {
  max-width: 1020px;
  margin: 0 auto 2.5em;
  text-align: justify;
}
.lightning-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  column-gap: 1.75em;
  row-gap: 2.5em;
  max-width: 1020px;
  margin: 0 auto 3.5em;
}
.lightning-card {
  display: flex;
  flex-direction: column;
  text-align: center;
  /* Grid items default to min-width:auto and refuse to shrink below their
     longest word, which overflows the grid on narrow screens. Hyphenate long
     names ("Priyadarshi") rather than snapping them mid-word; break-word is
     only the last resort. */
  min-width: 0;
  hyphens: auto;
  overflow-wrap: break-word;
}
.lightning-card img {
  width: 100%;
  max-width: 190px;
  aspect-ratio: 1 / 1;
  object-fit: cover;
  object-position: top;
  display: block;
  margin: 0 auto 0.9em;
}
.lightning-name {
  font-size: 1.15em;
  line-height: 1.3;
  font-weight: bold;
  text-wrap: balance;
}
.lightning-affiliation {
  font-size: 0.9em;
  line-height: 1.45;
  opacity: 0.75;
  margin-top: 0.2em;
}
.lightning-msa {
  font-size: 1em;
  font-weight: bold;
  line-height: 1.4;
  margin-top: 0.8em;
  padding-top: 0.7em;
  border-top: 3px solid #cc0000;
}
.lightning-focus {
  font-size: 0.9em;
  line-height: 1.45;
  margin-top: 0.3em;
  text-wrap: balance;
}
/* Stays 4-across at every width (like the keynote table) — cards scale down
   rather than reflow. A quarter of a phone screen is ~80px, so the type has
   to come down with the gutters to keep the longest names on one line. */
@media (max-width: 700px) {
  .lightning-grid { column-gap: 0.75em; row-gap: 2em; }
  .lightning-name { font-size: 0.85em; }
  .lightning-msa { font-size: 0.78em; padding-top: 0.5em; border-top-width: 2px; }
  .lightning-affiliation,
  .lightning-focus { font-size: 0.72em; }
}
</style>

<div class="lightning-intro">
  The week before OFC (the Optical Fiber Communication Conference) held in Los
  Angeles in March, four new Multi-Source Agreements (MSAs) were announced.
  Each is designed to accelerate design choices for some aspect of the AI data
  center, ideally in a way that serves the needs of the operator customers.
  They are not intended to give any vendor an advantage over the others but are
  meant to speed deployment by getting the suppliers (sources) to agree on some
  not-very-controversial aspects of these solutions. For each MSA, we have
  asked one of the founding companies to speak and to explain what problem the
  MSA is solving, why all the existing standards bodies and consortia are not
  solving that problem, what the MSA promises to actually produce, how the MSA
  will avoid stifling innovation, and how companies can join the MSA.
</div>

<div class="lightning-grid">

  <div class="lightning-card">
    <img src="{{ '/assets/img/lightning-drew-alduino.jpg' | relative_url }}" alt="Drew Alduino">
    <div class="lightning-name">Drew Alduino</div>
    <div class="lightning-affiliation">Meta</div>
    <div class="lightning-msa">OCI MSA</div>
    <div class="lightning-focus">Optical compute interface</div>
  </div>

  <div class="lightning-card">
    <img src="{{ '/assets/img/lightning-ryan-yu.jpeg' | relative_url }}" alt="Ryan Yu">
    <div class="lightning-name"><a href="https://www.linkedin.com/in/rangchenyu/" target="_blank">Ryan Yu</a></div>
    <div class="lightning-affiliation">TeraHop</div>
    <div class="lightning-msa">Open CPX MSA</div>
    <div class="lightning-focus">Open-socket NPO and CPO</div>
  </div>

  <div class="lightning-card">
    <img src="{{ '/assets/img/lightning-duane-robbins.jpeg' | relative_url }}" alt="Duane Robbins">
    <div class="lightning-name"><a href="https://www.linkedin.com/in/duane-robbins-230033113" target="_blank">Duane Robbins</a></div>
    <div class="lightning-affiliation">Corning</div>
    <div class="lightning-msa">SDM4 MCF MSA</div>
    <div class="lightning-focus">Multi-core fiber</div>
  </div>

  <div class="lightning-card">
    <img src="{{ '/assets/img/lightning-sunil-priyadarshi.jpeg' | relative_url }}" alt="Sunil Priyadarshi">
    <div class="lightning-name"><a href="https://www.linkedin.com/in/sunilpriyadarshi" target="_blank">Sunil Priyadarshi</a></div>
    <div class="lightning-affiliation">Arista</div>
    <div class="lightning-msa">XPO MSA</div>
    <div class="lightning-focus">Extreme pluggable optics</div>
  </div>

</div>



## Sponsor Talks

<style>
.sponsor-tier {
  display: grid;
  grid-template-columns: repeat(6, 1fr);
  column-gap: 1.75em;
  row-gap: 3em;
  max-width: 1020px;
  margin: 0 auto 3.5em;
}
.sponsor-card {
  grid-column: span 2;
  display: flex;
  flex-direction: column;
  text-align: center;
  /* Grid items default to min-width:auto and refuse to shrink below their
     longest word, which overflows the tier on narrow screens. */
  min-width: 0;
  overflow-wrap: break-word;
}
/* Offset the trailing pair by half a card -> chessboard stagger */
.sponsor-card.offset-a { grid-column: 2 / span 2; }
.sponsor-card.offset-b { grid-column: 4 / span 2; }

.sponsor-card img {
  width: 100%;
  max-width: 165px;
  aspect-ratio: 1 / 1;
  object-fit: cover;
  object-position: top;
  display: block;
  margin: 0 auto 0.9em;
}
.sponsor-name {
  font-size: 1.15em;
  line-height: 1.3;
  text-wrap: balance;
}
.sponsor-affiliation {
  font-size: 0.9em;
  line-height: 1.45;
  opacity: 0.75;
  margin-top: 0.35em;
  text-wrap: balance;
}
.sponsor-title {
  font-size: 1em;
  font-weight: bold;
  line-height: 1.4;
  margin-top: 0.9em;
  text-wrap: balance;
}
.sponsor-details {
  font-size: 0.9em;
  margin-top: auto;
  padding-top: 0.6em;
}

/* Diamond tier reads larger */
.sponsor-tier.diamond .sponsor-card img { max-width: 200px; }
.sponsor-tier.diamond .sponsor-name { font-size: 1.3em; }
.sponsor-tier.diamond .sponsor-title { font-size: 1.08em; }

/* Stays 3-across at every width (like the keynote table) — cards scale
   down rather than reflow. Narrow screens only tighten the gutters. */
@media (max-width: 560px) {
  .sponsor-tier { column-gap: 0.75em; row-gap: 2.5em; }
}
</style>

<!-- ============ DIAMOND ============ -->
<div class="sponsor-tier diamond">

  <div class="sponsor-card">
    <img src="{{ 'assets/img/napatech-Alex_Agerholm.jpeg' | relative_url }}" alt="Alex Omø Agerholm">
    <div class="sponsor-name">Alex Omø Agerholm</div>
    <div class="sponsor-affiliation">Chief Product Architect, Napatech</div>
    <div class="sponsor-title">AI Fabrics in Motion: Programmable Interconnects for Scale-Up, Scale-Out, and Scale-Across</div>
    <div class="sponsor-details"><a href="sponsortalk-napatech.html">[details]</a></div>
  </div>

  <div class="sponsor-card">
    <img src="{{ 'assets/img/nick-lightmatter.png'| relative_url }}" alt="Speaker TBD">
    <div class="sponsor-name">Nick Harris</div>
    <div class="sponsor-affiliation">Founder and CEO of Lightmatter, Lightmatter</div>
    <div class="sponsor-title">BiDi DWDM: The Interconnect Foundation for High-Performance AI Training and Inference</div>
    <div class="sponsor-details"><a href="sponsortalk-lightmatter.html">[details]</a></div>
  </div>

  <div class="sponsor-card">
    <img src="{{ 'assets/img/Marvell_Ravi.png' | relative_url }}" alt="Ravi Mahatme">
    <div class="sponsor-name">Ravi Mahatme</div>
    <div class="sponsor-affiliation">Senior Director, Product Management, Photonic Fabric Business Unit, Marvell</div>
    <div class="sponsor-title">A Shared Memory Architecture for Token-Efficient AI Infrastructure</div>
    <div class="sponsor-details"><a href="sponsortalk-marvell.html">[details]</a></div>
  </div>

</div>

<!-- ============ PLATINUM ============ -->
<div class="sponsor-tier">

  <div class="sponsor-card">
    <img src="{{ '/assets/img/Mohan.png' | relative_url }}" alt="Mohan Kalkunte">
    <div class="sponsor-name">Mohan Kalkunte</div>
    <div class="sponsor-affiliation">Vice President of Architecture &amp; Technology, Core Switching Group, Broadcom</div>
    <div class="sponsor-title">Distributed Computing @ Scale for AI Training &amp; Inference</div>
    <div class="sponsor-details"><a href="sponsortalk-broadcom.html">[details]</a></div>
  </div>

  <div class="sponsor-card">
    <img src="{{ '/assets/img/cisco-will.jpg' | relative_url }}" alt="Will Eatherton">
    <div class="sponsor-name">Will Eatherton</div>
    <div class="sponsor-affiliation">SVP, Data Center, Internet &amp; Cloud Infrastructure Engineering at Cisco</div>
    <div class="sponsor-title">Ethernet for Shared AI Fabrics: InfiniBand-Class Performance with Multi-Tenant Scale</div>
    <div class="sponsor-details"><a href="sponsortalk-cisco.html">[details]</a></div>
  </div>

  <div class="sponsor-card">
    <img src="{{ 'assets/img/Rohan.Gandhi.eliyan.png' | relative_url }}" alt="Rohan Gandhi">
    <div class="sponsor-name">Rohan Gandhi</div>
    <div class="sponsor-affiliation">Vice President of Optical Marketing at Eliyan</div>
    <div class="sponsor-title">From Long Reach to Smart Reach: The Evolution of SerDes for AI Infrastructure</div>
    <div class="sponsor-details"><a href="sponsortalk-eliyan.html">[details]</a></div>
  </div>

  <div class="sponsor-card offset-a">
    <img src="{{ 'assets/img/kritesh_patil.png' | relative_url }}" alt="Kirtesh Patil">
    <div class="sponsor-name">Kirtesh Patil</div>
    <div class="sponsor-affiliation">Tech Lead at Meta</div>
    <div class="sponsor-title">Co-Designing MTIA's Communication Stack</div>
    <div class="sponsor-details"><a href="sponsortalk-meta.html">[details]</a></div>
  </div>

  <div class="sponsor-card offset-b">
    <img src="{{ 'assets/img/dave-qualcomm.png' | relative_url }}" alt="Speaker TBD">
    <div class="sponsor-name">Dave Kulansky</div>
    <div class="sponsor-affiliation">Director of Product Management at Qualcomm</div>
    <div class="sponsor-title">Scaling AI with Chiplets & CPO</div>
    <div class="sponsor-details"><a href="sponsortalk-qualcomm.html">[details]</a></div>
  </div>

</div>