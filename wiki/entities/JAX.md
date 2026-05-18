---
title: "JAX"
type: entity
tags: [tool, deep-learning, framework, autodiff]
sources: [d2l-preface, d2l-preliminaries, d2l-builders-guide]
last_updated: 2026-05-16
---

# JAX

Open-source library from [[google|Google]] for composable function transformations of Python + [[NumPy]] programs — automatic differentiation, JIT compilation, vectorization (`vmap`), and parallelization (`pmap`). Aims for 1:1 parity with the NumPy API so existing code can often be ported by changing a single import statement. Built around an XLA backend; commonly paired with the [[flax|Flax]] neural-network library and [[optax|Optax]] optimizers.

One of four frameworks supported by *Dive into Deep Learning* ([[d2l-preface]]). JAX implementations were adapted from the PyTorch port by Anirudh Dagar.

## Connections
- [[google|Google]] — original developer.
- [[NumPy]] — API parity target.
- [[PyTorch]], [[TensorFlow]], [[MXNet]] — other D2L-supported frameworks.
- [[d2l-preface]] — references JAX as one of D2L's four framework targets.
