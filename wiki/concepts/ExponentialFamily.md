---
title: "Exponential Family"
type: concept
tags: [probability, distributions, foundational]
sources: [mml-book, d2l-linear-classification]
last_updated: 2026-05-16
---

# Exponential Family

A parametric family of distributions whose density factors as

$$p(\mathbf{x}\mid\boldsymbol\theta) = h(\mathbf{x})\,\exp\!\left(\langle\boldsymbol\eta(\boldsymbol\theta), \mathbf{T}(\mathbf{x})\rangle - A(\boldsymbol\theta)\right)$$

where $\mathbf{T}(\mathbf{x})$ is the **sufficient statistic**, $\boldsymbol\eta(\boldsymbol\theta)$ the natural parameter, $A(\boldsymbol\theta)$ the log-partition function, and $h(\mathbf{x})$ the base measure ([[mml-book]] §6.6).

## Members

[[GaussianDistribution|Gaussian]], Bernoulli, Binomial, Multinomial, Poisson, Exponential, Gamma, Beta, Dirichlet, Wishart — essentially every distribution in standard probabilistic ML.

## Why exponential families are special

- **Sufficient statistics summarize data**: for an i.i.d. sample, the log-likelihood depends on the data *only through* the sum $\sum_n \mathbf{T}(\mathbf{x}_n)$. This is the Fisher-Pitman-Koopman-Darmois result and is why empirical-mean / empirical-variance update rules exist for [[GaussianMixtureModel|GMM]] EM (Ch 11).
- **Conjugate priors always exist** ([[mml-book]] §6.6): for any exponential-family likelihood, there is an exponential-family prior such that the posterior stays in the same family. See [[ConjugatePrior]].
- **MLE = method of moments**: setting $\nabla A(\boldsymbol\theta) = \frac{1}{N}\sum_n\mathbf{T}(\mathbf{x}_n)$ gives the MLE for natural parameters.
- **Maximum entropy**: each exponential family is the *maximum-entropy* distribution consistent with the constraints $\mathbb{E}[\mathbf{T}(\mathbf{X})]=\boldsymbol\mu$.

## Connection to GLMs

[[GeneralizedLinearModels|Generalized linear models]] use an exponential-family conditional likelihood $p(y\mid\mathbf{x})$ with the natural parameter $\boldsymbol\eta = \mathbf{w}^\top\mathbf{x}$. Logistic regression is exponential-family + Bernoulli; Poisson regression is exponential-family + Poisson; linear regression is exponential-family + Gaussian. This is why [[CrossEntropyLoss]] (the NLL of an exponential-family Bernoulli/Categorical) appears uniformly across classification ML.

## Connections

- [[mml-book]] — §6.6 canonical reference.
- [[GaussianDistribution]] — exponential-family prototype.
- [[ConjugatePrior]] — conjugate to every exponential-family likelihood.
- [[MaximumLikelihoodEstimation]] — has a particularly clean form on the family.
- [[GeneralizedLinearModels]] — exponential-family + linear-in-parameters predictor.
- [[CrossEntropyLoss]] — exponential-family NLL.
