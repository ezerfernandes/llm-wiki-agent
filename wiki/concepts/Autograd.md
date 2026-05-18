---
title: "Autograd"
type: concept
tags: [deep-learning, frameworks]
sources: [d2l-preliminaries]
last_updated: 2026-05-16
---

# Autograd

Automatic differentiation engines ([[PyTorch]] autograd, [[JAX]] `grad`, [[TensorFlow]] `GradientTape`, [[MXNet]] `autograd.record`) that record forward-pass operations into a [[ComputationalGraph|computational graph]] and compute exact gradients via the [[ChainRule|chain rule]] = [[Backpropagation]]. Makes gradient computation tractable for arbitrary architectures and underpins all modern [[GradientDescent]] / [[Adam]] training.

## Historical note

[[d2l-preliminaries]] §Automatic Differentiation traces autograd's lineage further than most ML texts:

- **Wengert 1964** — earliest reference to automatic differentiation.
- **Speelpenning 1980 (PhD thesis)** — modern backpropagation ideas.
- **Griewank 1989** — further development of reverse-mode AD.

Backprop is the dominant method but not the only option — Julia's `ForwardDiff.jl` (Revels, Lubin, Papamarkou 2016) uses forward-mode AD.

## Framework cheat-sheet

| Framework | Enable gradient | Run forward | Trigger backward | Read gradient |
|---|---|---|---|---|
| PyTorch | `x.requires_grad_(True)` | `y = f(x)` | `y.backward()` | `x.grad` |
| TensorFlow | `x = tf.Variable(x)` | `with tf.GradientTape() as t: y = f(x)` | `t.gradient(y, x)` | (returned) |
| JAX | (functional) | `y = f(x)` | `grad(f)(x)` | (returned) |
| MXNet | `x.attach_grad()` | `with autograd.record(): y = f(x)` | `y.backward()` | `x.grad` |

**PyTorch *accumulates* gradients** across `backward()` calls (call `x.grad.zero_()` before each step); MXNet / TF / JAX overwrite. The PyTorch behavior is a footgun but enables clean multi-objective summation.

## Practical features

- **Non-scalar `y`**: frameworks reduce-via-sum before differentiating (Jacobian APIs available separately).
- **Detach / `stop_gradient`**: remove a subgraph from gradient flow without breaking the forward computation. See [[ComputationalGraph]].
- **Python control flow** (while/if) is supported in dynamic frameworks — the graph is realized per execution.
- **Higher-order gradients**: gradients of gradients via nested `grad` (JAX) or `create_graph=True` (PyTorch).
