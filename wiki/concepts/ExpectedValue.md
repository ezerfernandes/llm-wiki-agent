---
title: "Expected Value"
type: concept
tags: [probability, statistics, foundational]
sources: [mml-ch06-probability-and-distributions, mml-book]
last_updated: 2026-06-04
---

# Expected Value (Expectation)

The **expected value** of a function $g:\mathbb{R}\to\mathbb{R}$ of a [[RandomVariable]] $X\sim p(x)$ ([[mml-book]] §6.4.1, Def. 6.3):

$$\mathbb{E}_X[g(x)]=\int_{\mathcal{X}} g(x)\,p(x)\,dx\quad(\text{continuous, Eq. 6.28}),\qquad \mathbb{E}_X[g(x)]=\sum_{x\in\mathcal{X}} g(x)\,p(x)\quad(\text{discrete, Eq. 6.29}),$$

where $\mathcal{X}$ is the target space. The subscript $\mathbb{E}_X$ marks *which* random variable / density we average against (the integral for continuous, the sum for discrete). This is the "law of the unconscious statistician" (Casella & Berger 2002). For a multivariate RV, the expectation is taken element-wise (Eq. 6.30).

> "The concept of the expected value is central to machine learning, and the foundational concepts of probability itself can be derived from the expected value (Whittle, 2000)." — [[mml-book]] §6.4.1, p. 187

## Linearity

The expectation is a **linear operator** ([[mml-book]] Eq. 6.34): for $f(\mathbf x)=ag(\mathbf x)+bh(\mathbf x)$,

$$\mathbb{E}_X[a\,g(\mathbf x)+b\,h(\mathbf x)]=a\,\mathbb{E}_X[g(\mathbf x)]+b\,\mathbb{E}_X[h(\mathbf x)].$$

Linearity is what makes the affine-transformation rules (Eqs. 6.50–6.51), the raw-score [[Variance|variance]] formula, and the Gaussian mixture mean (Thm 6.12) fall out cleanly.

## Special cases

- $g=$ identity ⇒ the **[[Mean|mean]]** $\mathbb{E}_X[x]$ (Def. 6.4).
- $g(x)=(x-\mu)^2$ ⇒ the **[[Variance|variance]]** $\mathbb{V}_X[x]=\mathbb{E}_X[(x-\mu)^2]$ (Eq. 6.43).
- $g(x)=(x-\mathbb{E}[x])(y-\mathbb{E}[y])$ ⇒ the **[[Covariance|covariance]]** (Def. 6.5).
- The evidence in [[BayesTheorem]] is an expectation: $p(\mathbf y)=\mathbb{E}_X[p(\mathbf y\mid\mathbf x)]$ (Eq. 6.27).

The subscript is "often suppressed" when the RV is clear, e.g. $\mathbb{E}[x]$ ([[mml-book]] margin, p. 190).

## ML uses

- **Risk / loss** = expected loss over the data distribution ([[EmpiricalRiskMinimization]]).
- **[[MaximumLikelihoodEstimation|MLE]]** maximizes expected log-likelihood.
- **Importance-weighted Monte Carlo** estimates (e.g. GMM EM updates) are empirical expectations.

## Connections

- [[mml-ch06-probability-and-distributions]] — §6.4.1 deep dive.
- [[mml-book]] — §6.4.1 canonical reference.
- [[Mean]] — the expectation of the identity.
- [[Variance]] / [[Covariance]] — expectations of (squared) deviations.
- [[Median]] / [[Mode]] — alternative notions of "average".
- [[BayesTheorem]] — evidence as an expectation.
