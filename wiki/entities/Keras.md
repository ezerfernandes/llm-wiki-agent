---
title: "Keras"
type: entity
tags: [framework, deep-learning, high-level-api]
sources: [mlsysbook-ch07-ml-frameworks]
last_updated: 2026-06-05
---

# Keras

**Keras** (François Chollet, 2015) is the high-level layer/model API associated with [[TensorFlow]] (exposed as `tf.keras`). It implements the same three [[nnModule|module]] design principles as PyTorch's `nn.Module`: parameter discovery via `layer.trainable_weights`, non-trainable state via `non_trainable_weights`, and hierarchical composition (`tf.keras.Sequential`). In the mlsysbook framework comparison it represents the *declarative* design point — the `Sequential` API declares structure without executing it, prioritizing the abstraction problem (one declaration compiles to server GPUs, mobile NPUs, or browser WebGL).

## Connections

- [[mlsysbook-ch07-ml-frameworks]] — cited as TensorFlow's high-level API and a cross-framework example of the module pattern.
- [[TensorFlow]] — the parent framework; [[nnModule]] — the shared design principles.
- [[PyTorch]] / [[Flax]] — sibling layer/module abstractions.
