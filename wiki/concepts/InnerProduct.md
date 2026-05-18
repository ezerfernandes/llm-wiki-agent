---
title: "Inner Product"
type: concept
tags: [analytic-geometry, linear-algebra, foundational]
sources: [mml-book, d2l-preliminaries, d2l-appendix-mathematics]
last_updated: 2026-05-16
---

# Inner Product

A **bilinear**, **symmetric**, **positive-definite** mapping $\langle\cdot,\cdot\rangle:V\times V\to\mathbb{R}$ ([[mml-book]] Def. 3.3). The dot product $\mathbf{x}^\top\mathbf{y}=\sum x_iy_i$ on $\mathbb{R}^n$ is the canonical example, but it is not the only one — *any* symmetric positive-definite matrix $\mathbf{A}$ defines an inner product $\langle\mathbf{x},\mathbf{y}\rangle := \hat{\mathbf{x}}^\top\mathbf{A}\hat{\mathbf{y}}$ in coordinates with respect to some basis.

## The three axioms

1. **Bilinear**: linear in each argument.
2. **Symmetric**: $\langle\mathbf{x},\mathbf{y}\rangle = \langle\mathbf{y},\mathbf{x}\rangle$.
3. **Positive-definite**: $\langle\mathbf{x},\mathbf{x}\rangle\geq 0$, with equality iff $\mathbf{x}=\mathbf{0}$.

## What inner products give you

Adding an inner product to a vector space gives **geometry** on top of pure algebra ([[mml-book]] §3.3–3.4):

| Concept | Definition via inner product |
|---|---|
| [[Norm]] (length) | $\|\mathbf{x}\| := \sqrt{\langle\mathbf{x},\mathbf{x}\rangle}$ |
| Distance | $d(\mathbf{x},\mathbf{y}) := \|\mathbf{x}-\mathbf{y}\|$ |
| Angle | $\cos\omega := \frac{\langle\mathbf{x},\mathbf{y}\rangle}{\|\mathbf{x}\|\,\|\mathbf{y}\|}$ |
| Orthogonality | $\langle\mathbf{x},\mathbf{y}\rangle = 0$ |
| [[OrthogonalProjection]] | $\pi_U(\mathbf{x}) = \mathbf{U}(\mathbf{U}^\top\mathbf{U})^{-1}\mathbf{U}^\top\mathbf{x}$ |

The [[CauchySchwarzInequality]] $|\langle\mathbf{x},\mathbf{y}\rangle|\leq\|\mathbf{x}\|\,\|\mathbf{y}\|$ is what makes the angle definition well-formed.

## SPD matrices ↔ inner products

[[mml-book]] Theorem 3.5: *for a finite-dimensional real vector space $V$ and an ordered basis, $\langle\cdot,\cdot\rangle:V\times V\to\mathbb{R}$ is an inner product if and only if there exists a [[SymmetricPositiveDefiniteMatrix|symmetric positive-definite matrix]] $\mathbf{A}$ with $\langle\mathbf{x},\mathbf{y}\rangle = \hat{\mathbf{x}}^\top\mathbf{A}\hat{\mathbf{y}}$.*

This is the load-bearing identification underneath kernel methods (Ch 12.4): a [[Kernel]] $k(\mathbf{x},\mathbf{y})$ is admissible iff its Gram matrix is symmetric positive-(semi)definite.

## ML uses

- **Cosine similarity** for embeddings ($\cos\omega$ between sentence/word/image vectors).
- **Least-squares regression** is orthogonal projection onto the column space of the design matrix ([[mml-book]] §9.4).
- **PCA** maximizes variance under an inner-product-defined notion of "spread."
- **SVM kernel trick** lifts inputs into an inner-product space without computing the lift explicitly.

## Connections

- [[mml-book]] — §3.2 canonical reference.
- [[Norm]] — induced by every inner product.
- [[CauchySchwarzInequality]] — the inequality that makes angles work.
- [[OrthogonalProjection]] — the operation that decomposes vectors against subspaces.
- [[SymmetricPositiveDefiniteMatrix]] — the matrix form of an inner product.
- [[KernelTrick]] — generalizes inner products to feature maps.
