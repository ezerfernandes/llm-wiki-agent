---
title: "Overfitting"
type: concept
tags: [theory, training]
sources: [madewithml-training, d2l-linear-regression, d2l-multilayer-perceptrons]
last_updated: 2026-05-16
---

# Overfitting

When a model fits training noise rather than signal, harming generalization. Symptoms: training error low (often near zero) but validation error significantly higher — a large [[GeneralizationGap]]. The diagnostic mirror image of [[Underfitting]].

[[d2l-linear-regression]] §3.6 frames the canonical demo: a polynomial of degree $d \geq n$ achieves zero training error on *any* $n$-example dataset, including pure noise. Memorization, not learning.

## Modern caveat from [[d2l-linear-regression]]

"Note that overfitting is not always a bad thing. In deep learning especially, the best predictive models often perform far better on training data than on holdout data. Ultimately, we usually care about driving the generalization error lower, and only care about the gap insofar as it becomes an obstacle to that end." This foreshadows the **double-descent** phenomenon in overparameterized regimes (LLMs, modern DNNs).

## Deep-learning regime ([[d2l-multilayer-perceptrons]])

Modern over-parametrized networks can perfectly fit **arbitrary labels** (including random ones), yet they still generalize on real data. The classical "complexity → overfitting" mental model breaks down: increasing capacity (depth, width, training epochs) can actually *reduce* test error past the interpolation threshold — the [[DoubleDescent|double-descent]] curve in the [[InterpolationRegime|interpolation regime]]. [[Dropout]], [[EarlyStopping|early stopping]], and [[WeightDecay|weight decay]] are still useful, but the theoretical rationale shifts from "constraining capacity" to "encoding compatible inductive biases."

## Mitigations

- **More data** — most reliable; reduces overfitting risk monotonically.
- **[[Regularization]]** — [[WeightDecay|$\ell_2$ weight decay]], [[Lasso|$\ell_1$]], [[Dropout]], early stopping.
- **Reduce capacity** — fewer parameters, smaller polynomial degree, smaller network.
- **Proper [[TrainValTestSplit]]** + [[ModelSelection]] on validation, not test.

## Connections

- [[d2l-linear-regression]] — §3.6 canonical reference; polynomial-fitting demo.
- [[d2l-multilayer-perceptrons]] — modern deep-learning regime.
- [[DoubleDescent]] / [[InterpolationRegime]] — over-parametrized phenomena.
- [[Dropout]] / [[EarlyStopping]] — deep-learning regularizers.
- [[Underfitting]] — symmetric failure mode.
- [[GeneralizationGap]] — the gap-vs-validation diagnostic.
- [[Regularization]] / [[WeightDecay]] — primary mitigations.
- [[CrossValidation]] — what model selection should use.
