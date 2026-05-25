---
title: "Sparsity"
type: concept
tags: [model-compression, pruning, hardware, optimization]
sources: [ai-engineering-ch09-inference-optimization]
last_updated: 2024-12-04
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

## Connections

- [[Pruning]] — the technique that produces sparsity.
- [[ModelCompression]] — umbrella family.
- [[Quantization]] — orthogonal compression lever.
- [[TensorCore]] — Ampere/Hopper's sparsity-aware compute units.
- [[MFU]] — the metric where sparsity claims interact with achievable performance.
- [[SparseMatrix]] — adjacent linear-algebra concept.
- [[InferenceOptimization]] — broader discipline.
- [[ai-engineering-ch09-inference-optimization]] — primary source.
