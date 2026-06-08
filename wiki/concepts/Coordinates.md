---
title: "Coordinates"
type: concept
tags: [linear-algebra, foundational]
sources: [mml-ch02-linear-algebra, mml-book]
last_updated: 2026-06-04
---

# Coordinates

**Definition 2.18** ([[mml-ch02-linear-algebra|MML Ch 2]] §2.7.1): given a [[VectorSpace|vector space]] $V$ and an ordered [[Basis|basis]] $B=(\mathbf{b}_1,\ldots,\mathbf{b}_n)$, every $\mathbf{x}\in V$ has a **unique** representation

$$\mathbf{x}=\alpha_1\mathbf{b}_1+\cdots+\alpha_n\mathbf{b}_n.$$

The scalars $\alpha_1,\ldots,\alpha_n$ are the *coordinates* of $\mathbf{x}$ with respect to $B$, and the vector $\boldsymbol\alpha=[\alpha_1,\ldots,\alpha_n]^\top\in\mathbb{R}^n$ is the *coordinate vector / coordinate representation* of $\mathbf{x}$.

## A basis is a coordinate system

A basis effectively **defines a coordinate system**. The familiar Cartesian system uses the canonical basis $(\mathbf{e}_1,\ldots,\mathbf{e}_n)$, but any basis works. The **same vector has different coordinates under different bases** ([[mml-ch02-linear-algebra|MML Ch 2]] Figs. 2.8–2.9): e.g. $\mathbf{x}=[2,3]^\top$ in the standard basis is $\tfrac12[-1,5]^\top$ with respect to $(\mathbf{b}_1,\mathbf{b}_2)=([1,-1]^\top,[1,1]^\top)$ (Example 2.20).

This relativity is the entire motivation for [[BasisChange|basis change]] and for [[TransformationMatrix|transformation matrices]] (which act on coordinate vectors: $\hat{\mathbf{y}}=\mathbf{A}_\Phi\hat{\mathbf{x}}$).

## Connections

- [[Basis]] — an ordered basis is what coordinates are relative to.
- [[TransformationMatrix]] — maps coordinate vectors between spaces.
- [[BasisChange]] — relates coordinates under different bases.
- [[mml-ch02-linear-algebra|MML Ch 2]] / [[mml-book]] — §2.7.1 canonical reference.
