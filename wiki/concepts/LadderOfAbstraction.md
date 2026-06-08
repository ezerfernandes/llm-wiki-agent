---
title: "Ladder of Abstraction (ML Frameworks)"
type: concept
tags: [frameworks, history, abstraction]
sources: [mlsysbook-ch07-ml-frameworks]
last_updated: 2026-06-05
---

# Ladder of Abstraction (ML Frameworks)

The **Ladder of Abstraction** is the mlsysbook framing of how ML frameworks evolved over four decades, each rung automating what the rung below exposed:

1. **Solving performance (1979–1992)** — **BLAS** standardized low-level linear-algebra primitives; **LAPACK** built higher-level routines (SVD, eigendecomposition) on top. Stable interfaces let frameworks delegate `C = A @ B` ([[GEMM]]) to vendor-tuned implementations (e.g. [[CUBLAS|cuBLAS]]).
2. **Solving usability (2006)** — **[[NumPy]]** wrapped BLAS in high-level Python, creating the "vectorization contract" (logic in Python, loops in C/Fortran). PyTorch/TF tensors are direct descendants.
3. **Solving differentiation (2015–)** — deep-learning frameworks ([[Theano]] 2007, [[TensorFlow]] 2015, [[PyTorch]] 2016, [[JAX]] 2018) turned the chain rule into a software primitive via the [[ComputationalGraph|computational graph]] and [[AutomaticDifferentiation|autodiff]].

Each generation gains *productivity* but loses *transparency*: BLAS hid assembly but fixed the interface; NumPy hid memory management but required manual differentiation; modern frameworks hide gradient computation but introduce the [[EagerExecution|execution-model]] choice. The timeline (BLAS→LAPACK→NumPy→Theano→TensorFlow→PyTorch→JAX) frames frameworks as bridging mathematical intent and silicon reality.

## Connections

- [[mlsysbook-ch07-ml-frameworks]] — the historical evolution section.
- [[NumPy]] / [[GEMM]] / [[CUBLAS]] — the lower rungs.
- [[Theano]] / [[TensorFlow]] / [[PyTorch]] / [[JAX]] — the deep-learning rung.
- [[ComputationalGraph]] / [[AutomaticDifferentiation]] — the differentiation primitive added at the top.
