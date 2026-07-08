---
# title: Keynote Speakers
---
# Sponsor Talk

### Kirtesh Patil

Tech Lead at Meta

<img src="{{ '/assets/img/kritesh_patil.png' | relative_url }}" alt="Kritesh Patil" style="width:100%; max-width:250px; height:auto; object-fit:cover; object-position:top;">


**Title:** Co-Designing MTIA's Communication Stack

**Abstract:** 
<div style="text-align: justify; text-indent: 0em;">
 As AI models grow, communication increasingly determines the performance of large-scale AI systems, in both training and inference. In inference, it sits on the token-generation critical path, where collective latency directly affects responsiveness. This talk describes how Meta treats communication as a first-class design concern for MTIA, its family of homegrown AI accelerators, co-designing silicon, network, and software so that collectives are offloaded, overlapped with computation, and fused into compute kernels to cut latency, all exposed through the collective communications library (HCCL), which integrates natively with PyTorch. On the network side, MTIA builds its scale-up and scale-out networks on standard Ethernet rather than a proprietary interconnect, so we can leverage the maturity and openness of the Ethernet ecosystem. Drawing on our recently accepted SC26 paper, we share the design principles behind this approach, early results, and open challenges in building communication infrastructure for next-generation AI.
</div>
<br>

**Biography:** 
<div style="text-align: justify; text-indent: 0em;">
Kirtesh Patil is a tech lead at Meta, where he leads development of the collective communications library (HCCL) and co-designs the communication stack for MTIA, Meta's family of homegrown AI accelerators. He previously built the enforcement engine for Meta's Network Entitlement system (ACM SIGCOMM 2022), and earlier at Cisco worked on software-defined WAN, WAN optimization, and network security.
</div>
