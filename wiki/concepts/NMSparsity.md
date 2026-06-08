---
title: "N:M Structured Sparsity"
type: concept
tags: [model-compression, sparsity, hardware, nvidia, mlsysbook]
sources: [mlsysbook-ch10-model-compression]
last_updated: 2026-06-05
---

# N:M Structured Sparsity

**A structured-sparsity format where, in every group of M consecutive elements, exactly N are nonzero and M−N are zero.** Per [[mlsysbook-ch10-model-compression|mlsysbook Ch 10]], the canonical instance is **2:4 sparsity**, introduced commercially with [[NVIDIA]]'s A100 (2020).

## Why 2:4

The ratio halves multiply-accumulate operations while needing only low metadata overhead (~2 bits per nonzero to record which positions participate). The A100 **Sparse Tensor Core** path accelerates 2:4 operands for up to **2× speedup** over dense — *when kernels and layouts satisfy the constraint*. Other ratios are not accelerated by that specific path: the fixed ratio is a hardware constraint, not a mathematical optimum, illustrating that **hardware support is a contract between the sparse format and the execution path.**

## Connections

- [[StructuredSparsity]] / [[Sparsity]] — the broader family.
- [[SparseTensorCore]] — the hardware that exploits 2:4.
- [[Pruning]] — hardware-aware (N:M) structured pruning targets this pattern.
- [[NVIDIA]] — A100 / Ampere introduced it.
- [[mlsysbook-ch10-model-compression]] — source.
