---
title: "probability"
type: concept
tags: [probability, foundational]
sources: [d2l-preliminaries, mml-book, mml-ch06-probability-and-distributions, prealgebra-2e-ch05-decimals]
last_updated: 2026-06-07
---

# probability

The mathematical language for reasoning under uncertainty. Probabilities assign scores in $[0,1]$ to **events** (subsets of a sample space $\mathcal{S}$); the [[ProbabilitySpace]] $(\Omega, \mathcal{A}, P)$ formalizes the construction.

## Two interpretations

[[d2l-preliminaries]] §Probability and Statistics names both explicitly:

- **Frequentist**: probability = long-run relative frequency. Applies only to *repeatable* events (coin tosses, dice rolls). $P(\text{heads}) = 0.5$ means: in the limit of many independent tosses, half come up heads.
- **Bayesian**: probability = degree of belief. Applies also to *non-repeatable* events ("what is the probability that this dam will collapse?"). Admits subjective priors that get updated by evidence via [[BayesTheorem]].

Both interpretations satisfy Kolmogorov's 1933 axioms — both are mathematically the same theory, philosophically different.

## Elementary definition (equally likely outcomes)

Before the measure-theoretic machinery, probability is introduced concretely. For an experiment with **equally likely outcomes**, OpenStax [[Prealgebra]] 2e (Ch 5.5, [[prealgebra-2e-ch05-decimals]]) defines the probability of an event as

$$P(\text{event})=\frac{\text{number of favorable outcomes}}{\text{total number of outcomes}}.$$

This is a [[Fraction|fraction]] that can be reported as a fraction, a [[Decimal|decimal]], or a percent; it always lies in $[0,1]$, where $0$ means *impossible* and $1$ means *certain* — the same range the axioms below enforce. (This counting definition is the classical/Laplacian special case of the general theory, valid only when all outcomes are equally likely.)

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

## From [[mml-ch06-probability-and-distributions|MML Ch 6]]

[[mml-book]] §6.1 (book p. 172) opens with the same two-interpretations framing — "Probability can be thought of as the fraction of times an event occurs [frequentist], or as a degree of belief about an event [Bayesian]" — but adds a third, unifying claim: **probability generalizes logical / Boolean reasoning** (Jaynes 2003), formalized by the [[CoxJaynesTheorem]]. The book is *agnostic* between Bayesian and frequentist (§6.1 Remark, citing Bishop 2006, Efron & Hastie 2016) and uses both.

It cleanly separates **probability vs. statistics** (§6.1.3): probability starts from a model/process and derives outcomes; statistics observes outcomes and infers the process. **ML sits close to statistics** — it constructs a best-fitting model from data — but additionally cares about *generalization error* on future, non-identical instances (Ch 8). The whole edifice reduces to the [[SumRule]] + [[ProductRule]] + [[BayesTheorem]] (§6.3), built on the [[ProbabilitySpace]] $(\Omega,\mathcal{A},P)$ and the [[RandomVariable]] (§6.1.2). See the [[mml-ch06-probability-and-distributions|Ch 6 deep dive]] for the full treatment, including the chapter's repeated admission of "lazy notation" — the pmf, pdf, and cdf are all loosely called the "distribution."

## Connections

- [[mml-ch06-probability-and-distributions]] — Ch 6 deep dive.
- [[d2l-preliminaries]] — §Probability and Statistics canonical exposition.
- [[mml-book]] — Ch 6 canonical reference.
- [[ProbabilitySpace]] / [[RandomVariable]] — formal substrate.
- [[SumRule]] / [[ProductRule]] — the two fundamental rules.
- [[JointProbability]] / [[ConditionalProbability]] / [[StatisticalIndependence]] / [[BayesTheorem]] — derived concepts.
- [[CoxJaynesTheorem]] — justifies the axioms from coherence of belief.
- [[BayesianLinearRegression]] / [[MaximumLikelihoodEstimation]] — ML uses.
- [[ConjunctionFallacy]] / [[BaseRateFallacy]] — characteristic *failures* of intuitive probabilistic reasoning ([[logic-text-v2|Van Cleave]] Ch 3, after [[DanielKahneman|Kahneman]] & [[AmosTversky|Tversky]]); the base-rate fallacy is [[BayesTheorem|Bayes' theorem]] applied informally.
- [[prealgebra-2e-ch05-decimals]] — elementary favorable/total-outcomes definition (Ch 5.5).
