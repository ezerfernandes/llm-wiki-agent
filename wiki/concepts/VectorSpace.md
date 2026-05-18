---
title: "Vector Space"
type: concept
tags: [linear-algebra, foundational, algebra]
sources: [mml-book]
last_updated: 2026-05-16
---

# Vector Space

A set $V$ equipped with two operations — vector addition $+:V\times V\to V$ and scalar multiplication $\cdot:\mathbb{R}\times V\to V$ — that satisfies eight axioms (commutativity / associativity of addition, distributivity, etc.). Equivalently: a set with [[GroupTheory|abelian group]] structure under $+$, closed under scaling by elements of a field ([[mml-book]] §2.4).

## What can be a vector

[[mml-book]] §2 opens with the deliberately surprising claim that vectors are not just arrows:

| Vector type | Why it qualifies |
|---|---|
| Geometric vectors $\vec{x}\in\mathbb{R}^2,\mathbb{R}^3$ | Standard arrow-with-direction picture |
| Polynomials | Add polynomials, scale by $\lambda\in\mathbb{R}$ → still a polynomial |
| Audio signals | Pointwise addition + scaling of waveforms |
| Tuples in $\mathbb{R}^n$ | The standard ML representation |
| Functions $f:\mathbb{R}\to\mathbb{R}$ | $L^2$ inner-product spaces in kernel methods |

The pedagogical point: ML's *data-as-vectors* assumption is not a restriction to arrows — it's a commitment to additive + scalable structure.

## Why ML lives in $\mathbb{R}^n$

[[mml-book]] §2 marginal note (p. 18): "We will largely focus on vectors in $\mathbb{R}^n$ since most algorithms in linear algebra are formulated in $\mathbb{R}^n$." For finite-dimensional vector spaces, there is a 1:1 correspondence (an isomorphism) between any vector space and $\mathbb{R}^n$ via choice of [[Basis]] — so working in $\mathbb{R}^n$ loses no generality.

## The closure question

A central organizing question: *given a small set of vectors, what is the entire set of vectors reachable by adding and scaling them?* The answer is the **span**; if it equals the original set, that's a [[VectorSubspace|subspace]]. [[mml-book]] §2.4: "The concept of a vector space and its properties underlie much of machine learning."

## Connections

- [[mml-book]] — §2.4 canonical reference.
- [[vector-spaces]] — algebrica.org page.
- [[groups]], [[fields]] — algebraic structures vector spaces sit on top of.
- [[Basis]], [[LinearIndependence]], [[Rank]] — internal structure.
- [[LinearMapping]] — maps between vector spaces (i.e., what matrices represent).
- [[InnerProduct]] — geometric structure added in MML Ch 3.
