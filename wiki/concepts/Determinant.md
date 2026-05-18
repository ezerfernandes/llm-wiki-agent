---
title: "Determinant"
type: concept
tags: [linear-algebra, foundational]
sources: [mml-book, d2l-appendix-mathematics]
last_updated: 2026-05-16
---

# Determinant

A scalar function $\det:\mathbb{R}^{n\times n}\to\mathbb{R}$ on square matrices that ([[mml-book]] §4.1):

- **Tests invertibility**: $\mathbf{A}$ is invertible iff $\det(\mathbf{A})\neq 0$ (Thm 4.1) iff $\text{rk}(\mathbf{A})=n$ (Thm 4.3).
- **Measures signed volume**: $|\det(\mathbf{A})|$ is the volume of the parallelepiped spanned by columns of $\mathbf{A}$; the sign records orientation (Example 4.2). For $\mathbf{A}\in\mathbb{R}^{3\times 3}$, $V=|\det(\mathbf{A})|$.
- **Is multiplicative**: $\det(\mathbf{A}\mathbf{B}) = \det(\mathbf{A})\det(\mathbf{B})$.
- **Is invariant** under transposition and (since similar matrices have the same determinant) under change of basis — so the determinant is a property of the underlying *linear mapping*, not of any particular matrix representation.

## Computation

- $n=1$: $\det(a) = a$.
- $n=2$: $\det\begin{pmatrix} a&b\\c&d\end{pmatrix}=ad-bc$.
- $n=3$: Sarrus' rule (six terms).
- $n>3$: [[LaplaceExpansion]] (recursive) or — in practice — Gaussian elimination to triangular form, then product of diagonal entries.

## Where determinants surface in ML

- **Change-of-variables formula** for densities ([[mml-book]] §6.7): if $\mathbf{y} = f(\mathbf{x})$ is invertible, $p_Y(\mathbf{y}) = p_X(f^{-1}(\mathbf{y}))\,|\det J_{f^{-1}}(\mathbf{y})|$ — the Jacobian determinant is the volume-scaling factor. Underlies [[NormalizingFlow|normalizing flows]].
- **Multivariate Gaussian density** has $|\boldsymbol\Sigma|^{-1/2}$ in its normalizer ([[mml-book]] §6.5) — the determinant captures the "volume" of the covariance ellipsoid.
- **Test for linear independence** of $n$ vectors in $\mathbb{R}^n$.

## Appendix B Definition (Matloff)

Section B.4 of *Programming on Parallel Machines* ([[parproc-appB-matrix-algebra]]) presents a purely computational treatment. Let $A_{-(i,j)}$ denote the submatrix of A obtained by deleting row i and column j. The determinant is computed recursively across any fixed row k:

$$\det(A) = \sum_{m=1}^{n} (-1)^{k+m} \det(A_{-(k,m)})$$

Base case for $2 \times 2$:

$$\det\begin{pmatrix}s & t \\ u & v\end{pmatrix} = sv - tu$$

Matloff notes that determinants are "mainly of theoretical importance" in practice, but clarify conceptual understanding — particularly the invertibility criterion ($A^{-1}$ exists iff $\det(A) \neq 0$) and its equivalence to [[LinearIndependence|linear independence]] of the rows/columns.

## Connections

- [[mml-book]] — §4.1 canonical reference.
- [[determinant-of-a-square-matrix]] — algebrica.org's determinant page (computation-focused).
- [[Trace]] — companion summary statistic.
- [[CharacteristicPolynomial]] — defined via $\det(\mathbf{A}-\lambda\mathbf{I})$.
- [[MatrixDecomposition]] — broader taxonomy.
- [[LinearIndependence]] — $\det(A) \neq 0$ iff columns of A are linearly independent (square A).
- [[parproc-appB-matrix-algebra]] — §B.4 computational procedure.
