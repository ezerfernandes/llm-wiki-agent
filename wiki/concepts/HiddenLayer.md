---
title: "Hidden Layer"
type: concept
tags: [neural-networks, architecture, foundational]
sources: [d2l-multilayer-perceptrons]
last_updated: 2026-05-16
---

# Hidden Layer

An intermediate fully-connected layer in a [[MultilayerPerceptron|neural network]] whose output (a *hidden representation*) is consumed only by subsequent layers, never directly observed. The first $L-1$ layers of an $L$-layer MLP are interpreted as a learned representation; the final layer is a linear predictor on top ([[d2l-multilayer-perceptrons]] §Hidden Layers).

## Why hidden layers help

[[LinearRegression|Linear]] / [[Softmax|softmax]] models assume monotonic, feature-additive structure — sufficient for "income → loan repayment" but absurd for "pixel (13,17) → dog probability." Stacking *affine + activation* layers lets the network *jointly learn a representation and a linear predictor on it*, replacing handcrafted [[FeatureEngineering|feature engineering]] (Canny / SIFT / kernels).

## Math

One hidden layer with $h$ units, applied to a minibatch $\mathbf{X}\in\mathbb{R}^{n\times d}$:

$$
\mathbf{H} = \sigma(\mathbf{X}\mathbf{W}^{(1)} + \mathbf{b}^{(1)}), \quad
\mathbf{O} = \mathbf{H}\mathbf{W}^{(2)} + \mathbf{b}^{(2)}.
$$

[[ActivationFunction|$\sigma$]] is **essential** — without it, $\mathbf{O}$ collapses to $\mathbf{X}\mathbf{W}^{(1)}\mathbf{W}^{(2)} + \ldots$, a single affine map.

## Width vs depth

[[UniversalApproximationTheorem|Universal approximation]] guarantees a *single* wide enough hidden layer can represent any function, but [[d2l-multilayer-perceptrons]] notes that deeper-rather-than-wider networks tend to be more compact representations of the same target.

## Practical choices

- Width = hyperparameter; D2L's default for [[FashionMNIST]] = 256 units.
- "Typically, we choose the layer widths to be divisible by larger powers of 2" — hardware memory alignment.
- Hidden layers are paired with [[ReLU|ReLU]] in modern practice; the input layer has no parameters and is not counted in "layer depth."

## Connections

- [[d2l-multilayer-perceptrons]] — §Hidden Layers; the canonical reference.
- [[MultilayerPerceptron]] — stack of hidden layers.
- [[ActivationFunction]] — what makes a hidden layer nonlinear.
- [[ReLU]] / [[Sigmoid]] / [[Tanh]] — common choices.
- [[RepresentationLearning]] — hidden layer outputs *are* the learned representation.
- [[ForwardPropagation]] / [[Backpropagation]] — how values and gradients flow through hidden layers.
- [[UniversalApproximationTheorem]] — why a single hidden layer suffices in principle.
