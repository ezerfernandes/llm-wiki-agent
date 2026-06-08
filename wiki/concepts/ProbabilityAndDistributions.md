---
title: "Probability and Distributions"
type: concept
tags: [probability, distributions, foundational]
sources: [mml-book, mml-ch06-probability-and-distributions]
last_updated: 2026-06-04
---

# Probability and Distributions

Foundations of probability and uncertainty in ML: [[ProbabilitySpace]], [[RandomVariable]], [[GaussianDistribution]], [[ExponentialFamily]], [[ConjugatePrior]], [[BayesTheorem]]. Covered in [[mml-book]] Ch 6.

## From [[mml-ch06-probability-and-distributions|MML Ch 6]]

This is the umbrella concept for [[mml-book]] Chapter 6 (book pp. 172–224; see the [[mml-ch06-probability-and-distributions|full deep dive]]). The chapter's mind map (Fig. 6.1) makes the dependency structure explicit, centered on **random variable & distribution**:

- **Construction** (§6.1): probability as a generalization of Boolean logic ([[CoxJaynesTheorem]]); the [[ProbabilitySpace]] $(\Omega,\mathcal{A},P)$; the [[RandomVariable]] as a function $X:\Omega\to\mathcal{T}$; Bayesian-vs-frequentist agnosticism.
- **Describing distributions** (§6.2): [[ProbabilityMassFunction|pmf]] (discrete), [[ProbabilityDensityFunction|pdf]] + [[CumulativeDistributionFunction|cdf]] (continuous).
- **The two rules** (§6.3): [[SumRule]] / [[Marginalization]], [[ProductRule]], and [[BayesTheorem]] (prior · likelihood / evidence).
- **Summary statistics & comparison** (§6.4): [[ExpectedValue]], [[Mean]], [[Median]], [[Mode]], [[Variance]], [[Covariance]], [[CovarianceMatrix]], [[Correlation]], [[EmpiricalMean]] / [[DataCovarianceMatrix]], [[StatisticalIndependence]] / [[ConditionalIndependence]], and the [[InnerProduct|inner-product-space view of random variables]].
- **The Gaussian** (§6.5): [[GaussianDistribution]] — marginals/conditionals/products/linear-transforms/sampling.
- **Conjugacy & the exponential family** (§6.6): [[ConjugatePrior]], [[SufficientStatistics]], [[ExponentialFamily]], [[NaturalParameters]].
- **Change of variables** (§6.7): [[ChangeOfVariables]] / inverse transform, the Jacobian determinant.

These foundations feed regression (Ch 9), dimensionality reduction (Ch 10), and density estimation (Ch 11).
