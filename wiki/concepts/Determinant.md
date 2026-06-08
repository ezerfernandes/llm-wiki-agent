---
title: "Determinant"
type: concept
tags: [linear-algebra, foundational]
sources: [mml-book, mml-ch04-matrix-decompositions, mml-ch02-linear-algebra, d2l-appendix-mathematics]
last_updated: 2026-06-04
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

## First appearance in [[mml-ch02-linear-algebra|MML Ch 2]]

The determinant enters the book in §2.2.2 as the **$2\times2$ invertibility criterion**: $\mathbf{A}=\begin{bmatrix}a_{11}&a_{12}\\a_{21}&a_{22}\end{bmatrix}$ is invertible iff $a_{11}a_{22}-a_{12}a_{21}\neq0$, and this quantity is the determinant of a $2\times2$ matrix (Eq. 2.24). MML notes "we can generally use the determinant to check whether a matrix is invertible," deferring the full treatment to Ch 4. So the chain [[MatrixInverse|inverse exists]] ⟺ $\det\neq0$ ⟺ full [[Rank|rank]] ⟺ columns [[LinearIndependence|independent]] is set up already in Ch 2.

## Appendix B Definition (Matloff)

Section B.4 of *Programming on Parallel Machines* ([[parproc-appB-matrix-algebra]]) presents a purely computational treatment. Let $A_{-(i,j)}$ denote the submatrix of A obtained by deleting row i and column j. The determinant is computed recursively across any fixed row k:

$$\det(A) = \sum_{m=1}^{n} (-1)^{k+m} \det(A_{-(k,m)})$$

Base case for $2 \times 2$:

$$\det\begin{pmatrix}s & t \\ u & v\end{pmatrix} = sv - tu$$

Matloff notes that determinants are "mainly of theoretical importance" in practice, but clarify conceptual understanding — particularly the invertibility criterion ($A^{-1}$ exists iff $\det(A) \neq 0$) and its equivalence to [[LinearIndependence|linear independence]] of the rows/columns.

## From [[mml-ch04-matrix-decompositions|MML Ch 4]]

The full §4.1 treatment (book pp. 99–103). The determinant is a scalar function on square matrices (Eq. 4.1, written $\det(\mathbf{A})$ or $|\mathbf{A}|$ — *not* the absolute value, marginal note p. 99). Key results:

- **Closed forms**: $n=1$: $a_{11}$; $n=2$: $a_{11}a_{22}-a_{12}a_{21}$ (Eq. 4.6); $n=3$: **Sarrus' rule** (six terms, Eq. 4.7). For a triangular matrix, $\det(\mathbf{T})=\prod_i T_{ii}$ (Eq. 4.8).
- **[[LaplaceExpansion|Laplace expansion]]** (Thm 4.2): recursive computation via minors/cofactors for $n>3$.
- **Theorem 4.1**: $\mathbf{A}$ invertible iff $\det(\mathbf{A})\neq0$. **Theorem 4.3**: $\det(\mathbf{A})\neq0$ iff $\operatorname{rk}(\mathbf{A})=n$ (full [[Rank|rank]]).
- **Properties** (p. 103): multiplicative $\det(\mathbf{A}\mathbf{B})=\det(\mathbf{A})\det(\mathbf{B})$; $\det(\mathbf{A})=\det(\mathbf{A}^\top)$; $\det(\mathbf{A}^{-1})=1/\det(\mathbf{A})$; [[SimilarityTransform|basis-invariant]] (similar matrices share a determinant); adding a row/column multiple to another leaves $\det$ unchanged; scaling a row/column by $\lambda$ scales $\det$ by $\lambda$, so $\det(\lambda\mathbf{A})=\lambda^n\det(\mathbf{A})$; swapping two rows/columns flips the sign. These let one compute $\det$ by Gaussian elimination to triangular form.
- **Signed volume** (Example 4.2): $\det(\mathbf{A})$ is the signed volume of the parallelepiped spanned by the columns; the sign encodes orientation. Worked $3\times3$ example: $V=|\det(\mathbf{A})|=186$ (Eq. 4.11).
- **Eigenvalue identity** (Thm 4.16): $\det(\mathbf{A})=\prod_{i=1}^n\lambda_i$ — the *product* of eigenvalues (cf. [[Trace]] = sum). The determinant is also the coefficient $c_0$ of the [[CharacteristicPolynomial]] (Eq. 4.23).
- **Practical note** (§4.1, §4.8): contemporary ML supersedes explicit determinant computation with Gaussian elimination; the determinant survives as a *theoretical* tool (orientation, change-of-variables).

## Connections

- [[mml-book]] — §4.1 canonical reference.
- [[mml-ch04-matrix-decompositions|MML Ch 4]] — full §4.1 deep dive.
- [[LaplaceExpansion]] — recursive computation; [[MatrixPhylogeny]] — determinant splits square matrices into singular/regular.
- [[determinant-of-a-square-matrix]] — algebrica.org's determinant page (computation-focused).
- [[Trace]] — companion summary statistic.
- [[CharacteristicPolynomial]] — defined via $\det(\mathbf{A}-\lambda\mathbf{I})$.
- [[MatrixDecomposition]] — broader taxonomy.
- [[LinearIndependence]] — $\det(A) \neq 0$ iff columns of A are linearly independent (square A).
- [[parproc-appB-matrix-algebra]] — §B.4 computational procedure.
