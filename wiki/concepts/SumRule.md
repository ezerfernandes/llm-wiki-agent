---
title: "Sum Rule"
type: concept
tags: [probability, foundational]
sources: [mml-ch06-probability-and-distributions, mml-book]
last_updated: 2026-06-04
---

# Sum Rule

The **sum rule** — also called the **[[Marginalization|marginalization property]]** — is one of the *two* fundamental rules of probability ([[mml-book]] §6.3, the other being the [[ProductRule|product rule]]). It relates a [[JointProbability|joint]] distribution to a **marginal** distribution by summing or integrating out the unwanted variable:

$$p(\mathbf x)=\begin{cases}\displaystyle\sum_{\mathbf y\in\mathcal{Y}} p(\mathbf x,\mathbf y) & \text{if } \mathbf y \text{ is discrete}\\[1.2em] \displaystyle\int_{\mathcal{Y}} p(\mathbf x,\mathbf y)\,d\mathbf y & \text{if } \mathbf y \text{ is continuous}\end{cases}\qquad(\text{Eq. 6.20}).$$

For a vector $\mathbf x=[x_1,\dots,x_D]^\top$, repeated application yields any marginal:

$$p(x_i)=\int p(x_1,\dots,x_D)\,d\mathbf x_{\setminus i}\qquad(\text{Eq. 6.21}),$$

where $\setminus i$ reads "all variables except $i$."

## Why it's fundamental and why it's hard

The sum rule + [[ProductRule|product rule]] "arise naturally" from the [[CoxJaynesTheorem|Cox–Jaynes]] desiderata (Jaynes 2003, ch. 2; margin, p. 184) — all of probability reduces to these two rules plus [[BayesTheorem|Bayes' theorem]] (which is itself derived from them).

**Marginalization is the central computational bottleneck of probabilistic modeling** ([[mml-book]] §6.3 Remark, p. 184): with many variables, or discrete variables with many states, the sum rule "boils down to performing a high-dimensional sum or integral," and "there is no known polynomial-time algorithm to calculate them exactly." This is what makes the **evidence** $p(\mathbf y)=\int p(\mathbf y\mid\mathbf x)p(\mathbf x)\,d\mathbf x$ in Bayes' theorem (§6.3) hard, and it motivates approximate inference (MCMC, variational inference).

## ML uses

- Computing the **evidence / marginal likelihood** (denominator of [[BayesTheorem]]).
- **Marginalizing out latent variables / nuisance parameters** in [[BayesianLinearRegression]], GMMs, PGMs.
- Marginalizing a [[GaussianDistribution|Gaussian]] is closed-form — just read off the relevant mean/covariance block (§6.5.1), avoiding the intractable integral.

## Connections

- [[mml-ch06-probability-and-distributions]] — §6.3 deep dive.
- [[mml-book]] — §6.3 canonical reference.
- [[ProductRule]] — the other fundamental rule.
- [[Marginalization]] — the property the sum rule expresses.
- [[BayesTheorem]] — derived from the sum + product rules.
- [[JointProbability]] / [[ConditionalProbability]] — the objects related.
- [[CoxJaynesTheorem]] — why these rules are the rules.
