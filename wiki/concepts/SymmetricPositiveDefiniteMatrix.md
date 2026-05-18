---
title: "Symmetric Positive Definite Matrix"
type: concept
tags: [linear-algebra, foundational]
sources: [mml-book]
last_updated: 2026-05-16
---

# Symmetric Positive Definite (SPD) Matrix

A real square matrix $\mathbf{A}\in\mathbb{R}^{n\times n}$ is **symmetric positive definite** if ([[mml-book]] Def. 3.4):

1. $\mathbf{A}^\top = \mathbf{A}$ (symmetric).
2. $\mathbf{x}^\top\mathbf{A}\mathbf{x} > 0$ for every $\mathbf{x}\neq\mathbf{0}$.

If only $\geq$ holds in (2), $\mathbf{A}$ is **symmetric positive semi-definite (PSD)**.

## Equivalent characterizations

- All **eigenvalues** are positive (SPD) / non-negative (PSD).
- $\mathbf{A}$ admits a [[CholeskyDecomposition]] $\mathbf{A}=\mathbf{L}\mathbf{L}^\top$ with $\mathbf{L}$ lower-triangular and positive on the diagonal.
- $\mathbf{A}$ admits a unique symmetric square root $\mathbf{A}^{1/2}$ with $\mathbf{A} = \mathbf{A}^{1/2}\mathbf{A}^{1/2}$.
- All **leading principal minors** are positive (Sylvester's criterion).
- $\mathbf{A}$ is the **Gram matrix** of $n$ linearly independent vectors.

## Why SPD matrices are everywhere in ML

[[mml-book]] §3.2.3 makes the load-bearing observation: **on a finite-dimensional real vector space, inner products are *exactly* SPD matrices in disguise** (Thm 3.5).

| Object | Why it's SPD |
|---|---|
| [[DataCovarianceMatrix]] $\mathbf{S}$ | $\mathbf{v}^\top\mathbf{S}\mathbf{v}=\frac{1}{N}\sum(\mathbf{v}^\top\mathbf{x}_n)^2\geq 0$ |
| Gaussian covariance $\boldsymbol\Sigma$ | Required for $\mathcal{N}$ to be a proper density |
| Gram matrix $\mathbf{X}^\top\mathbf{X}$ | PSD always; SPD when $\mathbf{X}$ has full column rank |
| Kernel matrix $\mathbf{K}_{ij}=k(\mathbf{x}_i,\mathbf{x}_j)$ | Mercer's condition for valid kernels |
| Hessian at a minimum | SPD ⇒ strict local minimum |

So nearly every "covariance" / "kernel" / "metric" / "second-derivative" object in ML is SPD by construction.

## Geometric reading

An SPD matrix defines an ellipsoid: $\{\mathbf{x}:\mathbf{x}^\top\mathbf{A}\mathbf{x}\leq 1\}$. The eigenvectors give the axes; the eigenvalues give the inverse-squared semi-axis lengths. This is why Gaussian density contours are ellipsoids whose axes are the eigenvectors of $\boldsymbol\Sigma$.

## Why SPD admits a Cholesky decomposition

The Cholesky factorization $\mathbf{A}=\mathbf{L}\mathbf{L}^\top$ is the SPD analogue of "taking a square root" — only positive numbers have real square roots; only SPD matrices have real Cholesky factors. This is why we can sample multivariate Gaussians by $\boldsymbol\mu + \mathbf{L}\mathbf{z}$ where $\mathbf{z}\sim\mathcal{N}(\mathbf{0},\mathbf{I})$.

## Connections

- [[mml-book]] — §3.2.3 canonical reference.
- [[InnerProduct]] — SPD matrices encode all inner products.
- [[CholeskyDecomposition]] — exists iff matrix is SPD.
- [[DataCovarianceMatrix]] — PSD by construction.
- [[GaussianDistribution]] — covariance must be SPD.
- [[KernelTrick]] — Mercer's condition is SPD on the Gram matrix.
- [[Eigendecomposition]] — SPD ⇒ orthogonal eigenvectors + positive eigenvalues.
