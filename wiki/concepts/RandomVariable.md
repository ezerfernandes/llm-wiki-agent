---
title: "Random Variable"
type: concept
tags: [probability, foundational]
sources: [mml-book, d2l-preliminaries, mml-ch06-probability-and-distributions]
last_updated: 2026-06-04
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

## From [[mml-ch06-probability-and-distributions|MML Ch 6]]

[[mml-book]] §6.1.2 (book pp. 174–177) is explicit that a random variable is a **function** $X:\Omega\to\mathcal{T}$ from the sample space to a **target space** $\mathcal{T}$ (whose elements it calls *states*). For finite $\Omega$ and $\mathcal{T}$ it is "essentially a lookup table." The induced **law / distribution** is

$$P_X(S)=P(X\in S)=P(X^{-1}(S))=P(\{\omega\in\Omega : X(\omega)\in S\})\qquad(\text{Eq. 6.8}),$$

i.e. $P_X=P\circ X^{-1}$ — the probability of an event in $\mathcal{T}$ equals the probability of its pre-image in $\Omega$.

**Worked example (Example 6.1, p. 176).** Draw two coins from a bag with replacement ($\$$ with probability $0.3$); let $X$ = number of $\$$ drawn, so $\mathcal{T}=\{0,1,2\}$. Then $X((\$,\$))=2$, etc. (Eqs. 6.1–6.4), and the [[ProbabilityMassFunction|pmf]] is $P(X{=}2)=0.09$, $P(X{=}1)=0.42$, $P(X{=}0)=0.49$ (Eqs. 6.5–6.7). The calculation equates "probability of the output of $X$" with "probability of samples in $\Omega$."

When $\mathcal{T}$ is finite or countable, $X$ is a **discrete** RV; when $\mathcal{T}=\mathbb{R}$ or $\mathbb{R}^D$, it is **continuous** (§6.1.2 Remark). MML uses the symbol $X$ for both univariate and multivariate RVs, denoting states $x$ (scalar) and $\mathbf x$ (vector) (§6.2 / §6.2.3).

> "The name 'random variable' is a great source of misunderstanding as it is neither random nor it is a variable. It is a function." — [[mml-book]] §6.1.2 marginal, p. 175

## Connections

- [[mml-ch06-probability-and-distributions]] — §6.1.2 deep dive.
- [[mml-book]] — §6.1.2 canonical reference.
- [[ProbabilitySpace]] — the underlying triple $(\Omega, \mathcal{A}, P)$.
- [[ProbabilityMassFunction]], [[ProbabilityDensityFunction]], [[CumulativeDistributionFunction]] — how to specify the distribution.
- [[GaussianDistribution]] — most-used continuous RV in ML.
- [[BayesTheorem]] — updating rule for conditional distributions.
- [[InnerProduct]] — random variables as vectors in an inner-product space (§6.4.6).
