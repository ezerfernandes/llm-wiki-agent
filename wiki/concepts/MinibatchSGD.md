---
title: "Minibatch SGD"
type: concept
tags: [optimization, deep-learning, foundational]
sources: [d2l-linear-regression, d2l-optimization]
last_updated: 2026-05-16
---

# Minibatch Stochastic Gradient Descent

The practical compromise between batch [[GradientDescent]] (full-data gradient, slow per step) and pure [[StochasticGradientDescent|SGD]] (single-example gradient, hardware-inefficient). Each iteration $t$ samples a random minibatch $\mathcal{B}_t \subset \{1,\dots,n\}$ of fixed size $|\mathcal{B}|$ and updates:

$$\boldsymbol\theta \leftarrow \boldsymbol\theta - \frac{\eta}{|\mathcal{B}|}\sum_{i\in\mathcal{B}_t}\nabla \ell^{(i)}(\boldsymbol\theta).$$

[[d2l-linear-regression]] §3.1.4 introduces minibatch SGD as the universal DL optimizer (citing :cite:`Li.Zhang.Chen.ea.2014`).

## Why minibatches

Two complementary motivations from [[d2l-linear-regression]]:

1. **Hardware efficiency**: "It is up to an order of magnitude more efficient to perform a matrix-vector multiplication than a corresponding number of vector-vector operations." Pure SGD wastes accelerators; full-batch GD doesn't fit in memory.
2. **Layers that need batched statistics**: [[BatchNormalization|batch norm]] and similar require $|\mathcal{B}| > 1$ for stable per-feature statistics.

## Choosing batch size

D2L's heuristic: "a number between 32 and 256, preferably a multiple of a large power of 2, is a good start." Tradeoffs:

- **Larger $|\mathcal{B}|$** → lower-variance gradients → smoother loss curves, but fewer parameter updates per epoch and diminishing returns past hardware-throughput saturation.
- **Smaller $|\mathcal{B}|$** → noisier gradients (often a *good* implicit regularizer), but underutilizes the accelerator.
- **Practical norm**: pick the largest batch that fits in GPU memory after activation buffers; tune learning rate to match (linear-scaling rule is a common default).

## For quadratic loss + affine model

The closed-form gradient (from [[d2l-linear-regression]] §3.1.4):

$$\mathbf{w} \leftarrow \mathbf{w} - \frac{\eta}{|\mathcal{B}|}\sum_{i\in\mathcal{B}_t}\mathbf{x}^{(i)}\left(\mathbf{w}^\top\mathbf{x}^{(i)} + b - y^{(i)}\right).$$

With $\ell_2$ [[WeightDecay|weight decay]] $\lambda$:

$$\mathbf{w} \leftarrow (1-\eta\lambda)\mathbf{w} - \frac{\eta}{|\mathcal{B}|}\sum_{i\in\mathcal{B}_t}\mathbf{x}^{(i)}\left(\mathbf{w}^\top\mathbf{x}^{(i)} + b - y^{(i)}\right).$$

## Connections

- [[d2l-linear-regression]] — canonical chapter introducing minibatch SGD.
- [[StochasticGradientDescent]] — single-sample parent algorithm.
- [[GradientDescent]] — full-batch parent algorithm.
- [[LearningRate]] / [[HyperparameterTuning]] — $\eta$ and $|\mathcal{B}|$ as the two co-tuned hyperparameters.
- [[WeightDecay]] — modifies the update by a $(1-\eta\lambda)$ shrinkage factor.
- [[Adam]] / [[Momentum]] — first/second-moment variants on top of minibatch SGD.
- [[DataLoader]] — yields the minibatches.
