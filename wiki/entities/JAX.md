---
title: "JAX"
type: entity
tags: [tool, deep-learning, framework, autodiff]
sources: [d2l-preface, d2l-preliminaries, d2l-builders-guide, mlsysbook-ch07-ml-frameworks]
last_updated: 2026-06-05
---

# JAX

Open-source library from [[google|Google]] for composable function transformations of Python + [[NumPy]] programs — automatic differentiation, JIT compilation, vectorization (`vmap`), and parallelization (`pmap`). Aims for 1:1 parity with the NumPy API so existing code can often be ported by changing a single import statement. Built around an XLA backend; commonly paired with the [[flax|Flax]] neural-network library and [[optax|Optax]] optimizers.

One of four frameworks supported by *Dive into Deep Learning* ([[d2l-preface]]). JAX implementations were adapted from the PyTorch port by Anirudh Dagar.

## From [[mlsysbook-ch07-ml-frameworks|mlsysbook Vol 1 Ch 7]]

Ch 7 frames JAX as the **functional transformation engine** that *reframes* the differentiation problem. Because functions are **pure** (no side effects, immutable arrays), `grad(f)` returns a new *function* rather than a value, and transformations compose arbitrarily: `pmap(jit(vmap(grad(f))))` expresses distributed, compiled, batched gradient computation as one expression — compiling to a single [[XLA]] kernel at **>90% TPU utilization**. The cost: a steeper learning curve, explicit parameter management, and any impurity (printing, mutation, unkeyed randomness) silently vanishing after the first JIT trace. Contrasts with PyTorch's [[Autograd|tape-based]] autodiff (Ch 7's "tape-based vs transform-based" distinction).

## Connections
- [[google|Google]] — original developer.
- [[NumPy]] — API parity target.
- [[Flax]] — its neural-network library; [[XLA]] — its compiler backend.
- [[PyTorch]], [[TensorFlow]], [[MXNet]] — other D2L-supported frameworks.
- [[d2l-preface]] — references JAX as one of D2L's four framework targets.
- [[mlsysbook-ch07-ml-frameworks]] — analyzes JAX as the differentiation-reframing platform.
