---
title: "Convex Optimization"
type: concept
tags: [optimization, foundational]
sources: [mml-book, d2l-optimization]
last_updated: 2026-05-16
---

# Convex Optimization

Optimization problems of the form $\min f(\mathbf{x})$ subject to constraints, where $f$ is a **convex** function and the feasible set is a **convex** set ([[mml-book]] §7.3).

## Why convexity matters

> "*For convex functions all local minima are global minimum.*" — [[mml-book]] p. 227 marginal note.

This single property eliminates the local-minimum trap that plagues general nonlinear optimization. The first-order condition $\nabla f(\mathbf{x}^*) = \mathbf{0}$ is *both* necessary *and* sufficient for global optimality.

## Standard tests for convexity

- **First-order**: $f$ is convex iff $f(\mathbf{y})\geq f(\mathbf{x}) + \nabla f(\mathbf{x})^\top(\mathbf{y}-\mathbf{x})$ for all $\mathbf{x}, \mathbf{y}$.
- **Second-order**: $f$ is convex iff its [[Hessian]] is positive semidefinite ($\nabla^2 f(\mathbf{x})\succeq 0$) everywhere.
- **Composition rules**: sums of convex functions are convex; affine compositions $f(\mathbf{A}\mathbf{x}+\mathbf{b})$ preserve convexity; pointwise max of convex functions is convex.

## Standard convex ML problems

- **Linear / ridge regression** ([[mml-book]] Ch 9): quadratic objective ⇒ Hessian = $\mathbf{X}^\top\mathbf{X}\succeq 0$ ⇒ convex.
- **Logistic regression**: NLL is convex in the weights.
- **SVM** ([[mml-book]] Ch 12): hard-margin / soft-margin objectives are convex quadratic programs.
- **Lasso / $\ell_1$-regularized regression**: convex (though non-smooth).
- **Linear programming** and **quadratic programming**: convex problem classes that admit interior-point and simplex algorithms.

## Where deep learning departs

Neural-network training is **non-convex** — the standard gradient-descent guarantees no longer apply. Empirically, the loss landscape of overparameterized networks has many near-equivalent global minima (and the *bad* local minima predicted by classical theory turn out to be rare in practice); this is part of why scaling laws hold cleanly.

## Duality

[[mml-book]] §7.3.3: for convex problems, **strong duality** typically holds (Slater's condition: the constraint set has a strict interior). The dual problem is often easier than the primal — this is the route to the dual SVM in Ch 12.3.

## Connections

- [[mml-book]] — §7.3 canonical reference.
- [[LagrangeMultipliers]] — constraint handling.
- [[Hessian]] — second-order convexity test.
- [[SupportVectorMachine]] — convex QP example.
- [[LinearRegression]] — convex quadratic example.
- [[GradientDescent]] — globally optimal on convex problems.
