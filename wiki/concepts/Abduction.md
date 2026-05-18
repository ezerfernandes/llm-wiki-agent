---
title: "Abduction"
type: concept
tags: [philosophy, learning-theory, foundational]
sources: [mml-book]
last_updated: 2026-05-16
---

# Abduction

The third mode of inference (alongside induction and deduction): **inference to the best explanation**. [[mml-book]] §8.2 marginal (p. 258, citing the Stanford Encyclopedia of Philosophy / Douven 2017) frames machine-learning model fitting *as abduction* — neither induction (generalizing from instances) nor deduction (drawing logical entailments).

> "A good movie title is 'AI abduction.'" — [[mml-book]] margin, p. 258.

## Why ML is abductive

When a model overfits, ERM has done **induction** — generalized from the data — but failed to pick a *good* explanation. Regularization and priors push the search toward "simpler" or "more typical" explanations. The model-selection step ([[mml-book]] §8.6) — picking among hypothesis classes via held-out validation — is the explicit abduction step: choose the model class that best *explains* the observed regularities, not just the one that fits the training data.

This framing makes the [[NoFreeLunchTheorem]] more intuitive: without committing to *some* inductive bias / explanatory preference, no learner can do better than chance — there's nothing to *abduct toward*.

## Connection to Bayesian inference

The Bayesian posterior $p(\boldsymbol\theta\mid\mathcal{D})\propto p(\mathcal{D}\mid\boldsymbol\theta)\,p(\boldsymbol\theta)$ is a formal model of abduction: the prior $p(\boldsymbol\theta)$ encodes "which explanations are *a priori* plausible"; the likelihood $p(\mathcal{D}\mid\boldsymbol\theta)$ encodes "how well this explanation accounts for the data"; the product picks out the best trade-off. [[BayesianLinearRegression]] and [[MAPEstimation]] are abduction operationalized.

## Connections

- [[mml-book]] — §8.2 marginal canonical reference.
- [[EmpiricalRiskMinimization]] — the induction step.
- [[ModelSelection]] — the abduction step.
- [[NoFreeLunchTheorem]] — why inductive bias is required.
- [[BayesianLinearRegression]] — formal Bayesian-abductive inference.
