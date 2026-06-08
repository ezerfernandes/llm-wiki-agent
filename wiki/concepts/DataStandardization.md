---
title: "Data Standardization"
type: concept
tags: [preprocessing, statistics, dimensionality-reduction, pca, normalization]
sources: [mml-ch10-dimensionality-reduction-pca, mml-book]
last_updated: 2026-06-05
---

# Data Standardization

A preprocessing step that **centers each feature and divides it by its standard deviation**, producing a unit-free dataset with mean $\mathbf 0$ and variance $1$ along every axis ([[mml-book]] §10.6, p. 336). It is the second of the four practical [[PrincipalComponentAnalysis|PCA]] steps (after mean subtraction, before eigendecomposition).

## The two sub-steps ([[mml-ch10-dimensionality-reduction-pca|MML §10.6]])

1. **Mean subtraction** — subtract the dataset mean $\boldsymbol\mu$ from every point so the data has mean $\mathbf 0$ (Fig. 10.11b). "Not strictly necessary but reduces the risk of numerical problems."
2. **Scaling** — divide each dimension $d=1,\dots,D$ by its standard deviation $\sigma_d$, so each feature has variance $1$ (Fig. 10.11c). This completes the *standardization*.

For a held-out point $\mathbf x_*$, standardization uses the **training** statistics (Eq. 10.58):

$$x_*^{(d)}\leftarrow\frac{x_*^{(d)}-\mu_d}{\sigma_d},\qquad d=1,\dots,D.$$

## Undoing it

Because PCA is performed on standardized data, the projection $\tilde{\mathbf x}_*=\mathbf B\mathbf B^\top\mathbf x_*$ (Eq. 10.59) lives in standardized space. To return a reconstruction to the **original** data space, the standardization must be reversed (Eq. 10.61):

$$\tilde x_*^{(d)}\leftarrow\tilde x_*^{(d)}\,\sigma_d+\mu_d.$$

## Relationship to whitening

Standardization rescales each axis independently to unit variance. Full **[[Whitening|whitening]]** additionally *decorrelates* the features (so the covariance becomes the identity, not merely a unit diagonal). PCA's eigendecomposition step performs the decorrelating rotation; combining it with per-axis scaling gives the whitening transform. A subtlety the chapter does not belabor: standardizing changes which directions dominate — PCA on the standardized data is effectively PCA on the **correlation** matrix rather than the **covariance** matrix.

## Connections

- [[mml-ch10-dimensionality-reduction-pca|MML Ch 10]] — §10.6 canonical reference (Eqs. 10.58, 10.61).
- [[PrincipalComponentAnalysis]] — the consumer; standardization is step 2 of the practical pipeline.
- [[Whitening]] — the decorrelating generalization.
- [[DataCovarianceMatrix]] — standardizing turns covariance into correlation.
- [[DimensionalityReduction]] — typical preprocessing context.
