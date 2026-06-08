---
title: "Matrix Transpose"
type: concept
tags: [linear-algebra, matrix-algebra]
sources: [parproc-appB-matrix-algebra, mml-ch02-linear-algebra, mml-book]
last_updated: 2026-06-04
---

# Matrix Transpose

The transpose of a matrix A, denoted $A'$ or $A^T$, is obtained by exchanging its rows and columns: the (i,j) element of $A'$ is the (j,i) element of A.

## Key Properties

- **Sum rule:** If $A + B$ is defined, then $(A + B)' = A' + B'$.
- **Product-reversal rule:** If A and B are conformable, then $(AB)' = B'A'$. The order reversal is essential — transposing a product flips the factor order.
- **Rank invariance:** $\text{rk}(A') = \text{rk}(A)$ — see [[Rank]].

## From [[mml-ch02-linear-algebra|MML Ch 2]]

**Definition 2.4** (§2.2.2): for $\mathbf{A}\in\mathbb{R}^{m\times n}$, the transpose $\mathbf{B}=\mathbf{A}^\top\in\mathbb{R}^{n\times m}$ has $b_{ij}=a_{ji}$ — the columns of $\mathbf{A}$ become the rows of $\mathbf{A}^\top$. MML uses the superscript-$\top$ notation throughout (this page also uses Matloff's prime $A'$; same operation). Identities (Eqs. 2.29–2.31): $(\mathbf{A}^\top)^\top=\mathbf{A}$, $(\mathbf{AB})^\top=\mathbf{B}^\top\mathbf{A}^\top$, $(\mathbf{A}+\mathbf{B})^\top=\mathbf{A}^\top+\mathbf{B}^\top$, and for invertible $\mathbf{A}$: $(\mathbf{A}^{-1})^\top=(\mathbf{A}^\top)^{-1}=:\mathbf{A}^{-\top}$. A square matrix with $\mathbf{A}=\mathbf{A}^\top$ is [[SymmetricMatrix|symmetric]] (Def 2.5). A row vector is the transpose of a column vector, $\mathbf{x}^\top$.

## Orthogonal Matrices

A square matrix U is called **orthogonal** if its rows each have norm 1 and are mutually orthogonal (inner product 0). This is equivalent to $UU' = I$, i.e. $U^{-1} = U'$. Orthogonal matrices appear in [[QRDecomposition|QR decomposition]] and in the diagonalization of symmetric matrices via eigendecomposition (see [[Eigenvalue]]).

## Appendix B Definition (Matloff)

Section B.2 of *Programming on Parallel Machines* ([[parproc-appB-matrix-algebra]]) defines transpose and states the two key identities above. The notation $A'$ (prime) is used throughout the book alongside the standard $A^T$ notation.

## R Syntax

```r
t(a)   # transpose of matrix a
```

Extracting a single row of a matrix in R returns a plain vector (dropping the matrix class); use `x[1, , drop=FALSE]` to preserve the matrix type.

## Connections

- [[MatrixMultiplication]] — transpose interacts with multiplication via the product-reversal rule.
- [[MatrixInversion]] — for orthogonal matrices, $U^{-1} = U'$, which is the basis of the QR-based inverse formula $A^{-1} = R^{-1}Q'$.
- [[Rank]] — transposition preserves rank: $\text{rk}(A') = \text{rk}(A)$.
- [[Eigenvalue]] — the diagonalization $U'AU = D$ uses the transpose of the orthogonal eigenvector matrix.
- [[SymmetricMatrix]] — the $\mathbf{A}=\mathbf{A}^\top$ fixed point (MML Def 2.5).
- [[mml-ch02-linear-algebra|MML Ch 2]] / [[mml-book]] — §2.2.2 Def 2.4.
- [[parproc-appB-matrix-algebra]] — §B.2 primary definition.
- [[parproc-ch11-parallel-matrix-operations]] — parallel matrix transpose is one of the worked examples in Ch6 (Thrust) and appears throughout Ch11.
