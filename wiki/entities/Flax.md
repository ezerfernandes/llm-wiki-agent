---
title: "Flax"
type: entity
tags: [framework, deep-learning, jax, neural-network-library]
sources: [mlsysbook-ch07-ml-frameworks]
last_updated: 2026-06-05
---

# Flax

**Flax** is a neural-network library built on top of [[JAX]]. Because JAX's minimalist core provides only composable function transformations (`grad`/`jit`/`vmap`/`pmap`), it delegates conventional neural-network abstractions to companion libraries — Flax, Haiku, and Equinox — with optimization handled by Optax. Flax implements the [[nnModule|module]] pattern within JAX's functional paradigm: parameters are returned by `model.init(key, x)` as a nested dictionary, with non-trainable state kept in a separate `state` dict (mirroring PyTorch's parameter/buffer split). This separation reflects the functional philosophy: the core provides transformations, libraries build the conventional abstractions on top.

## Connections

- [[mlsysbook-ch07-ml-frameworks]] — cited as JAX's neural-network library and a cross-framework module-pattern example.
- [[JAX]] — the framework Flax builds on; [[nnModule]] — the shared design principles.
- [[Keras]] / [[PyTorch]] — sibling module abstractions.
