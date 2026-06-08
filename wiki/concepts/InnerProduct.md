---
title: "Inner Product"
type: concept
tags: [analytic-geometry, linear-algebra, foundational]
sources: [mml-ch03-analytic-geometry, mml-book, d2l-preliminaries, d2l-appendix-mathematics]
last_updated: 2026-06-04
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

## From [[mml-ch03-analytic-geometry|MML Ch 3]]

The chapter builds the definition in stages (§3.2):

1. A **[[BilinearForm|bilinear mapping]]** $\Omega:V\times V\to\mathbb{R}$ is linear in each argument (Eqs. 3.6–3.7).
2. **Definition 3.2**: it is *symmetric* if $\Omega(\mathbf{x},\mathbf{y})=\Omega(\mathbf{y},\mathbf{x})$, *positive definite* if $\Omega(\mathbf{x},\mathbf{x})>0$ for $\mathbf{x}\neq\mathbf{0}$ (Eq. 3.8).
3. **Definition 3.3**: a positive-definite, symmetric bilinear form *is* an inner product, written $\langle\mathbf{x},\mathbf{y}\rangle$. The pair $(V,\langle\cdot,\cdot\rangle)$ is an *inner product space*; with the dot product it is a *Euclidean vector space*.

The **[[DotProduct]]** $\mathbf{x}^\top\mathbf{y}=\sum_i x_iy_i$ (Eq. 3.5) is the canonical — but not the only — inner product. **Example 3.3** gives a non-dot-product inner product on $\mathbb{R}^2$: $\langle\mathbf{x},\mathbf{y}\rangle=x_1y_1-(x_1y_2+x_2y_1)+2x_2y_2$.

**Geometry it induces** (§3.3–3.4): [[Norm]] $\|\mathbf{x}\|=\sqrt{\langle\mathbf{x},\mathbf{x}\rangle}$, [[Metric]] $d(\mathbf{x},\mathbf{y})=\|\mathbf{x}-\mathbf{y}\|$, [[Angle]] $\cos\omega=\frac{\langle\mathbf{x},\mathbf{y}\rangle}{\|\mathbf{x}\|\|\mathbf{y}\|}$, and [[Orthogonality]] ($\langle\mathbf{x},\mathbf{y}\rangle=0$). **Key subtlety**: lengths, angles, and orthogonality depend on the *choice* of inner product (Examples 3.5, 3.7) — they are not intrinsic to the vectors. Inner product and metric move in *opposite directions*: similar vectors → large inner product, small distance (Remark, p. 76). Inner products also extend to functions (§3.7, [[InnerProductOfFunctions]]) by turning the sum into an integral.

## Connections

- [[mml-ch03-analytic-geometry]] / [[mml-book]] — §3.2 canonical reference (Defs. 3.2–3.3).
- [[BilinearForm]] — an inner product is a symmetric, positive-definite bilinear form.
- [[DotProduct]] — the canonical inner product (Euclidean space).
- [[Norm]] / [[Metric]] / [[Angle]] / [[Orthogonality]] — the geometry an inner product induces.
- [[CauchySchwarzInequality]] — the inequality that makes angles work.
- [[OrthogonalProjection]] — the operation that decomposes vectors against subspaces.
- [[SymmetricPositiveDefiniteMatrix]] — the matrix form of an inner product (Thm 3.5).
- [[InnerProductOfFunctions]] — the infinite-dimensional generalization.
- [[KernelTrick]] — generalizes inner products to feature maps.
