---
title: "He Initialization"
type: concept
tags: [weight-initialization, training, deep-learning]
sources: [d2l-multilayer-perceptrons]
last_updated: 2026-05-16
---

# He Initialization

Also called *Kaiming initialization*. A [[WeightInitialization|weight-initialization]] heuristic tailored to [[ReLU]] hidden units: weights are drawn from a zero-mean distribution with

$$\sigma^2 = \frac{2}{n_\text{in}}.$$

The factor of 2 compensates for ReLU zeroing roughly half its inputs in expectation, so layer-output variance is preserved forward. Introduced by [[KaimingHe|He]], Zhang, Ren & Sun (2015); the [[ReLU]]-era successor to [[XavierInitialization|Xavier]] ([[d2l-multilayer-perceptrons]] §Beyond).

## When to use He vs Xavier

- **[[ReLU]] / Leaky-ReLU / pReLU / GELU networks → He.**
- **[[Tanh]] / [[Sigmoid]] networks → [[XavierInitialization|Xavier (Glorot)]].**
- SELU networks → LeCun ($\sigma^2 = 1/n_\text{in}$).

## Framework defaults

| Framework | Default for `Linear` / `Dense` |
|---|---|
| [[PyTorch]] | `kaiming_uniform_` — He uniform with $\sqrt{5}$ gain (historical). |
| [[TensorFlow]] / Keras | `glorot_uniform` (Xavier) — override via `kernel_initializer='he_normal'` for ReLU nets. |
| [[JAX]] / Flax | `lecun_normal`. |

## Why "2" matters

Skipping the factor and using Xavier on a deep ReLU stack is the classic recipe for [[VanishingGradient|vanishing gradients]] — activation variance shrinks by ½ per layer, becoming negligible after a few dozen layers.

## Connections

- [[d2l-multilayer-perceptrons]] — §Numerical Stability and Initialization.
- [[WeightInitialization]] — parent concept.
- [[XavierInitialization]] — sibling for symmetric activations.
- [[ReLU]] — the activation He init is matched to.
- [[VanishingGradient]] / [[ExplodingGradient]] — pathologies it prevents.
- [[KaimingHe]] — author (entity / stub).
