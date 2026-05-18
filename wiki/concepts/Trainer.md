---
title: "Trainer"
type: concept
tags: [training, framework]
sources: [madewithml-training, d2l-linear-regression]
last_updated: 2026-05-16
---

# Trainer

An abstraction (e.g., HuggingFace `Trainer`, [[PyTorchLightning|PyTorch Lightning]], [[d2l-preface|D2L]]'s own `d2l.Trainer`) that encapsulates training loops, evaluation hooks, [[ModelCheckpoint]] saving, and distributed concerns like [[PyTorchDDP]]. Reduces boilerplate around the core gradient step.

## D2L's Trainer

[[d2l-linear-regression]] §3.2 introduces `d2l.Trainer` as the third leg of the [[Module]] / [[DataModule]] / [[Trainer]] OO scaffold (inspired by [[PyTorchLightning|Lightning]]). The key method `fit(model, data)` iterates `max_epochs` times, calling `model.training_step(batch)` over each minibatch followed by `optim.step()` / `optim.zero_grad()`, then `model.validation_step(batch)` over the val loader. The chapter's `fit_epoch` is framework-specific (PyTorch uses `loss.backward()`; TF uses `tf.GradientTape()`; JAX uses `jax.value_and_grad`).

## Connections

- [[d2l-linear-regression]] — §3.2 canonical reference for the D2L Trainer scaffold.
- [[Module]] / [[DataModule]] — sibling classes in the D2L OO scaffold.
- [[PyTorchLightning]] — the named inspiration for D2L's design.
- [[Backpropagation]] / [[StochasticGradientDescent]] — what each `fit_epoch` step executes.
