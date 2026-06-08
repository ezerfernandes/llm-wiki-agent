---
title: "Occam's Razor"
type: concept
tags: [model-selection, bayesian-inference, philosophy, foundational]
sources: [mml-ch08-when-models-meet-data, mml-book, d2l-gaussian-processes]
last_updated: 2026-06-04
---

# Occam's Razor

The principle that, among models that explain the data reasonably well, the **simplest should be preferred** ([[mml-book]] §8.6.2, p. 285). It is the objective behind [[ModelSelection|model selection]]: "the objective of model selection is to find the simplest model that explains the data reasonably well." Assuming simpler models are less prone to [[Overfitting|overfitting]], this trades off model complexity against data fit.

> "If we treat model selection as a hypothesis testing problem, we are looking for the simplest hypothesis that is consistent with the data." — [[mml-book]] §8.6.2, Remark (Murphy 2012).

## The automatic Occam's razor

One could place a prior favoring simpler models — but **it is unnecessary**. An *"automatic Occam's razor"* is quantitatively embodied in Bayesian probability itself (Smith & Spiegelhalter 1980; Jefferys & Berger 1992; MacKay 1992).

**The intuition** (Fig. 8.14, adapted from MacKay 2003): the evidence $p(\mathcal{D}\,|\,M_i)$ is a *normalized* probability distribution over the space of all datasets $\mathcal{D}$, so it integrates to 1. A simple model $M_1$ predicts a *small* range of datasets sharply; a complex model $M_2$ spreads probability over *more* datasets and so assigns *less* to any single one. If the observed data fall in the region $C$ that both models can explain, the **simpler model $M_1$ is the more probable** (under equal priors) — it concentrated its limited probability mass where the data actually landed.

## Where it lives

- **[[MarginalLikelihood|Marginal likelihood / evidence]]** (§8.6.2): "the marginal likelihood automatically embodies a trade-off between model complexity and data fit (Occam's razor)" — because the parameters are integrated out, the marginal likelihood is *not* prone to overfitting the way the bare likelihood is.
- **[[GaussianProcess|Gaussian-process]] marginal likelihood** ([[d2l-gaussian-processes]]): the $\log\det$ complexity term implements Occam's razor with no held-out validation set at all.

**Subtlety** (§8.6.4): the automatic Occam's razor penalizes **function complexity, not literally the number of parameters** (Rasmussen & Ghahramani 2001) — it even holds for Bayesian nonparametrics (Gaussian processes) with infinitely many parameters. The MLE-side approximations [[AkaikeInformationCriterion|AIC]] and [[BayesianInformationCriterion|BIC]] (Eqs. 8.48–8.49) instead penalize parameter count directly.

## Connections

- [[mml-ch08-when-models-meet-data]] — §8.6.2 canonical reference (Fig. 8.14).
- [[mml-book]] — §8.6.2.
- [[d2l-gaussian-processes]] — the GP marginal-likelihood realization.
- [[MarginalLikelihood]] — where the automatic razor lives.
- [[ModelSelection]] — the procedure Occam's razor guides.
- [[BayesFactor]] — comparison of two models' evidences.
- [[Overfitting]] — what preferring simplicity guards against.
- [[Abduction]] — simplicity as a criterion for the "best explanation".
- [[InferenceToBestExplanation]] — "simplicity" is one of [[logic-text-v2|Van Cleave]]'s seven explanatory virtues (the critical-thinking counterpart of this page's ML treatment).
- [[WilliamOfOckham]] — the medieval logician (1287–1347) the razor is named after.
- [[logic-text-v2]] — names Ockham and uses simplicity to grade explanations (§3.2).
