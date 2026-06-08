---
title: "Karhunen-Loève Transform"
type: concept
tags: [signal-processing, dimensionality-reduction, eigenvalue, matrix-decomposition]
sources: [mml-book, mml-ch04-matrix-decompositions, mml-ch10-dimensionality-reduction-pca]
last_updated: 2026-06-05
---

# Karhunen-Loève Transform

Signal-processing name for [[PrincipalComponentAnalysis|PCA]] ([[mml-book]] §10.1) — eigendecomposition of the data correlation operator.

## From [[mml-ch10-dimensionality-reduction-pca|MML Ch 10]]

[[mml-ch10-dimensionality-reduction-pca|MML §10.1]] (p. 318) states plainly: *"In the signal processing community, PCA is also known as the Karhunen–Loève transform."* The KLT is therefore **the same algorithm as [[PrincipalComponentAnalysis|PCA]]**, not an independent method — it eigendecomposes the [[DataCovarianceMatrix|data covariance / correlation matrix]] $\mathbf S$ and projects onto the leading eigenvectors. Per the book's own §10.8 recap, PCA has **three derivations** (max-variance §10.2, min-[[ReconstructionError|reconstruction-error]] §10.3, latent-variable / [[ProbabilisticPCA|PPCA]] §10.7); the KLT name is an *alias* for the resulting transform rather than a fourth derivation.

## From [[mml-ch04-matrix-decompositions|MML Ch 4]]

The KLT / PCA is a **spectral method** ([[mml-book]] §4.8): it [[Eigendecomposition|eigendecomposes]] a symmetric positive-(semi)definite operator (the data covariance/correlation matrix), which the [[SpectralTheorem|spectral theorem]] (Thm 4.15) guarantees has an orthonormal eigenbasis with real eigenvalues. Retaining the top-$k$ eigenvectors is exactly the [[LowRankApproximation|low-rank approximation]] / truncated [[SingularValueDecomposition|SVD]] of the data matrix, optimal by [[EckartYoung|Eckart–Young]]. MML §4.8 lists it alongside the related spectral methods Fisher discriminant analysis, multidimensional scaling, Isomap, Laplacian/Hessian eigenmaps, and spectral clustering.

## Connections

- [[mml-ch10-dimensionality-reduction-pca|MML Ch 10]] — §10.1 names PCA the KLT (p. 318).
- [[mml-ch04-matrix-decompositions|MML Ch 4]] — §4.8 (spectral methods).
- [[PrincipalComponentAnalysis]] — the ML name for the same transform.
- [[Eigendecomposition]] / [[SpectralTheorem]] / [[SingularValueDecomposition]] / [[LowRankApproximation]] — the machinery.
