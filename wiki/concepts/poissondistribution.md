---
title: "Poisson Distribution"
type: concept
tags: [probability, distributions, foundational]
sources: [d2l-appendix-mathematics]
last_updated: 2026-05-16
---

# Poisson Distribution

The probability distribution of the **count of rare events** in a fixed interval — derived as the limit of $\text{Binomial}(n, \lambda/n)$ as $n\to\infty$ with $np = \lambda$ held constant ([[d2l-appendix-mathematics]] §distributions). $X \sim \text{Poisson}(\lambda)$ with rate $\lambda > 0$ takes values in $\{0, 1, 2, \ldots\}$.

## PMF and moments

$$P(X = k) = \frac{\lambda^k e^{-\lambda}}{k!}, \qquad k = 0, 1, 2, \ldots$$

- **Mean**: $\mu_X = \lambda$.
- **Variance**: $\sigma_X^2 = \lambda$ — equality of mean and variance is the *Poisson signature*; if observed data has $\sigma^2 \gg \mu$ the model is mis-specified ([[OverDispersion|overdispersion]]).

## Where Poisson appears in ML

- **Count regression**: model word counts, click counts, web-request rates — the [[GLM|generalized linear model]] with log link.
- **[[Word2Vec]] / [[GloVe]] co-occurrence statistics** — early derivations modeled co-occurrence counts as Poisson.
- **Poisson noise / shot noise**: photon counts in low-light imaging, neural spike counts.
- **Anomaly detection**: rare-event count modeling.
- **Stochastic processes**: the Poisson process is the foundation of queueing theory, point processes, and Hawkes self-exciting processes.

## Key properties

- **Memorylessness** of the inter-arrival times: if events arrive according to a Poisson process with rate $\lambda$, inter-arrival times are i.i.d. [[ExponentialDistribution|Exponential]]($\lambda$).
- **Additivity**: independent $X_1\sim\text{Poisson}(\lambda_1)$, $X_2\sim\text{Poisson}(\lambda_2)$ have $X_1 + X_2 \sim \text{Poisson}(\lambda_1 + \lambda_2)$.
- **Normal approximation**: for large $\lambda$, $\text{Poisson}(\lambda)\approx\mathcal{N}(\lambda, \lambda)$ — directly by the [[CentralLimitTheorem|CLT]].

## Connections

- [[d2l-appendix-mathematics]] — §distributions canonical reference.
- [[BernoulliDistribution]] — Poisson is the limit of sums of independent low-probability Bernoullis.
- [[ExponentialDistribution]] — the waiting-time distribution of a Poisson process.
- [[GaussianDistribution]] — large-$\lambda$ approximation.
- [[CentralLimitTheorem]] — Gaussian-limit derivation.
- [[GLM]] — Poisson regression for count outcomes.
