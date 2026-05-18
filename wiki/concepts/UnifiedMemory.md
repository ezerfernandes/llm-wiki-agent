---
title: "Unified Memory (CUDA)"
type: concept
tags: [gpu, cuda, memory, programmer-convenience]
sources: [parproc-ch05-cuda-gpu-programming]
last_updated: 2026-05-17
---

# Unified Memory (CUDA)

A [[CUDA]] feature that lets the programmer declare data as `managed` and have CUDA **automatically migrate it between CPU and GPU memory** on demand, eliminating the explicit `cudaMemcpy(...)` pattern ([[parproc-ch05-cuda-gpu-programming]] §5.17.2).

> *"Under the Unified Memory, one can declare some data in one's code to be `managed`, and CUDA will automatically move the data to the proper processor, be it CPU or GPU."*

## How it works

Conceptually:

```c
__managed__ int x[1000];   // accessible from host AND device

// Host code reads x[42]  -> if last touched by GPU, system migrates to CPU
// Device code writes x[42] -> if last touched by CPU, system migrates to GPU
```

Migration granularity and triggers are runtime-implementation details; the programmer sees a single address space.

## Hardware assist from Pascal onward

Starting with the **[[NVIDIAPascal|Pascal]]** architecture, there is hardware support for unified memory *"using something similar to virtual memory page tables"* (§5.17.2). Pre-Pascal implementations relied on coarser-grained software migration with substantial performance penalties; Pascal's page-fault hardware enables on-demand migration at page granularity comparable to CPU virtual memory.

## Performance caveat

*"Again, this is for the convenience of the programmer. Hand coding of the memory-to-memory transfers may be much more efficient."* ([[parproc-ch05-cuda-gpu-programming]] §5.17.2).

Unified memory is a correctness-and-developer-productivity feature, not a performance escape hatch. The CUDA design pattern of *"copy once, compute many"* — explicit `cudaMallocHost` + `cudaMemcpy` + reused-on-device data — remains the high-performance path. Unified memory's value is to enable **incremental porting** of CPU code (`malloc` → `cudaMallocManaged`) without restructuring data ownership.

## Compare to host-device transfer optimization

| Pattern | Setup | Best speed | Programmer effort |
|---|---|---|---|
| `malloc` + `cudaMemcpy` | Plain pageable host memory | Slow transfer (no DMA) | Low |
| `cudaMallocHost` + `cudaMemcpy` | Page-locked host memory | **2× faster** transfer (DMA) | Low |
| `cudaMallocManaged` (Unified) | Pascal+ hardware-assisted | Implicit migration | **Lowest** |

## See also

- [[CUDA]] — parent programming model.
- [[GlobalMemory]] — the device-side counterpart of unified memory transfers.
- [[NVIDIA]] — Pascal introduced hardware assist.
- [[GPUMemoryHierarchy]] — the broader memory layout this hides.
- [[parproc-ch05-cuda-gpu-programming]] — §5.17.2.
