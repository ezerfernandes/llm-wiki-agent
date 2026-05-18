---
title: "Probability Density Function"
type: concept
tags: [probability, foundational]
sources: [d2l-appendix-mathematics]
last_updated: 2026-05-16
---

# Probability Density Function (PDF)

For a continuous random variable $X$, the **density** $p(x)$ encodes the probability that $X$ lies in a small interval around $x$ ([[d2l-appendix-mathematics]] §random-variables):

$$P\!\left(X \in [x, x+\epsilon]\right) \approx \epsilon \cdot p(x).$$

Two defining properties:

1. **Non-negative**: $p(x) \geq 0$ for all $x$.
2. **Normalized**: $\int_{-\infty}^\infty p(x)\,dx = 1$.

For any interval $(a, b]$, $P(X \in (a, b]) = \int_a^b p(x)\,dx$.

## PDF vs PMF vs CDF

| | Discrete | Continuous |
|---|---|---|
| **Probability of a single value** | PMF $p(x) = P(X=x)$ | $0$ (always) — single points have measure zero |
| **Probability mass** | $\sum$ over set | $\int$ over set |
| **Cumulative** | $F(x) = \sum_{x'\leq x} p(x')$ | $F(x) = \int_{-\infty}^x p(t)\,dt$, $F' = p$ |

Density values can exceed 1 — what's bounded is the integral, not the function. A very narrow Gaussian has density values arbitrarily large at the mean.

## Why density not probability

A continuous RV like the position where a dart lands on a board has probability *zero* of taking any exact value — you'd never write $P(X=2.0)$ for a continuous distribution. The density quantifies the *relative* likelihood of nearby values, which is what continuous probability calculations actually need.

[[d2l-appendix-mathematics]] §random-variables derives this from a thought experiment about dart-board accuracy: as you measure to more decimal places, the probability of hitting any specific bucket shrinks by a factor of 10 per digit — so the "probability per unit length" is the right invariant to define.

## Joint and conditional densities

For two RVs $(X, Y)$ with joint density $p(x, y)$:

- **Marginal**: $p(x) = \int p(x, y)\,dy$.
- **Conditional**: $p(y\mid x) = p(x, y) / p(x)$ (when $p(x) > 0$).
- **Independence**: $p(x, y) = p(x)\,p(y)$.

## Change of variables

For a monotonic transformation $Y = g(X)$:

$$p_Y(y) = p_X(g^{-1}(y))\,\left|\frac{d g^{-1}}{d y}\right|.$$

Multivariate: the absolute value of the Jacobian determinant replaces the absolute derivative — the foundation of [[NormalizingFlow|normalizing flows]] and diffusion-model likelihood computation.

## ML uses

- **[[MaximumLikelihoodEstimation|MLE]]**: NLL $= -\sum_n \log p_\theta(x_n)$ — minimizing densities the model assigns to observed data.
- **Density estimation**: [[KernelDensityEstimation|KDE]], [[GaussianMixtureModel|GMM]], [[NormalizingFlow|normalizing flows]], autoregressive density models all parameterize $p(x)$.
- **Generative modeling**: [[Diffusion]] models, [[VariationalAutoencoder|VAEs]], [[GAN|GANs]] all relate to PDFs (directly or implicitly).
- **Sampling**: inverse-CDF, rejection, MCMC, Langevin all leverage PDF structure.

## Connections

- [[d2l-appendix-mathematics]] — §random-variables canonical reference.
- [[CumulativeDistributionFunction]] — the integral of the PDF.
- [[RandomVariable]] — the entity a PDF describes.
- [[GaussianDistribution]] / [[BernoulliDistribution]] / [[PoissonDistribution]] — concrete PDFs / PMFs.
- [[IntegralCalculus]] — the math that makes PDFs computable.
- [[MaximumLikelihoodEstimation]] — minimizes negative log-PDF over data.
- [[NormalizingFlow]] — uses the Jacobian-determinant change-of-variables formula directly.
