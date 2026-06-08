---
title: "Mean"
type: concept
tags: [probability, statistics, foundational]
sources: [mml-ch06-probability-and-distributions, mml-book, prealgebra-2e-ch05-decimals]
last_updated: 2026-06-07
---

# Mean

The **mean** of a [[RandomVariable]] $X$ with states $\mathbf x\in\mathbb{R}^D$ is its [[ExpectedValue|expected value]] under the identity function ([[mml-book]] §6.4.1, Def. 6.4) — the "average" or center of mass of the distribution:

$$\mathbb{E}_X[\mathbf x]=\begin{bmatrix}\mathbb{E}_{X_1}[x_1]\\\vdots\\\mathbb{E}_{X_D}[x_D]\end{bmatrix}\in\mathbb{R}^D,\qquad \mathbb{E}_{X_d}[x_d]=\begin{cases}\int_{\mathcal{X}} x_d\,p(x_d)\,dx_d & \text{continuous}\\ \sum_{x_i\in\mathcal{X}} x_i\,p(x_d=x_i) & \text{discrete}\end{cases}\quad(\text{Eqs. 6.31–6.32}).$$

It is the special case of the [[ExpectedValue|expectation]] with $g=$ identity; computed element-wise for vectors.

## Mean vs median vs mode

The mean is one of *three* notions of "average" ([[mml-book]] §6.4.1, Fig. 6.4):

- **Mean** — the expectation; sensitive to outliers and long tails.
- **[[Median|Median]]** — the "middle" value (cdf $=0.5$); robust to outliers; hard to generalize to $>1$ dimension.
- **[[Mode|Mode]]** — the most frequent value / a peak of the density; can be multimodal.

For a symmetric unimodal distribution the three coincide; for the bimodal mixture in Example 6.4 they differ (the mean can even sit in a low-density valley between modes).

## Empirical mean

Given data, the population mean is estimated by the **[[EmpiricalMean|empirical / sample mean]]** $\bar{\mathbf x}=\frac1N\sum_n\mathbf x_n$ (Def. 6.9, Eq. 6.41).

## Prealgebra view (the "average")

In introductory arithmetic the mean is simply **the average**: add up the values and divide by how many there are,

$$\text{mean}=\frac{\text{sum of the values}}{n}.$$

OpenStax [[Prealgebra]] 2e (Ch 5.5, [[prealgebra-2e-ch05-decimals]]) presents it as one of three everyday "averages," alongside the [[Median|median]] (the middle value of the ordered list — the single middle value when `n` is odd, the average of the two middle values when `n` is even) and the [[Mode|mode]] (the value occurring most often). A reasonableness check: the mean must land **between the smallest and largest** data values. This elementary definition is exactly the [[EmpiricalMean|empirical/sample mean]] above, computed on a small concrete data set (test scores, ages, monthly bills, …).

## ML uses

- The mean vector $\boldsymbol\mu$ is one of the two parameters fully specifying a [[GaussianDistribution]].
- Mean-centering data is the first step in [[PrincipalComponentAnalysis|PCA]] / forming the [[DataCovarianceMatrix]].
- GMM EM recomputes cluster means as responsibility-weighted empirical means.

## Connections

- [[mml-ch06-probability-and-distributions]] — §6.4.1 deep dive.
- [[mml-book]] — §6.4.1 canonical reference.
- [[ExpectedValue]] — the mean is a special case.
- [[Median]] / [[Mode]] — the other two "averages".
- [[Variance]] — spread about the mean.
- [[EmpiricalMean]] — the data estimate.
- [[GaussianDistribution]] — parameterized by its mean.
- [[prealgebra-2e-ch05-decimals]] — elementary "average = sum ÷ n" treatment (Ch 5.5).
