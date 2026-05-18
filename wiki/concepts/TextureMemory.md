---
title: "Texture Memory (CUDA)"
type: concept
tags: [gpu, cuda, memory, image-processing]
sources: [parproc-ch05-cuda-gpu-programming]
last_updated: 2026-05-17
---

# Texture Memory (CUDA)

A read-only-from-device memory tier in [[CUDA]] similar to [[ConstantMemory]] but with **two-dimensional caching** ([[parproc-ch05-cuda-gpu-programming]] §5.4.3.5). The motivating workload is image / stencil access: in row-major storage, `a[i][j]` and `a[i+1][j]` are far apart in linear addresses but are "close" in 2D — texture caching makes them likely to share a cache line.

## Properties

| Property | Value |
|---|---|
| Scope | Global to application |
| Location | Off-chip, with **2D-aware** on-chip cache |
| Speed | Fast if cache hit |
| Lifetime | Application |
| Host access | Yes (read/write) |
| Device access | **Read only** |

## Why 2D caching matters

In conventional cache lines (1D, low-order interleaved), an `M × N` matrix stored row-major has cache hits only along **rows** — column scans miss every load. Texture caching reorganizes the cache geometry so that **neighborhoods** of 2D positions share lines, regardless of access direction. Stencil kernels (image filters, finite-difference solvers) reading `a[i-1][j]`, `a[i+1][j]`, `a[i][j-1]`, `a[i][j+1]` are typical beneficiaries.

## Texture vs constant memory

| Property | Texture | Constant |
|---|---|---|
| Cache geometry | 2D | 1D-style |
| Size limit | Larger | 64K |
| Update pattern | Less frequent | Per-pass |
| Use case | Stencils, image filters, lookup tables | Per-iteration scalars / small arrays |

## See also

- [[ConstantMemory]] — 1D-cached sibling tier.
- [[GlobalMemory]] — read/write counterpart.
- [[GPUMemoryHierarchy]] — full hierarchy.
- [[CUDA]] — parent model.
- [[parproc-ch05-cuda-gpu-programming]] — §5.4.3.5.
