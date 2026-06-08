---
title: "Sparsity"
type: concept
tags: [model-compression, pruning, hardware, optimization, mlsysbook]
sources: [ai-engineering-ch09-inference-optimization, mlsysbook-ch10-model-compression, mlsysbook-ch11-hardware-acceleration]
last_updated: 2026-06-05
---

# Sparsity

**The fraction of zero-valued parameters in a model's weights.** Produced primarily by [[Pruning|parameter-zeroing pruning]]; only exploitable when the hardware (and kernel) supports sparse matrix operations. Per [[ai-engineering-ch09-inference-optimization|*AI Engineering* Ch 9]]:

> *"In this case, pruning doesn't reduce the total number of parameters, only the number of non-zero parameters. This makes the model more sparse, which both reduces the model's storage space and speeds up computation."*

## Why hardware matters

> *"Not all hardware architectures are designed to take advantage of the resulting sparsity."* — Ch 9

A 50%-sparse tensor on a dense GPU kernel still costs 100% of the compute. **NVIDIA Ampere (A100) and later** include "structured sparsity" support (2:4 pattern — 2 of every 4 elements zero), with corresponding tensor-core paths. Outside that pattern, sparsity often doesn't accelerate anything.

The H100 SXM Table 9-2 in Ch 9 reports FLOP/s "with sparsity" — i.e. when the workload conforms to the 2:4 sparsity pattern, the chip can deliver up to 2× the dense FLOP/s. This is where the "peak FLOP/s hacking" critique applies (chip makers prefer to advertise the sparse number).

## Sparsity vs other compression

- **[[Pruning]]** → sparsity (sometimes).
- **[[Quantization]]** → fewer bytes per parameter; orthogonal to sparsity.
- **[[knowledgedistillation|Distillation]]** → fewer total parameters; orthogonal to sparsity.

Sparsity and quantization can stack — a 50%-sparse INT8 model uses **¼** the bytes/FLOPs of a dense FP16 baseline. But composition requires hardware that handles both.

## "Peak FLOP/s hacking" connection

Ch 9 footnote 12:

> *"Chip makers might also be doing what I call peak FLOP/s hacking. This might run experiments in certain conditions, such as using sparse matrices with specific shapes, to increase their peak FLOP/s. Higher peak FLOP/s numbers make their chips more attractive, but it can be harder for users to achieve high MFU."*

Sparsity is one of the main vehicles for this gap between marketing peak FLOP/s and achievable [[MFU|MFU]].

## Exploitation vs storage ([[mlsysbook-ch10-model-compression|mlsysbook Ch 10]])

Ch 10 draws a sharp line: **[[Pruning|pruning]] reduces what we *store*; sparsity exploitation reduces what we *compute*.** The processor cannot skip a multiplication unless it knows the operand is zero — and discovering that requires loading it first. Hence:

- **Unstructured sparsity** typically must exceed **90–95%** to beat dense kernels (a 16-wide SIMD register may yield only 1–2 nonzeros, wasting 14–15 lanes). CSR storage breaks even ~50% density, COO ~33%, before index overhead.
- **[[StructuredSparsity|Structured sparsity]]** ([[NMSparsity|N:M / 2:4]], block-sparse via cuSPARSE, Monarch matrices) earns speedup at ~50% because nonzeros pack contiguously — the **pattern-hardware contract**.
- Platform reality: [[SparseTensorCore|GPU Sparse Tensor Cores]] (Ampere+) accelerate 2:4; TPUs favor dense systolic arrays (path-dependent); FPGAs handle arbitrary patterns. Sparse INT8 moves less than either technique alone.

MegaBlocks reformulates sparse MoE training into block-sparse ops to keep accelerator utilization high. [[mlsysbook-ch10-model-compression]]

## Connections

- [[Pruning]] — the technique that produces sparsity.
- [[StructuredSparsity]] / [[NMSparsity]] / [[SparseTensorCore]] — the hardware-friendly patterns and units (mlsysbook Ch 10).
- [[mlsysbook-ch10-model-compression]] — sparsity exploitation vs storage; break-even thresholds.
- [[ModelCompression]] — umbrella family.
- [[Quantization]] — orthogonal compression lever.
- [[TensorCore]] — Ampere/Hopper's sparsity-aware compute units.
- [[MFU]] — the metric where sparsity claims interact with achievable performance.
- [[SparseMatrix]] — adjacent linear-algebra concept.
- [[InferenceOptimization]] — broader discipline.
- [[ai-engineering-ch09-inference-optimization]] — primary source.
