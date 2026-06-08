---
title: "Diagonalization"
type: concept
tags: [linear-algebra, matrix-decomposition, eigenvalue]
sources: [mml-ch04-matrix-decompositions, mml-book]
last_updated: 2026-06-04
---

# Diagonalization

A square matrix $\mathbf{A}\in\mathbb{R}^{n\times n}$ is **diagonalizable** if it is [[SimilarityTransform|similar]] to a diagonal matrix — i.e. there exists an invertible $\mathbf{P}$ with

$$\mathbf{D} = \mathbf{P}^{-1}\mathbf{A}\mathbf{P}$$

where $\mathbf{D}$ is diagonal ([[mml-book]] Def. 4.19, §4.4). Diagonalizing expresses the *same* linear mapping in a different basis — specifically, the basis of **eigenvectors** of $\mathbf{A}$.

## Why eigenvectors

Collecting candidate vectors $\mathbf{P}=[\mathbf{p}_1,\ldots,\mathbf{p}_n]$ and scalars into a diagonal $\mathbf{D}$, the identity $\mathbf{A}\mathbf{P}=\mathbf{P}\mathbf{D}$ holds **iff** the $\lambda_i$ are eigenvalues and the $\mathbf{p}_i$ the corresponding eigenvectors ([[mml-book]] Eqs. 4.50–4.54), because column $i$ reads $\mathbf{A}\mathbf{p}_i=\lambda_i\mathbf{p}_i$. Diagonalization further requires $\mathbf{P}$ to be invertible (full rank, Thm 4.3), i.e. **the eigenvectors must form a basis of $\mathbb{R}^n$**.

## The non-defective requirement

- **Only [[DefectiveMatrix|non-defective]] matrices are diagonalizable** — a matrix with fewer than $n$ independent eigenvectors has no eigenbasis ([[mml-book]] Thm 4.20). This is the [[Eigendecomposition]] $\mathbf{A}=\mathbf{P}\mathbf{D}\mathbf{P}^{-1}$.
- **Symmetric matrices always diagonalize** ([[mml-book]] Thm 4.21): the [[SpectralTheorem|spectral theorem]] (Thm 4.15) gives an *orthonormal* basis of eigenvectors, making $\mathbf{P}$ orthogonal so $\mathbf{D}=\mathbf{P}^\top\mathbf{A}\mathbf{P}$.
- **Diagonalizability is independent of invertibility** ([[mml-book]] §4.7, Exercise 4.5): a rotation matrix is invertible but not diagonalizable over $\mathbb{R}$; a defective matrix like $\begin{bmatrix}2&1\\0&2\end{bmatrix}$ is invertible but not diagonalizable. The **Jordan normal form** (Lang 1987) handles defective matrices but is beyond MML's scope.

## Why diagonal is desirable

Diagonal matrices give cheap determinants (product of diagonal), powers ($\mathbf{D}^k$ = element-wise), and inverses (reciprocals). Via diagonalization these extend to $\mathbf{A}$: $\mathbf{A}^k=\mathbf{P}\mathbf{D}^k\mathbf{P}^{-1}$ and $\det(\mathbf{A})=\prod_i d_{ii}$ ([[mml-book]] Eqs. 4.62–4.63).

## Geometric intuition

$\mathbf{A}=\mathbf{P}\mathbf{D}\mathbf{P}^{-1}$ reads as three maps: $\mathbf{P}^{-1}$ changes basis into the eigenbasis, $\mathbf{D}$ scales along the eigen-axes, $\mathbf{P}$ restores standard coordinates ([[mml-book]] Fig. 4.7). The eigendecomposition **undoes the same basis change it applies** — contrast with [[SingularValueDecomposition|SVD]], which changes basis in *both* domain and codomain.

## Connections

- [[mml-ch04-matrix-decompositions|MML Ch 4]] — §4.4 canonical reference (Def. 4.19).
- [[Eigendecomposition]] — the factorization $\mathbf{A}=\mathbf{P}\mathbf{D}\mathbf{P}^{-1}$ diagonalization produces.
- [[SimilarityTransform]] — diagonalizable = similar to a diagonal matrix.
- [[DefectiveMatrix]] — the obstruction; defective ⇒ not diagonalizable.
- [[SpectralTheorem]] — guarantees symmetric matrices always diagonalize orthogonally.
- [[Eigenvalue]] / [[Eigenvector]] — the diagonal entries and the columns of $\mathbf{P}$.
- [[matrix-diagonalization]] — algebrica.org's diagonalization page.
- [[SingularValueDecomposition]] — the generalization to non-square / non-diagonalizable matrices.
</content>
