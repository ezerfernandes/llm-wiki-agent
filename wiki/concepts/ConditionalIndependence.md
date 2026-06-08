---
title: "Conditional Independence"
type: concept
tags: [probability, foundational]
sources: [mml-ch06-probability-and-distributions, mml-book, mml-ch08-when-models-meet-data, d2l-preliminaries]
last_updated: 2026-06-04
---

# Conditional Independence

Two random variables $X$ and $Y$ are **conditionally independent given $Z$**, written $X\perp\!\!\!\perp Y\mid Z$, iff their joint conditional factorizes for *every* state of $Z$ ([[mml-book]] §6.4.5, Def. 6.11):

$$p(\mathbf x,\mathbf y\mid\mathbf z)=p(\mathbf x\mid\mathbf z)\,p(\mathbf y\mid\mathbf z)\quad\text{for all } \mathbf z\in\mathcal{Z}\qquad(\text{Eq. 6.55}).$$

The interpretation: "given knowledge about $\mathbf z$, the distribution of $\mathbf x$ and $\mathbf y$ factorizes."

## Equivalent formulation

Using the [[ProductRule|product rule]] to expand the left side as $p(\mathbf x\mid\mathbf y,\mathbf z)\,p(\mathbf y\mid\mathbf z)$ and comparing (Eqs. 6.56–6.57) gives the alternative definition:

$$p(\mathbf x\mid\mathbf y,\mathbf z)=p(\mathbf x\mid\mathbf z)\qquad(\text{Eq. 6.57}),$$

i.e. "given that we know $\mathbf z$, knowledge about $\mathbf y$ does not change our knowledge of $\mathbf x$."

## Relation to plain independence

Plain [[StatisticalIndependence|statistical independence]] is the special case of conditioning on nothing: $X\perp\!\!\!\perp Y\mid\emptyset$ ([[mml-book]] p. 195). Marginal and conditional independence are **distinct** — each can hold without the other ("explaining away": independent causes of a common effect become dependent once the effect is observed; common-cause effects become independent once the cause is conditioned on).

## Why it matters in ML

- **Naive Bayes** assumes features are conditionally independent given the label: $p(\mathbf x\mid y)=\prod_i p(x_i\mid y)$.
- **Bayes nets / [[ProbabilisticGraphicalModel|PGMs]]** encode a sparse pattern of conditional independencies via a DAG (d-separation), making inference tractable.
- **Causal inference** turns on which conditional independencies a graph implies.

## From [[mml-ch08-when-models-meet-data|MML Ch 8]]

[[mml-ch08-when-models-meet-data|MML Ch 8]] §8.5 makes conditional independence *readable from a graph*. A [[DirectedGraphicalModel|directed graphical model]] encodes a factorization $p(\mathbf{x})=\prod_k p(x_k\,|\,\mathrm{Pa}_k)$ (Eq. 8.31), and **[[DSeparation|d-separation]]** (§8.5.2, Pearl 1988) decides whether $\mathcal{A}\perp\!\!\!\perp\mathcal{B}\,|\,\mathcal{C}$ (Eq. 8.34) holds purely from the topology: examine all trails from $\mathcal{A}$ to $\mathcal{B}$; a trail is blocked at a head-to-tail/tail-to-tail node in $\mathcal{C}$, **or** at a head-to-head node whose node-and-descendants avoid $\mathcal{C}$; all trails blocked ⇒ d-separated ⇒ conditionally independent. The Example 8.9 results — $b\perp\!\!\!\perp d\,|\,a,c$ but $b\not\perp\!\!\!\perp d\,|\,c$ — show the **"explaining away"** subtlety: conditioning on the descendant of a collider *un*-blocks a path, creating dependence.

## Connections

- [[mml-ch08-when-models-meet-data]] — §8.5.2 d-separation: reading conditional independence off a DAG.

- [[mml-ch06-probability-and-distributions]] — §6.4.5 deep dive.
- [[mml-book]] — §6.4.5 canonical reference.
- [[StatisticalIndependence]] — the unconditional special case.
- [[ProductRule]] — used to derive the equivalent formulation.
- [[ConditionalProbability]] — the conditionals being factorized.
- [[ProbabilisticGraphicalModel]] — encodes conditional independencies.
