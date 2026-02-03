---
# title: hpcwire
---
<br>

<div style="text-align: center; font-size: 30px">
    <strong>HotI 2025 has concluded. Watch the recordings of all HotI 2025 sessions and talks on <a href="https://www.youtube.com/watch?v=b-ByJQDyWBU&list=PLBM5Lly_T4yRGBFgforeMTDpjasC_PV7r"> YouTube</a>!</strong>
    <a href="https://www.youtube.com/watch?v=b-ByJQDyWBU&list=PLBM5Lly_T4yRGBFgforeMTDpjasC_PV7r" target="_blank"> <img src="{{ '/assets/img/logo_youtube.png' | relative_url }}" alt="YouTube Logo" style="width: 50px; height: auto; vertical-align: middle;"></a>
</div>

<br>

## What’s Up with HPC Interconnects? A Q&A with HotI



> By Alex Woodie. The following article originally appeared on <a href="https://www.hpcwire.com/2025/10/07/whats-up-with-hpc-interconnects-a-qa-with-hoti/" target="_blank">HPCwire</a>.

<div class="article-content">
	<p>The AI revolution has exposed new bottlenecks in HPC architectures, particularly at the network level. As GPUs and other AI accelerators get faster, they’re outrunning the capability of storage to keep them fed with data. This is spurring research and development into new interconnect technology, which was the focus of the recent Hot Interconnects (now HotI) conference.</p>
  <p>Like the annual Hot Chips Symposium, the <a href="http://www.ieee.org/">Institute of Electrical and Electronics Engineers</a> has hosted an annual <a href="https://hoti.org/">Hot Interconnects</a> (or HotI) conference to showcase the latest advances in interconnect technology. This year’s event took place virtually over three days in late August 2025.</p>
  <p><em>HPCwire,</em> HotI&#8217;s media partner, had the chance to conduct an email Q&amp;A with HotI about the recent event. Several HotI representatives participated in the conversation, including Artem Polyakov (General Chair), Sayan Ghosh (Vice Chair), Dan Pitt (Keynote/Panel Chairs), and Scott Levy and Jim Dinan (both Finance Chairs).</p>
  <p>Here’s our conversation:</p>
  <p><em>HPCwire</em>: First, can you tell us more about what the Hot Interconnects conference is about?</p>
  <p>HotI: Hot Interconnects (which we now call HotI [sounds like Hot Eye]) was established in 1993 as a sister conference of the well-known Hot Chips Symposium. Both conferences were held back-to-back, sharing the same venues. Having a multi-decade history (this year marks the 32nd edition!), HotI was actively engaged in the establishment of high-performance communication. For further details, we would like to refer the interested reader to <a href="https://www.linkedin.com/pulse/perspective-hot-interconnects-dan-pitt-hot-interconnects/">a nostalgic retrospective outlook</a> by the  HotI “veteran” Dan Pitt.</p>
  <p>Today, HotI is the premier international forum for researchers and developers of state-of-the-art hardware and software architectures and implementations for high-performance interconnection networks of all scales, ranging from multi-core on-chip interconnects to those within systems, clusters, and data centers.</p>
  <p><em>HPCwire</em>: What was the focus of Hot Interconnects this year?</p>
  <p>HotI: The focus of HotI was always on the hottest trends of the year. In his <a href="https://youtu.be/b-ByJQDyWBU?si=hcoaCs95W_Lgi5tv">presentation to open the conference</a>, our General Chair, Artem Polyakov, outlined how trends in the field have shifted in the past decades.</p>
  <p>For example, routing was heavily discussed in the early 2000s, with up to 4 sessions on it in 2002. Hardware offloading periodically draws attention, e.g., in 2006, 2014, and 2020-2022. The infrastructure- and optic-related topics have shown consistent multi-year bursts. Beginning in 2023, we have observed a dramatic increase in interest in topics related to Artificial Intelligence (AI).</p>
  <p>This year, the HotI theme was dedicated to the communication software that enables systems to achieve the performance requirements of cutting-edge HPC and AI applications.</p>
  <p>Both of our stellar keynotes, by Amin Vahdat of Google (which you can <a href="https://youtu.be/ijnG0gx_ewE?si=pHpQ1UxZYqZcRb1K">watch on YouTube</a>) and Deepak Bansal of Microsoft (also <a href="https://youtu.be/vuo6KfdRRZw?si=jAWlQMTGlSw1hCHa">available for viewing on YouTube</a>), as well as Cornelis Networks, Cisco, Meta, and GigaIO talks delved into the AI infrastructures and respective software.</p>
  <p>The annual panel discussion (which you can <a href="https://youtu.be/jQOZlWD19G4?si=xH0qGAKVEGZTL-yj">also watch on YouTube</a>) provided an AI software perspective on interconnect requirements and explored the LLM token economy that drives cutting-edge AI systems.</p>
  <p>Continuing this topic, <a href="https://hoti.org/program.html">several papers in the technical program</a> focused on various aspects of AI communication. In addition, for the first time, we held a tutorial on NVIDIA GPU communication libraries that attracted a lot of attention.</p>
  <p><em>HPCwire</em>: So there has been an &#8220;AI effect&#8221; on Interconnects!</p>
  <p>HotI: Absolutely! The explosive growth of AI has exposed several shortcomings in interconnect performance and capabilities.  Specifically, the AI boom has brought into clear focus how much faster computing has evolved than networking and interconnect capabilities. It has become apparent to everyone that moving the data around has become the bottleneck to scaling AI computing. As a result, many of the technologies and systems discussed at Hot Interconnects addressed how to close the performance gap between computing and networking. We appreciate the attention we in the Interconnect industry have been receiving of late, as the world is looking to us to enable more acceleration of AI. Interestingly, for many years, the market for advanced interconnect technologies was primarily HPC. Suddenly, we find that these technologies are also needed for scaling AI, which represents a <em>much</em> larger market.</p>
  <p><em>HPCwire</em>: Were there any new technologies that we should watch?</p>
  <p>HotI: Hot Interconnects have always been at the forefront of showcasing contemporary cutting-edge interconnect technologies. All of these new technologies, including:</p>
  <ul>
  <li>Cray Seastar (2002), Gemini (2010), and Slingshot (2019, 2022);</li>
  <li>PathScale Infinipath (2005);</li>
  <li>Quadrics QsNetIII (2008);</li>
  <li>Fujitsu Tofu (2011) and Tofu2 (2014);</li>
  <li>Intel Omni-path (2015);</li>
  <li>Atos BXI (2015);</li>
  <li>Standards: RoCE (2009), CXL (2021);</li>
  <li>Lightmatter Passage (2023);</li>
  </ul>
  <p>have all been featured at various times over the history of Hot Interconnects.</p>
  <p>This year is no exception. Several emerging “hot interconnects,” including Ultra Ethernet (<a href="https://youtu.be/qqgGyY_K_Vw?si=VWj_MwrXNTHmWdug">view more on YouTube</a>:), NVIDIA NVLink Fusion (see <a href="https://youtu.be/GMJj4KDqYGo?si=hbowd0E8XHC7ehOf">this YouTube presentation</a>:), and UALink have set new standards for growing AI and HPC needs, and a paper on early adoption of UCIe for on-package memory implementation. We are excited about the impact of the scale of the next generation of AI products.</p>
  <p>Optical technologies have also been prominent over the last few years. As the newest advances reduce the power down to 1 pJ/bit, these technologies satisfy massive bandwidth and very low latency requirements at ultra-low cost. This year was unprecedented in the number of optics-related talks. Lightmatter presented an update on their Passage Co-Packaged Optics (CPO) solution and a paper on its impact for AI training applications, and Nubis discussed mixing active copper and CPO to improve scaling. Arista examined the power aspects of optics. Avicena presented a technical paper on the advantages of micro LEDs over lasers. Celestial AI presented the Photonic Fabric CPO solution.</p>
  <p><em>HPCwire</em>: Does HotI highlight the best work?</p>
  <p>HotI: Definitely. HOTI Technical Program Committee (TPC) has experts from industry, academia and labs, who have been instrumental in identifying the best research papers through meticulous peer review and discussions. Since 2024, we have reprised the best paper awards to further highlight two top papers in the &#8220;Industry&#8221; and &#8220;Academia&#8221; categories, respectively. This year, thanks to the generosity of our sponsors, each award included a $1000 cash prize. The Best Industry Paper award was given to “Accelerating Frontier MoE Training with 3D Integrated Optics” by Mikhail Bernadskiy et al., Lightmatter. The authors model the benefits of 3D CPO for scale-up GPU networks, which demonstrates an 8x increase in scale-up pod bandwidth using half the energy of conventional CPO, a 6x reduction in package area expansion compared to CPO, and 2.7x increase in MoE training throughput. The Best Academic Paper was given to “Deadlock-free routing for Full-mesh networks without using Virtual Channels” by Alejandro Cano Cos et al., Universidad de Cantabria. This work actualizes the routing topic from the 2000s in contemporary realities. The authors present their Topology-Embedded Routing Algorithm, which deconstructs the physical topology into two components that provide up to 32% performance improvement.</p>
  <p><em>HPCwire</em>: What is the focus for 2026 Hot Interconnects?</p>
  <p>HotI: Continuing an emerging trend from the past few years, this year featured a remarkable number of talks dedicated to optics for bridging the growing gap between computation and bandwidth. Looking ahead, we plan to focus on strategies for increasing bandwidth density while addressing the limitations of conventional electrical interconnects.</p>
  <p>&nbsp;</p>
</div>