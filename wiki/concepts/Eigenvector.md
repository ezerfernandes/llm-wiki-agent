---
title: "Eigenvector"
type: concept
tags: [linear-algebra, mathematics, parallel-computing]
sources: [parproc-ch11-parallel-matrix-operations, mml-ch04-matrix-decompositions, mml-book]
last_updated: 2026-06-04
---

# Eigenvector

A nonzero vector $v$ such that $Av = \lambda v$ for a scalar $\lambda$ (the corresponding [[Eigenvalue|eigenvalue]]). For a symmetric matrix, eigenvectors corresponding to distinct eigenvalues are orthogonal.

The dominant eigenvector (corresponding to the largest $|\lambda|$) is the target of the [[PowerMethod|power method]]. Subsequent eigenvectors are obtained by deflation: removing the contribution of the already-found eigenpairs from A.

## Applications

- **PageRank:** Google's link-ranking algorithm is based on the dominant eigenvector of the web's link matrix.
- **Principal component analysis (PCA):** Leading eigenvectors of a covariance matrix capture the directions of maximum variance.

## Appendix B Definition (Matloff)

Section B.6 of *Programming on Parallel Machines* ([[parproc-appB-matrix-algebra]]) states that for a symmetric real matrix A, eigenvectors corresponding to distinct eigenvalues are orthogonal, and the full eigenvector matrix U satisfies $U'U = I$ (U is orthogonal). The diagonalization $U'AU = D$ holds with D diagonal. For non-symmetric matrices with distinct eigenvalues, diagonalization still holds but U is not necessarily orthogonal.

## From [[mml-ch04-matrix-decompositions|MML Ch 4]]

**Definition 4.6** (§4.2, Eq. 4.25): a nonzero $\mathbf{x}\in\mathbb{R}^n$ with $\mathbf{A}\mathbf{x}=\lambda\mathbf{x}$ is an eigenvector of square $\mathbf{A}$ for [[Eigenvalue|eigenvalue]] $\lambda$.

- **Non-uniqueness** (Eq. 4.26): if $\mathbf{x}$ is an eigenvector, so is every $c\mathbf{x}$ ($c\neq0$) — all vectors *collinear* to $\mathbf{x}$ are eigenvectors with the same $\lambda$. Software typically reports normalized ($\|\mathbf{x}\|=1$) eigenvectors.
- **Independence** (Thm 4.12): eigenvectors for $n$ *distinct* eigenvalues are linearly independent and form a basis of $\mathbb{R}^n$ — making $\mathbf{A}$ [[Diagonalization|diagonalizable]]. If eigenvectors fail to form a basis, $\mathbf{A}$ is [[DefectiveMatrix|defective]] (Def. 4.13).
- **[[Eigenspace]]** (Def. 4.10): all eigenvectors for a given $\lambda$ span $E_\lambda=\ker(\mathbf{A}-\lambda\mathbf{I})$.
- **[[SpectralTheorem|Spectral theorem]]** (Thm 4.15): a *symmetric* matrix has an **orthonormal** basis of eigenvectors — used in PCA, kernels, and the [[SingularValueDecomposition|SVD]] construction (right-singular vectors = eigenvectors of $\mathbf{A}^\top\mathbf{A}$; left = eigenvectors of $\mathbf{A}\mathbf{A}^\top$). For a repeated eigenvalue, a non-orthogonal eigenbasis is orthogonalized via [[GramSchmidt|Gram–Schmidt]] (Example 4.8).
- **PageRank** (Example 4.9): the dominant eigenvector of a web transition matrix (eigenvalue 1) ranks pages.

## Connections

- [[mml-ch04-matrix-decompositions|MML Ch 4]] — §4.2 canonical reference (Def. 4.6, Thm 4.12).
- [[Eigenvalue]] — the associated scalar. [[Eigenspace]] — the subspace eigenvectors span.
- [[Diagonalization]] / [[Eigendecomposition]] / [[DefectiveMatrix]] / [[SpectralTheorem]] — eigenbasis existence and use.
- [[PowerMethod]] — the iterative algorithm that converges to the dominant eigenvector.
- [[MatrixTranspose]] — the orthogonality condition $U^{-1} = U'$ is central to the symmetric diagonalization.
- [[parproc-ch11-parallel-matrix-operations]] — §11.6 primary source.
- [[parproc-appB-matrix-algebra]] — §B.6 formal definition.
