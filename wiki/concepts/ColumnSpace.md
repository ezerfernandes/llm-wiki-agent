---
title: "Column Space"
type: concept
tags: [linear-algebra, foundational]
sources: [mml-ch02-linear-algebra, mml-book]
last_updated: 2026-06-04
---

# Column Space

The *column space* of a matrix $\mathbf{A}=[\mathbf{a}_1,\ldots,\mathbf{a}_n]\in\mathbb{R}^{m\times n}$ is the span of its columns, $\operatorname{span}[\mathbf{a}_1,\ldots,\mathbf{a}_n]\subseteq\mathbb{R}^m$ ([[mml-ch02-linear-algebra|MML Ch 2]] §2.7.3, Eqs. 2.124).

It is exactly the [[Image|image / range]] of the [[LinearMapping|linear mapping]] $\Phi(\mathbf{x})=\mathbf{A}\mathbf{x}$:

$$\operatorname{Im}(\Phi)=\{\mathbf{A}\mathbf{x}:\mathbf{x}\in\mathbb{R}^n\}=\operatorname{span}[\mathbf{a}_1,\ldots,\mathbf{a}_n].$$

The column space is a subspace of $\mathbb{R}^m$ — the "height" of the matrix. Its dimension equals the [[Rank|rank]]: $\dim(\text{column space})=\operatorname{rk}(\mathbf{A})$, and (by column-rank = row-rank) equals the dimension of the **row space** (span of the rows, a subspace of $\mathbb{R}^n$).

A [[Basis|basis]] of the column space sits at the **pivot columns** of the [[RowEchelonForm|row-echelon form]] of $\mathbf{A}$.

## Solvability

$\mathbf{A}\mathbf{x}=\mathbf{b}$ has a solution **iff** $\mathbf{b}$ lies in the column space — equivalently $\operatorname{rk}(\mathbf{A})=\operatorname{rk}(\mathbf{A}|\mathbf{b})$.

## Connections

- [[Image]] — the column space *is* the image of $\mathbf{x}\mapsto\mathbf{A}\mathbf{x}$.
- [[NullSpace]] — the complementary subspace in the domain.
- [[Rank]] — column rank = row rank = dim(column space).
- [[Span]] / [[Basis]] / [[Pivot]] — a basis sits at the pivot columns.
- [[SystemOfLinearEquations]] — $\mathbf{b}$ in the column space ⇔ solvable.
- [[mml-ch02-linear-algebra|MML Ch 2]] / [[mml-book]] — §2.7.3 canonical reference.
