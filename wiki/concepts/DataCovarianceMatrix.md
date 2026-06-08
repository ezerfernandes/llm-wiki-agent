---
title: "Data Covariance Matrix"
type: concept
tags: [statistics, linear-algebra, foundational]
sources: [mml-book, mml-ch06-probability-and-distributions, mml-ch10-dimensionality-reduction-pca]
last_updated: 2026-06-05
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

## From [[mml-ch06-probability-and-distributions|MML Ch 6]]

The data covariance matrix is the **empirical covariance** of §6.4.2 ([[mml-book]] Def. 6.9, Eq. 6.42), the data estimate of the population [[CovarianceMatrix|covariance matrix]] $\boldsymbol\Sigma$ (Def. 6.7). On (not-yet-centered) data it is written $\boldsymbol\Sigma=\frac1N\sum_n(\mathbf x_n-\bar{\mathbf x})(\mathbf x_n-\bar{\mathbf x})^\top$, which for mean-centered data reduces to the $\mathbf S=\frac1N\sum_n\mathbf x_n\mathbf x_n^\top$ used in PCA. The companion estimator is the **[[EmpiricalMean|empirical mean]]** $\bar{\mathbf x}=\frac1N\sum_n\mathbf x_n$ (Eq. 6.41). Ch 6 confirms two facts this page already states:

- **Biased by default**: [[mml-book]] divides by $N$ (the MLE) "throughout the book"; the unbiased / corrected estimator uses $N-1$ (Bessel's correction) (margin, p. 192).
- **Symmetric PSD**: $\mathbf v^\top\mathbf S\mathbf v=\frac1N\sum_n(\mathbf v^\top\mathbf x_n)^2\ge0$, and the population $\boldsymbol\Sigma$ is generally *assumed* positive definite "to enable better intuition" (§6.4.1 Remark, p. 191).

Its diagonal holds the marginal [[Variance|variances]] and off-diagonal the cross-[[Covariance|covariances]]; standardizing gives the [[Correlation|correlation]] matrix (§6.4.1).

## From [[mml-ch10-dimensionality-reduction-pca|MML Ch 10]] (PCA decomposes $\mathbf S$)

Ch 10 is where $\mathbf S$ becomes the central object. All three [[PrincipalComponentAnalysis|PCA]] derivations reduce to its [[Eigendecomposition|eigendecomposition]]:

- **Max-variance** (§10.2): the constrained problem $\max\mathbf b_1^\top\mathbf S\mathbf b_1$ s.t. $\|\mathbf b_1\|=1$ gives $\mathbf S\mathbf b_1=\lambda_1\mathbf b_1$ (Eq. 10.13); variance along $\mathbf b_m$ equals $\lambda_m$ (Eq. 10.23) and total retained variance is $\sum_{m=1}^M\lambda_m$ (Eq. 10.24).
- **Computation** (§10.4): $\mathbf S=\frac1N\mathbf X\mathbf X^\top$ (Eq. 10.45), so the columns of $\mathbf U$ in the [[SingularValueDecomposition|SVD]] $\mathbf X=\mathbf U\boldsymbol\Sigma\mathbf V^\top$ are its eigenvectors, with eigenvalues $\lambda_d=\sigma_d^2/N$ (Eq. 10.49).
- **High-dim trick** ($N\ll D$, §10.5): $\mathbf S$ has rank $N$ (so $D-N+1$ zero eigenvalues); its nonzero spectrum is shared with the small $N\times N$ matrix $\frac1N\mathbf X^\top\mathbf X$ (Eqs. 10.55–10.57), avoiding the cubic-in-$D$ cost.
- **Probabilistic view** (§10.7–10.8): the [[ProbabilisticPCA|PPCA]] marginal likelihood has covariance $\mathbf B\mathbf B^\top+\sigma^2\mathbf I$ (Eq. 10.70b), and in the noise-free limit $\mathbf B\mathbf B^\top=\mathrm{Cov}[\mathcal X]$ (Eq. 10.81) — so **(P)PCA literally performs a decomposition of $\mathbf S$**.

When the data is [[DataStandardization|standardized]] first (§10.6), PCA effectively diagonalizes the **correlation** matrix rather than the raw covariance.

## Connections

- [[mml-ch10-dimensionality-reduction-pca]] — §10.1/10.4 canonical PCA reference (Eq. 10.1, 10.45).
- [[mml-ch06-probability-and-distributions]] — §6.4.2 deep dive (empirical statistics).
- [[mml-book]] — §10.1 canonical reference (PCA); §6.4.2 (empirical covariance).
- [[CovarianceMatrix]] — the population analogue.
- [[EmpiricalMean]] — its companion empirical statistic.
- [[Covariance]] / [[Variance]] / [[Correlation]] — entry-level interpretation.
- [[PrincipalComponentAnalysis]] — primary consumer.
- [[Eigendecomposition]] — spectral structure.
- [[SymmetricPositiveDefiniteMatrix]] — class of $\mathbf{S}$.
- [[GaussianDistribution]] — covariance interpretation.
