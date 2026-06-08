---
title: "nn.Module Abstraction"
type: concept
tags: [frameworks, pytorch, programming-model, abstraction]
sources: [mlsysbook-ch07-ml-frameworks]
last_updated: 2026-06-05
---

# nn.Module Abstraction

The **module abstraction** bundles parameters, forward computation, and state management into a single reusable, nestable unit. PyTorch's `nn.Module` is the instructive case, but the same three design principles recur across [[Keras]] layers, JAX's [[Flax]] modules, and TensorFlow's `tf.Module`:

1. **Automatic parameter discovery** — assigning an `nn.Parameter` triggers metaclass registration; `.parameters()` does a recursive depth-first traversal of the module tree, so `optimizer.step()` updates millions of parameters in one vectorized call (avoiding per-parameter Python dispatch). Cross-framework: Keras `trainable_weights`, Flax `params`, TF `trainable_variables`.
2. **Mode-dependent behavior** — a single `.eval()` on the root recursively sets `training=False` on all descendants, switching dropout (identity at inference) and batch norm (running stats vs per-batch). Forgetting it yields silently wrong predictions.
3. **Hierarchical composition + serialization** — `state_dict()` flattens the tree to dotted keys (`blocks.0.conv1.weight`), enabling sequential-byte-stream checkpointing (a 7B model's ~14 GB FP16 checkpoint) and cross-framework exchange via [[ONNX]]. The tree also gives natural partition boundaries for model parallelism.

**Parameters vs buffers**: buffers (`register_buffer`) travel with the model on `.to('cuda')` but receive no gradients (e.g. BatchNorm running statistics). **Hooks** (`register_forward_hook`/`register_full_backward_hook`) intercept activations/gradients non-invasively for inspection or clipping.

## Connections

- [[mlsysbook-ch07-ml-frameworks]] — the nn.Module abstraction section (upper half of the abstraction problem).
- [[NeuralNetworkModule]] — closely related module concept.
- [[PyTorch]] / [[Keras]] / [[Flax]] / [[TensorFlow]] — frameworks implementing the same three principles.
- [[ONNX]] — cross-framework state-dict exchange; [[AutomaticDifferentiation]] — what parameter discovery feeds.
