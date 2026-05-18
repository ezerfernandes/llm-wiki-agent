---
title: "Tensor"
type: concept
tags: [math, deep-learning]
sources: [madewithml-baselines, d2l-preliminaries]
last_updated: 2026-05-16
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
