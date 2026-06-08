---
title: "Orthogonal Complement"
type: concept
tags: [analytic-geometry, linear-algebra, foundational]
sources: [mml-ch03-analytic-geometry, mml-book]
last_updated: 2026-06-04
---

# Orthogonal Complement

For a $D$-dimensional inner-product space $V$ and an $M$-dimensional subspace $U\subseteq V$, the **orthogonal complement** $U^\perp$ is the $(D-M)$-dimensional subspace of $V$ containing **all vectors orthogonal to every vector in $U$** ([[mml-ch03-analytic-geometry|MML Ch 3]] §3.6).

Two fundamental facts:

- $U\cap U^\perp=\{\mathbf{0}\}$ — the only vector in both is $\mathbf{0}$.
- **Unique decomposition** (Eq. 3.36): every $\mathbf{x}\in V$ splits uniquely as
$$\mathbf{x}=\sum_{m=1}^{M}\lambda_m\mathbf{b}_m+\sum_{j=1}^{D-M}\psi_j\mathbf{b}_j^\perp,$$
where $(\mathbf{b}_1,\ldots,\mathbf{b}_M)$ is a basis of $U$ and $(\mathbf{b}_1^\perp,\ldots,\mathbf{b}_{D-M}^\perp)$ a basis of $U^\perp$. The first sum is exactly the [[OrthogonalProjection|orthogonal projection]] $\pi_U(\mathbf{x})$; the second is the projection error.

## Normal vectors and hyperplanes

In a 3-D space, a plane $U$ (2-dim subspace) has a 1-dim orthogonal complement spanned by a unit vector $\mathbf{w}$ ($\|\mathbf{w}\|=1$): the **normal vector** of $U$ ([[mml-book]] Fig. 3.7, p. 80). All vectors orthogonal to $\mathbf{w}$ lie in $U$. Generally, orthogonal complements describe **[[Hyperplane|hyperplanes]]** in $n$-dimensional vector and affine spaces — the substrate for the [[SeparatingHyperplane|separating hyperplane]] of the SVM (Ch 12).

## ML uses

- **Separating hyperplane / SVM** — a hyperplane is defined by its normal vector $\mathbf{w}$, the basis of the 1-D orthogonal complement ([[mml-book]] §12.1).
- **Residual analysis in regression** — the least-squares residual lives in the orthogonal complement of the column space of the design matrix.
- **PCA** — the discarded directions form the orthogonal complement of the principal subspace (Ch 10).

## Connections

- [[mml-ch03-analytic-geometry]] — §3.6 canonical reference.
- [[Orthogonality]] — $U^\perp$ collects everything orthogonal to $U$.
- [[OrthogonalProjection]] — the decomposition splits $\mathbf{x}$ into $\pi_U(\mathbf{x})$ + error.
- [[Hyperplane]] / [[SeparatingHyperplane]] — described by a normal vector.
- [[VectorSubspace]] / [[Basis]] / [[Dimension]] — the Ch 2 structures it builds on.
