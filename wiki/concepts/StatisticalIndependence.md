---
title: "Statistical Independence"
type: concept
tags: [probability, foundational]
sources: [d2l-preliminaries, mml-book]
last_updated: 2026-05-16
---

# Statistical Independence

Two random variables $A$ and $B$ are **independent** ($A \perp B$) iff conditioning on one tells us nothing about the other:

$$P(A \mid B) = P(A) \quad\Longleftrightarrow\quad P(A, B) = P(A)\,P(B).$$

The two formulations are equivalent via the product rule. Independence factorizes the [[JointProbability|joint]] into marginals — the cleanest possible probabilistic relationship ([[d2l-preliminaries]] §Multiple Random Variables; [[mml-book]] §6.4.5).

## Conditional independence

$A$ and $B$ are **conditionally independent given $C$** ($A \perp B \mid C$) iff

$$P(A, B \mid C) = P(A \mid C)\,P(B \mid C).$$

Marginal and conditional independence are distinct: each can hold without the other (see "explaining away" on [[ConditionalProbability]]).

## Two characteristic reversals

- **Independent → dependent under conditioning**: when $A$ and $B$ are independent causes of a common effect $C$, observing $C$ couples them. *Broken bones and lung cancer are independent in the general population but become correlated once you condition on hospitalization.*
- **Dependent → independent under conditioning**: when $A$ and $B$ are both effects of a common cause $C$, conditioning on $C$ decouples them. *Shoe size and reading level are correlated among children but become independent once you condition on age.*

## Why it matters

- **i.i.d. assumption**: training examples are typically assumed *independent and identically distributed*, allowing $P(\mathcal{D}\mid\boldsymbol\theta) = \prod_i P(\mathbf{x}_i\mid\boldsymbol\theta)$ and making [[MaximumLikelihoodEstimation|MLE]] tractable.
- **Naive Bayes** assumes features are conditionally independent given the label, factorizing $P(\mathbf{x}\mid y) = \prod_i P(x_i\mid y)$.
- **Bayes nets / [[ProbabilisticGraphicalModel|PGMs]]** encode a sparse pattern of conditional independencies via a DAG, making inference tractable.
- **Causal inference** turns on which conditional independencies a graph implies (d-separation).

## Connections

- [[d2l-preliminaries]] — definition + both reversal examples.
- [[mml-book]] — §6.4.5 canonical reference.
- [[JointProbability]] — factorization criterion.
- [[ConditionalProbability]] — alternate definition; conditional independence.
- [[RandomVariable]] — the entities related.
- [[BayesTheorem]] — independence simplifies its denominator.
