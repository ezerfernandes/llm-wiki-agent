---
title: "Conjugate Prior"
type: concept
tags: [probability, bayesian-inference, foundational]
sources: [mml-book]
last_updated: 2026-05-16
---

# Conjugate Prior

A prior $p(\boldsymbol\theta)$ is **conjugate** to a likelihood $p(\mathcal{D}\mid\boldsymbol\theta)$ if the posterior $p(\boldsymbol\theta\mid\mathcal{D})\propto p(\mathcal{D}\mid\boldsymbol\theta)\,p(\boldsymbol\theta)$ stays in the **same family** as the prior ([[mml-book]] §6.6).

## Classical conjugate pairs

| Likelihood | Conjugate prior | Posterior |
|---|---|---|
| Bernoulli / Binomial | Beta | Beta |
| Multinomial / Categorical | Dirichlet | Dirichlet |
| Poisson | Gamma | Gamma |
| [[GaussianDistribution|Gaussian]] (known $\sigma^2$, unknown $\mu$) | Gaussian | Gaussian |
| Gaussian (known $\mu$, unknown $\sigma^2$) | Inverse-Gamma | Inverse-Gamma |
| Gaussian (both unknown) | Normal-Inverse-Wishart | Normal-Inverse-Wishart |
| Exponential | Gamma | Gamma |

Conjugate pairs *exist* because most useful likelihoods are members of the [[ExponentialFamily]] — and exponential-family likelihoods always have conjugate priors of a matching form.

## Why ML cares

- **Closed-form posterior updates** — no MCMC, no variational approximation. This is what makes [[BayesianLinearRegression]] tractable.
- **Sequential / online learning**: posterior at step $n$ becomes the prior at step $n+1$; conjugacy means the running representation stays compact.
- **Pedagogical scaffold**: conjugate cases give the analytical baseline against which approximate inference (MCMC, VI) is benchmarked.

## When conjugacy fails

For neural-network likelihoods or non-conjugate combinations (e.g., Bernoulli likelihood + Gaussian prior over logits → no closed-form posterior on the original probability), you fall back to **variational inference**, **MCMC**, or **Laplace approximation**.

## Connections

- [[mml-book]] — §6.6 canonical reference.
- [[ExponentialFamily]] — where conjugate priors come from systematically.
- [[GaussianDistribution]] — self-conjugate.
- [[BayesianLinearRegression]] — primary conjugate-prior application in [[mml-book]] Ch 9.
- [[BayesTheorem]] — the update rule conjugacy preserves form for.
