---
title: "Weight Initialization"
type: concept
tags: [training, neural-networks, foundational]
sources: [madewithml-baselines, d2l-multilayer-perceptrons, d2l-builders-guide]
last_updated: 2026-05-16
---

# Weight Initialization

Choosing starting values for [[NeuralNetwork]] parameters so signals propagate without exploding or vanishing through depth. Co-determined with the activation function: [[XavierInitialization|Xavier]] for symmetric activations (tanh / sigmoid), [[HeInitialization|He / Kaiming]] for [[ReLU]] ([[d2l-multilayer-perceptrons]] §Parameter Initialization).

## Three problems init must solve

1. **Variance preservation.** Activations should neither vanish nor blow up across layers — both [[XavierInitialization|Xavier]] and [[HeInitialization|He]] target this with layer-fanin/fanout variance formulas.
2. **Symmetry breaking.** If every weight is initialized to the same value, all hidden units compute the same function and receive the same gradient — the layer behaves as if it had a single unit. *Random* init is the only way SGD alone breaks this (dropout also does; minibatch SGD on its own does not).
3. **Numerical stability of the first few steps.** Pathological initialization can put the loss on a plateau or in a regime where exploding gradients destroy parameters before any learning happens.

## The canon

| Scheme | Variance | When |
|---|---|---|
| **[[XavierInitialization|Xavier (Glorot)]]** | $2/(n_\text{in} + n_\text{out})$ | tanh / sigmoid |
| **[[HeInitialization|He / Kaiming]]** | $2/n_\text{in}$ | ReLU / Leaky-ReLU / pReLU |
| **LeCun** | $1/n_\text{in}$ | SELU / self-normalizing nets |
| **Orthogonal** | — | RNN recurrent matrices |
| **Identity / near-identity** | — | Residual blocks, sometimes |

## Modern deep nets

Initialization remains an active research area. [[d2l-multilayer-perceptrons]] §Beyond cites Xiao et al. (2018) training 10,000-layer networks *without* skip connections by using a carefully-designed init — a reminder that init can substitute for architectural tricks.

## Framework defaults

| Framework | Default for fully-connected |
|---|---|
| [[PyTorch]] | `kaiming_uniform_` (He uniform, $\sqrt 5$ gain) |
| [[TensorFlow]] / Keras | `glorot_uniform` (Xavier uniform) |
| [[JAX]] / Flax | `lecun_normal` |
| [[MXNet]] | Xavier |

## Connections

- [[d2l-multilayer-perceptrons]] — §Numerical Stability and Initialization (canonical reference for the *math*).
- [[d2l-builders-guide]] — §`init-param.md` — the *framework mechanics*: `net.apply(init_fn)`, per-layer overrides, custom initializers.
- [[ParameterInitialization]] — companion page covering the framework-mechanics layer in detail.
- [[XavierInitialization]] / [[HeInitialization]] — the two dominant schemes.
- [[ActivationFunction]] — paired choice.
- [[VanishingGradient]] / [[ExplodingGradient]] — pathologies init prevents.
- [[NeuralNetwork]] / [[MultilayerPerceptron]] — where init is set.
- [[BatchNormalization]] — partly compensates for poor init.
