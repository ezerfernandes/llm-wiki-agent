---
title: "Mini-Batch Gradient Descent"
type: concept
tags: [training, optimization, neural-networks, ml-systems]
sources: [mlsysbook-ch05-neural-computation]
last_updated: 2026-06-05
---

# Mini-Batch Gradient Descent

The training procedure that updates network weights using the *average* gradient over a batch of B examples, rather than after each single example (pure SGD) or after the whole dataset (full-batch). The update is `θ ← θ − η · (1/B) Σ ∇L_i`. It is the workhorse of neural-network training and the default form of [[StochasticGradientDescent|stochastic gradient descent]].

Per [[mlsysbook-ch05-neural-computation|mlsysbook Vol 1 Ch 5]], batching serves two purposes simultaneously:

- **Statistical**: averaging gradients across examples gives a more stable gradient estimate by canceling noise.
- **Hardware**: GPUs process 32 inputs at nearly the same latency as 1 because [[MatrixMultiplication|matrix multiplication]] parallelizes across the batch dimension.

The trade-off is memory: each doubling of [[BatchSize|batch size]] roughly doubles activation storage, so batch size is ultimately a *hardware-memory* decision as much as a statistical one. The training loop runs in **[[NumberOfEpochs|epochs]]** (full passes over the data); MNIST at 60,000 images / batch 32 = 1,875 batch iterations per epoch.

## Connections

- [[GradientDescent]] / [[StochasticGradientDescent]] — the parent algorithms.
- [[BatchSize]] / [[LearningRate]] — the coupled hyperparameters (linear scaling rule).
- [[NumberOfEpochs]] / [[Training]] — the loop it runs inside.
- [[Backpropagation]] — supplies the per-example gradients.
- [[Adam]] / [[OptimizerState]] — adaptive variants and their memory cost.
- [[mlsysbook-ch05-neural-computation]] — source.
