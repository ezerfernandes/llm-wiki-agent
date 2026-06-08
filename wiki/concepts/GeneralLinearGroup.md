---
title: "General Linear Group"
type: concept
tags: [algebra, linear-algebra, matrix-algebra]
sources: [mml-ch02-linear-algebra, mml-book]
last_updated: 2026-06-04
---

# General Linear Group

**Definition 2.8** ([[mml-ch02-linear-algebra|MML Ch 2]] §2.4.1): the set of regular (invertible) matrices $\mathbf{A}\in\mathbb{R}^{n\times n}$ is a [[GroupTheory|group]] with respect to [[MatrixMultiplication|matrix multiplication]], called the *general linear group* $GL(n,\mathbb{R})$.

- **Neutral element**: the [[IdentityMatrix|identity matrix]] $\mathbf{I}_n$.
- **Inverse element**: the [[MatrixInverse|matrix inverse]] $\mathbf{A}^{-1}$, which exists precisely because the elements are regular.
- **Not Abelian**: matrix multiplication is non-commutative ($\mathbf{AB}\neq\mathbf{BA}$ in general), so $GL(n,\mathbb{R})$ is a non-commutative group.

Closure and associativity follow directly from the definition of matrix multiplication; singular matrices must be excluded because they lack inverses. Contrast with $(\mathbb{R}^{n\times n},+)$, which **is** an Abelian group (additive inverses always exist).

## Connections

- [[GroupTheory]] — $GL(n,\mathbb{R})$ is the canonical non-Abelian group example.
- [[MatrixInverse]] / [[IdentityMatrix]] / [[MatrixMultiplication]] — its operation and elements.
- [[Determinant]] — $\mathbf{A}\in GL(n,\mathbb{R})$ iff $\det(\mathbf{A})\neq0$.
- [[Rank]] — $\mathbf{A}\in GL(n,\mathbb{R})$ iff $\operatorname{rk}(\mathbf{A})=n$.
- [[mml-ch02-linear-algebra|MML Ch 2]] / [[mml-book]] — §2.4.1 canonical reference.
