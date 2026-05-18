---
title: "Orthogonal Projection"
type: concept
tags: [analytic-geometry, linear-algebra, foundational]
sources: [mml-book]
last_updated: 2026-05-16
---

# Orthogonal Projection

Given a subspace $U\subseteq V$ of an inner-product space, the orthogonal projection $\pi_U(\mathbf{x})$ of a vector $\mathbf{x}\in V$ onto $U$ is the unique closest point in $U$ to $\mathbf{x}$ ([[mml-book]] §3.8). The residual $\mathbf{x}-\pi_U(\mathbf{x})$ is orthogonal to every vector in $U$.

## Closed-form

If $U$ is the column space of $\mathbf{B}\in\mathbb{R}^{D\times M}$ (i.e., $\mathbf{B}$'s columns span $U$):

$$
\pi_U(\mathbf{x}) = \mathbf{B}\,(\mathbf{B}^\top\mathbf{B})^{-1}\mathbf{B}^\top\,\mathbf{x}
$$

The matrix $\mathbf{B}(\mathbf{B}^\top\mathbf{B})^{-1}\mathbf{B}^\top$ is the *projection matrix*; it is symmetric and idempotent ($\mathbf{P}^2=\mathbf{P}$).

When $\mathbf{B}$ has orthonormal columns ($\mathbf{B}^\top\mathbf{B}=\mathbf{I}$), this collapses to $\pi_U(\mathbf{x}) = \mathbf{B}\mathbf{B}^\top\mathbf{x}$.

## Why orthogonal projection is everywhere in ML

- **[[LinearRegression|Least-squares regression]]** ([[mml-book]] §9.4): $\boldsymbol\theta_{\text{ML}} = (\mathbf{X}^\top\mathbf{X})^{-1}\mathbf{X}^\top\mathbf{y}$ is exactly the projection coefficients of $\mathbf{y}$ onto the column space of the [[DesignMatrix]] $\mathbf{X}$. The MLE *is* orthogonal projection.
- **[[PrincipalComponentAnalysis|PCA]]** (Ch 10): the reconstructed point $\tilde{\mathbf{x}}_n = \mathbf{B}\mathbf{B}^\top\mathbf{x}_n$ is the orthogonal projection of $\mathbf{x}_n$ onto the $M$-dim principal subspace.
- **[[SupportVectorMachine|SVM margin]]** (Ch 12.2): the distance from a training point to the separating hyperplane is computed via orthogonal projection onto the hyperplane.
- **Gram-Schmidt orthogonalization** is iterated orthogonal projection.

## The single unifying picture

[[mml-book]] §9.4 makes the connection explicit: linear regression *is* orthogonal projection. The normal equations $\mathbf{X}^\top(\mathbf{y}-\mathbf{X}\boldsymbol\theta) = \mathbf{0}$ are exactly the orthogonality condition: the residual is orthogonal to every column of $\mathbf{X}$.

## Connections

- [[mml-book]] — §3.8 canonical reference.
- [[InnerProduct]] — the structure projection needs.
- [[LinearRegression]] — projection interpretation of MLE.
- [[PrincipalComponentAnalysis]] — projection to principal subspace.
- [[SupportVectorMachine]] — margin via projection.
