---
title: "Linear Combination"
type: concept
tags: [linear-algebra, foundational]
sources: [mml-ch02-linear-algebra, mml-book]
last_updated: 2026-06-04
---

# Linear Combination

**Definition 2.11** ([[mml-ch02-linear-algebra|MML Ch 2]] §2.5): given a [[VectorSpace|vector space]] $V$ and vectors $\mathbf{x}_1,\ldots,\mathbf{x}_k\in V$, every vector of the form

$$\mathbf{v}=\lambda_1\mathbf{x}_1+\cdots+\lambda_k\mathbf{x}_k=\sum_{i=1}^k\lambda_i\mathbf{x}_i\in V,\qquad\lambda_i\in\mathbb{R}$$

is a *linear combination* of $\mathbf{x}_1,\ldots,\mathbf{x}_k$.

The zero vector is always a **trivial** linear combination: $\mathbf{0}=\sum_i 0\cdot\mathbf{x}_i$. The interesting question is whether $\mathbf{0}$ admits a **non-trivial** combination (some $\lambda_i\neq0$) — that is exactly the definition of [[LinearIndependence|linear dependence]].

## Roles

- The matrix–vector product $\mathbf{A}\mathbf{x}$ is the linear combination of the columns of $\mathbf{A}$ with weights $\mathbf{x}$ (MML §2.2.4).
- The [[Span|span]] of a set is the set of *all* its linear combinations.
- [[Coordinates]] express a vector as the unique linear combination of a [[Basis|basis]].

## Connections

- [[LinearIndependence]] — about non-trivial combinations equalling $\mathbf{0}$.
- [[Span]] — set of all linear combinations.
- [[Basis]] — a set whose linear combinations represent every vector uniquely.
- [[MatrixMultiplication]] — $\mathbf{A}\mathbf{x}$ as a combination of columns.
- [[mml-ch02-linear-algebra|MML Ch 2]] / [[mml-book]] — §2.5 canonical reference.
