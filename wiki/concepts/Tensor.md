---
title: "Tensor"
type: concept
tags: [math, deep-learning]
sources: [madewithml-baselines, d2l-preliminaries, mlsysbook-ch07-ml-frameworks]
last_updated: 2026-06-05
---

# Tensor

A multidimensional array generalizing scalars (0th-order), vectors (1st-order), and matrices (2nd-order). The fundamental data structure of [[NeuralNetwork]] frameworks ([[PyTorch]], [[TensorFlow]], [[JAX]], [[MXNet]]), closely related to the [[NDArray]] from [[NumPy]].

## What the framework tensor adds over NumPy's ndarray

[[d2l-preliminaries]] §Data Manipulation calls out two "killer features" that distinguish framework tensors from plain ndarrays:

1. **[[Autograd|Automatic differentiation]]** — every operation is recorded on a [[ComputationalGraph|computational graph]] so gradients can be computed by reverse-mode chain rule.
2. **GPU acceleration** — operations dispatch to CUDA/Metal/TPU kernels; NumPy is CPU-only.

The API surface is otherwise deliberately NumPy-shaped: `arange`, `zeros`, `ones`, `randn`, `reshape`, indexing, slicing, broadcasting, elementwise arithmetic, reductions (`sum`, `mean`, `cumsum`), `cat`/`concat`, `T` (transpose), `@` / `matmul`.

## Order vs dimensionality

D2L distinguishes **order** (number of axes — what `len(tensor.shape)` returns) from **dimensionality** (length along a particular axis). Avoids the overloaded word "dimension". Images are 3rd-order ($H\times W\times C$); image batches are 4th-order ($B\times H\times W\times C$).

## Systems view from [[mlsysbook-ch07-ml-frameworks|mlsysbook Vol 1 Ch 7]]

Ch 7 defines a framework tensor as an $n$-dimensional array carrying explicit **shape + dtype + device + [[Stride|stride]] metadata** that maps math operations onto hardware vector units without runtime type checking. Memory footprint is fully deterministic (a contiguous 1024×1024 FP32 tensor = exactly 4,194,304 bytes ≈ 4.2 MB). Layout matters: non-contiguous (post-transpose) tensors need `.contiguous()` copies, and choosing NCHW when hardware prefers NHWC can *halve* throughput by breaking coalescing ([[MemoryLayout]]). The dtype is the lever trading numerical range against data movement (FP32 training, FP16/INT8 inference). The word *tensor* comes from Latin *tendere* ("to stretch"), coined by physicist Woldemar Voigt (1898) for objects defined by transformation behavior.

## Connections

- [[mlsysbook-ch07-ml-frameworks]] — tensor as the universal data container of the abstraction problem.
- [[MemoryLayout]] / [[Stride]] — physical layout and index→address mapping.
- [[PyTorch]] / [[TensorFlow]] / [[JAX]] — implementing frameworks; [[NumPy]] — the ndarray ancestor.
