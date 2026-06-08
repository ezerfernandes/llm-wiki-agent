---
title: "Structured Sparsity"
type: concept
tags: [model-compression, sparsity, hardware, mlsysbook]
sources: [mlsysbook-ch10-model-compression, mlsysbook-ch11-hardware-acceleration]
last_updated: 2026-06-05
---

# Structured Sparsity

**Sparsity with a regular, predictable pattern — removing entire components (filters, channels, neurons, layers) or enforcing fixed zero patterns — so hardware can actually skip the zeros.** Per [[mlsysbook-ch10-model-compression|mlsysbook Ch 10]], structured sparsity is the preferred form because it produces predictable memory-access patterns that GPUs/TPUs accelerate, unlike [[Sparsity|unstructured sparsity]] which scatters nonzeros and wastes SIMD lanes.

## The break-even contrast

Structured sparsity achieves speedups at ~50% sparsity (nonzeros packed contiguously); unstructured sparsity typically needs **>90–95%** to break even, because the processor cannot skip a zero without first loading it. Block-sparse formats (cuSPARSE, Monarch matrices) and [[NMSparsity|N:M patterns]] (2:4) make the regularity explicit.

## Connections

- [[Sparsity]] / [[NMSparsity]] — the broader concept and the canonical hardware-friendly pattern.
- [[Pruning]] — structured pruning produces structured sparsity.
- [[SparseTensorCore]] — hardware that accelerates structured (2:4) patterns.
- [[mlsysbook-ch10-model-compression]] — source.
- [[mlsysbook-ch11-hardware-acceleration]] — the hardware mechanics: NVIDIA Sparse Tensor Cores implement 2:4 (50% density at the accuracy-performance knee; 4 metadata bits per 4-block) for a theoretical 2× speedup. The principle — "hardware achieves efficiency not by computing zeros faster, but by *never loading them*" — connects sparsity directly to the [[MemoryWall|memory wall]], since structured patterns (vs CSR/random) keep memory access predictable.
