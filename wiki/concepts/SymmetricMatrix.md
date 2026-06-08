---
title: "Symmetric Matrix"
type: concept
tags: [linear-algebra, foundational, matrix-algebra]
sources: [mml-ch02-linear-algebra, mml-book]
last_updated: 2026-06-04
---

# Symmetric Matrix

**Definition 2.5** ([[mml-ch02-linear-algebra|MML Ch 2]] §2.2.2): a matrix $\mathbf{A}\in\mathbb{R}^{n\times n}$ is *symmetric* if $\mathbf{A}=\mathbf{A}^\top$. Only square matrices can be symmetric.

## Properties (MML §2.2.2)

- If $\mathbf{A}$ is symmetric and invertible, so is $\mathbf{A}^\top$, with $(\mathbf{A}^{-1})^\top=(\mathbf{A}^\top)^{-1}=:\mathbf{A}^{-\top}$.
- The **sum** of symmetric matrices is always symmetric.
- The **product** of two symmetric matrices is defined but **generally not symmetric** (MML Eq. 2.32, counterexample $\begin{bmatrix}1&0\\0&0\end{bmatrix}\begin{bmatrix}1&1\\1&1\end{bmatrix}=\begin{bmatrix}1&1\\0&0\end{bmatrix}$).

## Why ML cares

Symmetric matrices are the entry point to the geometry of MML Ch 3–4: a [[SymmetricPositiveDefiniteMatrix|symmetric positive-definite matrix]] defines an [[InnerProduct|inner product]] (Thm 3.5), every symmetric matrix is orthogonally diagonalizable with real eigenvalues (spectral theorem, Ch 4), covariance matrices and Gram matrices are symmetric, and quadratic forms $\mathbf{x}^\top\mathbf{A}\mathbf{x}$ assume symmetric $\mathbf{A}$.

## Connections

- [[MatrixTranspose]] — symmetry is the fixed-point condition $\mathbf{A}=\mathbf{A}^\top$.
- [[SymmetricPositiveDefiniteMatrix]] — the inner-product-defining special case.
- [[InnerProduct]] — every inner product on $\mathbb{R}^n$ is $\hat{\mathbf{x}}^\top\mathbf{A}\hat{\mathbf{y}}$ for symmetric positive-definite $\mathbf{A}$ (MML Thm 3.5).
- [[Matrix]] — parent concept.
- [[mml-ch02-linear-algebra|MML Ch 2]] / [[mml-book]] — §2.2.2 canonical reference.
