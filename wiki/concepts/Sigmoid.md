---
title: "Sigmoid"
type: concept
tags: [activation-function, neural-networks]
sources: [d2l-multilayer-perceptrons, d2l-convolutional-neural-networks]
last_updated: 2026-05-16
---

# Sigmoid

The logistic *squashing function* $\sigma(x) = \frac{1}{1+\exp(-x)}$, mapping $\mathbb{R} \to (0,1)$. Historically the default hidden-layer [[ActivationFunction|activation]] — a smooth, differentiable approximation to a thresholding ([[McCullochPittsNeuron|McCulloch–Pitts]]) unit — now largely displaced by [[ReLU]] for hidden layers, while remaining a standard *output*-layer activation for binary classification and a core building block of gating ([[LSTM]] / [[GRU]]).

## Derivative

$$\frac{d}{dx}\sigma(x) = \sigma(x)(1 - \sigma(x)).$$

Maxes at $0.25$ when $x=0$ and vanishes for $|x|\gg 0$ — the proximal cause of the [[VanishingGradient|vanishing-gradient]] problem in deep stacks of sigmoids ([[d2l-multilayer-perceptrons]] §Vanishing Gradients).

## Why it lost the hidden-layer war

- Saturating gradient → backprop signal dies through many layers unless inputs sit in the "Goldilocks zone" near 0.
- $\sigma(x)$ is not zero-centred → gradient updates have correlated signs across all weights of a unit.
- [[ReLU]] gradient is exactly 0 or 1 — no shrinkage.

## Where sigmoid still belongs

- **Output layer for binary classification** — a special case of [[Softmax|softmax]]; output interpreted as $P(y=1\mid\mathbf{x})$.
- **Gating units inside [[LSTM]] / [[GRU]]** — controlling how much information flows through.
- **Attention mechanisms** where bounded $(0,1)$ "on/off" weights are desired.

## Relation to tanh

$\tanh(x) + 1 = 2\sigma(2x)$ — tanh is a shifted/scaled sigmoid. Tanh is zero-centred and has max derivative 1 (vs sigmoid's 0.25), so it was often preferred *before* ReLU.

## Connections

- [[d2l-multilayer-perceptrons]] — §Activation Functions; §Vanishing Gradients.
- [[ActivationFunction]] — parent concept.
- [[ReLU]] — modern replacement for hidden layers.
- [[Tanh]] — closely related squasher.
- [[Softmax]] — multi-class generalization.
- [[VanishingGradient]] — pathology sigmoid causes in deep stacks.
- [[LogisticRegression]] — sigmoid applied to a linear model.
- [[LSTM]] / [[GRU]] — gating still uses sigmoid.
