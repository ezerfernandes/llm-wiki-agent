---
title: "Linear Independence"
type: concept
tags: [linear-algebra, matrix-algebra]
sources: [parproc-appB-matrix-algebra, mml-ch02-linear-algebra, mml-book]
last_updated: 2026-06-04
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

## From [[mml-ch02-linear-algebra|MML Ch 2]]

**Definition 2.12** (§2.5): vectors $\mathbf{x}_1,\ldots,\mathbf{x}_k\in V$ are *linearly dependent* if there is a **non-trivial** [[LinearCombination|linear combination]] $\mathbf{0}=\sum_{i=1}^k\lambda_i\mathbf{x}_i$ with at least one $\lambda_i\neq0$; *linearly independent* if **only** the trivial solution $\lambda_1=\cdots=\lambda_k=0$ works. MML calls this "one of the most important concepts in linear algebra": independent vectors have **no redundancy** — removing any one loses information.

**Useful properties** (Remark, p. 41): $k$ vectors are dependent or independent, no third option; any set containing $\mathbf{0}$ or two identical vectors is dependent; if one vector is a multiple of another the set is dependent.

**Practical Gaussian-elimination test**: write the vectors as columns of a matrix and reduce to [[RowEchelonForm|row-echelon form]]. **Pivot columns are linearly independent; non-pivot columns are linear combinations of the pivot columns to their left.** All columns are independent **iff** all are pivot columns (Examples 2.14–2.15). For linear combinations $\mathbf{x}_j=\mathbf{B}\boldsymbol\lambda_j$, the $\mathbf{x}_j$ are independent iff the coordinate vectors $\boldsymbol\lambda_j$ are; and $m$ combinations of $k$ vectors are always dependent when $m>k$.

A maximal linearly independent set that also spans is a [[Basis|basis]] (Def 2.14).

## Connections

- [[LinearCombination]] — independence is about non-trivial combinations equalling $\mathbf{0}$.
- [[Basis]] / [[Span]] / [[Dimension]] — a basis is a maximal independent set; MML §2.6.
- [[Pivot]] / [[RowEchelonForm]] — pivot columns reveal the independent vectors.
- [[mml-ch02-linear-algebra|MML Ch 2]] / [[mml-book]] — §2.5 canonical reference.
- [[Rank]] — rank is the maximum number of linearly independent columns (or rows) of a matrix.
- [[Determinant]] — $\det(A) \neq 0$ iff the columns of A are linearly independent (for square A).
- [[MatrixInversion]] — A is invertible iff its rows/columns are linearly independent.
- [[StatisticalIndependence]] — a distinct concept (probability theory); do not confuse with linear independence.
- [[parproc-appB-matrix-algebra]] — §B.3 primary definition.
