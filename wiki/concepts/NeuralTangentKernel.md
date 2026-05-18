---
title: "Neural Tangent Kernel"
type: concept
tags: [theory, deep-learning, kernel-methods]
sources: [d2l-multilayer-perceptrons, d2l-gaussian-processes]
last_updated: 2026-05-16
---

# Neural Tangent Kernel (NTK)

A kernel function that captures the behaviour of an *infinitely-wide* [[NeuralNetwork|neural network]] trained by gradient descent. [[ArthurJacot|Jacot]], Gabriel & Hongler (2018) proved that as an MLP's width $\to\infty$ at standard initialization, training dynamics under gradient descent become equivalent to kernel regression with a specific kernel — the **neural tangent kernel** — making the [[InterpolationRegime|interpolation-regime]] correspondence between over-parametrized networks and [[KernelMethods|kernel methods]] precise ([[d2l-multilayer-perceptrons]] §Inspiration from Nonparametrics).

## What NTK does for us

- **Analytical tool.** Predicts learning curves, generalization, and inductive bias for very wide networks without simulating gradient descent.
- **Justification for the nonparametric framing.** "In the limit, as multilayer perceptrons with randomly initialized weights grow infinitely wide, they become equivalent to (nonparametric) kernel methods" — bridges the classical kernel literature ([[ScholkopfSmola2002|Schölkopf & Smola 2002]]) to modern deep learning.
- **Lower bound on generalization understanding.** NTK models don't fully explain finite-width / feature-learning behaviour, but they're the cleanest theoretical handle we currently have.

## Limits

NTK is a *lazy regime*: features are essentially frozen at their initialization values. Real-world deep networks do *feature learning* (their hidden representations change non-trivially), which NTK cannot model. Bridging lazy and feature-learning regimes is an active research area.

## Connections

- [[d2l-multilayer-perceptrons]] — §Inspiration from Nonparametrics.
- [[InterpolationRegime]] — the empirical regime NTK formalizes.
- [[DoubleDescent]] — kernel-regression analyses recover double-descent curves.
- [[KernelMethods]] — the framework NTK reduces deep nets to.
- [[Generalization]] — what NTK lets us prove things about (in the wide limit).
- [[NeuralNetwork]] / [[MultilayerPerceptron]] — the model NTK characterizes (in infinite-width limit).
- [[NeuralNetworkKernel]] — [[RadfordNeal|Neal 1996]]'s 1990s precursor: a *Bayesian* one-hidden-layer NN at infinite width is a GP with a closed-form arcsine kernel ([[d2l-gaussian-processes]] gp-priors).
- [[GaussianProcess]] — the inferential framework NTK reduces gradient-trained wide nets to.
