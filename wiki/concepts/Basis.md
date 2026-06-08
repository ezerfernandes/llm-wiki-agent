---
title: "Basis"
type: concept
tags: [linear-algebra, foundational]
sources: [mml-ch02-linear-algebra, mml-book]
last_updated: 2026-06-04
---

# Basis

**Definition 2.14** ([[mml-ch02-linear-algebra|MML Ch 2]] §2.6.1): a generating set $\mathcal{A}$ of a [[VectorSpace|vector space]] $V$ is *minimal* if no smaller subset spans $V$. Every **linearly independent generating set** is minimal and is a *basis* of $V$.

For $\mathcal{B}\subseteq\mathcal{V}$, $\mathcal{B}\neq\emptyset$, the following are **equivalent** (MML p. 45):

- $\mathcal{B}$ is a basis of $V$;
- $\mathcal{B}$ is a **minimal** [[Span|generating set]];
- $\mathcal{B}$ is a **maximal** [[LinearIndependence|linearly independent]] set (adding any other vector makes it dependent);
- every $\mathbf{x}\in V$ is a **unique** linear combination of $\mathcal{B}$: $\mathbf{x}=\sum_i\lambda_i\mathbf{b}_i=\sum_i\psi_i\mathbf{b}_i\Rightarrow\lambda_i=\psi_i$.

> *"A basis is a minimal generating set and a maximal linearly independent set of vectors."* — MML marginal note, p. 45.

## Key facts

- **Every vector space possesses a basis** (MML Remark, p. 45).
- **Bases are not unique** — there are many bases of a given $V$ (Example 2.16: standard basis $\{\mathbf{e}_1,\mathbf{e}_2,\mathbf{e}_3\}$ of $\mathbb{R}^3$, plus infinitely many others).
- **All bases of $V$ have the same number of elements** — that count is the [[Dimension|dimension]] $\dim(V)$.
- A linearly independent set that does **not** span is not a basis (e.g. 3 independent vectors in $\mathbb{R}^4$).

## Ordered basis and coordinates

An *ordered basis* $B=(\mathbf{b}_1,\ldots,\mathbf{b}_n)$ fixes an order, defining a **coordinate system**: each $\mathbf{x}=\alpha_1\mathbf{b}_1+\cdots+\alpha_n\mathbf{b}_n$ has a unique [[Coordinates|coordinate vector]] $\boldsymbol\alpha$. The *same* vector has *different* coordinates under different bases (MML §2.7.1, Figs. 2.8–2.9) — the foundation of [[BasisChange|basis change]].

## Finding a basis of a subspace

For $U=\operatorname{span}[\mathbf{x}_1,\ldots,\mathbf{x}_m]\subseteq\mathbb{R}^n$ (MML p. 46): write the spanning vectors as columns of a matrix, reduce to [[RowEchelonForm|row-echelon form]], and the spanning vectors at the **pivot columns** form a basis.

## Connections

- [[Span]] — a basis is a minimal generating set.
- [[LinearIndependence]] — a basis is a maximal independent set.
- [[Dimension]] — number of basis vectors.
- [[Coordinates]] / [[TransformationMatrix]] / [[BasisChange]] — bases as coordinate systems.
- [[Rank]] — a basis of the [[ColumnSpace|column space]] sits at the pivot columns.
- [[OrthonormalBasis]] — basis with unit, mutually orthogonal vectors (MML Ch 3).
- [[mml-ch02-linear-algebra|MML Ch 2]] / [[mml-book]] — §2.6.1 canonical reference.
