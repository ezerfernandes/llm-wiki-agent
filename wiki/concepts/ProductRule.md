---
title: "Product Rule"
type: concept
tags: [probability, foundational]
sources: [mml-ch06-probability-and-distributions, mml-book]
last_updated: 2026-06-04
---

# Product Rule

The **product rule** is the second of the *two* fundamental rules of probability ([[mml-book]] §6.3; the first is the [[SumRule|sum rule]]). It relates a [[JointProbability|joint]] distribution to a [[ConditionalProbability|conditional]] distribution:

$$p(\mathbf x,\mathbf y)=p(\mathbf y\mid\mathbf x)\,p(\mathbf x)\qquad(\text{Eq. 6.22}).$$

It says **every joint distribution of two random variables factorizes** into the marginal of the first and the conditional of the second given the first. Because the ordering is arbitrary, it equivalently gives $p(\mathbf x,\mathbf y)=p(\mathbf x\mid\mathbf y)\,p(\mathbf y)$ ([[mml-book]] p. 185).

## Discrete vs continuous

The product rule holds for [[ProbabilityMassFunction|pmfs]] (discrete) and [[ProbabilityDensityFunction|pdfs]] (continuous) alike ([[mml-book]] §6.3, p. 185).

## Chain rule for probability

Iterating the product rule factorizes any joint over $n$ variables:

$$p(x_1,\dots,x_n)=p(x_1)\prod_{i=2}^n p(x_i\mid x_1,\dots,x_{i-1}),$$

the **chain rule of probability** (distinct from the calculus [[ChainRule]]) — the factorization underlying autoregressive sequence/language models $p(x_t\mid x_{<t})$.

## Derives Bayes' theorem

Equating the two factorizations of the joint gives [[BayesTheorem|Bayes' theorem]] directly (Eqs. 6.24–6.26):

$$p(\mathbf x\mid\mathbf y)\,p(\mathbf y)=p(\mathbf y\mid\mathbf x)\,p(\mathbf x)\iff p(\mathbf x\mid\mathbf y)=\frac{p(\mathbf y\mid\mathbf x)\,p(\mathbf x)}{p(\mathbf y)}.$$

The product rule is also the route to the alternative definition of [[ConditionalIndependence|conditional independence]] (Eqs. 6.55–6.57).

## Connections

- [[mml-ch06-probability-and-distributions]] — §6.3 deep dive.
- [[mml-book]] — §6.3 canonical reference.
- [[SumRule]] — the other fundamental rule.
- [[BayesTheorem]] — derived by equating the two joint factorizations.
- [[ConditionalProbability]] — the conditional factor $p(\mathbf y\mid\mathbf x)$.
- [[JointProbability]] — the object factorized.
- [[StatisticalIndependence]] — the special case $p(\mathbf x,\mathbf y)=p(\mathbf x)p(\mathbf y)$.
