---
title: "Rank"
type: concept
tags: [linear-algebra, matrix-algebra]
sources: [mml-book, d2l-appendix-mathematics, parproc-appB-matrix-algebra]
last_updated: 2026-05-17
---

# Rank

Dimension of the image of a linear mapping — number of linearly independent rows or columns of its matrix representation. $\mathbf{A}\in\mathbb{R}^{m\times n}$ is invertible iff square and full rank ([[mml-book]] §2.6, §4.1).

## Appendix B Definition (Matloff)

Section B.7 of *Programming on Parallel Machines* ([[parproc-appB-matrix-algebra]]) defines rank formally and lists its key properties. Let $\text{rk}(A)$ denote the rank of A:

- **Definition:** $\text{rk}(A)$ is the maximal number of linearly independent columns in A (see [[LinearIndependence]]).
- **Row-column symmetry:** $\text{rk}(A') = \text{rk}(A)$, so rank also equals the maximal number of linearly independent rows.
- **Dimension bound:** for an $r \times s$ matrix, $\text{rk}(A) \leq \min(r, s)$.
- **Gram matrix property:** $\text{rk}(A'A) = \text{rk}(A)$.

Matloff cautions that although rank is well-defined in theory, roundoff error makes numerical rank computation unreliable. In R, rank can be obtained from the `rank` component of `qr()` output, but should be treated with caution.

## R Syntax

```r
qr(a)$rank   # numerical rank (subject to roundoff)
```

## Connections

- [[LinearIndependence]] — rank counts the maximum number of linearly independent columns.
- [[Determinant]] — for square A, $\text{rk}(A) = n$ iff $\det(A) \neq 0$.
- [[MatrixInversion]] — A is invertible iff it is square and full rank.
- [[MatrixTranspose]] — transposition preserves rank: $\text{rk}(A') = \text{rk}(A)$.
- [[mml-book]] — §2.6, §4.1 primary references.
- [[parproc-appB-matrix-algebra]] — §B.7 formal properties.
