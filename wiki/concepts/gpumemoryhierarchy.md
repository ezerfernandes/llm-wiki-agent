---
title: "GPU Memory Hierarchy"
type: concept
tags: [gpu, systems, hardware]
sources: [2205.14135-flashattention, d2l-computational-performance, parproc-ch05-cuda-gpu-programming]
last_updated: 2026-05-17
---

# GPU Memory Hierarchy

GPUs expose multiple tiers of memory of different sizes and bandwidths. Algorithms that ignore this asymmetry pay for it in wall-clock time, even when their FLOP count looks favorable. [[2205.14135-flashattention]] makes the hierarchy explicit as the cost model for attention.

## NVIDIA A100 reference

| Tier | Size | Bandwidth |
|---|---|---|
| On-chip SRAM (per SM) | 192 KB | ~19 TB/s |
| HBM (high-bandwidth memory) | 40–80 GB | 1.5–2.0 TB/s |
| CPU DRAM | >1 TB | ~12.8 GB/s |

SRAM is **~10× faster** than HBM and **~1500× faster** than CPU DRAM, but only ~200 KB per streaming multiprocessor — many orders of magnitude smaller than HBM.

## Execution model

A GPU kernel loads inputs from HBM into registers and SRAM, computes, and writes outputs back to HBM. Operations are characterized by **arithmetic intensity** (FLOPs per byte loaded):

- **Compute-bound:** runtime determined by FLOPs. Examples: matmul with large inner dim.
- **Memory-bound:** runtime determined by HBM accesses. Examples: softmax, layer norm, dropout, attention (in the standard implementation).

Most non-matmul operations in Transformers are memory-bound, which is the wedge [[FlashAttention]] exploits: rearrange the algorithm so SRAM holds the working set, write only the final result to HBM.

## CUDA tier nomenclature (programmer view)

[[parproc-ch05-cuda-gpu-programming]] §5.4.3 gives the **programmer-facing** memory taxonomy underneath the SRAM/HBM hardware-tier view:

| CUDA tier | Hardware tier | Scope | Speed | Notes |
|---|---|---|---|---|
| Registers | On-chip SRAM | Per-thread | Fast | Most numerous storage on the SM |
| [[SharedMemory]] | On-chip SRAM | Per-[[Block|block]] | Fast | Programmer-managed cache; 16K/SM on Tesla |
| [[ConstantMemory]] | Off-chip + on-chip cache | Per-app | Fast on hit | 64K, device-read / host-write |
| [[TextureMemory]] | Off-chip + on-chip cache | Per-app | Fast on hit | **2D-aware** caching |
| [[GlobalMemory]] (HBM) | Off-chip HBM | Per-app | Slow (hundreds of cycles) | The bulk store; cached on Fermi+ |
| Local | Off-chip HBM | Per-thread | Slow | Misleading name — **physically global**; [[RegisterSpill|register spill]] target |
| [[UnifiedMemory|Managed]] | Migrated | Per-app, host+device | — | Hardware-assisted on Pascal+ |

Same hierarchy as the SRAM/HBM table above; this view exposes the programmer-API names that map onto each hardware tier. The [[FlashAttention]] cost model uses the *hardware* names (SRAM, HBM); CUDA kernels are written in terms of the *programmer* names (`__shared__`, `cudaMalloc`-allocated buffers in global, `__constant__`, etc.).

[[MemoryCoalescing|Coalescing]] (half-warp consecutive-word global accesses) and bank-conflict avoidance (shared-memory low-order interleaving) are the two big bandwidth optimizations specific to this hierarchy.

## See also
- [[FlashAttention]]
- [[IOComplexity]]
- [[KernelFusion]]
- [[CUDA]] — programming model exposing this hierarchy.
- [[SharedMemory]] / [[GlobalMemory]] / [[ConstantMemory]] / [[TextureMemory]] / [[UnifiedMemory]] — per-tier pages.
- [[parproc-ch05-cuda-gpu-programming]] — Matloff's full hierarchy walkthrough.
