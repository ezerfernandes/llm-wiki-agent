---
title: "Eigenvector"
type: concept
tags: [linear-algebra, mathematics, parallel-computing]
sources: [parproc-ch11-parallel-matrix-operations]
last_updated: 2026-05-17
---

# Eigenvector

A nonzero vector $v$ such that $Av = \lambda v$ for a scalar $\lambda$ (the corresponding [[Eigenvalue|eigenvalue]]). For a symmetric matrix, eigenvectors corresponding to distinct eigenvalues are orthogonal.

The dominant eigenvector (corresponding to the largest $|\lambda|$) is the target of the [[PowerMethod|power method]]. Subsequent eigenvectors are obtained by deflation: removing the contribution of the already-found eigenpairs from A.

## Applications

- **PageRank:** Google's link-ranking algorithm is based on the dominant eigenvector of the web's link matrix.
- **Principal component analysis (PCA):** Leading eigenvectors of a covariance matrix capture the directions of maximum variance.

## Appendix B Definition (Matloff)

Section B.6 of *Programming on Parallel Machines* ([[parproc-appB-matrix-algebra]]) states that for a symmetric real matrix A, eigenvectors corresponding to distinct eigenvalues are orthogonal, and the full eigenvector matrix U satisfies $U'U = I$ (U is orthogonal). The diagonalization $U'AU = D$ holds with D diagonal. For non-symmetric matrices with distinct eigenvalues, diagonalization still holds but U is not necessarily orthogonal.

## Connections

- [[Eigenvalue]] — the associated scalar.
- [[PowerMethod]] — the iterative algorithm that converges to the dominant eigenvector.
- [[MatrixTranspose]] — the orthogonality condition $U^{-1} = U'$ is central to the symmetric diagonalization.
- [[parproc-ch11-parallel-matrix-operations]] — §11.6 primary source.
- [[parproc-appB-matrix-algebra]] — §B.6 formal definition.
