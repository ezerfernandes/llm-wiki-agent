---
title: "Sufficient Statistics"
type: concept
tags: [probability, statistics, foundational, bayesian-inference]
sources: [mml-ch06-probability-and-distributions, mml-book]
last_updated: 2026-06-04
---

# Sufficient Statistics

A **statistic** is any deterministic function of a [[RandomVariable]] (e.g. the sample [[Mean|mean]] $\hat\mu=\frac1N(x_1+\cdots+x_N)$). **Sufficient statistics** $\boldsymbol\phi(x)$ are statistics that "carry all the information needed to make inference about the population" — i.e. they are *sufficient to represent the distribution* ([[mml-book]] §6.6.2, p. 210). The idea is due to Sir Ronald Fisher.

## Fisher–Neyman factorization theorem

For a family parameterized by $\theta$ with density $p(x\mid\theta)$, $\boldsymbol\phi(x)$ are sufficient for $\theta$ iff the density factors into a $\theta$-free part and a part depending on $\theta$ *only through* $\boldsymbol\phi(x)$ ([[mml-book]] Theorem 6.14, Lehmann & Casella 1998):

$$p(x\mid\theta)=h(x)\,g_\theta(\boldsymbol\phi(x))\qquad(\text{Eq. 6.106}).$$

If $p(x\mid\theta)$ does not depend on $\theta$, then $\boldsymbol\phi$ is trivially sufficient; the interesting case is when $p(x\mid\theta)$ depends on the data only via $\boldsymbol\phi(x)$.

## Finite-dimensional sufficient statistics ⇒ exponential family

A natural question: as we observe more data, do we need *more* parameters? In general yes (studied in non-parametric statistics, Wasserman 2007). The converse question — *which* distributions have **finite-dimensional** sufficient statistics (parameter count bounded regardless of sample size)? — has a striking answer: the **[[ExponentialFamily|exponential family]]** ([[mml-book]] §6.6.2–6.6.3). In the exponential-family form $p(\mathbf x\mid\boldsymbol\theta)=h(\mathbf x)\exp(\langle\boldsymbol\theta,\boldsymbol\phi(\mathbf x)\rangle-A(\boldsymbol\theta))$ (Eq. 6.107), $\boldsymbol\phi(\mathbf x)$ is precisely the vector of sufficient statistics — a particular expression of $g_\theta(\boldsymbol\phi(x))$ from Fisher–Neyman. The Pitman–Darmois–Koopman result (1935–1936) is that exponential families are the *only* families with finite-dimensional sufficient statistics under repeated i.i.d. sampling.

## Examples

- **Gaussian** $\mathcal{N}(\mu,\sigma^2)$: $\boldsymbol\phi(x)=[x, x^2]^\top$ (Example 6.13). The empirical mean and variance are the sufficient statistics — which is why GMM EM update rules depend on the data only through accumulated $\sum x_n$ and $\sum x_n x_n^\top$.
- **Bernoulli**: $\phi(x)=x$ (Example 6.14).

## Why ML cares

- For an i.i.d. sample the log-likelihood depends on the data **only through** $\sum_n\boldsymbol\phi(\mathbf x_n)$ — a fixed-size summary, so you can discard the raw data.
- **MLE of sufficient statistics is optimal** for the population values ([[mml-book]] p. 214), and the log-likelihood is concave (efficient optimization).

## Connections

- [[mml-ch06-probability-and-distributions]] — §6.6.2 deep dive.
- [[mml-book]] — §6.6.2 canonical reference.
- [[ExponentialFamily]] — the family with finite-dimensional sufficient statistics.
- [[NaturalParameters]] — the parameters paired with $\boldsymbol\phi(\mathbf x)$ in the exponential form.
- [[ConjugatePrior]] — conjugate priors live on the sufficient statistics.
- [[EmpiricalMean]] / [[DataCovarianceMatrix]] — the Gaussian's sufficient statistics.
- [[MaximumLikelihoodEstimation]] — estimates sufficient statistics.
