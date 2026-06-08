---
title: "Conditional Probability"
type: concept
tags: [probability, foundational]
sources: [d2l-preliminaries, mml-book, mml-ch06-probability-and-distributions]
last_updated: 2026-06-04
---

# Conditional Probability

Given two random variables $A, B$ with [[JointProbability|joint probability]] $P(A, B)$ and marginal $P(A) > 0$, the **conditional probability** of $B=b$ given $A=a$ is

$$P(B = b \mid A = a) = \frac{P(A = a, B = b)}{P(A = a)}.$$

Intuitively: restrict attention to the subset of the sample space where $A=a$ occurred, then renormalize so probabilities sum to 1 ([[d2l-preliminaries]] §Multiple Random Variables).

## Properties

- **Still a valid probability**: conditional probabilities obey all of Kolmogorov's axioms, *provided every term in a statement conditions on the same event*. So e.g. $P(\mathcal{B}\cup\mathcal{B}' \mid A=a) = P(\mathcal{B}\mid A=a) + P(\mathcal{B}'\mid A=a)$ for disjoint $\mathcal{B}, \mathcal{B}'$.
- **Product rule**: $P(A, B) = P(B \mid A)\,P(A) = P(A \mid B)\,P(B)$ — both decompositions of the joint must match, which gives [[BayesTheorem|Bayes' theorem]].
- **Chain rule for probability** (not the calculus chain rule): $P(X_1, \ldots, X_n) = P(X_1)\,\prod_{i=2}^n P(X_i \mid X_1, \ldots, X_{i-1})$ — the factorization that underlies autoregressive sequence models.
- **Conditional [[StatisticalIndependence|independence]]**: $A \perp B \mid C \iff P(A, B \mid C) = P(A \mid C)\,P(B \mid C)$.

## "Explaining away" and Simpson-style reversals

Two random variables can be *marginally independent* yet *conditionally dependent* (broken bones ⊥ lung cancer in general, but they become negatively correlated when conditioning on hospitalization, because either explains the admission). Conversely two *marginally dependent* variables can be *conditionally independent* given a common cause (shoe size ⊥ reading level given age). [[d2l-preliminaries]] §Multiple Random Variables walks through both directions.

## ML uses

- **Classification** is conditional density estimation: $P(y \mid \mathbf{x})$ ([[Classification]]).
- **Autoregressive language modeling**: $P(x_t \mid x_{<t})$ for $t=1,\ldots,T$.
- **Variational inference**: approximate intractable $P(\mathbf{z} \mid \mathbf{x})$ with a tractable $q_\phi(\mathbf{z} \mid \mathbf{x})$ ([[Autoencoder|VAE]]).
- **Conditional independence assumptions** are how Bayes nets / PGMs become tractable.

## From [[mml-ch06-probability-and-distributions|MML Ch 6]]

[[mml-book]] §6.2.1 (book pp. 179–180) defines the discrete conditional as a cell divided by its row/column total: $p(y_j\mid x_i)=n_{ij}/c_i$ (Eq. 6.13), $p(x_i\mid y_j)=n_{ij}/r_j$ (Eq. 6.14) — "the fraction of a row or column in a particular cell." It is written lazily as $p(y\mid x)$ in ML notation (§6.2.1). The conditional is one leg of the [[ProductRule|product rule]] $p(\mathbf x,\mathbf y)=p(\mathbf y\mid\mathbf x)p(\mathbf x)$ (Eq. 6.22), the foundation of [[BayesTheorem|Bayes' theorem]] and of the **chain rule for probability** $p(x_1,\dots,x_n)=p(x_1)\prod_{i\ge2}p(x_i\mid x_{<i})$.

The chapter develops **[[ConditionalIndependence|conditional independence]]** $X\perp\!\!\!\perp Y\mid Z$ from conditionals (§6.4.5, Def. 6.11): $p(\mathbf x,\mathbf y\mid\mathbf z)=p(\mathbf x\mid\mathbf z)p(\mathbf y\mid\mathbf z)$, equivalently $p(\mathbf x\mid\mathbf y,\mathbf z)=p(\mathbf x\mid\mathbf z)$ (Eq. 6.57). It also stresses (§6.8) that the lazy notation $p(\mathbf y\mid\mathbf x)$ for *continuous* RVs hides genuine measure-theoretic subtlety — a precise statement conditions a test function's expectation on the $\sigma$-algebra of $\mathbf x$.

## Connections

- [[mml-ch06-probability-and-distributions]] — §6.2/§6.4.5 deep dive.
- [[d2l-preliminaries]] — definition + explaining-away exposition.
- [[mml-book]] — §6.2 canonical reference.
- [[JointProbability]] — numerator of the definition.
- [[ProductRule]] — the conditional is one factor.
- [[BayesTheorem]] — inverting the conditioning.
- [[StatisticalIndependence]] — when $P(B\mid A) = P(B)$.
- [[ConditionalIndependence]] — conditioning on a third variable.
- [[RandomVariable]] — the entities being conditioned.
