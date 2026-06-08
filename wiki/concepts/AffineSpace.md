---
title: "Affine Space"
type: concept
tags: [linear-algebra, geometry, foundational]
sources: [mml-ch02-linear-algebra, mml-book]
last_updated: 2026-06-04
---

# Affine Space

An *affine space* is a space "offset from the origin" — a [[VectorSubspace|vector subspace]] translated by a fixed support point, so it generally does **not** contain $\mathbf{0}$ and is therefore **not** a vector (sub)space ([[mml-ch02-linear-algebra|MML Ch 2]] §2.8). Affine spaces are where the chapter's pure algebra meets everyday geometry: points, lines, and planes that need not pass through the origin.

The concrete object is the [[AffineSubspace|affine subspace]] $L=\mathbf{x}_0+U$ (Def 2.25), built from a support point $\mathbf{x}_0$ and a *direction space* $U$ (a subspace).

> **ML caveat** (MML Remark, p. 61): "In the machine learning literature, the distinction between linear and affine is sometimes not clear so that we can find references to affine spaces/mappings as linear spaces/mappings." A neural-network "linear layer" $\mathbf{W}\mathbf{x}+\mathbf{b}$ is, strictly, *affine* (the bias is the translation).

## Connections

- [[AffineSubspace]] — the formal definition $L=\mathbf{x}_0+U$.
- [[AffineMapping]] — structure-preserving maps between affine spaces ($\mathbf{x}\mapsto\mathbf{a}+\Phi(\mathbf{x})$).
- [[VectorSubspace]] — the special case with support point $\mathbf{x}_0=\mathbf{0}$.
- [[Hyperplane]] — an $(n-1)$-dimensional affine subspace.
- [[LinearMapping]] — the linear part of an affine map.
- [[mml-ch02-linear-algebra|MML Ch 2]] / [[mml-book]] — §2.8 canonical reference.
