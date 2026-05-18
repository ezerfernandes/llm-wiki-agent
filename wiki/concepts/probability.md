---
title: "probability"
type: concept
tags: [probability, foundational]
sources: [d2l-preliminaries, mml-book]
last_updated: 2026-05-16
---

# probability

The mathematical language for reasoning under uncertainty. Probabilities assign scores in $[0,1]$ to **events** (subsets of a sample space $\mathcal{S}$); the [[ProbabilitySpace]] $(\Omega, \mathcal{A}, P)$ formalizes the construction.

## Two interpretations

[[d2l-preliminaries]] §Probability and Statistics names both explicitly:

- **Frequentist**: probability = long-run relative frequency. Applies only to *repeatable* events (coin tosses, dice rolls). $P(\text{heads}) = 0.5$ means: in the limit of many independent tosses, half come up heads.
- **Bayesian**: probability = degree of belief. Applies also to *non-repeatable* events ("what is the probability that this dam will collapse?"). Admits subjective priors that get updated by evidence via [[BayesTheorem]].

Both interpretations satisfy Kolmogorov's 1933 axioms — both are mathematically the same theory, philosophically different.

## Kolmogorov axioms

For events $\mathcal{A}, \mathcal{A}_1, \mathcal{A}_2, \ldots \subseteq \mathcal{S}$:

1. **Non-negativity**: $P(\mathcal{A}) \geq 0$.
2. **Normalization**: $P(\mathcal{S}) = 1$.
3. **Countable additivity**: for pairwise disjoint events, $P(\bigcup_i \mathcal{A}_i) = \sum_i P(\mathcal{A}_i)$.

Consequences: $P(\emptyset) = 0$; $P(\mathcal{A}') = 1 - P(\mathcal{A})$; impossible events have probability 0.

## Statistics vs probabilities

[[d2l-preliminaries]] sharpens a distinction worth memorizing:

- **Probabilities** are *theoretical* quantities — properties of the data-generating process.
- **Statistics** are *empirical* quantities — functions of observed data (sample mean, sample frequency).

An **estimator** is a statistic designed to estimate a probability or parameter; **consistent** estimators converge to the truth as sample size grows. The **law of large numbers** and **central limit theorem** govern this convergence (rate $\sim 1/\sqrt n$ for the CLT).

## Multiple random variables

- **[[JointProbability|Joint]]** $P(A, B)$ — both events happen.
- **Marginal** $P(A) = \sum_b P(A, B=b)$ — sum out unwanted variables.
- **[[ConditionalProbability|Conditional]]** $P(B \mid A) = P(A, B) / P(A)$ — renormalize on $A=a$.
- **[[BayesTheorem|Bayes' theorem]]** $P(A \mid B) = P(B \mid A)\,P(A) / P(B)$ — invert conditioning.
- **[[StatisticalIndependence|Independence]]** $A \perp B \iff P(A, B) = P(A)\,P(B)$.

## Connections

- [[d2l-preliminaries]] — §Probability and Statistics canonical exposition.
- [[mml-book]] — Ch 6 canonical reference.
- [[ProbabilitySpace]] / [[RandomVariable]] — formal substrate.
- [[JointProbability]] / [[ConditionalProbability]] / [[StatisticalIndependence]] / [[BayesTheorem]] — derived concepts.
- [[CoxJaynesTheorem]] — justifies the axioms from coherence of belief.
- [[BayesianLinearRegression]] / [[MaximumLikelihoodEstimation]] — ML uses.
