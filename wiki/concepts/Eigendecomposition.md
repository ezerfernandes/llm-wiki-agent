---
title: "Eigendecomposition"
type: concept
tags: [linear-algebra, matrix-decomposition, foundational]
sources: [mml-book, d2l-appendix-mathematics]
last_updated: 2026-05-16
---

# Eigendecomposition

A diagonalizable square matrix $\mathbf{A}\in\mathbb{R}^{n\times n}$ factors as

$$\mathbf{A} = \mathbf{P}\,\mathbf{D}\,\mathbf{P}^{-1}$$

where $\mathbf{D}$ is diagonal (containing eigenvalues $\lambda_1,\dots,\lambda_n$) and $\mathbf{P}$ has the corresponding eigenvectors as columns ([[mml-book]] §4.4).

When $\mathbf{A}$ is **symmetric**, the spectral theorem (Thm 4.15) guarantees $\mathbf{P}$ is orthogonal — i.e., $\mathbf{A}=\mathbf{P}\mathbf{D}\mathbf{P}^\top$ with $\mathbf{P}^\top\mathbf{P}=\mathbf{I}$. This is the case for every [[DataCovarianceMatrix]] (Ch 10) and every [[GramMatrix]] in kernel methods (Ch 12).

## Connection to the characteristic polynomial

Eigenvalues are roots of the [[CharacteristicPolynomial]] $p_\mathbf{A}(\lambda) = \det(\mathbf{A}-\lambda\mathbf{I})$ ([[mml-book]] Def 4.5). Hence the algebrica.org pages [[roots-of-a-polynomial]] / [[polynomial-equations]] are the prerequisites for computing eigenvalues by hand.

## ML uses

- **[[PrincipalComponentAnalysis|PCA]]** (Ch 10): principal components = eigenvectors of the data covariance matrix, ordered by eigenvalue magnitude. The fraction of variance captured by the first $M$ components is $\sum_{m=1}^M \lambda_m / \sum_{m=1}^D \lambda_m$.
- **PageRank** and **spectral clustering**: dominant eigenvector of a transition / similarity matrix.
- **Stability analysis** of dynamical systems and RNNs: eigenvalues of the recurrence matrix.

## Connections

- [[mml-book]] — §4.4 canonical reference.
- [[eigenvalues-and-eigenvectors]] — algebrica.org's eigenvalue page.
- [[matrix-diagonalization]] — algebrica.org's diagonalization page.
- [[SingularValueDecomposition]] — generalization to non-square / non-symmetric.
- [[PrincipalComponentAnalysis]] — primary ML application.
- [[CharacteristicPolynomial]] — algebraic route to eigenvalues.
