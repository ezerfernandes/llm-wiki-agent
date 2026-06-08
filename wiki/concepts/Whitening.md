---
title: "Whitening"
type: concept
tags: [preprocessing, statistics, dimensionality-reduction, pca, normalization, decorrelation]
sources: [mml-ch10-dimensionality-reduction-pca, mml-book]
last_updated: 2026-06-05
---

# Whitening

A linear transformation that makes a dataset have **zero mean, unit variance, and uncorrelated features** — i.e. an identity covariance matrix. It generalizes [[DataStandardization|standardization]] (which only sets a unit *diagonal*) by also **decorrelating** the dimensions. In [[mml-book]] §10.6 the practical [[PrincipalComponentAnalysis|PCA]] pipeline performs the ingredients of whitening: centering, per-axis scaling to unit variance, and the eigendecomposition that supplies the decorrelating rotation.

## The PCA connection ([[mml-ch10-dimensionality-reduction-pca|MML §10.6]])

PCA's machinery decomposes the [[DataCovarianceMatrix|data covariance]] $\mathbf S=\mathbf P\boldsymbol\Lambda\mathbf P^\top$ into an orthonormal eigenbasis $\mathbf P$ (the principal directions) and eigenvalues $\boldsymbol\Lambda$ (the variances along them). Whitening then:

1. **rotates** the data into the eigenbasis ($\mathbf P^\top\mathbf x$) — decorrelating it, and
2. **rescales** each principal axis by $1/\sqrt{\lambda_d}$ — equalizing the variances to $1$.

The result has covariance $\mathbf I$. Standardization performs only the axis-rescaling part on the *original* axes; whitening adds the rotation so cross-correlations also vanish.

## Why it matters

- **PCA preprocessing** — the §10.6 "divide by the standard deviation … data has variance 1 along each axis" step makes the data unit-free (Fig. 10.11c) and reduces numerical problems; the eigendecomposition then handles decorrelation.
- **Downstream learning** — whitened inputs decorrelate features so that optimizers see a better-conditioned problem (smaller [[ConditionNumber|condition number]]), a recurring motivation across ML preprocessing.

## Connections

- [[mml-ch10-dimensionality-reduction-pca|MML Ch 10]] — §10.6 (standardization / eigendecomposition pipeline).
- [[DataStandardization]] — the per-axis-scaling subset of whitening.
- [[PrincipalComponentAnalysis]] — supplies the decorrelating rotation.
- [[DataCovarianceMatrix]] — whitening drives its covariance to $\mathbf I$.
- [[Eigendecomposition]] — the rotation + rescaling factorization.
- [[ConditionNumber]] — whitened data is better-conditioned for optimization.
