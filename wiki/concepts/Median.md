---
title: "Median"
type: concept
tags: [probability, statistics, foundational]
sources: [mml-ch06-probability-and-distributions, mml-book, prealgebra-2e-ch05-decimals]
last_updated: 2026-06-07
---

# Median

The **median** is the "middle" value of a [[RandomVariable]]: if you sort the values, 50% are above and 50% below ([[mml-book]] §6.4.1, p. 188). It generalizes to continuous RVs as the value where the [[CumulativeDistributionFunction|cdf]] equals $0.5$. It is one of three notions of "average," alongside the [[Mean|mean]] and [[Mode|mode]].

In introductory arithmetic (OpenStax [[Prealgebra]] 2e Ch 5.5, [[prealgebra-2e-ch05-decimals]]) the median of a finite data set is found concretely: order the values from least to greatest and count them (`n`); if `n` is **odd** the median is the single middle value, and if `n` is **even** it is the [[Mean|mean]] (average) of the two middle values.

## Why the median over the mean

- **Robustness**: for distributions that are asymmetric or have long tails, the median "provides an estimate of a typical value that is closer to human intuition than the mean." It is **more robust to outliers** than the mean ([[mml-book]] p. 188).

## The multivariate difficulty

Generalizing the median to higher dimensions is **non-trivial** ([[mml-book]] p. 188; Hallin et al. 2010, Kong & Mizera 2012): there is no obvious way to "sort" points in $>1$ dimension. Naively concatenating per-dimension medians fails because there is no canonical ordering $<$ on $\mathbb{R}^D$ — e.g. there is more than one way to define $<$ so that $[3,0]^\top < [2,3]^\top$ (Fig. 6.4 / p. 189).

## Connections

- [[mml-ch06-probability-and-distributions]] — §6.4.1 deep dive.
- [[mml-book]] — §6.4.1 canonical reference.
- [[Mean]] / [[Mode]] — the other two "averages".
- [[CumulativeDistributionFunction]] — median is where the cdf is $0.5$.
- [[ExpectedValue]] — by contrast, the mean *is* an expectation.
- [[prealgebra-2e-ch05-decimals]] — elementary middle-value procedure (Ch 5.5).
