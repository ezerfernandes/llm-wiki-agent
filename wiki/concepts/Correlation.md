---
title: "Correlation"
type: concept
tags: [probability, statistics, foundational]
sources: [mml-ch06-probability-and-distributions, mml-book]
last_updated: 2026-06-04
---

# Correlation

The **correlation** between two random variables $X, Y$ is the **normalized [[Covariance|covariance]]** ([[mml-book]] §6.4.1, Def. 6.8):

$$\mathrm{corr}[x,y]=\frac{\mathrm{Cov}[x,y]}{\sqrt{\mathbb{V}[x]\,\mathbb{V}[y]}}\in[-1,1]\qquad(\text{Eq. 6.40}).$$

Dividing the covariance by the product of the standard deviations removes the effect of each variable's own [[Variance|variance]], so correlations from different variable pairs are comparable on the same $[-1,1]$ scale.

- **Positive** correlation: when $x$ grows, $y$ tends to grow.
- **Negative** correlation: when $x$ grows, $y$ tends to shrink.

Fig. 6.5 in [[mml-book]] shows two datasets with **identical means and per-axis variances** but opposite-sign covariance/correlation.

## Correlation matrix

The **correlation matrix** is the [[CovarianceMatrix|covariance matrix]] of the *standardized* random variables $x/\sigma(x)$ — each variable divided by its standard deviation ([[mml-book]] p. 191).

## Correlation = cosine of the angle between random variables

In the [[InnerProduct|inner-product space of random variables]] (§6.4.6), with $\langle X,Y\rangle=\mathrm{Cov}[x,y]$ and length $\|X\|=\sigma[x]$, the angle $\theta$ between $X$ and $Y$ satisfies

$$\cos\theta=\frac{\langle X,Y\rangle}{\|X\|\,\|Y\|}=\frac{\mathrm{Cov}[x,y]}{\sqrt{\mathbb{V}[x]\mathbb{V}[y]}}=\mathrm{corr}[x,y]\qquad(\text{Eq. 6.61}).$$

So **correlation is the cosine of the angle** between two random variables, and $X\perp Y$ (orthogonal / uncorrelated) iff $\mathrm{Cov}[x,y]=0$. Note: zero correlation means *uncorrelated*, **not** [[StatisticalIndependence|independent]] (covariance captures only linear dependence; Example 6.5).

## Connections

- [[mml-ch06-probability-and-distributions]] — §6.4.1/§6.4.6 deep dive.
- [[mml-book]] — §6.4.1 canonical reference.
- [[Covariance]] — correlation normalizes it.
- [[Variance]] — the normalizer.
- [[CovarianceMatrix]] — correlation matrix = standardized covariance matrix.
- [[InnerProduct]] — correlation as cosine of the angle.
- [[StatisticalIndependence]] — uncorrelated ≠ independent.
