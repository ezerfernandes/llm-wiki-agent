---
title: "Dimension"
type: concept
tags: [linear-algebra, foundational]
sources: [mml-ch02-linear-algebra, mml-book]
last_updated: 2026-06-04
---

# Dimension

For a finite-dimensional [[VectorSpace|vector space]] $V$, the *dimension* $\dim(V)$ is the number of [[Basis|basis]] vectors of $V$ ([[mml-ch02-linear-algebra|MML Ch 2]] §2.6.1, p. 45). This is well-defined because **all bases of $V$ have the same number of elements**.

Intuitively, the dimension is the **number of independent directions** in the space.

## Key facts (MML p. 45–46)

- If $U\subseteq V$ is a subspace, then $\dim(U)\leq\dim(V)$, with equality **iff** $U=V$.
- The dimension is **not** the number of entries in a vector. Example: $V=\operatorname{span}[\begin{smallmatrix}0\\1\end{smallmatrix}]$ is one-dimensional even though its single basis vector has two components.
- $\dim(\mathbb{R}^n)=n$; $\dim(\mathbb{R}^{m\times n})=mn$.

## Relation to rank and rank–nullity

For a linear mapping $\Phi:V\to W$ with matrix $\mathbf{A}$:

- $\dim(\operatorname{Im}(\Phi))=\operatorname{rk}(\mathbf{A})$ (the [[ColumnSpace|column space]] dimension);
- $\dim(\ker(\Phi))=n-\operatorname{rk}(\mathbf{A})$ (the [[NullSpace|null space]] dimension);
- these sum to $\dim(V)$ — the [[RankNullityTheorem|rank–nullity theorem]].

Two finite-dimensional spaces are **isomorphic iff they have the same dimension** (MML Thm 2.17).

## Connections

- [[Basis]] — dimension counts basis vectors.
- [[Rank]] — dimension of the image / column space.
- [[RankNullityTheorem]] — $\dim(\ker)+\dim(\operatorname{Im})=\dim(V)$.
- [[VectorSubspace]] — $\dim(U)\leq\dim(V)$.
- [[IntrinsicDimension]] / [[CurseOfDimensionality]] — ML notions building on this.
- [[mml-ch02-linear-algebra|MML Ch 2]] / [[mml-book]] — §2.6.1 canonical reference.
