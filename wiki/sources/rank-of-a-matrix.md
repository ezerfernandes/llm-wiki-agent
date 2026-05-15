---
title: "Rank of a Matrix"
type: source
tags: [math, vectors-and-matrices]
date: 2026-05-10
source_file: raw/vectors-and-matrices/rank-of-a-matrix.md
---

## Summary
The rank of a matrix \\( A \\), denoted \\( r(A) \\) or \\( \\mathrm{rank}(A) \\), is the maximum number of linearly independent rows (or equivalently, columns) of \\( A \\). For an \\( m \\times n \\) matrix \\( A \\), the rank satisfies:

## Key Claims
- **Submatrices and minors** — A submatrix of a matrix \\( A \\in M_{m,n}(\\mathbb{R}) \\) is any matrix obtained by selecting \\( k \\) rows and \\( h \\) columns from \\( A \\), preserving the original order of elements, with \\( k \\leq m \\) and \\( h \\leq n \\).
- **Definition via minors** — The rank of a matrix \\( A \\) is the largest integer \\( r \\) such that at least one minor of order \\( r \\) is nonzero.
- **Computing the rank via Gaussian elimination** — For matrices of large order, computing all minors is impractical.
- **Properties of the rank**

## Key Quotes
> Source page: algebrica.org — see `source_file`.

## Connections
- [[vectors|Vectors]] — vectors
- [[SystemsOfLinearEquations]] — systems of linear equations
- [[rouche-capelli-theorem|RoucheCapelliTheorem]] — rouché-capelli theorem
- [[inverse-matrix|InverseMatrix]] — invertible
- [[determinant-of-a-square-matrix|Determinant]] — determinant
- [[SolvingLinearSystemsUsingGaussianElimination]] — gaussian elimination

## Contradictions
None.
