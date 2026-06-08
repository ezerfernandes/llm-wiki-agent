---
title: "Probability Mass Function"
type: concept
tags: [probability, distributions, foundational]
sources: [mml-ch06-probability-and-distributions, mml-book, d2l-appendix-mathematics]
last_updated: 2026-06-04
---

# Probability Mass Function (PMF)

For a **discrete** [[RandomVariable]] $X$ with a finite or countable target space $\mathcal{T}$, the **probability mass function** is the point-probability $P(X=x)$ for each $x\in\mathcal{T}$ ([[mml-book]] §6.2, [[mml-ch06-probability-and-distributions|MML Ch 6]]). It is the discrete counterpart of the [[ProbabilityDensityFunction|pdf]].

## Defining properties

1. **Non-negative**: $P(X=x)\ge 0$.
2. **Normalized**: for a finite-state RV, $\sum_{x\in\mathcal{T}} P(X=x)=1$ (Eq. 6.12).

Unlike a density, a pmf value *is* a genuine probability in $[0,1]$.

## Joint, marginal, conditional (discrete)

For two discrete RVs $X,Y$ ([[mml-book]] §6.2.1, Example 6.2), arranging counts $n_{ij}$ in a table with $N$ total events:

- **[[JointProbability|Joint]]**: $P(X=x_i, Y=y_j)=\dfrac{n_{ij}}{N}$ (Eq. 6.9) — the entry of both values jointly, $=P(X=x_i\cap Y=y_j)$.
- **[[Marginalization|Marginal]]**: $P(X=x_i)=\dfrac{c_i}{N}=\dfrac{\sum_j n_{ij}}{N}$ — column sum (Eq. 6.10); analogously $P(Y=y_j)=r_j/N$ (Eq. 6.11).
- **[[ConditionalProbability|Conditional]]**: $P(Y=y_j\mid X=x_i)=\dfrac{n_{ij}}{c_i}$ (Eq. 6.13) — fraction within a row/column.

## Nomenclature (Table 6.1)

| | "Point probability" | "Interval probability" |
|---|---|---|
| **Discrete** | $P(X=x)$ — **pmf** | not applicable |
| **Continuous** | $p(x)$ — [[ProbabilityDensityFunction\|pdf]] | $P(X\le x)$ — [[CumulativeDistributionFunction\|cdf]] |

[[mml-book]] flags an "abuse of notation": the pmf is loosely called the "distribution," and ML literature hides the distinction between sample space $\Omega$, target space $\mathcal{T}$, and the RV $X$ (§6.2.3).

## ML uses

- Models **categorical variables** — discrete features (e.g. degree taken) or labels (e.g. alphabet letters in handwriting recognition) (§6.2.1).
- Bernoulli / Binomial / Multinomial / Categorical are pmfs and members of the [[ExponentialFamily]].
- The softmax output of a classifier is a pmf over labels; [[CrossEntropyLoss]] is its NLL.

## Connections

- [[mml-ch06-probability-and-distributions]] — §6.2 deep dive.
- [[mml-book]] — §6.2 canonical reference.
- [[ProbabilityDensityFunction]] — continuous counterpart.
- [[CumulativeDistributionFunction]] — interval/cumulative version.
- [[RandomVariable]] — the entity a pmf describes.
- [[Marginalization]] / [[SumRule]] — how marginals are recovered.
