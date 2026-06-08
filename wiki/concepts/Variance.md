---
title: "Variance"
type: concept
tags: [probability, statistics, foundational]
sources: [mml-ch06-probability-and-distributions, mml-book]
last_updated: 2026-06-04
---

# Variance

The **variance** measures the *spread* of a [[RandomVariable]] about its [[Mean|mean]] $\mu=\mathbb{E}_X[x]$ ([[mml-book]] §6.4.1/§6.4.3, Def. 6.7). It is the [[ExpectedValue|expectation]] of the squared deviation:

$$\mathbb{V}_X[x]:=\mathbb{E}_X[(x-\mu)^2]\qquad(\text{Eq. 6.43}).$$

Equivalently, the variance is the [[Covariance|covariance]] of a variable with itself, $\mathbb{V}_X[\mathbf x]=\mathrm{Cov}_X[\mathbf x,\mathbf x]$, and for a multivariate RV its matrix form is the **[[CovarianceMatrix|covariance matrix]]**:

$$\mathbb{V}_X[\mathbf x]=\mathbb{E}_X[(\mathbf x-\boldsymbol\mu)(\mathbf x-\boldsymbol\mu)^\top]=\mathbb{E}_X[\mathbf x\mathbf x^\top]-\mathbb{E}_X[\mathbf x]\,\mathbb{E}_X[\mathbf x]^\top\qquad(\text{Eq. 6.38}).$$

The square root $\sigma(x)=\sqrt{\mathbb{V}_X[x]}$ is the **standard deviation**.

## Three expressions for the variance (§6.4.3)

[[mml-book]] derives three equivalent forms — a notable exam-favourite:

1. **Standard definition** (Eq. 6.43): $\mathbb{V}_X[x]=\mathbb{E}_X[(x-\mu)^2]$. Needs a **two-pass** algorithm empirically (compute $\mu$, then squared deviations).
2. **Raw-score formula** (Eq. 6.44): $\mathbb{V}_X[x]=\mathbb{E}_X[x^2]-(\mathbb{E}_X[x])^2$ — "the **mean of the square minus the square of the mean**." Computable in **one pass** (accumulate $x_i$ and $x_i^2$ together), but **numerically unstable** when the two terms are large and nearly equal (catastrophic cancellation). Used to derive the [[BiasVarianceDecomposition|bias–variance decomposition]].
3. **Sum of pairwise differences** (Eq. 6.45): $\frac{1}{N^2}\sum_{i,j}(x_i-x_j)^2 = 2\big[\frac1N\sum_i x_i^2-(\frac1N\sum_i x_i)^2\big]$ = twice the raw-score expression. Geometrically: the sum of $N^2$ pairwise distances equals (twice) the sum of $N$ distances from the center.

## Sums and transformations

- $\mathbb{V}[\mathbf x\pm\mathbf y]=\mathbb{V}[\mathbf x]+\mathbb{V}[\mathbf y]\pm\mathrm{Cov}[\mathbf x,\mathbf y]\pm\mathrm{Cov}[\mathbf y,\mathbf x]$ (Eqs. 6.48–6.49).
- For **uncorrelated** $X,Y$: $\mathbb{V}[\mathbf x+\mathbf y]=\mathbb{V}[\mathbf x]+\mathbb{V}[\mathbf y]$ (Eq. 6.58) — the **Pythagorean theorem** in the [[InnerProduct|inner-product space of random variables]] (§6.4.6), with $\sigma$ as side lengths.
- Affine: $\mathbb{V}_Y[\mathbf A\mathbf x+\mathbf b]=\mathbf A\,\mathbb{V}_X[\mathbf x]\,\mathbf A^\top=\mathbf A\boldsymbol\Sigma\mathbf A^\top$ (Eq. 6.51).
- **Law of total variance** (Eq. 6.85c): $\mathbb{V}_X[x]=\mathbb{E}_Y[\mathbb{V}_X[x\mid y]]+\mathbb{V}_Y[\mathbb{E}_X[x\mid y]]$ — total variance = expected conditional variance + variance of the conditional mean (appears in the Gaussian-mixture variance, Thm 6.12).

## Connections

- [[mml-ch06-probability-and-distributions]] — §6.4.1/§6.4.3 deep dive.
- [[mml-book]] — §6.4 canonical reference.
- [[ExpectedValue]] — variance is an expectation of squared deviation.
- [[Covariance]] / [[CovarianceMatrix]] — variance is self-covariance.
- [[Correlation]] — normalized covariance.
- [[BiasVarianceDecomposition]] — uses the raw-score form.
- [[StatisticalIndependence]] — variances add for uncorrelated RVs.
