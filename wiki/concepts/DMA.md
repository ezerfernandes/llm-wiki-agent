---
title: "Direct Memory Access (DMA)"
type: concept
tags: [frameworks, memory, gpu, hardware]
sources: [mlsysbook-ch07-ml-frameworks, mlsysbook-ch11-hardware-acceleration]
last_updated: 2026-06-05
---

# Direct Memory Access (DMA)

**Direct Memory Access (DMA)** lets the GPU's copy engine (memory controller) transfer data over the PCIe bus directly from host RAM without interrupting the CPU. Frameworks coordinate with the CUDA Runtime — acting as the "operating system" of the single node — to implement DMA, using [[PinnedMemory|pinned (page-locked) memory]] so the controller can read host RAM safely while the CPU continues other work.

DMA is what makes high-throughput training loops possible despite the ~64× bandwidth gap between host↔device (PCIe 4.0 ≈ 32 GB/s) and on-device ([[HBM]] ≈ 2 TB/s). Placed on a separate [[CUDAStream|CUDA stream]], a DMA transfer overlaps with computation so effective latency approaches max(compute, transfer) rather than their sum.

## Connections

- [[mlsysbook-ch07-ml-frameworks]] — frameworks as the OS interface; device/memory management.
- [[PinnedMemory]] — the precondition for async DMA.
- [[CUDAStream]] — overlaps DMA with compute; [[CachingAllocator]] — adjacent memory layer.
- [[PCIe]] / [[HBM]] / [[NVLink]] — the interconnect hierarchy.
