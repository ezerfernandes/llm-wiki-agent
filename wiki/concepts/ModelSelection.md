---
title: "Model Selection"
type: concept
tags: [learning-theory, methodology, foundational]
sources: [mml-book, d2l-linear-regression]
last_updated: 2026-05-16
---

# Model Selection

The problem of choosing among competing model classes / hyperparameter configurations ([[mml-book]] §8.6).

## What it's *not*

Model selection is **not** parameter estimation. Parameter estimation (MLE / MAP / Bayesian) optimizes parameters *within* a chosen model class. Model selection picks the *class itself* — polynomial degree, network depth, number of GMM components, regularization strength, kernel type, etc.

## The standard recipes

- **Held-out validation set**: fit each candidate on the training set, score on the validation set, pick the best. Then re-fit the winner on training + validation, evaluate on the (untouched) test set.
- **$k$-fold cross-validation** ([[mml-book]] §8.2.4): partition the training data into $k$ folds; train on $k-1$ folds, validate on the held-out fold; average. Reduces variance vs single-split validation.
- **Nested cross-validation** (§8.6.1): outer loop estimates generalization error; inner loop selects hyperparameters. Critical when reporting performance on a small dataset — single-loop CV that's *also* the model-selection criterion overfits to the validation folds.
- **Marginal likelihood / evidence** $p(\mathcal{D})$: the principled Bayesian alternative — integrate over parameters and compare model classes by $p(\mathcal{D}\mid\mathcal{M})$. Used in [[BayesianLinearRegression]] for polynomial-degree selection.
- **Information criteria**: AIC, BIC, MDL — approximations to marginal likelihood that penalize parameter count.

## Why model selection is *abduction*, not induction

[[mml-book]] §8.2 frames the whole learning procedure as [[Abduction|abduction]] — inference to the best explanation. Within a model class, parameter estimation is inductive. *Across* model classes, the choice itself is abductive — the modeler is picking the explanation framework that best accounts for the data while respecting Occam's razor.

## Hyperparameter vs parameter

[[mml-book]] §8.1.4 (p. 258): "*The distinction between parameters and hyperparameters is somewhat arbitrary, and is mostly driven by the distinction between what can be numerically optimized versus what needs to use search techniques.*" The pragmatic test: gradient methods optimize parameters; grid search / random search / Bayesian optimization optimize hyperparameters.

## Connection to Corpus II / V

- **[[madewithml-mlops-tuning]]** is the applied counterpart: [[RayTune]] + [[HyperOpt]] + [[ASHA]] for hyperparameter search, with [[NestedCrossValidation]] mentioned as the right outer protocol.
- **[[2605.08083-autotts]]** can be read as *automated model selection* over a controller-program space — the Explorer searches the space of TTS controllers, validating each on an offline replay environment.

## Connections

- [[mml-book]] — §8.6 canonical reference.
- [[CrossValidation]] — existing wiki concept.
- [[HyperparameterTuning]] — existing wiki concept.
- [[Abduction]] — philosophical framing.
- [[NoFreeLunchTheorem]] — why model selection requires a prior over model classes.
- [[Overfitting]] — what model selection guards against.
- [[BayesianLinearRegression]] — marginal-likelihood route to model selection.
