---
title: "Sparse Tensor Core"
type: concept
tags: [hardware, sparsity, accelerator, nvidia, mlsysbook]
sources: [mlsysbook-ch10-model-compression]
last_updated: 2026-06-05
---

# Sparse Tensor Core

**[[NVIDIA]] Tensor Core hardware (Ampere/A100 and later) that accelerates structured [[NMSparsity|2:4 sparsity]] by physically skipping zero multiplications, up to 2× over dense execution.** Per [[mlsysbook-ch10-model-compression|mlsysbook Ch 10]], this is the hardware that turns the theoretical zeros of [[Pruning|pruning]] into actual speedup — but only when the sparsity pattern matches what the silicon expects.

## The pattern-hardware contract

Unstructured sparsity sees limited benefit on Sparse Tensor Cores; the acceleration requires the regular 2:4 layout. TPUs emphasize dense systolic-array matrix units (sparse benefit is path-dependent), while FPGAs offer the most flexibility for arbitrary sparse formats. Across platforms, sparse ops also cut memory bandwidth and energy by touching fewer elements — a benefit that compounds with [[Quantization|quantization]] (sparse INT8 moves less than either alone).

## Connections

- [[NMSparsity]] / [[StructuredSparsity]] — the patterns it accelerates.
- [[TensorCore]] — the dense matrix-unit baseline it extends.
- [[Sparsity]] — the broader exploitation discipline.
- [[NVIDIA]] — vendor.
- [[mlsysbook-ch10-model-compression]] — source.
