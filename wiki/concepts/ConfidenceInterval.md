---
title: "Confidence Interval"
type: concept
tags: [statistics, foundational]
sources: [d2l-appendix-mathematics]
last_updated: 2026-05-16
---

# Confidence Interval

A random interval $[L(X), U(X)]$ computed from a sample that, under repeated sampling, contains the true (fixed) parameter $\theta$ with probability $1-\alpha$ ([[d2l-appendix-mathematics]] §statistics):

$$P\!\big(L(X) \leq \theta \leq U(X)\big) = 1 - \alpha.$$

Standard $1-\alpha$ confidence interval for a Gaussian mean with known variance $\sigma^2$:

$$\bar X \pm z_{1-\alpha/2}\,\frac{\sigma}{\sqrt{n}}, \qquad z_{0.975}\approx 1.96 \text{ for } \alpha=0.05.$$

## The subtle interpretation

[[d2l-appendix-mathematics]] §statistics is emphatic: a 95% CI **does not** mean "the parameter has 95% probability of being in this interval." The parameter $\theta$ is a *fixed* number — it is either in any given computed CI or not. The 95% refers to the **frequentist coverage**: across many repeated experiments, 95% of the resulting *intervals* would contain the true $\theta$.

The Bayesian analogue — the *credible interval* — does have the natural "probability the parameter is in this interval" reading, but requires a prior and a posterior, not just a sample.

## Construction from the CLT

For a sample mean $\bar X$ of i.i.d. observations with unknown mean $\mu$ and (known or estimated) variance $\sigma^2$:

1. **Pivotal quantity**: by the [[CentralLimitTheorem|CLT]], $Z = (\bar X - \mu)/(\sigma/\sqrt n) \xrightarrow{d} \mathcal{N}(0,1)$.
2. **Pivot transformation**: $P(-z_{1-\alpha/2} \leq Z \leq z_{1-\alpha/2}) = 1-\alpha$.
3. **Invert**: $P(\bar X - z_{1-\alpha/2}\sigma/\sqrt n \leq \mu \leq \bar X + z_{1-\alpha/2}\sigma/\sqrt n) = 1-\alpha$.

When $\sigma$ is unknown and estimated by sample SD $s$, $z$ is replaced by the Student's $t_{n-1}$ quantile.

## Duality with hypothesis testing

The $1-\alpha$ confidence interval for $\theta$ is exactly the set of $\theta_0$ values that would **not be rejected** by a two-sided level-$\alpha$ [[HypothesisTesting|hypothesis test]] of $H_0:\theta = \theta_0$. CIs and hypothesis tests are two views of the same calculation.

## ML uses

- **[[ABTesting|A/B test reporting]]**: the standard practice is to report the lift's point estimate **with** a 95% CI — not just the *p*-value — because the CI carries the magnitude information that significance alone hides.
- **Model accuracy comparisons**: bootstrap CIs around test-set accuracy give an honest sense of estimator variance.
- **[[GaussianProcess|GP]] regression**: posterior variance $\sigma^2(x_*)$ provides per-point credible intervals on predictions.
- **[[Bootstrap|Bootstrap CIs]]**: when an analytic CI is unavailable, resample with replacement and take quantiles.

## Cautions

- **Coverage is asymptotic** under the CLT — small $n$ + heavy-tailed data can break coverage badly.
- **Width $\propto 1/\sqrt n$**: halving the CI width requires $4\times$ the data.
- **Misinterpretation is endemic** — even working statisticians confuse "95% CI" with the Bayesian credible-interval reading.

## Connections

- [[d2l-appendix-mathematics]] — §statistics canonical reference.
- [[Statistics]] — parent discipline.
- [[CentralLimitTheorem]] — justifies the construction.
- [[HypothesisTesting]] — dual concept.
- [[Bootstrap]] — non-parametric CI construction.
- [[ABTesting]] — primary ML use.
- [[GaussianDistribution]] — supplies the $z$ quantiles.
