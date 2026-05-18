---
title: "Computational Graph"
type: concept
tags: [autograd, deep-learning, foundational]
sources: [d2l-preliminaries, d2l-multilayer-perceptrons]
last_updated: 2026-05-16
---

# Computational Graph

A directed acyclic graph (DAG) whose nodes are tensor values and whose edges are differentiable primitive operations (add, multiply, matmul, exp, log, …). Every modern [[Autograd|autograd]] engine ([[PyTorch]], [[TensorFlow]] `GradientTape`, [[JAX]], [[MXNet]]) implements [[Backpropagation]] as a **reverse traversal** of this graph, applying the [[ChainRule|chain rule]] at each node.

## Two regimes

| Style | Frameworks | Graph constructed when |
|---|---|---|
| **Dynamic / define-by-run** | [[PyTorch]] (default), [[MXNet]] (autograd), TF eager mode | Forward pass — graph realized per execution |
| **Static / define-then-run** | [[TensorFlow]] (`tf.function`), [[JAX]] (`jit`) | Ahead of time — graph traced + compiled before running |

Both reach the same chain-rule answer; static graphs trade flexibility for optimization headroom (kernel fusion, XLA, constant folding).

## Forward = build, backward = walk

[[d2l-preliminaries]] §Autograd makes the framing explicit:

> "As we pass data through each successive function, the framework builds a *computational graph* that tracks how each value depends on others. To calculate derivatives, automatic differentiation works backwards through this graph applying the chain rule."

Because the graph is realized per execution in dynamic frameworks, [[Autograd|autograd]] handles arbitrary **Python control flow** (`while`, `if`, recursion) — the path through the graph is whatever the function actually executed.

## Detaching subgraphs

Sometimes we want a value's *numerical* result but not its gradient contribution — e.g., computing a target that should be treated as a constant. The frameworks expose this as:

- PyTorch: `y.detach()`
- TensorFlow: `tf.stop_gradient(y)`
- JAX: `jax.lax.stop_gradient(y)`
- MXNet: `y.detach()`

Detaching erases ancestor edges leading into the detached node — gradients no longer flow through it — while leaving the original graph intact for separate gradient calls.

## Why memory matters

For a depth-$L$ network with batch $B$ and width $H$, retaining the full graph (activations at every layer) costs $O(LBH)$ memory. *Gradient checkpointing* trades compute for memory by re-running forward segments during backward. [[FlashAttention]] is a related IO-aware rewrite that avoids materializing intermediate attention matrices.

## Connections

- [[d2l-preliminaries]] — defines the graph + dynamic-vs-static distinction.
- [[d2l-multilayer-perceptrons]] — works through the MLP forward/backward graph explicitly.
- [[ForwardPropagation]] — the build phase.
- [[Autograd]] — the engine that walks the graph backwards.
- [[Backpropagation]] — the reverse-mode algorithm.
- [[ChainRule]] — applied at each node.
- [[Gradient]] / [[Jacobian]] — what the walk produces.
- [[PyTorch]] / [[TensorFlow]] / [[JAX]] / [[MXNet]] — implementations.
