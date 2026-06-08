---
title: "Caching Allocator"
type: concept
tags: [frameworks, memory, gpu, runtime]
sources: [mlsysbook-ch07-ml-frameworks]
last_updated: 2026-06-05
---

# Caching Allocator

A **caching allocator** is the framework's memory-management abstraction that maximizes the hardware-utilization factor $\eta_{\text{hw}}$ in the [[IronLawOfMLSystems|iron law]]. Instead of calling the device allocator for every tensor, the framework requests large blocks of GPU memory upfront and manages its own internal pool, subdividing and reusing freed blocks without returning them to the driver. PyTorch's caching allocator is the canonical example.

It addresses two costs:

1. **Allocation latency** — `cudaMalloc` is synchronous (10–100 μs, can stall the whole device); the allocator pays this once, then serves subsequent requests in nanoseconds from its pool.
2. **[[MemoryFragmentation|Fragmentation]]** — by binning allocations into power-of-2 sizes, it ensures freed memory is reusable. Without this, a "Swiss cheese" pattern arises where 10 GB is free but the largest contiguous block is too small for a 2 GB tensor.

This is why **OOM errors appear despite `nvidia-smi` showing free memory** — fragmentation, not absolute capacity, is the culprit.

## Connections

- [[mlsysbook-ch07-ml-frameworks]] — memory management in gradient computation; system-level operations.
- [[PinnedMemory]] / [[DMA]] — adjacent memory mechanisms for host↔device transfer.
- [[MemoryWall]] / [[HBM]] — the bandwidth/capacity constraints it works within.
- [[PyTorch]] — implements the canonical caching allocator.
