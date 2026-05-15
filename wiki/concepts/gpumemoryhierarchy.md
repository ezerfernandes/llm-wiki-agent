---
title: "GPU Memory Hierarchy"
type: concept
tags: [gpu, systems, hardware]
sources: [2205.14135-flashattention]
last_updated: 2026-05-10
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

## See also
- [[FlashAttention]]
- [[IOComplexity]]
- [[KernelFusion]]
