---
title: "Empirical Mean"
type: concept
tags: [probability, statistics, foundational]
sources: [mml-ch06-probability-and-distributions, mml-book]
last_updated: 2026-06-04
---

# Empirical Mean (Sample Mean)

The **empirical mean** (a.k.a. **sample mean**) is the arithmetic average of observed data, used as an estimate of the population [[Mean|mean]] $\mathbb{E}_X[\mathbf x]$ ([[mml-book]] §6.4.2, Def. 6.9). For realizations $\mathbf x_1,\dots,\mathbf x_N\in\mathbb{R}^D$:

$$\bar{\mathbf x}:=\frac{1}{N}\sum_{n=1}^N \mathbf x_n\qquad(\text{Eq. 6.41}).$$

## Population vs empirical statistics

The definitions in §6.4.1 (mean, variance, covariance) are **population statistics** — the true statistics of the data-generating process. In ML we learn from *finite* data, so there are two conceptual steps to go from population to empirical statistics ([[mml-book]] p. 191–192): (1) form a statistic that is a function of $N$ identical random variables $X_1,\dots,X_N$; (2) observe the realizations $\mathbf x_1,\dots,\mathbf x_N$ and apply it.

## Empirical covariance

The companion to the empirical mean is the **empirical covariance** matrix ($D\times D$, [[mml-book]] Eq. 6.42):

$$\boldsymbol\Sigma:=\frac{1}{N}\sum_{n=1}^N (\mathbf x_n-\bar{\mathbf x})(\mathbf x_n-\bar{\mathbf x})^\top,$$

which is symmetric and positive semidefinite — see [[CovarianceMatrix]] and [[DataCovarianceMatrix]].

## Biased by default

[[mml-book]] uses the **biased** empirical covariance throughout — dividing by $N$ (the MLE). The **unbiased** ("corrected") estimator divides by $N-1$ (Bessel's correction) (margin, p. 192). The empirical mean itself is unbiased.

## Connections

- [[mml-ch06-probability-and-distributions]] — §6.4.2 deep dive.
- [[mml-book]] — §6.4.2 canonical reference.
- [[Mean]] — the population quantity being estimated.
- [[DataCovarianceMatrix]] — the empirical covariance used in PCA.
- [[CovarianceMatrix]] — the population analogue.
- [[MaximumLikelihoodEstimation]] — empirical statistics as MLEs of sufficient statistics.
- [[SufficientStatistics]] — empirical mean/covariance are sufficient for the Gaussian.
