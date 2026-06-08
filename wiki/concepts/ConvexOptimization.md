---
title: "Convex Optimization"
type: concept
tags: [optimization, convex-optimization, foundational]
sources: [mml-ch07-continuous-optimization, mml-ch12-classification-svm, mml-book, d2l-optimization]
last_updated: 2026-06-05
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

## From [[mml-ch07-continuous-optimization|MML Ch 7]]

§7.3 (pp. 236–246) gives the formal definition (Eq. 7.38): $\min_{\mathbf{x}} f(\mathbf{x})$ s.t. $g_i(\mathbf{x})\le0$, $h_j(\mathbf{x})=0$, where all $f,g_i$ are **[[ConvexFunction|convex functions]]** and all $h_j=0$ define **[[ConvexSet|convex sets]]**. The defining payoff: *"In this setting, we have **strong duality**: the optimal solution of the dual problem is the same as the optimal solution of the primal problem"* (p. 236) — contrast §7.2 where only weak duality is guaranteed. The chapter develops:

- **[[ConvexSet|Convex sets]]** (Def. 7.2): $\theta x+(1-\theta)y\in\mathcal{C}$ — the chord stays inside.
- **[[ConvexFunction|Convex functions]]** (Def. 7.3): the chord lies above the graph; tests via first-order tangent-below or [[Hessian]] $\succeq0$ (Eq. 7.31); the defining inequality is **[[JensensInequality|Jensen's inequality]]**.
- Two well-understood sub-classes: **[[LinearProgramming|linear programming]]** (§7.3.1, all-linear) and **[[QuadraticProgramming|quadratic programming]]** (§7.3.2, convex-quadratic objective + affine constraints — the [[SupportVectorMachine|SVM]] of Ch 12).
- A second duality, the **[[ConvexConjugate|Legendre–Fenchel transform]]** (§7.3.3), which derives duals without constraints; Example 7.9 (Eq. 7.68) shows it agrees with the Lagrangian dual under strong duality.

## From [[mml-ch12-classification-svm|MML Ch 12]] — the SVM as the worked convex program

[[mml-ch12-classification-svm|MML Ch 12]] is the chapter that *exercises* this theory. The [[SupportVectorMachine|SVM]] is deliberately chosen as a four-pillar example because, unlike [[LinearRegression|linear regression]] (Ch 9, closed form), its optimization "does not admit an analytic solution so that we need to resort to a variety of optimization tools introduced in Chapter 7" (§12, p. 371). The [[HardMarginSVM|hard-margin]] and [[SoftMarginSVM|soft-margin]] SVMs are convex [[QuadraticProgramming|quadratic programs]]; convexity gives the unique global optimum and licenses solving the easier [[DualSVM|dual]] (via [[Duality|strong duality]] + [[KKTConditions|KKT]]); the non-smooth [[HingeLoss|hinge-loss]] reformulation is still convex and solved by subgradient/[[StochasticGradientDescent|SGD]] (§12.5). It is the textbook's clearest end-to-end demonstration that "geometric ML design" reduces to convex optimization.

## Connections

- [[mml-ch07-continuous-optimization]] — §7.3 canonical deep dive.
- [[mml-ch12-classification-svm]] — §12 the worked convex-program example (SVM).
- [[mml-book]] — umbrella source.
- [[ConvexSet]] / [[ConvexFunction]] / [[JensensInequality]] — the building blocks.
- [[LinearProgramming]] / [[QuadraticProgramming]] — the two sub-classes.
- [[ConvexConjugate]] / [[Duality]] — Legendre–Fenchel + strong duality.
- [[LagrangeMultipliers]] — constraint handling.
- [[Hessian]] — second-order convexity test.
- [[SupportVectorMachine]] — convex QP example.
- [[LinearRegression]] — convex quadratic example.
- [[GradientDescent]] — globally optimal on convex problems.
