---
title: "Spectral Theorem"
type: concept
tags: [linear-algebra, eigenvalue, matrix-decomposition, foundational]
sources: [mml-ch04-matrix-decompositions, mml-book]
last_updated: 2026-06-04
---

# Spectral Theorem

**Theorem 4.15** ([[mml-book]] §4.2): *if $\mathbf{A}\in\mathbb{R}^{n\times n}$ is **symmetric**, there exists an orthonormal basis of the corresponding vector space $V$ consisting of eigenvectors of $\mathbf{A}$, and each eigenvalue is real.*

This is the single most consequential theorem of MML Ch 4. It guarantees two things at once for every real symmetric matrix:

1. **Real eigenvalues** — no complex spectrum.
2. **An orthonormal eigenbasis** — eigenvectors can be chosen mutually orthogonal and unit length.

## Direct implication: orthogonal eigendecomposition

A symmetric $\mathbf{A}$ always admits an [[Eigendecomposition]] with real eigenvalues, and the eigenvector matrix can be made an [[OrthogonalMatrix|orthogonal matrix]] $\mathbf{P}$ (columns = orthonormal eigenvectors):

$$\mathbf{A} = \mathbf{P}\mathbf{D}\mathbf{P}^\top, \qquad \mathbf{P}^\top\mathbf{P}=\mathbf{I}$$

with $\mathbf{D}$ diagonal of eigenvalues. Hence **symmetric matrices are always [[Diagonalization|diagonalizable]]** ([[mml-book]] Thm 4.21), and orthogonally so.

## Repeated eigenvalues need Gram–Schmidt

The theorem promises an *orthogonal* eigenbasis exists, but a naively computed basis of a repeated eigenvalue's [[Eigenspace|eigenspace]] need not be orthogonal. Since any linear combination of eigenvectors for the same $\lambda$ is again an eigenvector for $\lambda$ ([[mml-book]] Eq. 4.40), applying [[GramSchmidt|Gram–Schmidt]] (§3.8.3) orthogonalizes within each eigenspace (Example 4.8: the 2-D $E_1$ of $\begin{bmatrix}3&2&2\\2&3&2\\2&2&3\end{bmatrix}$ is orthogonalized to $[-1,1,0]^\top,\tfrac12[-1,-1,2]^\top$).

## Why it matters for ML

- **Every [[DataCovarianceMatrix|covariance matrix]] is symmetric (in fact SPD)** — so [[PrincipalComponentAnalysis|PCA]] (Ch 10) rests directly on the spectral theorem: principal components are the orthonormal eigenvectors.
- **Kernel [[GramMatrix|Gram matrices]]** (Ch 12) are symmetric PSD — spectral methods (kernel-PCA, spectral clustering, Laplacian/Hessian eigenmaps, Isomap, MDS) all eigendecompose a symmetric positive-(semi)definite operator ([[mml-book]] §4.8).
- **SVD construction** ([[mml-book]] §4.5.2) uses the spectral theorem twice: on $\mathbf{A}^\top\mathbf{A}$ (right-singular vectors) and on $\mathbf{A}\mathbf{A}^\top$ (left-singular vectors).
- For **symmetric matrices the eigendecomposition and the [[SingularValueDecomposition|SVD]] coincide** ([[mml-book]] §4.5.3).

## Connections

- [[mml-ch04-matrix-decompositions|MML Ch 4]] — §4.2 canonical reference (Thm 4.15).
- [[Eigendecomposition]] / [[Diagonalization]] — guaranteed orthogonal for symmetric matrices.
- [[SymmetricPositiveDefiniteMatrix]] — the most common symmetric matrices in ML (positive real eigenvalues).
- [[OrthogonalMatrix]] / [[OrthonormalBasis]] — the eigenbasis the theorem guarantees.
- [[GramSchmidt]] — orthogonalizes a repeated eigenvalue's eigenspace.
- [[SingularValueDecomposition]] — its construction invokes the spectral theorem on $\mathbf{A}^\top\mathbf{A}$ and $\mathbf{A}\mathbf{A}^\top$.
- [[PrincipalComponentAnalysis]] — the headline ML application.
</content>
