---
title: "Linear Algebra"
type: concept
tags: [math, foundational]
sources: [mml-book, mml-ch02-linear-algebra, d2l-preliminaries, d2l-appendix-mathematics]
last_updated: 2026-06-04
---

# Linear Algebra

Study of vectors, matrices, and linear mappings between vector spaces. The substrate of every algorithm in machine learning. [[mml-book]] Ch 2 develops the topic mathematically; [[d2l-preliminaries]] §Linear Algebra develops the same material with code in [[PyTorch]] / [[TensorFlow]] / [[JAX]] / [[MXNet]] — scalars → vectors → matrices → higher-order [[Tensor|tensors]] → Hadamard product → reductions → [[DotProduct|dot products]] → matrix–vector and matrix–matrix products → [[Norm|norms]] ($\ell_1$, $\ell_2$, $\ell_p$, Frobenius).

The chain rule (cf. [[ChainRule]]) makes [[LinearAlgebra]] structurally inseparable from deep learning: gradient evaluation reduces to a sequence of vector–matrix products through the layers' Jacobians.

## From [[mml-ch02-linear-algebra|MML Ch 2]]

MML's opening definition (p. 17): "Linear algebra is the study of vectors and certain rules to manipulate vectors." A *vector* is any object closed under addition and scalar multiplication — geometric vectors, [[VectorSpace|polynomials, audio signals]], and $\mathbb{R}^n$ tuples all qualify. The chapter is organized around **closure** (the [[VectorSpace|vector space]]) and develops bottom-up:

- [[SystemOfLinearEquations]] → [[Matrix]] algebra → [[GaussianElimination]] / [[ReducedRowEchelonForm]] (solving, inverting);
- [[GroupTheory|Group]] → [[VectorSpace]] → [[VectorSubspace]] (the algebraic scaffolding);
- [[LinearIndependence]] → [[Span]] → [[Basis]] → [[Dimension]] → [[Rank]] (internal structure);
- [[LinearMapping]] → [[TransformationMatrix]] → [[BasisChange]], with [[Image]] / [[NullSpace]] and the [[RankNullityTheorem]];
- [[AffineSpace]] / [[AffineMapping]] (spaces offset from the origin).

The full chapter mind map (Fig. 2.2) and a per-section breakdown live on the deep-dive page [[mml-ch02-linear-algebra|MML Ch 2 — Linear Algebra]]. Geometry (inner products, norms, angles, projections) is deferred to Ch 3.
