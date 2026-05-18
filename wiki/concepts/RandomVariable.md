---
title: "Random Variable"
type: concept
tags: [probability, foundational]
sources: [mml-book, d2l-preliminaries]
last_updated: 2026-05-16
---

# Random Variable

A function $X:\Omega\to\mathcal{T}$ from the sample space of a [[ProbabilitySpace]] to a **target space** $\mathcal{T}$ (typically $\mathbb{R}$ or $\mathbb{R}^D$). The name is misleading on two counts:

> *"The name 'random variable' is a great source of misunderstanding as it is neither random nor it is a variable. It is a function."* — [[mml-book]] §6.1.2 marginal, p. 175

## Why we need them

Working directly with $\Omega$ is awkward (e.g., $\Omega=\{hh,ht,th,tt\}$). A random variable $X$ = "number of heads" maps $\Omega\to\{0,1,2\}$ — a much more usable space for inference.

The induced **distribution** is $P_X(S) := P(X^{-1}(S))$ for $S\subseteq\mathcal{T}$ — i.e., the probability that the outcome lies in the preimage of $S$ under $X$.

## Discrete vs continuous

- **Discrete RV**: $\mathcal{T}$ is finite or countably infinite. Distribution specified by a [[ProbabilityMassFunction|PMF]] $P(X=x)$ for $x\in\mathcal{T}$.
- **Continuous RV**: $\mathcal{T}=\mathbb{R}$ or $\mathbb{R}^D$. Distribution specified by a [[ProbabilityDensityFunction|PDF]] $p(x)$, with probabilities computed via integration: $P(a\leq X\leq b) = \int_a^b p(x)\,dx$. The [[CumulativeDistributionFunction|CDF]] $F(x) := P(X\leq x)$ also fully specifies a continuous RV.

[[mml-book]] §6.2: "*Some machine learning texts on probabilistic models use lazy notation and jargon, which is confusing. Multiple distinct concepts are all referred to as 'probability distribution.' One trick to help make sense of probability distributions is to check whether we are trying to model something categorical (a discrete random variable) or something continuous.*"

## Vector-valued RVs

A multivariate RV is a vector $\mathbf{X} = (X_1,\dots,X_D)^\top$ of RVs. The *joint distribution* $p(\mathbf{x})$ captures dependencies; marginals are obtained by summing/integrating out coordinates; conditionals via the product rule $p(\mathbf{x}|\mathbf{y}) = p(\mathbf{x},\mathbf{y})/p(\mathbf{y})$.

## Connections

- [[mml-book]] — §6.1.2 canonical reference.
- [[ProbabilitySpace]] — the underlying triple $(\Omega, \mathcal{A}, P)$.
- [[ProbabilityMassFunction]], [[ProbabilityDensityFunction]], [[CumulativeDistributionFunction]] — how to specify the distribution.
- [[GaussianDistribution]] — most-used continuous RV in ML.
- [[BayesTheorem]] — updating rule for conditional distributions.
