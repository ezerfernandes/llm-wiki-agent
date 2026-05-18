---
title: "Tanh"
type: concept
tags: [activation-function, neural-networks]
sources: [d2l-multilayer-perceptrons]
last_updated: 2026-05-16
---

# Tanh

The hyperbolic-tangent squashing [[ActivationFunction|activation]] $\tanh(x) = \frac{1-\exp(-2x)}{1+\exp(-2x)}$, mapping $\mathbb{R} \to (-1, 1)$. Zero-centred (unlike [[Sigmoid|sigmoid]]) and with max derivative $1$ at $x=0$ vs sigmoid's $0.25$ — historically the preferred hidden-layer activation *before* [[ReLU]] ([[d2l-multilayer-perceptrons]] §Tanh Function).

## Derivative

$$\frac{d}{dx}\tanh(x) = 1 - \tanh^2(x).$$

Vanishes for $|x|\gg 0$, so tanh still suffers [[VanishingGradient|vanishing gradients]] in deep networks — but less aggressively than sigmoid.

## Relation to sigmoid

$\tanh(x) + 1 = 2\sigma(2x)$, so an MLP with biases parametrizes the same function class under either nonlinearity. The practical difference is the gradient *magnitude*, which affects optimization speed.

## Where tanh still belongs

- **[[LSTM]] / [[GRU]]** cell-state and candidate-activation units — the bounded $(-1, 1)$ range keeps recurrent state in check.
- Some normalization-free architectures where a zero-centred saturating activation is desired.
- Pre-ReLU CNNs (LeNet-5, classical MLPs).

## Connections

- [[d2l-multilayer-perceptrons]] — §Tanh Function.
- [[ActivationFunction]] — parent.
- [[Sigmoid]] — closely related squasher.
- [[ReLU]] — modern replacement in hidden layers.
- [[VanishingGradient]] — pathology tanh shares with sigmoid (milder).
- [[LSTM]] / [[GRU]] — recurrent architectures that still use tanh.
