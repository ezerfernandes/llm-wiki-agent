---
title: "Multilayer Perceptron"
type: concept
tags: [neural-networks, architecture, foundational]
sources: [madewithml-baselines, d2l-multilayer-perceptrons]
last_updated: 2026-05-16
---

# Multilayer Perceptron (MLP)

A feedforward [[NeuralNetwork|neural network]] of one or more fully-connected [[HiddenLayer|hidden layers]] with nonlinear [[ActivationFunction|activations]] (typically [[ReLU]]) followed by a linear output layer. The canonical "first deep network" in [[d2l-multilayer-perceptrons|D2L]]'s pedagogy and the architectural baseline that pre-dates convolutional, recurrent, and [[Transformer|transformer]] models.

## Math (one hidden layer)

For minibatch $\mathbf{X}\in\mathbb{R}^{n\times d}$, hidden width $h$, output dim $q$:

$$
\mathbf{H} = \sigma(\mathbf{X}\mathbf{W}^{(1)} + \mathbf{b}^{(1)}), \quad
\mathbf{O} = \mathbf{H}\mathbf{W}^{(2)} + \mathbf{b}^{(2)}.
$$

**The activation $\sigma$ is essential.** Without it, the composition collapses to a single affine map $\mathbf{X}\mathbf{W} + \mathbf{b}$ — adding layers gains nothing ([[d2l-multilayer-perceptrons]] §From Linear to Nonlinear).

## Why MLPs work

- **Hidden layers learn a representation jointly with the predictor**, replacing handcrafted [[FeatureEngineering|feature engineering]].
- **[[UniversalApproximationTheorem|Universal approximation]]** ([[GeorgeCybenko|Cybenko 1989]]): one wide-enough hidden layer can approximate any continuous function — though learning it is the hard part.
- **Depth ≥ width in practice.** Deeper-rather-than-wider networks tend to be exponentially more compact for the same approximation quality (Simonyan & Zisserman 2014).

## What you have to get right

| Failure mode | Cause | Fix |
|---|---|---|
| Symmetry collapse | All weights initialized equal | Random init breaks the permutation symmetry |
| [[VanishingGradient]] | Saturating activations through deep stacks | [[ReLU]], [[XavierInitialization|Xavier]]/[[HeInitialization|He]] init, [[BatchNormalization]] |
| [[ExplodingGradient]] | Eigenvalue blowup in $L$-layer Jacobian product | Gradient clipping, careful init |
| Overfitting | Over-parametrized model with finite data | [[Dropout]], [[WeightDecay]], [[EarlyStopping]] |

## D2L's MLP for [[FashionMNIST]]

- 784 inputs (28×28 flattened) → 256 hidden ReLU → 10-way [[Softmax|softmax]] head.
- Layer widths "divisible by larger powers of 2" for memory-alignment performance.
- Trained with [[MinibatchSGD|minibatch SGD]] + [[Backpropagation|backprop]]; dropout = 0.5 on each hidden layer is the canonical regularized variant.

## Connections

- [[d2l-multilayer-perceptrons]] — canonical reference (this chapter).
- [[HiddenLayer]] — the central building block.
- [[ActivationFunction]] / [[ReLU]] / [[Sigmoid]] / [[Tanh]] — choices for $\sigma$.
- [[ForwardPropagation]] / [[Backpropagation]] — the training-loop primitives.
- [[XavierInitialization]] / [[HeInitialization]] — initialization choices.
- [[Dropout]] / [[WeightDecay]] / [[EarlyStopping]] — regularization companions.
- [[UniversalApproximationTheorem]] — expressivity guarantee.
- [[DoubleDescent]] / [[InterpolationRegime]] / [[NeuralTangentKernel]] — modern generalization story.
- [[NeuralNetwork]] — superclass.
- [[Transformer]] / [[CNN]] / [[RNN]] — architectural descendants for sequence / image / sequence data.
