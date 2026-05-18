---
title: "Learning Rate Scheduler"
type: concept
tags: [optimization, training, deep-learning]
sources: [d2l-optimization]
last_updated: 2026-05-16
---

# Learning Rate Scheduler

A policy $\eta(t)$ that varies the [[LearningRate]] across training. The choice of schedule is often as consequential as the choice of optimizer ([[d2l-optimization]] §lr-scheduler).

## The three axes of scheduling

[[d2l-optimization]] §lr-scheduler distinguishes three orthogonal concerns:

1. **Magnitude.** Too large diverges; too small stalls. Set relative to the [[ConditionNumber|condition number]] of the loss.
2. **Decay rate.** For nonconvex DL, slower than $\mathcal{O}(t^{-1/2})$ is typically desirable. Too-fast decay (e.g. exponential $e^{-\lambda t}$) "leads to premature stopping before the algorithm has converged."
3. **Initialization (warmup).** Random-init parameters with large $\eta$ point in meaningless directions; [[Warmup|linear warmup]] from 0 to $\eta_0$ avoids early divergence.

## Canonical policies

| Schedule | Form | Typical use |
|---|---|---|
| **Piecewise constant** | $\eta(t) = \eta_i$ on $[t_i, t_{i+1}]$ | drop $\eta$ at fixed milestones |
| **Factor** | $\eta_{t+1} = \max(\eta_\min, \alpha\eta_t)$ | smooth multiplicative decay |
| **MultiFactor** | drop by $\alpha$ at $t \in \{15, 30, \ldots\}$ | step-decay (classic for CNN training) |
| **Polynomial** | $\eta_0(t+1)^{-\alpha}$, default $\alpha=0.5$ | provably well-behaved on convex SGD |
| **Exponential** | $\eta_0 e^{-\lambda t}$ | generally too aggressive — "leads to premature stopping" |
| **[[CosineLRSchedule|Cosine annealing]]** | $\eta_T + \tfrac{\eta_0-\eta_T}{2}(1+\cos(\pi t/T))$ | Loshchilov & Hutter 2016; default for CV + LLM pretraining |
| **[[Warmup]] + decay** | linear ramp $0\to\eta_0$ then decay | LLM pretraining standard |

## Why scheduling helps even in non-theoretical terms

[[d2l-optimization]] §lr-scheduler:

> "Decreasing the learning rate during training can lead to improved accuracy and (most perplexingly) reduced overfitting of the model… A warmup period before optimization can prevent divergence."

The piecewise-constant intuition: let SGD wander until it reaches the *neighborhood* of a good local minimum (large $\eta$ helps escape suboptimal basins and saddle points), then **reduce $\eta$ to converge into a single nearby minimum** (small $\eta$ reduces the parameter-variance of the SGD iterate, yielding a sharper / more confident solution).

## Modern default recipes

- **[[transformer|Transformer]] pretraining (GPT / BERT / T5 / LLaMA)**: linear warmup over 1–10k steps → cosine decay to $\eta_T = 0.1\eta_0$.
- **CNN ImageNet training**: step decay (MultiFactor) or cosine annealing; sometimes ReduceLROnPlateau on validation loss.
- **Fine-tuning**: very short warmup (a few hundred steps) → linear decay to zero.

## Framework support

- **PyTorch**: `torch.optim.lr_scheduler.{StepLR, MultiStepLR, ExponentialLR, CosineAnnealingLR, LambdaLR, ReduceLROnPlateau, OneCycleLR, SequentialLR}`.
- **TensorFlow / Keras**: `tf.keras.optimizers.schedules.{ExponentialDecay, PiecewiseConstantDecay, PolynomialDecay, CosineDecay, CosineDecayRestarts}` + `LearningRateScheduler` callback.
- **MXNet**: `mxnet.lr_scheduler.{FactorScheduler, MultiFactorScheduler, PolyScheduler, CosineScheduler}`.

## Connections

- [[d2l-optimization]] — canonical reference (§lr-scheduler).
- [[LearningRate]] — what the scheduler modifies.
- [[CosineLRSchedule]] — most-used decay in modern DL.
- [[Warmup]] — typically composed at the start of any schedule.
- [[GradientDescent]] / [[StochasticGradientDescent]] / [[MinibatchSGD]] / [[Adam]] — algorithms whose effective convergence the scheduler shapes.
- [[transformer|Transformer]] / [[BERT]] / [[T5]] / [[GPT]] — LLM pretraining recipes standardize on warmup + cosine.
- [[FineTuning]] / [[LLMFineTuning]] — short-warmup + linear-decay is the standard.
