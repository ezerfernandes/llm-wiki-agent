---
title: "Double Descent"
type: concept
tags: [theory, generalization, deep-learning]
sources: [d2l-multilayer-perceptrons]
last_updated: 2026-05-16
---

# Double Descent

A non-monotonic test-error curve in modern over-parametrized models: as model complexity (depth, width, number of parameters) grows, test error first decreases (classical regime), then *rises* near the [[InterpolationRegime|interpolation threshold]] (when the model can just barely fit the training set), then **decreases again** in the over-parametrized regime ([[d2l-multilayer-perceptrons]] §Revisiting Overfitting and Regularization; [[PreetumNakkiran|Nakkiran]] et al. 2021).

## Why it matters

It directly contradicts the classical [[GeneralizationGap|U-shape]] story (capacity ↑ → overfitting ↑ → test error ↑). In deep learning we routinely operate *past* the interpolation threshold and observe further generalization gains — the empirical foundation of "make the model bigger" as a default lever in the LLM era ([[2001.08361-scaling-laws|Kaplan et al.]] scaling laws are an extreme of this regime).

## The three regimes

1. **Under-parametrized** (model too small) — high bias, high test error.
2. **Around the interpolation threshold** — test error peaks; classical complexity theory predicts this is where models *should* be worst.
3. **Over-parametrized** ($\#\text{params} \gg \#\text{train examples}$) — test error decreases again. Networks behave more like nonparametric / kernel-method interpolators; implicit regularization from [[StochasticGradientDescent|SGD]] favours low-norm interpolants.

## What classical theory misses

Per [[d2l-multilayer-perceptrons]]: "traditional complexity-based generalization bounds, e.g., those based on the [[VCDimension|VC dimension]] or [[RademacherComplexity|Rademacher complexity]] of a hypothesis class, cannot explain why neural networks generalize." Modern over-parametrized networks can fit *random labels* yet still generalize on clean ones — see [[ChiyuanZhang|Zhang]] et al. 2021.

## Connections

- [[d2l-multilayer-perceptrons]] — §Revisiting Overfitting and Regularization.
- [[Generalization]] / [[GeneralizationGap]] — modern story whose U-shape this complicates.
- [[Overfitting]] — old framing that double descent breaks.
- [[InterpolationRegime]] — the regime where the second descent lives.
- [[NeuralTangentKernel]] — kernel-method analogy for over-parametrized nets.
- [[VCDimension]] / [[RademacherComplexity]] — bounds that fail to predict double descent.
- [[ScalingLaws]] / [[2001.08361-scaling-laws]] — empirical second descent at LLM scale.
- [[StochasticGradientDescent]] — implicit-regularization candidate explanation.
