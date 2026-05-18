---
title: "Module"
type: concept
tags: [training, framework, d2l]
sources: [d2l-linear-regression]
last_updated: 2026-05-16
---

# Module (D2L)

Base class for **models** in the [[d2l-preface|D2L]] [[ObjectOrientedDesign|OO]] scaffold ([[d2l-linear-regression]] §3.2). Inspired by [[PyTorchLightning|PyTorch Lightning]]. Inherits the framework-native module ([[PyTorch]] `nn.Module`, [[MXNet]] `nn.Block`, [[TensorFlow]] `tf.keras.Model`, [[JAX]]/Flax `linen.Module`) plus [[D2LPackage]]'s `HyperParameters` mixin.

## Required API

Every D2L `Module` subclass provides at minimum:

| Method | Role |
|---|---|
| `__init__` | Stores learnable parameters; calls `self.save_hyperparameters()` |
| `forward(X)` | Returns predictions (or sets `self.net` to a callable layer) |
| `loss(y_hat, y)` | Returns scalar loss on a minibatch |
| `configure_optimizers()` | Returns an `SGD` / `optim` instance |
| `training_step(batch)` | Default impl: `loss(forward(X), y)` + plot |
| `validation_step(batch)` | Default impl: `loss(forward(X), y)` + plot (no grad) |

## Why a thin shared abstraction

[[d2l-linear-regression]]: "Treating components in deep learning as objects, we can start by defining classes for these objects and their interactions. This object-oriented design for implementation will greatly streamline the presentation and you might even want to use it in your projects."

Every D2L architecture from linear regression through Transformers subclasses `Module`. Reuse: swap the optimizer, swap the model, swap the dataset — independently.

## Connections

- [[d2l-linear-regression]] — §3.2 canonical reference.
- [[DataModule]] — sibling class for data loaders.
- [[Trainer]] — orchestrates `fit(model, data)`.
- [[PyTorchLightning]] — named inspiration.
- [[D2LPackage]] — `Module`, `DataModule`, `Trainer`, `HyperParameters`, `ProgressBoard`, `add_to_class` all `#@save`-persisted.
- [[ObjectOrientedDesign]] — the broader design pattern.
