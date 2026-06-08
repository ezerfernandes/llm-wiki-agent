---
title: "IID (Independent and Identically Distributed)"
type: concept
tags: [probability, statistics, assumptions, estimation]
sources: [mml-ch06-probability-and-distributions, mml-ch08-when-models-meet-data]
last_updated: 2026-06-04
---

# IID (Independent and Identically Distributed)

Data points $\mathbf{x}_1,\dots,\mathbf{x}_N$ are **independent and identically distributed** when (i) each is drawn from the *same* distribution $p$ (*identically distributed*), and (ii) the draws do not influence one another (*[[StatisticalIndependence|independent]]*). The i.i.d. assumption is the workhorse premise behind nearly all supervised learning: it is what justifies treating a finite training set as a representative sample of an underlying data-generating distribution, and what lets the joint probability of a dataset factorize into a product.

$$p(\mathbf{x}_1,\dots,\mathbf{x}_N)\overset{\text{iid}}{=}\prod_{n=1}^{N}p(\mathbf{x}_n).$$

## Why it matters

This factorization is what makes [[Likelihood|likelihoods]] tractable: the [[NegativeLogLikelihood|negative log-likelihood]] of the whole dataset becomes a *sum* of per-example terms, enabling [[StochasticGradientDescent|stochastic gradient descent]] over mini-batches (an unbiased estimate of the full-data gradient). Without the i.i.d. assumption the loss would not decompose additively over examples and mini-batch optimization would be biased.

## From [[mml-ch06-probability-and-distributions|MML Ch 6]]

[[mml-ch06-probability-and-distributions|MML Ch 6]] §6.4.4 develops [[StatisticalIndependence|statistical independence]] and [[ConditionalIndependence|conditional independence]] — the "independent" half of i.i.d. — and §6.4.3 defines the empirical mean/covariance estimators whose unbiasedness relies on identically-distributed samples.

## From [[mml-ch08-when-models-meet-data|MML Ch 8]]

[[mml-ch08-when-models-meet-data|MML Ch 8]] makes the i.i.d. assumption explicit as the foundation of [[EmpiricalRiskMinimization|empirical risk minimization]] (§8.2) and [[MaximumLikelihoodEstimation|maximum likelihood estimation]] (§8.3.1): *"we assume the examples are independent and identically distributed,"* which is precisely what allows the likelihood to factorize, $p(\mathcal{Y}\mid\mathcal{X},\boldsymbol\theta)=\prod_n p(y_n\mid\mathbf{x}_n,\boldsymbol\theta)$, and the [[ExpectedRisk|expected risk]] (generalization error) to be estimated by the average [[EmpiricalRisk|empirical risk]] over the training sample. The chapter also flags the limits of the assumption — distribution shift between train and test breaks the guarantee.

## Connections

- [[StatisticalIndependence]] — the "independent" component.
- [[Likelihood]] / [[NegativeLogLikelihood]] — factorize under i.i.d.
- [[EmpiricalRiskMinimization]] — i.i.d. links empirical risk to [[ExpectedRisk|expected risk]].
- [[MaximumLikelihoodEstimation]] — the factorized likelihood it estimates.
- [[StochasticGradientDescent]] — unbiased mini-batch gradients require i.i.d. sampling.
- [[Generalization]] — i.i.d. is the bridge from training performance to test performance.
