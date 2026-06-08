---
title: "Autograd"
type: concept
tags: [deep-learning, frameworks]
sources: [d2l-preliminaries, mlsysbook-ch07-ml-frameworks]
last_updated: 2026-06-05
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

## Internals from [[mlsysbook-ch07-ml-frameworks|mlsysbook Vol 1 Ch 7]]

Ch 7 details PyTorch's autograd as a dynamic **tape** (also called the reverse-linked graph): each forward op records a `Function` node storing input references + a backward rule; every differentiable tensor stores a `grad_fn`, and `next_functions` forms a reverse chain (`PowBackward0`→`MulBackward0`→`AccumulateGrad` at leaf tensors). The tape is destroyed after `backward()` (use `retain_graph=True` for multi-loss/higher-order, at doubled memory). The dominant cost is the **activation tax**: stored intermediates make training memory ~100× inference. Safe gradient control: `.detach()` (and `.detach().clone()` before in-place mutation), hooks (`register_hook`) for clipping/inspection; the legacy `.data` attribute and in-place ops (`x += 1`) can silently corrupt gradients (PyTorch's tensor version counters catch the latter). Ch 7's "tape-based vs transform-based" perspective contrasts this with [[JAX]]'s function transformations.

## Connections

- [[mlsysbook-ch07-ml-frameworks]] — PyTorch autograd internals (grad_fn chain, memory tax, hooks, detach).
- [[ReverseModeAutodiff]] / [[ForwardModeAutodiff]] / [[DualNumbers]] — the modes.
- [[ActivationCheckpointing]] / [[GradientAccumulation]] — managing the activation tax.
