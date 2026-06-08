---
title: "Matrix Inverse"
type: concept
tags: [linear-algebra, foundational, matrix-algebra]
sources: [mml-ch02-linear-algebra, mml-book]
last_updated: 2026-06-04
---

# Matrix Inverse

**Definition 2.3** ([[mml-ch02-linear-algebra|MML Ch 2]] §2.2.2): for a square matrix $\mathbf{A}\in\mathbb{R}^{n\times n}$, a matrix $\mathbf{B}$ with $\mathbf{A}\mathbf{B}=\mathbf{I}_n=\mathbf{B}\mathbf{A}$ is the *inverse* of $\mathbf{A}$, denoted $\mathbf{A}^{-1}$. Not every matrix has one:

- If $\mathbf{A}^{-1}$ exists, $\mathbf{A}$ is **regular / invertible / nonsingular**.
- Otherwise $\mathbf{A}$ is **singular / noninvertible**.
- When it exists, the inverse is **unique**.

> This page treats the inverse as an *object* and the MML view; for the parallel-computing / numerical treatment (power-series, QR route, R `solve()`), see the sibling page [[MatrixInversion]].

## The $2\times 2$ case and the determinant

For $\mathbf{A}=\begin{bmatrix}a_{11}&a_{12}\\a_{21}&a_{22}\end{bmatrix}$ ([[mml-ch02-linear-algebra|MML Ch 2]] Eq. 2.24):

$$\mathbf{A}^{-1}=\frac{1}{a_{11}a_{22}-a_{12}a_{21}}\begin{bmatrix}a_{22}&-a_{12}\\-a_{21}&a_{11}\end{bmatrix}$$

which exists iff $a_{11}a_{22}-a_{12}a_{21}\neq0$. That quantity is the [[Determinant|determinant]] — the inverse exists iff $\det(\mathbf{A})\neq0$, equivalently iff $\operatorname{rk}(\mathbf{A})=n$, equivalently iff the rows/columns are [[LinearIndependence|linearly independent]].

## Identities (MML Eqs. 2.26–2.31)

- $\mathbf{A}\mathbf{A}^{-1}=\mathbf{I}=\mathbf{A}^{-1}\mathbf{A}$.
- $(\mathbf{A}\mathbf{B})^{-1}=\mathbf{B}^{-1}\mathbf{A}^{-1}$ (order reverses).
- $(\mathbf{A}+\mathbf{B})^{-1}\neq\mathbf{A}^{-1}+\mathbf{B}^{-1}$ in general.
- $(\mathbf{A}^{-1})^\top=(\mathbf{A}^\top)^{-1}=:\mathbf{A}^{-\top}$.

## Computing it via the augmented matrix

To find $\mathbf{A}^{-1}$, bring the augmented matrix $[\mathbf{A}\,|\,\mathbf{I}_n]$ to [[ReducedRowEchelonForm|reduced row-echelon form]] using [[GaussianElimination|Gaussian elimination]]; the result is $[\mathbf{I}_n\,|\,\mathbf{A}^{-1}]$ ([[mml-ch02-linear-algebra|MML Ch 2]] Eqs. 2.56–2.58). This is exactly solving the simultaneous systems $\mathbf{A}\mathbf{X}=\mathbf{I}_n$ — inverting a matrix is equivalent to solving systems of linear equations. For non-square or non-invertible $\mathbf{A}$ with independent columns, the **Moore–Penrose pseudo-inverse** $(\mathbf{A}^\top\mathbf{A})^{-1}\mathbf{A}^\top$ gives the minimum-norm least-squares solution (Eq. 2.59).

## Connections

- [[MatrixInversion]] — sibling page: numerical/parallel methods and R syntax.
- [[Determinant]] — $\mathbf{A}^{-1}$ exists iff $\det(\mathbf{A})\neq0$.
- [[Rank]] — invertible iff full rank $\operatorname{rk}(\mathbf{A})=n$.
- [[GaussianElimination]] / [[ReducedRowEchelonForm]] — the augmented-matrix method.
- [[IdentityMatrix]] — the multiplicative neutral element $\mathbf{A}\mathbf{A}^{-1}=\mathbf{I}$.
- [[GeneralLinearGroup]] — the group of invertible matrices.
- [[mml-ch02-linear-algebra|MML Ch 2]] / [[mml-book]] — §2.2.2, §2.3 canonical reference.
