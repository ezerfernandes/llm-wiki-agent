---
title: "Matrix"
type: concept
tags: [linear-algebra, foundational, matrix-algebra]
sources: [mml-ch02-linear-algebra, mml-book]
last_updated: 2026-06-04
---

# Matrix

**Definition 2.1** ([[mml-ch02-linear-algebra|MML Ch 2]] §2.2): a real $(m,n)$ matrix $\mathbf{A}$ is an $m\cdot n$-tuple of elements $a_{ij}\in\mathbb{R}$ ($i=1,\ldots,m$; $j=1,\ldots,n$) arranged in a rectangular scheme of $m$ rows and $n$ columns. $\mathbb{R}^{m\times n}$ denotes the set of all such matrices.

Matrices serve two roles in linear algebra (MML §2.2): they **compactly represent [[SystemOfLinearEquations|systems of linear equations]]** ($\mathbf{A}\mathbf{x}=\mathbf{b}$), and they **represent [[LinearMapping|linear mappings]]** between vector spaces (in chosen bases — see [[TransformationMatrix]]). When working with a matrix it is essential to keep in mind which of these it stands for.

## Special shapes and reshaping

- A $(1,n)$-matrix is a **row** / *row vector*; an $(m,1)$-matrix is a **column** / *column vector*.
- By stacking its $n$ columns, $\mathbf{A}\in\mathbb{R}^{m\times n}$ can be flattened to a long vector $\mathbf{a}\in\mathbb{R}^{mn}$; in fact $\mathbb{R}^{m\times n}\cong\mathbb{R}^{mn}$ as vector spaces.
- A **square** matrix has $m=n$. A square matrix is [[SymmetricMatrix|symmetric]] if $\mathbf{A}=\mathbf{A}^\top$.

## Operations (MML §2.2)

- **Addition** (Eq. 2.12): element-wise, requiring equal shapes.
- **[[MatrixMultiplication|Multiplication]]** (Eq. 2.13): $c_{ij}=\sum_l a_{il}b_{lj}$; non-commutative.
- **Scalar multiplication** (§2.2.3): $\lambda\mathbf{A}$ scales every entry.
- **[[MatrixTranspose|Transpose]]** (Def 2.4): $b_{ij}=a_{ji}$.
- **[[MatrixInverse|Inverse]]** (Def 2.3): the unique $\mathbf{A}^{-1}$ with $\mathbf{A}\mathbf{A}^{-1}=\mathbf{I}$, when it exists.

$(\mathbb{R}^{m\times n},+)$ is an Abelian [[GroupTheory|group]]; with scalar multiplication it is a [[VectorSpace|vector space]]; the invertible square matrices under multiplication form the [[GeneralLinearGroup|general linear group]] $GL(n,\mathbb{R})$.

## Connections

- [[MatrixMultiplication]] / [[MatrixInverse]] / [[MatrixTranspose]] / [[IdentityMatrix]] / [[SymmetricMatrix]] — the algebra.
- [[Determinant]] / [[Rank]] / [[Trace]] — scalar/integer summaries.
- [[LinearMapping]] / [[TransformationMatrix]] — the mapping interpretation.
- [[SystemOfLinearEquations]] — the equation interpretation.
- [[MatrixDecomposition]] — factoring matrices (MML Ch 4).
- [[mml-ch02-linear-algebra|MML Ch 2]] / [[mml-book]] — §2.2 canonical reference.
