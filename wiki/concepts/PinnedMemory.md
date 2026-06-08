---
title: "Pinned Memory"
type: concept
tags: [frameworks, memory, gpu, data-pipeline]
sources: [mlsysbook-ch07-ml-frameworks]
last_updated: 2026-06-05
---

# Pinned Memory

**Pinned memory** (page-locked host memory) is host RAM that the OS cannot swap to disk, enabling the GPU's copy engine to read directly from it via [[DMA|Direct Memory Access]] without an intermediate copy. Frameworks expose it through `tensor.pin_memory()` and the DataLoader's `pin_memory=True`.

It is the precondition for **asynchronous, non-blocking** host→device transfers: `tensor.to("cuda", non_blocking=True)` returns immediately *only* if the source is pinned — from pageable memory the transfer still blocks, because the copy engine cannot DMA from swappable pages. For a 64×224²×3 FP32 batch (~38 MB), pinned transfer over PCIe 4.0 takes ~1.2 ms vs ~3.0 ms pageable (a 2–3× speedup). The cost is reduced available system memory, since pinned pages cannot be swapped.

## Connections

- [[mlsysbook-ch07-ml-frameworks]] — device/memory management and the data pipeline.
- [[DMA]] / [[CUDAStream]] — the transfer mechanism it enables (overlap copy with compute).
- [[DataLoader]] — exposes `pin_memory=True`; [[CachingAllocator]] — adjacent memory layer.
- [[PCIe]] / [[HBM]] — the bandwidth hierarchy the transfer crosses.
