---
title: "Calculus"
type: concept
tags: [math, vector-calculus, foundational]
sources: [d2l-preliminaries, mml-book]
last_updated: 2026-05-16
---

# Calculus

The branch of mathematics concerned with continuous change. ML uses **differential calculus** (how to *change* function inputs to *change* outputs — gradients, optimization) far more than **integral calculus** (accumulation — expectations, marginalization).

## Why ML cares

[[d2l-preliminaries]] §Calculus opens with the punchline:

> "*Differential calculus* […] can tell us how to increase or decrease a function's value by manipulating its arguments. This comes in handy for the *optimization problems* that we face in deep learning, where we repeatedly update our parameters in order to decrease the loss function."

Every parameter update in a neural network is a step taken using the [[Gradient|gradient]] — which is itself a calculus object computed by [[Autograd|automatic differentiation]] applying the [[ChainRule|chain rule]] backwards through a [[ComputationalGraph|computational graph]].

## Minimum viable calculus

| Concept | What it gives you | Wiki page |
|---|---|---|
| **Derivative** $f'(x) = \lim_{h\to 0}(f(x+h)-f(x))/h$ | Slope; instantaneous rate of change | [[derivatives]] |
| **Differentiation rules** | Constant, power $\frac{d}{dx}x^n=nx^{n-1}$, $e^x$, $\ln x$, sum, product, quotient, constant-multiple | [[derivatives]] |
| **Partial derivative** $\partial f/\partial x_i$ | Slope along one axis when others held fixed | [[PartialDerivative]] |
| **Gradient** $\nabla_\mathbf{x} f$ | Vector of all partials; direction of steepest ascent | [[Gradient]] |
| **Jacobian** $\partial \mathbf{f}/\partial \mathbf{x}$ | Matrix of partials for vector-output $\mathbf{f}$ | [[Jacobian]] |
| **Hessian** $\partial^2 f/\partial x_i\partial x_j$ | Matrix of second partials; curvature; convexity test | [[Hessian]] |
| **Chain rule** $(g\circ f)' = g'(f)\,f'$ | Composition; basis of [[Backpropagation|backprop]] | [[ChainRule]] |
| **Taylor expansion** $f(\mathbf{x}+\boldsymbol\delta) \approx f(\mathbf{x}) + \nabla f(\mathbf{x})^\top\boldsymbol\delta$ | Local linearization | — |

## ML uses

- **[[GradientDescent]]**: parameter update $\boldsymbol\theta \leftarrow \boldsymbol\theta - \eta\nabla_{\boldsymbol\theta}\mathcal{L}$ is pure calculus.
- **[[Backpropagation]]**: iterated chain rule on a computational graph.
- **Newton-style optimization**: uses the [[Hessian]] for second-order curvature.
- **Differentiable surrogate losses**: accuracy / AUC aren't differentiable, so we optimize a smooth surrogate (cross-entropy, hinge) and pray correlations hold.
- **Normalizing flows**: log-determinant of the Jacobian for change-of-variables in densities.

## Connections

- [[d2l-preliminaries]] — minimum viable calculus for deep learning.
- [[mml-book]] — Ch 5 canonical reference for ML-flavored vector calculus.
- [[derivatives]] / [[PartialDerivative]] / [[Gradient]] / [[Jacobian]] / [[Hessian]] / [[ChainRule]] — the operators.
- [[VectorCalculus]] — multivariate extension.
- [[Autograd]] / [[Backpropagation]] — algorithmic consumers.
- [[GradientDescent]] / [[Adam]] — optimization consumers.
