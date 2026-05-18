---
title: "Central Limit Theorem"
type: concept
tags: [probability, foundational, statistics]
sources: [d2l-appendix-mathematics]
last_updated: 2026-05-16
---

# Central Limit Theorem (CLT)

For i.i.d. random variables $X_1, X_2, \ldots$ with finite mean $\mu$ and variance $\sigma^2$, the standardized sample mean converges in distribution to a standard Normal as $n\to\infty$:

$$\frac{\bar X_n - \mu}{\sigma/\sqrt{n}} \;\xrightarrow{d}\; \mathcal{N}(0, 1).$$

Equivalently, the *sum* $S_n=X_1+\ldots+X_n$ approaches $\mathcal{N}(n\mu, n\sigma^2)$ for large $n$.

[[d2l-appendix-mathematics]] §distributions states it in pedagogical form: *"the normal distribution is essentially the limit of any sum of a large number of equal small independent contributions."*

## What the CLT does *not* require

- The $X_i$ need *not* be Normal — they only need finite mean and variance.
- The $X_i$ can be discrete, continuous, mixed.
- Convergence is in distribution (CDF pointwise), not pointwise or in $L^1$.

## D2L's binomial illustration

[[d2l-appendix-mathematics]] §distributions demonstrates the CLT operationally: sums of Bernoulli($p$) draws form a Binomial($n, p$) random variable; as $n$ grows the Binomial PMF visibly approaches the Normal density $\mathcal{N}(np, np(1-p))$. This is the textbook *Normal approximation to the Binomial* (de Moivre–Laplace, 1733/1812) — the historical first instance of the CLT.

## Why ML uses Gaussian noise everywhere

- **[[LinearRegression|Linear regression]] noise model** $\epsilon\sim\mathcal{N}(0,\sigma^2)$ — justified by treating noise as the sum of many small independent fluctuations.
- **[[GaussianDistribution|Gaussian distributions]]** in [[BayesianLinearRegression]], [[GaussianProcess|GPs]], [[VariationalAutoencoder|VAEs]], [[Diffusion]] models — the closed-form algebra of Gaussians is justified empirically by the CLT.
- **Initialization**: [[XavierInitialization|Xavier]] / [[HeInitialization|He]] init draw weights from Gaussians because pre-activations are sums of many small terms, hence approximately Gaussian.
- **Confidence intervals**: $\bar X\pm 1.96\,\sigma/\sqrt{n}$ derives directly from the CLT — the 95% CI underlying most A/B-testing and statistical-inference workflows.

## Generalizations

- **Lyapunov / Lindeberg CLTs**: drop the identical-distribution assumption; require a uniform tail-decay condition.
- **Multivariate CLT**: $\bar{\mathbf{X}}_n \xrightarrow{d} \mathcal{N}(\boldsymbol\mu, \boldsymbol\Sigma/n)$ for vector-valued i.i.d. samples.
- **Berry–Esseen theorem**: quantitative finite-$n$ rate of convergence ($\mathcal{O}(1/\sqrt{n})$ in Kolmogorov distance).
- **Stable laws**: when the variance is infinite, the limit is no longer Gaussian — Lévy stable distributions take over (basis of modern heavy-tailed statistics).

## Connections

- [[d2l-appendix-mathematics]] — §distributions canonical reference.
- [[GaussianDistribution]] — the limit distribution.
- [[BernoulliDistribution]] — sums to a Binomial, the textbook CLT illustration.
- [[ConfidenceInterval]] — derived from the CLT under known $\sigma$.
- [[HypothesisTesting]] — most $z$-tests and $t$-tests are justified by the CLT.
- [[XavierInitialization]] / [[HeInitialization]] — NN initialization heuristics motivated by Gaussian-pre-activation arguments.
