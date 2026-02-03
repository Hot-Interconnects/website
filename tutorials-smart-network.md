---

---
# High-Performance and Smart Networking Technologies for HPC and AI @ HotI 2025

## Abstract

High-Performance Networking technologies are generating a lot of excitement towards building next generation High-End Computing (HEC) systems for HPC and AI with GPGPUs, accelerators, and Data Center Processing Units (DPUs), and a variety of application workloads. This tutorial will provide an overview of these emerging technologies, their architectural features, current market standing, and suitability for designing HEC systems. It will start with a brief overview of IB, HSE, RoCE, and Omni-Path interconnect. An in-depth overview of the architectural features of these interconnects will be presented. It will be followed with an overview of the emerging NVLink, NVLink2, NVSwitch, EFA, and Slingshot architectures. We will then present advanced features of commodity high-performance networks that enable performance and scalability. We will then provide an overview of enhanced offload capable network adapters like DPUs/IPUs (Smart NICs), their capabilities and features. Next, an overview of software stacks for high-performance networks like Open Fabrics Verbs, LibFabrics, and UCX comparing the performance of these stacks will be given. Next, challenges in designing MPI library for these interconnects, solutions and sample performance numbers will be presented.

## Tutorial Outline

1. **Trends in High-End Computing**
2. **Why High-Performance Networking for HPC and AI?**
3. **Communication Model and Semantics of High-Performance Networks**
4. **Architectural Overview of High-Performance Networks**
5. **Overview of Emerging Data Center Processing Units (DPUs)**
6. **High-Performance Network Deployments for AI Workloads**
7. **Overview of Software Stacks for Commodity High-Performance Networks**
8. **Sample Case Studies and Performance Numbers**
9. **Hands-on Exercises**
10. **Conclusions, Final Q&A, and Discussion**

## Speakers

- **Dhabaleswar K. (DK) Panda**, Ohio State University
- **Benjamin Michalowicz**, The Ohio State University




## Presenter Bios

**Dhabaleswar K. (DK) Panda** is a Professor and University Distinguished Scholar of Computer Science and Engineering at the Ohio State University.  He serves as the Director of the newly-established $20M NSF-AI Institute, ICICLE (https://icicle.ai). He has published over 500 papers in the area of high-end computing and networking.  The MVAPICH (High-Performance MPI over InfiniBand, Omni-Path, iWARP, RoCE, and Slingshot) libraries, designed and developed by his research group (http://mvapich.cse.ohio-state.edu), are currently being used by more than 3,450 organizations worldwide (in 92 countries). More than 1.91 million downloads of this software have taken place from the project's site. This software is empowering several InfiniBand clusters (including the 21st, 67th, and 88th ranked ones) in the TOP500 list. High-performance and scalable solutions for AI frameworks (Deep Learning and Machine Learning) from his group are available from https://hidl.cse.ohio-state.edu. Similarly, scalable, and high-performance solutions for Big Data and Data science frameworks are available from https://hibd.cse.ohio-state.edu. Prof. Panda is a Fellow of ACM and IEEE. He is a recipient of the 2022 IEEE Charles Babbage Award and the 2024 IEEE TCPP Outstanding Service and Contributions Award. More details about Prof. Panda are available at http://www.cse.ohio-state.edu/~panda.

**Ben Michalowicz** is a PhD student at the Ohio State University under Prof. DK Panda and Prof. Hari Subramoni in the Network-Based Computing Laboratory. His research interests lie include high-performance computing (HPC), parallel architectures, network-based computing for HPC, and parallel programming environments. Specifically, he is interested in efficiently offloading workloads to Smart Network Cards like NVIDIA's BlueField DPUs. Ben actively contributes to the MVAPICH software.