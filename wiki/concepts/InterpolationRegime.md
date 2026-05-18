---
title: "Interpolation Regime"
type: concept
tags: [theory, generalization, deep-learning]
sources: [d2l-multilayer-perceptrons]
last_updated: 2026-05-16
---

# Interpolation Regime

The training regime in which a model has *zero training error* — it interpolates (perfectly fits) the training data. Modern over-parametrized [[NeuralNetwork|networks]] routinely live here; classical learning theory expected this to be a disaster, but in practice it coexists with strong generalization ([[d2l-multilayer-perceptrons]] §Revisiting Overfitting and Regularization).

## Why it broke classical theory

The classical [[GeneralizationGap|U-shape]] picture says zero training error → memorization → high test error. Empirically, deep networks can fit *arbitrary labels* on millions-of-examples datasets ([[ChiyuanZhang|Zhang]] et al. 2021), yet on real labels they generalize. So:

> "Because all models under consideration achieve zero training error, *the only avenue for further gains is to reduce overfitting*." — [[d2l-multilayer-perceptrons]]

The remaining axis is the **[[GeneralizationGap|generalization gap]]**, not training loss.

## Connection to nonparametric / kernel methods

When networks interpolate, they behave more like *nonparametric* models: [[d2l-multilayer-perceptrons]] cites $k$-nearest-neighbour as the simplest nonparametric interpolator (zero training error, still consistent). [[ArthurJacot|Jacot]] et al. (2018) made this rigorous via the [[NeuralTangentKernel|neural tangent kernel]] — infinite-width MLPs at standard initialization are equivalent to kernel-method interpolators.

## Implicit regularization

Among the infinitely many interpolants, [[StochasticGradientDescent|SGD]] reliably picks low-norm / "simple" ones; [[WeightDecay|weight decay]] and [[EarlyStopping|early stopping]] further bias the implicit selection. The mystery of *why* SGD's preference produces well-generalizing interpolants remains a major open question.

## Connections

- [[d2l-multilayer-perceptrons]] — §Inspiration from Nonparametrics.
- [[DoubleDescent]] — the curve that lives past the interpolation threshold.
- [[Generalization]] / [[GeneralizationGap]] — the diagnostics that matter here.
- [[NeuralTangentKernel]] — kernel-method correspondence for over-parametrized networks.
- [[Overfitting]] — the failure mode classical theory expected here.
- [[StochasticGradientDescent]] — supplies the implicit regularization.
- [[ScalingLaws]] / [[2001.08361-scaling-laws]] — empirical interpolation-regime scaling.
