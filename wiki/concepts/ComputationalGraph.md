---
title: "Computational Graph"
type: concept
tags: [autograd, deep-learning, foundational]
sources: [mml-ch05-vector-calculus, d2l-preliminaries, d2l-multilayer-perceptrons, mlsysbook-ch07-ml-frameworks]
last_updated: 2026-06-05
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

## From [[mml-ch05-vector-calculus|MML Ch 5]]

§5.6.2 introduces the computation graph as the structure [[AutomaticDifferentiation|automatic differentiation]] traverses. MML's running example (Example 5.14, Fig. 5.11) decomposes $f(x)=\sqrt{x^2+\exp(x^2)}+\cos(x^2+\exp(x^2))$ into **intermediate variables** $a=x^2$, $b=\exp(a)$, $c=a+b$, $d=\sqrt{c}$, $e=\cos(c)$, $f=d+e$ (Eqs. 5.123–5.128) — fewer operations than a direct implementation. Formally (Eqs. 5.143–5.145): with input variables $x_1..x_d$, intermediates $x_{d+1}..x_{D-1}$, output $x_D$, each node is $x_i=g_i(x_{\mathrm{Pa}(x_i)})$ for elementary $g_i$ and parent set $\mathrm{Pa}(x_i)$. **Forward propagation** is Eq. 5.143; **backpropagation** of the gradient is the reverse walk $\frac{\partial f}{\partial x_i}=\sum_{x_j:\,x_i\in\mathrm{Pa}(x_j)}\frac{\partial f}{\partial x_j}\frac{\partial g_j}{\partial x_i}$ (Eq. 5.145). MML notes this *"is a representation that is widely used in implementations of neural network software libraries"* and that reverse-mode autodiff *"requires a parse tree"*; control structures (`for`, `if`) need extra care.

## Systems framing from [[mlsysbook-ch07-ml-frameworks|mlsysbook Vol 1 Ch 7]]

Ch 7 treats the graph (a DAG, "pioneered by [[Theano]] in 2007") as *the* data structure that makes both [[KernelFusion|kernel fusion]] and [[AutomaticDifferentiation|autodiff]] possible — "a framework can only fuse operations it can see together." The execution problem turns on *when* the graph is built, with a four-way cascade: debugging, optimization, deployment (Python-independent execution), and flexibility (data-dependent control flow). [[EagerExecution|Eager]] builds it dynamically per forward pass; [[StaticGraph|static graphs]] build it ahead of time; [[JITCompilation|JIT]] captures it at runtime.

## Connections

- [[mml-ch05-vector-calculus|MML Ch 5]] — §5.6.2 (intermediate-variable graph + forward/backprop equations).
- [[mlsysbook-ch07-ml-frameworks]] — the graph as the structure enabling fusion + autodiff; static vs dynamic vs JIT.
- [[d2l-preliminaries]] — defines the graph + dynamic-vs-static distinction.
- [[d2l-multilayer-perceptrons]] — works through the MLP forward/backward graph explicitly.
- [[ForwardPropagation]] — the build phase.
- [[Autograd]] — the engine that walks the graph backwards.
- [[Backpropagation]] — the reverse-mode algorithm.
- [[ChainRule]] — applied at each node.
- [[Gradient]] / [[Jacobian]] — what the walk produces.
- [[PyTorch]] / [[TensorFlow]] / [[JAX]] / [[MXNet]] — implementations.
