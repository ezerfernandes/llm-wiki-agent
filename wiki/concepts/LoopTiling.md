---
title: "Loop Tiling"
type: concept
tags: [compiler, kernel, optimization, memory]
sources: [ai-engineering-ch09-inference-optimization]
last_updated: 2024-12-04
---

# Loop Tiling

**Reordering the data access pattern in a loop to match the hardware's memory hierarchy and cache layout.** One of four kernel-writing techniques named in [[ai-engineering-ch09-inference-optimization|*AI Engineering* Ch 9]]:

> *"Optimize the data accessing order in a loop for the hardware's memory layout and cache. This optimization is hardware-dependent. An efficient CPU tiling pattern may not work well on GPUs."*

## What loop tiling does

Naive nested loops (matrix multiply, convolution) often access memory in patterns that thrash caches and incur unnecessary memory loads. Tiling rewrites the loop to process **blocks** (tiles) that fit in a fast level of the memory hierarchy (L1 cache on CPU; on-chip SRAM on GPU), reusing data within the tile before moving on.

Conceptually: instead of computing all output positions one at a time, compute a tile-sized rectangle, keeping its inputs in fast memory for the duration.

## Hardware-dependent

> *"An efficient CPU tiling pattern may not work well on GPUs."* — Ch 9

CPU tiling targets L1/L2 cache lines and TLB friendliness. GPU tiling targets shared memory (on-chip SRAM) sizes, warp sizes, and tensor-core tile shapes. The two have nothing in common — which is part of why kernel writing is so hardware-specific.

## Loop tiling in famous kernels

- **[[FlashAttention|FlashAttention]]** — its central insight is tiling Q, K, V into blocks that fit in on-chip SRAM, recomputing the partial softmax statistics rather than materializing the full N×N matrix in HBM. This is loop tiling at scale.
- **cuBLAS / cuDNN matrix-multiply kernels** — heavily tiled for tensor-core 16×16×16 shapes on Volta+.

## Connections

- [[FlashAttention]] — canonical loop-tiling exemplar at the LLM scale.
- [[OperatorFusion]] / [[Vectorization]] — sibling kernel techniques.
- [[Kernel]] — what loop tiling produces.
- [[SRAM]] / [[HBM]] — the memory hierarchy loop tiling exploits.
- [[gpumemoryhierarchy]] — adjacent existing concept page.
- [[Compiler]] / [[Lowering]] — where compilers apply tiling automatically.
- [[InferenceOptimization]] — broader discipline.
- [[ai-engineering-ch09-inference-optimization]] — primary source.
