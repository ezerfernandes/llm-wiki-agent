---
title: "Learning Rate"
type: concept
tags: [optimization, hyperparameters]
sources: [mml-ch07-continuous-optimization, mml-book, d2l-linear-regression, d2l-optimization]
last_updated: 2026-06-05
---

# Learning Rate

The scalar $\eta$ that scales [[Gradient]] updates in [[GradientDescent]] / [[StochasticGradientDescent|SGD]] / [[Adam]]. Often the single most consequential hyperparameter — too high diverges, too low stalls; tuned via [[HyperparameterTuning]] and shaped over time by a [[LearningRateScheduler]].

[[d2l-linear-regression]] §3.1.4 introduces $\eta$ as one of two hyperparameters (with [[MinibatchSGD|minibatch]] size) that are "user-defined" — "tunable parameters that are not updated in the training loop are called *hyperparameters*. They can be tuned automatically by a number of techniques, such as [[BayesianOptimization|Bayesian optimization]]." Standard practical guidance: "Since our loss is computed as an average over the minibatch, we do not need to adjust the learning rate against the batch size."

## From [[mml-ch07-continuous-optimization|MML Ch 7]] — "step-size"

[[mml-ch07-continuous-optimization|MML Ch 7]] §7.1.1 calls this scalar the **step-size** $\gamma$ and notes in the margin that it "is also called the learning rate." Same quantity, different symbol ($\gamma$ vs the D2L/PyTorch $\eta$). The chapter's guidance:

- **Too small ⇒ slow; too large ⇒ overshoot, fail to converge, or even diverge** (p. 229). Getting $\gamma$ right is "important in gradient descent."
- **Two adaptive heuristics** (Toussaint 2012): if the function value *increased* after a step, $\gamma$ was too large — **undo the step and decrease** $\gamma$ (the undo guarantees monotonic convergence); if it *decreased*, the step could have been larger — **increase** $\gamma$.
- For [[StochasticGradientDescent|SGD]], a learning rate that **decreases at an appropriate rate** is what guarantees almost-sure convergence to a local minimum (Bottou 1998).

Curvature-aware step-size choices ([[ConditionNumber|condition number]], [[Preconditioner|preconditioning]], momentum) are the deeper remedy when a single global $\gamma$ is inadequate.

## Connections

- [[mml-ch07-continuous-optimization]] — §7.1.1 (step-size = learning rate; adaptive heuristics).
- [[d2l-linear-regression]] — first formal definition; paired with minibatch size as the two co-tuned hyperparameters.
- [[GradientDescent]] / [[StochasticGradientDescent]] / [[MinibatchSGD]] — uses $\eta$ as its step size.
- [[HyperparameterTuning]] — strategies for selecting $\eta$.
- [[LearningRateScheduler]] — varies $\eta$ over training.
- [[BayesianOptimization]] — automated $\eta$ search.
