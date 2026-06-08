---
title: "Basis Change"
type: concept
tags: [linear-algebra, foundational]
sources: [mml-ch02-linear-algebra, mml-book]
last_updated: 2026-06-04
---

# Basis Change

How the [[TransformationMatrix|transformation matrix]] of a [[LinearMapping|linear mapping]] $\Phi:V\to W$ changes when the bases of $V$ and $W$ are replaced.

**Theorem 2.20 (Basis Change)** ([[mml-ch02-linear-algebra|MML Ch 2]] §2.7.2): for ordered bases $B,\tilde B$ of $V$ and $C,\tilde C$ of $W$, if $\mathbf{A}_\Phi$ is the transformation matrix w.r.t. $B,C$, then the matrix w.r.t. $\tilde B,\tilde C$ is

$$\tilde{\mathbf{A}}_\Phi=\mathbf{T}^{-1}\mathbf{A}_\Phi\mathbf{S},$$

where $\mathbf{S}\in\mathbb{R}^{n\times n}$ is the transformation matrix of $\operatorname{id}_V$ mapping $\tilde B$-coordinates to $B$-coordinates (its $j$-th column is the [[Coordinates|coordinate representation]] of $\tilde{\mathbf{b}}_j$ in basis $B$), and $\mathbf{T}\in\mathbb{R}^{m\times m}$ is the transformation matrix of $\operatorname{id}_W$ mapping $\tilde C$-coordinates to $C$-coordinates. Both $\mathbf{S}$ and $\mathbf{T}$ are regular.

The execution order in $\tilde{\mathbf{A}}_\Phi=\mathbf{T}^{-1}\mathbf{A}_\Phi\mathbf{S}$ reads right-to-left on a coordinate vector: $\mathbf{x}\mapsto\mathbf{S}\mathbf{x}\mapsto\mathbf{A}_\Phi(\mathbf{S}\mathbf{x})\mapsto\mathbf{T}^{-1}(\mathbf{A}_\Phi\mathbf{S}\mathbf{x})$.

## Equivalence and similarity

- **Definition 2.21 (Equivalence)**: $\mathbf{A},\tilde{\mathbf{A}}\in\mathbb{R}^{m\times n}$ are *equivalent* if $\tilde{\mathbf{A}}=\mathbf{T}^{-1}\mathbf{A}\mathbf{S}$ for some regular $\mathbf{S},\mathbf{T}$.
- **Definition 2.22 (Similarity)**: $\mathbf{A},\tilde{\mathbf{A}}\in\mathbb{R}^{n\times n}$ are *similar* if $\tilde{\mathbf{A}}=\mathbf{S}^{-1}\mathbf{A}\mathbf{S}$ for some regular $\mathbf{S}$.
- Similar matrices are always equivalent; equivalent matrices need not be similar.

## Why it matters

Basis change is the engine behind [[Eigendecomposition|eigendecomposition]] and diagonalization (MML Ch 4): for an endomorphism, choosing the eigenbasis makes $\mathbf{A}_\Phi$ diagonal. Quantities **invariant under basis change** — [[Determinant|determinant]], [[Trace|trace]], eigenvalues, [[Rank|rank]] — are intrinsic to the *mapping*, not the representation. Similar matrices share all of these.

## Connections

- [[TransformationMatrix]] — the object that changes.
- [[Coordinates]] / [[Basis]] — the coordinate systems being switched.
- [[LinearMapping]] — the invariant underneath.
- [[Eigendecomposition]] / [[Determinant]] / [[Trace]] / [[Rank]] — basis-change invariants (Ch 4).
- [[mml-ch02-linear-algebra|MML Ch 2]] / [[mml-book]] — §2.7.2 canonical reference.
