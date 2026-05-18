---
title: "Exploding Gradient"
type: concept
tags: [deep-learning, training, foundational]
sources: [d2l-multilayer-perceptrons]
last_updated: 2026-05-16
---

# Exploding Gradient

A training pathology where gradient magnitudes grow exponentially through [[Backpropagation|backprop]] in deep networks, blowing up parameter updates and destabilizing training. The symmetric counterpart of the [[VanishingGradient|vanishing gradient]] problem; both arise from the same $L$-fold Jacobian product structure ([[d2l-multilayer-perceptrons]] §Exploding Gradients).

## Mechanism + demo

D2L's $4\times 4$ demo: draw 100 IID standard-normal matrices and multiply them. The product's entries blow up rapidly — variances $\sim 4^{100}$. If a network's initial layer Jacobians look anything like these random matrices, gradients explode and SGD diverges before it can converge.

## Where it bites

- **Vanilla [[RNN|RNNs]] across long sequences** — the time-unrolled Jacobian product is exactly this scenario.
- **Very deep MLPs / CNNs without normalization or residual connections.**
- **Adversarial / GAN training** where saddle dynamics push gradients into pathological regions.

## Mitigations

- **Gradient clipping** — cap $\|\nabla\|_2 \leq \tau$ or per-component clip.
- **Careful [[WeightInitialization|initialization]]** — [[XavierInitialization|Xavier]] / [[HeInitialization|He]] keep per-layer variance controlled.
- **Residual / skip connections** — identity paths give gradients a stable route.
- **[[LSTM]] / [[GRU]] gating** for sequence models.
- **[[BatchNormalization|Normalization layers]]** rescale activations.

## Connections

- [[d2l-multilayer-perceptrons]] — §Exploding Gradients (canonical exposition).
- [[VanishingGradient]] — symmetric counterpart.
- [[Backpropagation]] — the Jacobian product is the mechanism.
- [[XavierInitialization]] / [[HeInitialization]] / [[WeightInitialization]] — initialization remedies.
- [[LSTM]] / [[GRU]] / [[RNN]] — historical sequence-model setting.
- [[BatchNormalization]] — orthogonal stabilization.
