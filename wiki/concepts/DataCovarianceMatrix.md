---
title: "Data Covariance Matrix"
type: concept
tags: [statistics, linear-algebra, foundational]
sources: [mml-book]
last_updated: 2026-05-16
---

# Data Covariance Matrix

For mean-centered data $\{\mathbf{x}_1,\dots,\mathbf{x}_N\}\subset\mathbb{R}^D$:

$$\mathbf{S} = \frac{1}{N}\sum_{n=1}^N \mathbf{x}_n\mathbf{x}_n^\top \;\in\; \mathbb{R}^{D\times D}.$$

The entry $S_{ij}$ is the empirical covariance between feature $i$ and feature $j$ across the sample. $\mathbf{S}$ is symmetric and positive semi-definite ([[mml-book]] §6.4.4, §10.1, Eq. 10.1).

## Why it's the central object of dimensionality reduction

[[PrincipalComponentAnalysis|PCA]] ([[mml-book]] Ch 10) builds entirely on $\mathbf{S}$:

- The **principal components** are the eigenvectors of $\mathbf{S}$.
- The **eigenvalues** of $\mathbf{S}$ are the variances along each principal direction.
- The **fraction of variance** retained by the top-$M$ projection is $\frac{\sum_{m=1}^M \lambda_m}{\sum_{d=1}^D \lambda_d}$.

This is justified two ways in MML:
1. **Maximum variance** (§10.2): maximizing $\mathbf{b}_1^\top \mathbf{S}\mathbf{b}_1$ subject to $\|\mathbf{b}_1\|=1$ yields $\mathbf{S}\mathbf{b}_1 = \lambda_1\mathbf{b}_1$ via Lagrange multipliers.
2. **Minimum reconstruction error** (§10.3): minimizing $\|\mathbf{x}_n - \mathbf{B}\mathbf{B}^\top\mathbf{x}_n\|^2$ recovers the same eigenvalue problem.

## Why it's symmetric positive semi-definite

For any $\mathbf{v}\in\mathbb{R}^D$:

$$\mathbf{v}^\top\mathbf{S}\mathbf{v} = \tfrac{1}{N}\sum_n (\mathbf{v}^\top\mathbf{x}_n)^2 \geq 0.$$

So $\mathbf{S}$ is PSD. It is PD when the data spans $\mathbb{R}^D$ — which fails when $N<D$ (more features than samples), the high-dim regime that motivates PCA in the first place.

## Sample vs population

$\mathbf{S}$ is the **maximum-likelihood** estimate of the population covariance under the Gaussian model — Bessel's correction (dividing by $N-1$ instead of $N$) gives the unbiased estimator. ML practice typically uses the MLE form.

## Connections

- [[mml-book]] — §10.1 canonical reference.
- [[PrincipalComponentAnalysis]] — primary consumer.
- [[Eigendecomposition]] — spectral structure.
- [[SymmetricPositiveDefiniteMatrix]] — class of $\mathbf{S}$.
- [[GaussianDistribution]] — covariance interpretation.
