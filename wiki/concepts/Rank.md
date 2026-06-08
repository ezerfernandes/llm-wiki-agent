---
title: "Rank"
type: concept
tags: [linear-algebra, matrix-algebra]
sources: [mml-book, mml-ch02-linear-algebra, mml-ch04-matrix-decompositions, d2l-appendix-mathematics, parproc-appB-matrix-algebra]
last_updated: 2026-06-04
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

## From [[mml-ch02-linear-algebra|MML Ch 2]]

**Definition** (§2.6.2): $\operatorname{rk}(\mathbf{A})$ is the number of linearly independent columns of $\mathbf{A}\in\mathbb{R}^{m\times n}$, which **equals** the number of linearly independent rows. Properties (Examples 2.18):

- **Column rank = row rank**: $\operatorname{rk}(\mathbf{A})=\operatorname{rk}(\mathbf{A}^\top)$.
- The columns span the [[Image|image / range]] (=[[ColumnSpace|column space]]) $U\subseteq\mathbb{R}^m$ with $\dim(U)=\operatorname{rk}(\mathbf{A})$; rows span $W\subseteq\mathbb{R}^n$ with $\dim(W)=\operatorname{rk}(\mathbf{A})$. A basis of either is found via Gaussian elimination ([[Pivot|pivot]] columns of $\mathbf{A}$ / of $\mathbf{A}^\top$).
- **Invertibility**: $\mathbf{A}\in\mathbb{R}^{n\times n}$ is regular iff $\operatorname{rk}(\mathbf{A})=n$.
- **Solvability**: $\mathbf{A}\mathbf{x}=\mathbf{b}$ is solvable iff $\operatorname{rk}(\mathbf{A})=\operatorname{rk}(\mathbf{A}|\mathbf{b})$.
- **Kernel dimension**: the solution space of $\mathbf{A}\mathbf{x}=\mathbf{0}$ (the [[NullSpace|kernel/null space]]) has dimension $n-\operatorname{rk}(\mathbf{A})$.
- **Full rank / rank deficient**: $\mathbf{A}$ has *full rank* iff $\operatorname{rk}(\mathbf{A})=\min(m,n)$; otherwise it is *rank deficient*.

Rank is the "rank" half of the [[RankNullityTheorem|rank–nullity theorem]]: $\dim(\ker\Phi)+\operatorname{rk}(\mathbf{A})=\dim(V)$ (Thm 2.24). Rank is a [[BasisChange|basis-change]] invariant of the underlying linear mapping.

## From [[mml-ch04-matrix-decompositions|MML Ch 4]]

Rank ties the chapter together. **Theorem 4.3** (§4.1): a square $\mathbf{A}$ has $\det(\mathbf{A})\neq0$ iff $\operatorname{rk}(\mathbf{A})=n$ — full rank ⟺ regular/invertible (the [[MatrixPhylogeny|matrix phylogeny]]'s "regular vs singular" split). In the [[SingularValueDecomposition|SVD]] (§4.5), the rank $r$ equals the number of nonzero singular values; the rank also bounds $r\in[0,\min(m,n)]$. The [[LowRankApproximation|rank-$k$ approximation]] (§4.6) deliberately *lowers* the rank — $\operatorname{rk}(\widehat{\mathbf{A}}(k))=k$ — and the [[EckartYoung|Eckart–Young]] proof invokes the rank–nullity theorem. An eigenvalue $\lambda$ of $\mathbf{A}$ satisfies $\operatorname{rk}(\mathbf{A}-\lambda\mathbf{I})<n$ (Def. 4.6 equivalence).

## R Syntax

```r
qr(a)$rank   # numerical rank (subject to roundoff)
```

## Connections

- [[LinearIndependence]] — rank counts the maximum number of linearly independent columns.
- [[Determinant]] — for square A, $\text{rk}(A) = n$ iff $\det(A) \neq 0$.
- [[MatrixInversion]] — A is invertible iff it is square and full rank.
- [[MatrixTranspose]] — transposition preserves rank: $\text{rk}(A') = \text{rk}(A)$.
- [[Image]] / [[ColumnSpace]] / [[NullSpace]] / [[RankNullityTheorem]] — rank ties image and kernel dimensions (MML §2.7.3).
- [[mml-book]] / [[mml-ch02-linear-algebra|MML Ch 2]] — §2.6, §2.7, §4.1 primary references.
- [[parproc-appB-matrix-algebra]] — §B.7 formal properties.
