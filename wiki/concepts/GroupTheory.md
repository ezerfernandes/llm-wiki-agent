---
title: "Group Theory"
type: concept
tags: [algebra, linear-algebra, foundational]
sources: [mml-ch02-linear-algebra, mml-book]
last_updated: 2026-06-04
---

# Group Theory

A **group** is the most basic algebraic structure that keeps "some structure of a set intact" under an operation. **Definition 2.7** ([[mml-ch02-linear-algebra|MML Ch 2]] §2.4.1): a set $\mathcal{G}$ with an operation $\otimes:\mathcal{G}\times\mathcal{G}\to\mathcal{G}$ forms a group $G=(\mathcal{G},\otimes)$ if:

1. **Closure**: $\forall x,y\in\mathcal{G}:\ x\otimes y\in\mathcal{G}$.
2. **Associativity**: $\forall x,y,z\in\mathcal{G}:\ (x\otimes y)\otimes z=x\otimes(y\otimes z)$.
3. **Neutral element**: $\exists e\in\mathcal{G}\ \forall x:\ x\otimes e=x$ and $e\otimes x=x$.
4. **Inverse element**: $\forall x\ \exists y:\ x\otimes y=e$ and $y\otimes x=e$, written $x^{-1}$.

If additionally $x\otimes y=y\otimes x$ for all $x,y$, the group is **Abelian (commutative)**.

> The inverse is relative to the operation $\otimes$ and does **not** necessarily mean $1/x$ ([[mml-ch02-linear-algebra|MML Ch 2]] Remark, p. 36).

## Examples (MML Example 2.10)

| Set & op | Group? | Notes |
|---|---|---|
| $(\mathbb{Z},+)$ | Abelian | textbook example |
| $(\mathbb{N}_0,+)$ | **No** | inverses missing |
| $(\mathbb{Z},\cdot)$ | **No** | inverses missing (except $\pm1$) |
| $(\mathbb{R}\setminus\{0\},\cdot)$ | Abelian | 0 has no inverse, so it is excluded |
| $(\mathbb{R}^n,+)$, $(\mathbb{Z}^n,+)$, $(\mathbb{R}^{m\times n},+)$ | Abelian | component-wise addition |
| $(\mathbb{R}^{n\times n},\cdot)$ | Group only on regular elements | → [[GeneralLinearGroup]] |

## Why it matters for ML

The group is the foundation of the [[VectorSpace|vector space]]: a vector space requires $(\mathcal{V},+)$ to be an **Abelian group** before adding scalar multiplication (MML Def 2.9). The mind map (Fig. 2.2) draws "Group → Vector space" labelled *Abelian with +*. Groups also underpin cryptography, coding theory, graphics, and symmetry/equivariance in modern deep learning.

## Connections

- [[VectorSpace]] — built on an Abelian group under $+$.
- [[GeneralLinearGroup]] — invertible matrices form a (non-Abelian) group under multiplication.
- [[IdentityMatrix]] — the neutral element of matrix multiplication.
- [[MatrixInverse]] — the group inverse for $GL(n,\mathbb{R})$.
- [[mml-ch02-linear-algebra|MML Ch 2]] / [[mml-book]] — §2.4.1 canonical reference.
