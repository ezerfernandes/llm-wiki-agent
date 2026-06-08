---
title: "Vector Subspace"
type: concept
tags: [linear-algebra, foundational, algebra]
sources: [mml-ch02-linear-algebra, mml-book]
last_updated: 2026-06-04
---

# Vector Subspace

**Definition 2.10** ([[mml-ch02-linear-algebra|MML Ch 2]] §2.4.3): let $V=(\mathcal{V},+,\cdot)$ be a [[VectorSpace|vector space]] and $\mathcal{U}\subseteq\mathcal{V}$, $\mathcal{U}\neq\emptyset$. Then $U=(\mathcal{U},+,\cdot)$ is a *vector subspace* (or *linear subspace*) of $V$, written $U\subseteq V$, if it is itself a vector space under the operations of $V$ restricted to $\mathcal{U}\times\mathcal{U}$ and $\mathbb{R}\times\mathcal{U}$.

Intuitively, subspaces are sets contained in $V$ that are **closed** under vector-space operations — performing addition and scaling on their elements never leaves the subset.

## The closure test

A subspace inherits the Abelian-group, distributivity, associativity, and neutral-element properties from $V$ for free (they hold for all of $\mathcal{V}\supseteq\mathcal{U}$). So to verify $U\subseteq V$ one only needs:

1. $\mathcal{U}\neq\emptyset$, in particular $\mathbf{0}\in\mathcal{U}$;
2. **Closure** under scalar multiplication: $\forall\lambda\in\mathbb{R},\mathbf{x}\in\mathcal{U}:\ \lambda\mathbf{x}\in\mathcal{U}$;
3. **Closure** under addition: $\forall\mathbf{x},\mathbf{y}\in\mathcal{U}:\ \mathbf{x}+\mathbf{y}\in\mathcal{U}$.

## Examples (MML Example 2.12)

- The **trivial** subspaces of any $V$ are $V$ itself and $\{\mathbf{0}\}$.
- The solution set of a **homogeneous** system $\mathbf{A}\mathbf{x}=\mathbf{0}$ is a subspace of $\mathbb{R}^n$ (the [[NullSpace|kernel]]).
- The solution set of an **inhomogeneous** system $\mathbf{A}\mathbf{x}=\mathbf{b}$ ($\mathbf{b}\neq\mathbf{0}$) is **not** a subspace (it lacks $\mathbf{0}$) — it is an [[AffineSubspace|affine subspace]].
- The **intersection** of arbitrarily many subspaces is itself a subspace.
- Conversely, **every** subspace $U\subseteq(\mathbb{R}^n,+,\cdot)$ is the solution space of some homogeneous system $\mathbf{A}\mathbf{x}=\mathbf{0}$.

## Why ML cares

Subspaces are "a key idea in machine learning" (MML §2.4.3): dimensionality reduction ([[PrincipalComponentAnalysis|PCA]], Ch 10) projects data onto a low-dimensional subspace; the [[ColumnSpace|column space]] / [[Image|image]] and [[NullSpace|kernel]] of a linear mapping are subspaces.

## Connections

- [[VectorSpace]] — the parent space.
- [[Span]] / [[Basis]] / [[Dimension]] — a subspace is the span of a basis; $\dim(U)\leq\dim(V)$.
- [[NullSpace]] / [[ColumnSpace]] / [[Image]] — subspaces arising from a linear mapping.
- [[AffineSubspace]] — the offset (non-subspace) generalization.
- [[SystemOfLinearEquations]] — homogeneous solution sets are subspaces.
- [[mml-ch02-linear-algebra|MML Ch 2]] / [[mml-book]] — §2.4.3 canonical reference.
