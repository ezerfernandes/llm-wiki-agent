---
title: "Span"
type: concept
tags: [linear-algebra, foundational]
sources: [mml-ch02-linear-algebra, mml-book]
last_updated: 2026-06-04
---

# Span

**Definition 2.13** ([[mml-ch02-linear-algebra|MML Ch 2]] §2.6.1): for a [[VectorSpace|vector space]] $V$ and a set $\mathcal{A}=\{\mathbf{x}_1,\ldots,\mathbf{x}_k\}\subseteq\mathcal{V}$, the *span* of $\mathcal{A}$ is the set of all [[LinearCombination|linear combinations]] of its elements. If every $\mathbf{v}\in V$ can be written as a linear combination of $\mathcal{A}$, then $\mathcal{A}$ is a *generating set* of $V$ and we write

$$V=\operatorname{span}[\mathcal{A}]=\operatorname{span}[\mathbf{x}_1,\ldots,\mathbf{x}_k].$$

The span answers the **closure question** at the heart of the chapter: starting from a few vectors, what is the entire set reachable by adding and scaling them? The answer is always a [[VectorSubspace|subspace]].

## Generating set vs basis

A generating set *spans* the (sub)space but may carry redundancy. The smallest such set — a *minimal* generating set, equivalently a linearly independent one — is a [[Basis|basis]] (Def 2.14). The number of vectors in a basis is the [[Dimension|dimension]].

## Connections

- [[LinearCombination]] — span = set of all linear combinations.
- [[Basis]] — a minimal / linearly independent generating set.
- [[Dimension]] — size of any basis of the span.
- [[VectorSubspace]] — a span is always a subspace; $U=\operatorname{span}[\mathbf{x}_1,\ldots,\mathbf{x}_m]$.
- [[ColumnSpace]] — the image of $\mathbf{x}\mapsto\mathbf{A}\mathbf{x}$ is the span of the columns of $\mathbf{A}$.
- [[mml-ch02-linear-algebra|MML Ch 2]] / [[mml-book]] — §2.6.1 canonical reference.
