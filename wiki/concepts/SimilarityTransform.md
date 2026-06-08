---
title: "Similarity Transform"
type: concept
tags: [linear-algebra, matrix-algebra, basis-change]
sources: [mml-ch04-matrix-decompositions, mml-book, mml-ch02-linear-algebra]
last_updated: 2026-06-04
---

# Similarity Transform

Two square matrices $\mathbf{A},\mathbf{D}\in\mathbb{R}^{n\times n}$ are **similar** (Definition 2.22; [[mml-book]] §2.7.2) if there exists an invertible $\mathbf{P}$ with

$$\mathbf{D} = \mathbf{P}^{-1}\mathbf{A}\mathbf{P}.$$

The map $\mathbf{A}\mapsto\mathbf{P}^{-1}\mathbf{A}\mathbf{P}$ is a **similarity transform**. It is exactly a **change of basis**: $\mathbf{A}$ and $\mathbf{D}$ represent the *same linear mapping* $\Phi:V\to V$ in two different bases related by $\mathbf{P}$ ([[mml-book]] §2.7.2).

## Invariants under similarity

Because similar matrices are the same mapping in different coordinates, all *intrinsic* properties of the mapping are preserved ([[mml-book]] §4.1–4.2):

- **[[Determinant]]**: $\det(\mathbf{P}^{-1}\mathbf{A}\mathbf{P})=\det(\mathbf{A})$ — the determinant is basis-invariant.
- **[[Trace]]**: $\operatorname{tr}(\mathbf{S}^{-1}\mathbf{A}\mathbf{S})=\operatorname{tr}(\mathbf{A})$ via cyclic invariance (Eq. 4.21).
- **[[Eigenvalue|Eigenvalues]]**: similar matrices have the same eigenvalues (and the same [[CharacteristicPolynomial|characteristic polynomial]]) — so a mapping's eigenvalues are basis-independent.
- **[[Rank]]** is likewise a basis-change invariant.

Together, determinant, trace, and eigenvalues are the **key basis-invariant characteristics** of a linear mapping.

## Connection to diagonalization

[[Diagonalization]] is the special case where the target $\mathbf{D}$ is *diagonal*: $\mathbf{A}$ is diagonalizable iff it is **similar to a diagonal matrix** ([[mml-book]] Def. 4.19). Then $\mathbf{P}$ is the eigenvector matrix and $\mathbf{D}$ the diagonal of eigenvalues — the [[Eigendecomposition]] $\mathbf{A}=\mathbf{P}\mathbf{D}\mathbf{P}^{-1}$. For symmetric $\mathbf{A}$, $\mathbf{P}$ can be chosen orthogonal ($\mathbf{P}^{-1}=\mathbf{P}^\top$) by the [[SpectralTheorem|spectral theorem]].

## Connections

- [[mml-ch04-matrix-decompositions|MML Ch 4]] — §4.1, §4.4 (invariants, diagonalization).
- [[mml-ch02-linear-algebra|MML Ch 2]] — §2.7.2 (basis change, Def. 2.22 similar matrices).
- [[Diagonalization]] — similarity to a *diagonal* matrix.
- [[Eigendecomposition]] — the diagonalizing similarity transform.
- [[Determinant]] / [[Trace]] / [[Eigenvalue]] / [[Rank]] — the invariants preserved.
- [[BasisChange]] — what a similarity transform *is*.
</content>
