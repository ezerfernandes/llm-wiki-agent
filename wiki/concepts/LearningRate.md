---
title: "Learning Rate"
type: concept
tags: [optimization, hyperparameters]
sources: [d2l-linear-regression, d2l-optimization]
last_updated: 2026-05-16
---

# Learning Rate

The scalar $\eta$ that scales [[Gradient]] updates in [[GradientDescent]] / [[StochasticGradientDescent|SGD]] / [[Adam]]. Often the single most consequential hyperparameter — too high diverges, too low stalls; tuned via [[HyperparameterTuning]] and shaped over time by a [[LearningRateScheduler]].

[[d2l-linear-regression]] §3.1.4 introduces $\eta$ as one of two hyperparameters (with [[MinibatchSGD|minibatch]] size) that are "user-defined" — "tunable parameters that are not updated in the training loop are called *hyperparameters*. They can be tuned automatically by a number of techniques, such as [[BayesianOptimization|Bayesian optimization]]." Standard practical guidance: "Since our loss is computed as an average over the minibatch, we do not need to adjust the learning rate against the batch size."

## Connections

- [[d2l-linear-regression]] — first formal definition; paired with minibatch size as the two co-tuned hyperparameters.
- [[GradientDescent]] / [[StochasticGradientDescent]] / [[MinibatchSGD]] — uses $\eta$ as its step size.
- [[HyperparameterTuning]] — strategies for selecting $\eta$.
- [[LearningRateScheduler]] — varies $\eta$ over training.
- [[BayesianOptimization]] — automated $\eta$ search.
