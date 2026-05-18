---
title: "Matrix Transpose"
type: concept
tags: [linear-algebra, matrix-algebra]
sources: [parproc-appB-matrix-algebra]
last_updated: 2026-05-17
---

# Matrix Transpose

The transpose of a matrix A, denoted $A'$ or $A^T$, is obtained by exchanging its rows and columns: the (i,j) element of $A'$ is the (j,i) element of A.

## Key Properties

- **Sum rule:** If $A + B$ is defined, then $(A + B)' = A' + B'$.
- **Product-reversal rule:** If A and B are conformable, then $(AB)' = B'A'$. The order reversal is essential — transposing a product flips the factor order.
- **Rank invariance:** $\text{rk}(A') = \text{rk}(A)$ — see [[Rank]].

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
- [[parproc-appB-matrix-algebra]] — §B.2 primary definition.
- [[parproc-ch11-parallel-matrix-operations]] — parallel matrix transpose is one of the worked examples in Ch6 (Thrust) and appears throughout Ch11.
