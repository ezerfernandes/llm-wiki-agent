---
title: "Expected Risk"
type: concept
tags: [learning-theory, foundational]
sources: [mml-ch08-when-models-meet-data, mml-book]
last_updated: 2026-06-04
---

# Expected Risk (True Risk / Population Risk)

The **expected [[LossFunction|loss]] over the entire (infinite) data-generating distribution** for a predictor $f$ with parameters fixed ([[mml-book]] §8.2.2, Eq. 8.10):

$$\mathbf{R}_{\text{true}}(f)=\mathbb{E}_{\mathbf{x},y}\big[\ell(y,f(\mathbf{x}))\big].$$

"This is the true risk if we had access to an infinite amount of data. The expectation is over the (infinite) set of all possible data and labels." It is the quantity machine learning actually wants to minimize — performing well on **unseen** data.

## Names

§8.2.2 (margin, p. 261) notes **population risk** as an alternative phrase. The [[Generalization]] page (from [[d2l-linear-regression|D2L]]) calls the same quantity the **generalization error** $R=\mathbb{E}_{(X,Y)\sim P}[\ell(X,Y,f(X))]$.

## Why we can never compute it

We never see the distribution $p(\mathbf{x},y)$ exactly, so $\mathbf{R}_{\text{true}}$ is unknowable in general. The two practical questions of §8.2 follow directly:

1. **How to train so as to generalize well?** → [[Regularization|regularization]] (§8.2.3), priors (§8.3.2).
2. **How to *estimate* $\mathbf{R}_{\text{true}}$ from finite data?** → the held-out test set and [[CrossValidation|cross-validation]] (§8.2.4).

The [[EmpiricalRisk|empirical risk]] $\mathbf{R}_{\text{emp}}$ is the finite-sample estimator; the training empirical risk is a *biased* (optimistic) estimate, the test empirical risk an (approximately) unbiased one.

## ERM is not "probability free"

§8.2.5 (p. 265): although [[EmpiricalRiskMinimization|ERM]] never specifies $p(\mathbf{x},y)$, the expected risk is defined as an expectation *under* that unknown joint. Since it is a joint over $\mathbf{x}$ and $y$, labels can be non-deterministic, and — unlike standard statistics — ERM need not specify the noise distribution for $y$.

## Connections

- [[mml-ch08-when-models-meet-data]] — §8.2.2 canonical reference (Eq. 8.10).
- [[mml-book]] — §8.2.2 / §8.2.5.
- [[EmpiricalRisk]] — the finite-sample estimator of this.
- [[Generalization]] — the same quantity under D2L's "generalization error" name.
- [[GeneralizationGap]] — $\mathbf{R}_{\text{true}}-\mathbf{R}_{\text{emp}}$.
- [[CrossValidation]] — how it is estimated in practice.
- [[Overfitting]] — when empirical risk under-estimates expected risk.
