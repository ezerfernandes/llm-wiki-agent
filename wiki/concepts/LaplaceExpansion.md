---
title: "Laplace Expansion"
type: concept
tags: [linear-algebra, determinant, matrix-algebra]
sources: [mml-ch04-matrix-decompositions, mml-book]
last_updated: 2026-06-04
---

# Laplace Expansion

A recursive algorithm for computing the [[Determinant]] of an $n\times n$ matrix by reducing it to determinants of $(n-1)\times(n-1)$ submatrices ([[mml-book]] Theorem 4.2, §4.1). Applied repeatedly, it bottoms out at $2\times2$ determinants.

**Theorem 4.2** — for $\mathbf{A}\in\mathbb{R}^{n\times n}$ and any fixed $j=1,\ldots,n$:

- **Expansion along column $j$:**
$$\det(\mathbf{A}) = \sum_{k=1}^n (-1)^{k+j}\, a_{kj}\, \det(\mathbf{A}_{k,j})$$
- **Expansion along row $j$:**
$$\det(\mathbf{A}) = \sum_{k=1}^n (-1)^{k+j}\, a_{jk}\, \det(\mathbf{A}_{j,k})$$

Here $\mathbf{A}_{k,j}\in\mathbb{R}^{(n-1)\times(n-1)}$ is the submatrix obtained by **deleting row $k$ and column $j$**.

## Minors and cofactors

([[mml-book]] §4.1, marginal note): $\det(\mathbf{A}_{k,j})$ is called a **minor**, and $(-1)^{k+j}\det(\mathbf{A}_{k,j})$ a **cofactor**. The $(-1)^{k+j}$ sign factor forms a checkerboard pattern across the matrix.

## Example

([[mml-book]] Example 4.3, Eq. 4.15): expanding $\mathbf{A}=\begin{bmatrix}1&2&3\\3&1&2\\0&0&1\end{bmatrix}$ along the first row,
$$\det(\mathbf{A}) = 1\begin{vmatrix}1&2\\0&1\end{vmatrix} - 2\begin{vmatrix}3&2\\0&1\end{vmatrix} + 3\begin{vmatrix}3&1\\0&0\end{vmatrix} = 1 - 6 + 0 = -5,$$
matching [[Determinant|Sarrus' rule]] ($-5$).

## Practical note

For all but the smallest matrices, Laplace expansion is $O(n!)$ and is superseded in practice by Gaussian elimination to triangular form, then a diagonal product ([[mml-book]] §4.1, §4.8 — Press et al. 2007). It remains the standard *definitional / by-hand* route and the foundation of the cofactor formula for the inverse.

## Connections

- [[mml-ch04-matrix-decompositions|MML Ch 4]] — §4.1 canonical reference (Thm 4.2).
- [[Determinant]] — what it computes; see also Sarrus' rule ($n=3$) and the triangular-matrix product.
- [[CharacteristicPolynomial]] — $p_\mathbf{A}(\lambda)=\det(\mathbf{A}-\lambda\mathbf{I})$ is itself a determinant expandable this way.
- [[Rank]] — full rank ⟺ nonzero determinant (Thm 4.3).
</content>
