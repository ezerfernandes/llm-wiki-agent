---
title: "Power Iteration"
type: concept
tags: [linear-algebra, eigenvalue, numerical-methods, iterative-algorithm, pca]
sources: [mml-ch10-dimensionality-reduction-pca, mml-book]
last_updated: 2026-06-05
---

# Power Iteration

A simple **iterative method for computing the eigenvector associated with the largest (dominant) eigenvalue** of a matrix ([[mml-book]] §10.4.2, Eq. 10.52). Used in [[PrincipalComponentAnalysis|PCA]] when only a few leading principal components are needed, where it is computationally cheaper than a full [[Eigendecomposition|eigendecomposition]] or [[SingularValueDecomposition|SVD]].

## The iteration ([[mml-ch10-dimensionality-reduction-pca|MML §10.4.2]])

Choose a random start vector $\mathbf x_0$ that is **not** in the null space of $\mathbf S$ (if $\mathbf S$ is invertible, $\mathbf x_0\neq\mathbf 0$ suffices), then repeatedly multiply by $\mathbf S$ and renormalize:

$$\mathbf x_{k+1}=\frac{\mathbf S\,\mathbf x_k}{\lVert\mathbf S\,\mathbf x_k\rVert},\qquad k=0,1,2,\dots$$

Renormalization keeps $\lVert\mathbf x_k\rVert=1$. The sequence **converges to the eigenvector of the largest eigenvalue** of $\mathbf S$ (the [[DataCovarianceMatrix|data covariance matrix]] in PCA — the first [[PrincipalSubspace|principal component]]). Subsequent eigenvectors are obtained by deflation (subtracting the already-found components, as in §10.2.2).

## Why iterative methods are necessary

By the **Abel–Ruffini theorem** (Ruffini 1799; Abel 1826), there is no algebraic (closed-form) solution for the roots of the [[CharacteristicPolynomial|characteristic polynomial]] of matrices larger than $4\times4$, so eigenvalues cannot be found exactly by formula. All modern linear-algebra packages (`np.linalg.eigh`, `np.linalg.svd`) solve for eigenvalues / singular values **iteratively**. When only the first few eigenvectors are required, computing a full decomposition and discarding most of it is wasteful — power iteration directly optimizes the dominant eigenvector.

## Where it shows up

The original **Google PageRank** algorithm (Page et al. 1999) is a power iteration: it ranks web pages by the dominant eigenvector of the hyperlink transition matrix — the same machinery PCA uses to find the top principal component ([[mml-book]] §10.4.2, p. 335).

## Connections

- [[mml-ch10-dimensionality-reduction-pca|MML Ch 10]] — §10.4.2 canonical reference (Eq. 10.52).
- [[PrincipalComponentAnalysis]] — efficient leading-eigenvector computation.
- [[DataCovarianceMatrix]] — the matrix $\mathbf S$ iterated on.
- [[Eigendecomposition]] / [[SingularValueDecomposition]] — the alternative full decompositions.
- [[CharacteristicPolynomial]] — why no closed form (Abel–Ruffini).
- [[PrincipalSubspace]] — successive eigenvectors found by deflation.
