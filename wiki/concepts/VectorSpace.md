---
title: "Vector Space"
type: concept
tags: [linear-algebra, foundational, algebra]
sources: [mml-book, mml-ch02-linear-algebra]
last_updated: 2026-06-04
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

## From [[mml-ch02-linear-algebra|MML Ch 2]]

**Definition 2.9** (§2.4.2): a real vector space $V=(\mathcal{V},+,\cdot)$ is a set $\mathcal{V}$ with an *inner* operation $+:\mathcal{V}\times\mathcal{V}\to\mathcal{V}$ (vector addition) and an *outer* operation $\cdot:\mathbb{R}\times\mathcal{V}\to\mathcal{V}$ (scalar multiplication) such that:

1. $(\mathcal{V},+)$ is an Abelian [[GroupTheory|group]] (zero vector $\mathbf{0}$ is the neutral element);
2. **distributivity**: $\lambda\cdot(\mathbf{x}+\mathbf{y})=\lambda\mathbf{x}+\lambda\mathbf{y}$ and $(\lambda+\psi)\cdot\mathbf{x}=\lambda\mathbf{x}+\psi\mathbf{x}$;
3. **associativity** of the outer operation: $\lambda\cdot(\psi\cdot\mathbf{x})=(\lambda\psi)\cdot\mathbf{x}$;
4. **neutral element** of the outer operation: $1\cdot\mathbf{x}=\mathbf{x}$.

So a vector space is precisely an Abelian group under $+$ that is also closed under scaling by a field (here $\mathbb{R}$) — the mind map (Fig. 2.2) labels this edge "Abelian with +". The inner/outer terminology has nothing to do with inner/outer products.

**No vector–vector multiplication** is defined (Remark, p. 37). Only the *outer product* $\mathbf{a}\mathbf{b}^\top\in\mathbb{R}^{n\times n}$ and the *inner/scalar/dot product* $\mathbf{a}^\top\mathbf{b}\in\mathbb{R}$ exist.

**Examples** (2.11): $\mathbb{R}^n$, $\mathbb{R}^{m\times n}$ (with $\mathbb{R}^{m\times n}\cong\mathbb{R}^{mn}$), and $\mathbb{C}$. By default a vector is a **column**; a *row vector* is its transpose $\mathbf{x}^\top$. The closure question of §2.4 resolves into [[Span|span]] → [[VectorSubspace|subspace]]; internal structure is [[LinearIndependence]] → [[Basis]] → [[Dimension]] → [[Rank]]. See also [[VectorSubspace]] (Def 2.10) for the subspace closure test.

## Connections

- [[mml-book]] / [[mml-ch02-linear-algebra|MML Ch 2]] — §2.4 canonical reference.
- [[GroupTheory]] — the Abelian group under $+$ that a vector space is built on.
- [[VectorSubspace]] / [[Span]] / [[Basis]] / [[Dimension]] — internal structure (MML §2.4–2.6).
- [[vector-spaces]] — algebrica.org page.
- [[groups]], [[fields]] — algebraic structures vector spaces sit on top of.
- [[Basis]], [[LinearIndependence]], [[Rank]] — internal structure.
- [[LinearMapping]] — maps between vector spaces (i.e., what matrices represent).
- [[InnerProduct]] — geometric structure added in MML Ch 3.
