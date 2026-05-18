---
title: "Nesterov Accelerated Gradient"
type: concept
tags: [optimization, mathematics]
sources: [d2l-optimization]
last_updated: 2026-05-16
---

# Nesterov Accelerated Gradient (NAG)

[[YuriiNesterov|Nesterov]] 1983 — a refinement of [[BorisPolyak|Polyak]]'s heavy-ball [[Momentum]] with **optimal $\mathcal{O}(1/T^2)$ convergence rate** on smooth convex objectives, versus Polyak's $\mathcal{O}(1/T)$. The key trick: evaluate the gradient at a *lookahead* position rather than the current iterate.

## The algorithm

Compare standard momentum (Polyak):

$$\mathbf{v}_t = \beta\mathbf{v}_{t-1} + \nabla f(\mathbf{x}_{t-1}), \quad \mathbf{x}_t = \mathbf{x}_{t-1} - \eta\mathbf{v}_t,$$

with Nesterov:

$$\mathbf{v}_t = \beta\mathbf{v}_{t-1} + \nabla f(\mathbf{x}_{t-1} - \eta\beta\mathbf{v}_{t-1}), \quad \mathbf{x}_t = \mathbf{x}_{t-1} - \eta\mathbf{v}_t.$$

The gradient is evaluated at $\mathbf{x}_{t-1} - \eta\beta\mathbf{v}_{t-1}$ — where the iterate *would be* if the previous-step velocity were applied without the new gradient. This "looking ahead" lets NAG correct the velocity *before* taking the step, avoiding the overshoot that pure Polyak momentum can exhibit.

## Convergence

- **Polyak momentum on smooth convex $f$**: $\mathcal{O}(1/T)$ rate.
- **Nesterov NAG**: $\mathcal{O}(1/T^2)$ rate — provably optimal among first-order methods (matches the lower bound for smooth convex optimization).

## In practice (DL frameworks)

PyTorch's `torch.optim.SGD(..., nesterov=True)` and TensorFlow's `tf.keras.optimizers.SGD(..., nesterov=True)` toggle NAG vs Polyak. Empirically the difference for DL is modest — both are dominated by the choice of [[LearningRateScheduler|schedule]] and base optimizer ([[Adam]] vs SGD-with-momentum). NAG is more commonly used for fine-tuning Computer Vision models with SGD, where it noticeably improves convergence speed.

## Connections

- [[d2l-optimization]] — references Nesterov 2018 *Lectures on Convex Optimization* (§momentum).
- [[YuriiNesterov]] — author.
- [[BorisPolyak]] — heavy-ball momentum that NAG accelerates.
- [[Momentum]] — the parent algorithm.
- [[ConvexOptimization]] — where NAG's $\mathcal{O}(1/T^2)$ rate is proven optimal.
- [[Adam]] — Nadam variant uses NAG-style lookahead with Adam's bias-corrected moments.
