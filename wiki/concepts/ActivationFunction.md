---
title: "Activation Function"
type: concept
tags: [deep-learning, neural-networks, foundational]
sources: [d2l-multilayer-perceptrons]
last_updated: 2026-05-16
---

# Activation Function

A (usually nonlinear) elementwise function applied after the affine transformation of a [[HiddenLayer|hidden layer]], converting weighted-sum inputs into outputs that propagate forward. The piece that *unlocks depth*: without a nonlinear activation, an arbitrarily deep [[MultilayerPerceptron|MLP]] collapses to a single affine map ([[d2l-multilayer-perceptrons]] §From Linear to Nonlinear).

## The canon

| Activation | Formula | Range | Where it lives |
|---|---|---|---|
| **[[ReLU]]** | $\max(0, x)$ | $[0, \infty)$ | Default for hidden layers — cheap, non-saturating |
| **Leaky / pReLU** | $\max(0,x) + \alpha\min(0,x)$ | $\mathbb{R}$ | Lets a small gradient through for $x<0$ |
| **[[Sigmoid]]** | $1/(1+e^{-x})$ | $(0,1)$ | Output for binary classification; gating in [[LSTM]]/[[GRU]] |
| **[[Tanh]]** | $\tanh(x)$ | $(-1,1)$ | Zero-centred squasher; classical hidden-layer choice |
| **GELU** | $x\,\Phi(x)$ | $\mathbb{R}$ | Default in [[Transformer]]s ([[Hendrycks-Gimpel-2016|Hendrycks & Gimpel 2016]]) |
| **Swish / SiLU** | $x\,\sigma(\beta x)$ | $\mathbb{R}$ | Common in CV / RL backbones (Ramachandran et al. 2017) |

## Why ReLU won the hidden-layer war

Per [[d2l-multilayer-perceptrons]] §Activation Functions: "ReLU is significantly more amenable to optimization than the sigmoid or the tanh function. One could argue that this was one of the key innovations that helped the resurgence of deep learning over the past decade." Its derivative is exactly 0 or 1 — no [[VanishingGradient|saturation-induced shrinkage]] of gradients, no need for delicate input scaling.

## Where saturating activations still live

- **Output layers** — sigmoid for binary classification, softmax for multi-class.
- **Gating** — sigmoid / tanh inside [[LSTM]] / [[GRU]] cells controlling information flow.
- **Bounded representations** — tanh in some RL value / policy heads.

## Interaction with initialization

The choice of activation co-determines the right [[WeightInitialization|initialization]]: [[XavierInitialization|Xavier]] for symmetric (tanh / sigmoid), [[HeInitialization|He / Kaiming]] for [[ReLU]] (factor-of-2 variance correction because ReLU zeroes half its inputs).

## Connections

- [[d2l-multilayer-perceptrons]] — §Activation Functions canonical reference.
- [[ReLU]] / [[Sigmoid]] / [[Tanh]] — the three core entries.
- [[HiddenLayer]] — where activations live.
- [[VanishingGradient]] / [[ExplodingGradient]] — pathologies the activation choice influences.
- [[XavierInitialization]] / [[HeInitialization]] — paired-initialization choice.
- [[Backpropagation]] — flows the activation's derivative.
- [[Dropout]] — composed after the activation in standard practice.
- [[Softmax]] — output-layer activation for classification.
