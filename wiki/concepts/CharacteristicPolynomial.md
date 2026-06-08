---
title: "Characteristic Polynomial"
type: concept
tags: [linear-algebra, eigenvalue, matrix-decomposition]
sources: [mml-book, mml-ch04-matrix-decompositions]
last_updated: 2026-06-04
---

# Characteristic Polynomial

$p_\mathbf{A}(\lambda) = \det(\mathbf{A}-\lambda\mathbf{I})$ ([[mml-book]] §4.2) — its roots are the [[Eigenvalue|eigenvalues]] of $\mathbf{A}$. The algebraic route to [[Eigendecomposition]].

## From [[mml-ch04-matrix-decompositions|MML Ch 4]]

**Definition 4.5** (§4.1, Eqs. 4.22a–4.22b): for $\lambda\in\mathbb{R}$ and square $\mathbf{A}\in\mathbb{R}^{n\times n}$,

$$p_\mathbf{A}(\lambda) := \det(\mathbf{A}-\lambda\mathbf{I}) = c_0 + c_1\lambda + c_2\lambda^2 + \cdots + c_{n-1}\lambda^{n-1} + (-1)^n\lambda^n$$

with $c_0,\ldots,c_{n-1}\in\mathbb{R}$. The **two extreme coefficients are the [[Determinant]] and [[Trace]]** (Eqs. 4.23–4.24):

$$c_0 = \det(\mathbf{A}), \qquad c_{n-1} = (-1)^{n-1}\operatorname{tr}(\mathbf{A}).$$

## Why it gives eigenvalues

**Theorem 4.8**: $\lambda$ is an eigenvalue of $\mathbf{A}$ iff it is a root of $p_\mathbf{A}(\lambda)$. The reasoning: $\mathbf{A}\mathbf{x}=\lambda\mathbf{x}$ for some $\mathbf{x}\neq\mathbf{0}$ requires $(\mathbf{A}-\lambda\mathbf{I})$ to have a non-trivial kernel, hence to be singular, hence $\det(\mathbf{A}-\lambda\mathbf{I})=0$.

- The **[[Eigenvalue|algebraic multiplicity]]** of an eigenvalue (Def. 4.9) is the number of times it appears as a root of $p_\mathbf{A}$.
- Computing eigenvalues by hand = factoring $p_\mathbf{A}(\lambda)$ (Examples 4.5, 4.8, 4.11) — so algebrica.org's [[roots-of-a-polynomial]] / [[polynomial-equations]] are the prerequisites.

## Connections

- [[mml-book]] / [[mml-ch04-matrix-decompositions|MML Ch 4]] — §4.1–4.2 canonical reference (Def. 4.5, Thm 4.8).
- [[Eigenvalue]] / [[Eigenvector]] / [[Eigenspace]] — roots and their associated vectors/subspaces.
- [[Determinant]] / [[Trace]] — the two extreme coefficients.
- [[Eigendecomposition]] — the algebraic route to it.
- [[DefectiveMatrix]] — repeated roots can yield geometric < algebraic multiplicity.
