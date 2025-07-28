---

---
# GPU Communication Libraries for Accelerating HPC and AI Applications @ HotI 2025


## Abstract

This tutorial provides a comprehensive introduction to two advanced GPU communication libraries: NVIDIA Collective Communication Library (NCCL) and NVSHMEM. Designed for researchers, engineers, and developers working on HPC and deep learning, the session explores the core concepts, programming models, and practical use cases of both libraries. 

NCCL is optimized for collective and point-to-point communication among GPUs, offering high throughput and low latency by leveraging hardware features such as NVLink, PCIe, and RDMA networking (InfiniBand, RoCE, etc). It is widely used for distributed deep learning and scientific computing, enabling efficient data movement and synchronization across multiple GPUs within and across nodes. 

NVSHMEM, on the other hand, implements a Partitioned Global Address Space (PGAS) model for NVIDIA GPUs, supporting one-sided communication and fine-grained data exchange. It enables both host- and device-initiated operations, allowing for asynchronous, in-kernel communication and efficient overlap of computation and communication. NVSHMEM is particularly suited for irregular communication patterns and workloads requiring low-latency, fine-grained GPU-initiated operations. 

Through hands-on examples we elaborate on the new features in both libraries, participants will gain practical skills in leveraging NCCL and NVSHMEM to accelerate multi-GPU applications, understand their interoperability, and select the right tool for diverse HPC and DL scenarios.

## Presenters
- **Benjamin Glick**, NVIDIA 
- **Arnav Goel**, NVIDIA
- **Andreas Herten**, Jülich Supercomputing Centre
- **Pouya Kousha**, NVIDIA 

## Tutorial Outline 
1. **Introduction to NCCL & NVSHMEM**
2. **NCCL API Walkthrough with Examples** 
3. **NVSHMEM API Walkthrough with Examples** 
4. **Advanced Features For GPU Communication Libraries** — NCCL Symmetric Memory Kernels, NVSHMEM Python Language Bindings
5. **Hands-on Session**
6. **Conclusions, Final Q&A, and Discussion**  
