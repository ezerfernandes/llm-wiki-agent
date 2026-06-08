---
title: "Affine Mapping"
type: concept
tags: [linear-algebra, geometry, foundational]
sources: [mml-ch02-linear-algebra, mml-book]
last_updated: 2026-06-04
---

# Affine Mapping

**Definition 2.26** ([[mml-ch02-linear-algebra|MML Ch 2]] §2.8.2): for vector spaces $V,W$, a [[LinearMapping|linear mapping]] $\Phi:V\to W$, and a fixed $\mathbf{a}\in W$, the map

$$\phi:V\to W,\qquad\mathbf{x}\mapsto\mathbf{a}+\Phi(\mathbf{x})$$

is an *affine mapping* from $V$ to $W$. The vector $\mathbf{a}$ is the *translation vector*.

## Properties (MML p. 63)

- Every affine mapping is a **composition** $\phi=\tau\circ\Phi$ of a linear mapping $\Phi$ and a translation $\tau:W\to W$; $\Phi$ and $\tau$ are **uniquely determined**.
- The composition $\phi'\circ\phi$ of affine mappings is affine.
- A **bijective** affine mapping keeps geometric structure invariant — it preserves **dimension** and **parallelism**.

## Why ML cares

The bias term makes most "linear" ML layers affine: a fully-connected layer $\mathbf{x}\mapsto\mathbf{W}\mathbf{x}+\mathbf{b}$ is an affine mapping (linear part $\mathbf{W}$, translation $\mathbf{b}$). As MML notes (§2.8 Remark), ML literature often blurs "linear" and "affine." The augmentation trick — appending a constant 1 to $\mathbf{x}$ — folds the translation into a single matrix so an affine map can be written as one linear map in homogeneous coordinates (cf. MML Example 8.1).

## Connections

- [[AffineSpace]] / [[AffineSubspace]] — the spaces affine maps act between.
- [[LinearMapping]] — the linear part $\Phi$.
- [[TransformationMatrix]] — represents the linear part in coordinates.
- [[mml-ch02-linear-algebra|MML Ch 2]] / [[mml-book]] — §2.8.2 canonical reference.
