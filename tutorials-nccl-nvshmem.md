---

---
# GPU Communication Libraries for Accelerating HPC and AI Applications @ HotI 2025


## Abstract

This tutorial provides a comprehensive introduction to two advanced GPU communication libraries: NVIDIA Collective Communication Library (NCCL) and NVSHMEM. Designed for researchers, engineers, and developers working on HPC and deep learning, the session explores the core concepts, programming models, and practical use cases of both libraries. 

NCCL is optimized for collective and point-to-point communication among GPUs, offering high throughput and low latency by leveraging hardware features such as NVLink, PCIe, and RDMA networking (InfiniBand, RoCE, etc). It is widely used for distributed deep learning and scientific computing, enabling efficient data movement and synchronization across multiple GPUs within and across nodes. 

NVSHMEM, on the other hand, implements a Partitioned Global Address Space (PGAS) model for NVIDIA GPUs, supporting one-sided communication and fine-grained data exchange. It enables both host- and device-initiated operations, allowing for asynchronous, in-kernel communication and efficient overlap of computation and communication. NVSHMEM is particularly suited for irregular communication patterns and workloads requiring low-latency, fine-grained GPU-initiated operations. 

Through hands-on examples we elaborate on the new features in both libraries, participants will gain practical skills in leveraging NCCL and NVSHMEM to accelerate multi-GPU applications, understand their interoperability, and select the right tool for diverse HPC and DL scenarios.

## Tutorial Outline 
1. **Introduction to NCCL & NVSHMEM**
2. **NCCL API Walkthrough with Examples** 
3. **NVSHMEM API Walkthrough with Examples** 
4. **Advanced Features For GPU Communication Libraries** — NCCL Symmetric Memory Kernels, NVSHMEM Python Language Bindings
5. **Hands-on Session**
6. **Conclusions, Final Q&A, and Discussion**  

## Presenters
- **Benjamin Glick**, NVIDIA 
- **Arnav Goel**, NVIDIA
- **Andreas Herten**, Jülich Supercomputing Centre
- **Pouya Kousha**, NVIDIA 

## Presenter Bios
**Benjamin Glick** is a Senior Software Engineer at NVIDIA, specializing in GPU communication libraries, high-performance computing, and scalable system software. He currently focuses on NVSHMEM, making high-performance, GPU-aware distributed programming more accessible to  developers.
Prior to NVIDIA, Ben held engineering roles at AI hardware startups including SAPEON and SambaNova Systems, where he designed distributed operating systems, memory and I/O architectures, collective communication libraries, and virtualization frameworks for custom AI accelerators. He has led software and hardware co-design efforts spanning multiple product generations, from pre-silicon through deployment.
Ben’s expertise includes parallel and distributed runtime systems, accelerator and OS architecture, GPU- and network-optimized communication, and HPC/AI infrastructure. His work has been published at SC and ROSS and deployed in advanced AI and HPC environments worldwide.

**Arnav Goel** is a Senior Systems Software Engineer at NVIDIA Corporation, specializing in GPU Communications, Reconfigurable Dataflow Architectures, and High-Performance Networking. He earned an M.S. in Electrical Engineering from the University of Southern California (2016) and a B.Eng. (Honors) in Electrical & Electronics from BITS Pilani, India (2014).
He possesses over eight years of industry experience encompassing enterprise-grade datacenter networking systems (Cisco Nexus ACI, Oracle X5 Server), AI/ML compiler frameworks and distributed training libraries (PyTorch, XLA, Torch Distributed). His technical expertise includes developing communication libraries using userspace networking stacks (RDMA verbs, DPDK ethdev) and system software runtimes for AI accelerators (SambaNova’s RDU) and modern NVIDIA GPUs.
He has authored multiple publications in VLSI Design and SC ROSS, and holds 15+ patents in Reconfigurable DataFlow Architecture, particularly reconfigurable processor-as-a-service systems, network acceleration & runtime virtualization frameworks. Currently, he advances GPU communication libraries, including NVIDIA's NCCL and NVSHMEM, with a continued focus on hardware-software co-design methodologies for next-generation AI and HPC communication architectures.

**Andreas Herten** is a researcher at Jülich Supercomputing Centre heading the Accelerator Devices Lab within the Novel System Architecture Design Division, which he co-leads; he is a lecturer at University of Cologne. He is part of the NVIDIA Application Lab at Jülich, in which he analyses, ports, and optimizes scientific applications for GPUs. He is part of the core JUPITER team to deploy the system. Andreas is also involved in a number of EU-funded projects for improving scalability of accelerated applications and libraries.

**Pouya Kousha** is a Senior HPC Software Developer at NVIDIA, specializing in optimizing HPC communication and performance analysis at scale. His work spans benchmarking and AI workloads to ensure efficient data transfer in large-scale HPC environments.
During his Ph.D. at The Ohio State University he focused on advancing HPC communication through runtime libraries like MVAPICH2 and profiling tools such as OSU INAM. His research centered on designing real-time, scalable profiling tools to identify and resolve communication bottlenecks, critical for system performance. He also integrated conversational AI interfaces to enhance HPC user task execution.
Dr. Kousha has led multiple software releases of OSU INAM and contributed to MVAPICH2, which are widely deployed at HPC centers worldwide. His expertise includes performance analysis, parallel programming, high performance deep learning, and HPC architecture. 