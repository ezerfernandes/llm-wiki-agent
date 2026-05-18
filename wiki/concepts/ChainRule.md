---
title: "Chain Rule"
type: concept
tags: [calculus, foundational]
sources: [mml-book, d2l-preliminaries, d2l-multilayer-perceptrons, d2l-appendix-mathematics]
last_updated: 2026-05-16
---

# Chain Rule

The derivative of a composition. For scalar functions $y = f(g(x))$ with $y = f(u)$ and $u = g(x)$:

$$\frac{dy}{dx} = \frac{dy}{du}\,\frac{du}{dx}.$$

Multivariate version ([[d2l-preliminaries]] §Calculus): if $y = f(\mathbf{u})$ with $\mathbf{u} = g(\mathbf{x})$, then

$$\nabla_\mathbf{x} y = \mathbf{A}\,\nabla_\mathbf{u} y,$$

where $\mathbf{A} \in \mathbb{R}^{n\times m}$ is the [[Jacobian]] $\partial\mathbf{u}/\partial\mathbf{x}$. Evaluating gradients of composed functions is therefore a **vector–matrix product** — which is why [[LinearAlgebra]] is structurally inseparable from deep learning.

## Why deep learning depends on it

> "Functions composed from differentiable functions are often themselves differentiable. […] This is one of the key reasons why linear algebra is such an integral building block in building deep learning systems."
> — [[d2l-preliminaries]] §Calculus

A neural network of depth $L$ is exactly a composition $f_L \circ f_{L-1} \circ \cdots \circ f_1$. Gradients of the loss with respect to layer-1 parameters require composing $L$ Jacobians — efficiently done by reverse-mode [[Backpropagation]] over the [[ComputationalGraph]].

## Connections

- [[mml-book]] — §5.1.2 / §5.6 canonical reference.
- [[d2l-preliminaries]] — multivariate version stated explicitly.
- [[derivatives]] / [[PartialDerivative]] / [[Gradient]] / [[Jacobian]] — operands.
- [[Backpropagation]] — algorithmic application across a computational graph.
- [[Autograd]] / [[ComputationalGraph]] — frameworks that automate it.
