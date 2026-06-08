---
title: "Null Space (Kernel)"
type: concept
tags: [linear-algebra, foundational]
sources: [mml-ch02-linear-algebra, mml-book]
last_updated: 2026-06-04
---

# Null Space (Kernel)

> Disambiguation: this is the linear-algebra *kernel / null space* of a mapping. The unrelated OS-privilege "kernel" lives at [[Kernel]]; ML kernel methods at [[KernelTrick]] / [[KernelFunction]].

**Definition 2.23** ([[mml-ch02-linear-algebra|MML Ch 2]] §2.7.3): for a [[LinearMapping|linear mapping]] $\Phi:V\to W$, the *kernel / null space* is

$$\ker(\Phi):=\Phi^{-1}(\mathbf{0}_W)=\{\mathbf{v}\in V\mid\Phi(\mathbf{v})=\mathbf{0}_W\}.$$

It is the set of vectors $V$ maps to the zero vector of $W$. MML uses **"kernel" and "null space" interchangeably**.

## Key facts

- $\Phi(\mathbf{0}_V)=\mathbf{0}_W$ always, so $\mathbf{0}_V\in\ker(\Phi)$ — the kernel is **never empty**.
- $\ker(\Phi)\subseteq V$ is a [[VectorSubspace|subspace]] of the domain.
- $\Phi$ is **injective** (one-to-one) **iff** $\ker(\Phi)=\{\mathbf{0}\}$.

## Null space of a matrix

For $\Phi(\mathbf{x})=\mathbf{A}\mathbf{x}$ ([[mml-ch02-linear-algebra|MML Ch 2]] Remark, Eqs. 2.124): $\ker(\Phi)$ is the **general solution of the homogeneous system** $\mathbf{A}\mathbf{x}=\mathbf{0}$ — the set of all linear combinations of columns of $\mathbf{A}$ that produce $\mathbf{0}\in\mathbb{R}^m$. It is a subspace of $\mathbb{R}^n$ (the "width" $n$). The kernel captures *relationships among columns* — how a column can be written as a combination of others. Its dimension is $n-\operatorname{rk}(\mathbf{A})$.

A basis of the kernel is read off from the [[ReducedRowEchelonForm|reduced row-echelon form]] of $\mathbf{A}$ via the **Minus-1 Trick** (MML §2.3.3), or by expressing non-pivot columns through pivot columns (Example 2.25).

## Connections

- [[Image]] / [[ColumnSpace]] — the complementary subspaces (in the codomain).
- [[RankNullityTheorem]] — $\dim(\ker(\Phi))+\dim(\operatorname{Im}(\Phi))=\dim(V)$.
- [[Rank]] — $\dim(\ker(\Phi))=n-\operatorname{rk}(\mathbf{A})$.
- [[SystemOfLinearEquations]] / [[ReducedRowEchelonForm]] — kernel = homogeneous solution set.
- [[LinearMapping]] / [[VectorSubspace]] — parent concepts.
- [[mml-ch02-linear-algebra|MML Ch 2]] / [[mml-book]] — §2.7.3 canonical reference.
