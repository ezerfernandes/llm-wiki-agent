---
title: "Linear Algebra"
type: concept
tags: [math, foundational]
sources: [mml-book, d2l-preliminaries, d2l-appendix-mathematics]
last_updated: 2026-05-16
---

# Linear Algebra

Study of vectors, matrices, and linear mappings between vector spaces. The substrate of every algorithm in machine learning. [[mml-book]] Ch 2 develops the topic mathematically; [[d2l-preliminaries]] §Linear Algebra develops the same material with code in [[PyTorch]] / [[TensorFlow]] / [[JAX]] / [[MXNet]] — scalars → vectors → matrices → higher-order [[Tensor|tensors]] → Hadamard product → reductions → [[DotProduct|dot products]] → matrix–vector and matrix–matrix products → [[Norm|norms]] ($\ell_1$, $\ell_2$, $\ell_p$, Frobenius).

The chain rule (cf. [[ChainRule]]) makes [[LinearAlgebra]] structurally inseparable from deep learning: gradient evaluation reduces to a sequence of vector–matrix products through the layers' Jacobians.
