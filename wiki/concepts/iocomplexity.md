---
title: "IO Complexity"
type: concept
tags: [systems, gpu, analysis]
sources: [2205.14135-flashattention]
last_updated: 2026-05-10
---

# IO Complexity

A cost model for algorithms running on hierarchical memory systems that counts **bytes moved between memory levels** rather than arithmetic operations. The framework, originally formalized by Aggarwal & Vitter (1988) for external-memory algorithms, was adapted to GPU deep learning by [[2205.14135-flashattention]].

## Why FLOPs are the wrong cost model on modern GPUs

Compute throughput on GPUs has grown faster than memory bandwidth for two decades. On an A100, on-chip SRAM is ~19 TB/s; HBM is ~1.5–2.0 TB/s; CPU DRAM is ~12.8 GB/s. For memory-bound operations — and in Transformers, **attention is memory-bound** — wall-clock time is determined by HBM accesses, not arithmetic intensity.

A memory-bound operation can have *more* FLOPs and still be faster, if it does *fewer* HBM reads/writes. [[2205.14135-flashattention]] proves this concretely: it recomputes the softmax during the backward pass (more FLOPs than caching) and still beats the standard attention implementation 7.6× on GPT-2 because of the HBM-access reduction.

## Standard vs FlashAttention IO bounds

For sequence length N, head dim d, SRAM size M:

| Algorithm | HBM accesses |
|---|---|
| Standard attention | Θ(Nd + N²) |
| FlashAttention | Θ(N²d²M⁻¹) |
| Block-sparse FlashAttention (sparsity ratio s) | Θ(Nd + N²d²M⁻¹·s) |
| Lower bound for exact attention | Ω(N²d²M⁻¹) |

For typical d (64–128) and M (~100 KB on A100), d²/M is many times smaller than 1, making FlashAttention's bound dominant.

## See also
- [[FlashAttention]]
- [[GpuMemoryHierarchy]]
- [[KernelFusion]]
