---
title: "Linear Independence"
type: concept
tags: [linear-algebra, matrix-algebra]
sources: [parproc-appB-matrix-algebra]
last_updated: 2026-05-17
---

# Linear Independence

Equal-length vectors $X_1, \ldots, X_k$ are **linearly independent** if the only solution to

$$a_1 X_1 + a_2 X_2 + \cdots + a_k X_k = 0$$

is $a_1 = a_2 = \cdots = a_k = 0$. Equivalently, no vector in the set can be expressed as a linear combination of the others.

## Appendix B Definition (Matloff)

Section B.3 of *Programming on Parallel Machines* ([[parproc-appB-matrix-algebra]]) states this definition and uses it as the foundation for two downstream concepts:

1. **Matrix inverse** (§B.5): $A^{-1}$ exists if and only if the rows (or columns) of A are linearly independent.
2. **Matrix rank** (§B.7): the rank of A is the *maximal number of linearly independent columns* in A.

## Relationship to Determinant

For square matrices of size $n$, $n$ vectors are linearly independent if and only if the determinant of the matrix they form is nonzero (see [[Determinant]]). This links the algebraic definition to the computational test.

## Connections

- [[Rank]] — rank is the maximum number of linearly independent columns (or rows) of a matrix.
- [[Determinant]] — $\det(A) \neq 0$ iff the columns of A are linearly independent (for square A).
- [[MatrixInversion]] — A is invertible iff its rows/columns are linearly independent.
- [[StatisticalIndependence]] — a distinct concept (probability theory); do not confuse with linear independence.
- [[parproc-appB-matrix-algebra]] — §B.3 primary definition.
