---
title: "Convexity"
type: concept
tags: [optimization, mathematics, foundational]
sources: [d2l-optimization, mml-ch07-continuous-optimization, mml-book]
last_updated: 2026-06-05
---

# Convexity

The structural property of sets and functions that makes optimization tractable: **local minima are global minima**, and a single first-order optimality condition ($\nabla f = 0$) suffices for global optimality. [[ConvexOptimization]] is the algorithmic theory built on this foundation.

## Convex sets

A set $\mathcal{X}$ in a vector space is **convex** if for any $a, b \in \mathcal{X}$ and $\lambda \in [0,1]$:

$$\lambda a + (1-\lambda) b \in \mathcal{X}.$$

The line segment between any two points stays inside the set ([[d2l-optimization]] §convexity).

Properties:

- **Intersections** of convex sets are convex (the line-segment inequality holds in each set, so it holds in the intersection).
- **Unions** in general are *not* convex.
- $\mathbb{R}^d$ and $\ell_p$ balls are convex.

## Convex functions

Given a convex set $\mathcal{X}$, a function $f: \mathcal{X} \to \mathbb{R}$ is **convex** if for all $x, x' \in \mathcal{X}$ and $\lambda \in [0,1]$:

$$\lambda f(x) + (1-\lambda) f(x') \geq f(\lambda x + (1-\lambda) x').$$

The chord lies above the function. Standard examples: $\frac{1}{2}x^2$, $\exp(x)$, $\log\sum_i\exp(x_i)$ (log-sum-exp / softmax normalizer), $\|\mathbf{x}\|_p$ for $p \geq 1$. Nonconvex example: $\cos(\pi x)$.

## Tests for convexity

- **First-order**: $f(\mathbf{y}) \geq f(\mathbf{x}) + \nabla f(\mathbf{x})^\top(\mathbf{y}-\mathbf{x})$ everywhere.
- **Second-order**: the [[Hessian]] is positive semidefinite, $\nabla^2 f \succeq 0$ — equivalent to $\mathbf{x}^\top \mathbf{H} \mathbf{x} \geq 0$ for all $\mathbf{x}$.
- **One-dimensional**: $f'' \geq 0$ everywhere.

## Local minima are global minima

> "For convex functions all local minima are global minima." — [[d2l-optimization]] / [[mml-book]]

Proof by contradiction: if $x^*$ is local and $x'$ has $f(x') < f(x^*)$, the convex combination $\lambda x^* + (1-\lambda) x'$ for $\lambda$ close to 1 lies arbitrarily near $x^*$ but has $f < f(x^*)$, violating local-minimum property.

## [[JensensInequality|Jensen's inequality]]

For a convex $f$ and weights $\alpha_i \geq 0$ with $\sum_i \alpha_i = 1$:

$$\sum_i \alpha_i f(x_i) \geq f\left(\sum_i \alpha_i x_i\right) \quad \textrm{and} \quad E_X[f(X)] \geq f(E_X[X]).$$

The expectation of a convex function is no less than the convex function of an expectation. Used in [[SGD]] convergence analysis ([[d2l-optimization]] §sgd) and variational methods.

## Why convexity matters for deep learning

DL loss landscapes are **almost always nonconvex** — yet convex analysis is the only setting where rigorous convergence proofs exist. The chapter's framing: *"if the algorithm performs poorly even in the convex setting, typically we should not hope to see great results otherwise."* Convex analysis supplies the intuitions ([[Preconditioning|preconditioning]], leaky averaging, [[LineSearch|line search]]) that survive into nonconvex DL.

## From [[mml-ch07-continuous-optimization|MML Ch 7]]

§7.3 (pp. 236–239) defines both halves precisely: a **[[ConvexSet|convex set]]** $\theta x+(1-\theta)y\in\mathcal{C}$ for $\theta\in[0,1]$ (Def. 7.2, Eq. 7.29) and a **[[ConvexFunction|convex function]]** $f(\theta\mathbf{x}+(1-\theta)\mathbf{y})\le\theta f(\mathbf{x})+(1-\theta)f(\mathbf{y})$ (Def. 7.3, Eq. 7.30 — the chord lies above the graph). The **epigraph** ("pour water into the bowl") of a convex function *is* a convex set — the bridge between the two notions, and the basis of the [[ConvexConjugate|Legendre–Fenchel]] description by supporting hyperplanes. Convexity-preserving operations (Example 7.4): nonnegative weighted sums, affine compositions, pointwise max — "again the idea of closure introduced in Ch 2 for vector spaces." MML names Eq. 7.30 **[[JensensInequality|Jensen's inequality]]** (Remark, p. 239) and verifies convexity of the negative entropy $x\log_2 x$ in Example 7.3.

## Connections

- [[d2l-optimization]] — canonical D2L reference (§convexity).
- [[mml-ch07-continuous-optimization]] — MML §7.3 deep dive (Defs. 7.2–7.3, closure, Jensen).
- [[mml-book]] — umbrella source.
- [[ConvexSet]] / [[ConvexFunction]] — the two precise definitions.
- [[ConvexOptimization]] — the algorithmic theory built on convexity.
- [[Hessian]] — second-order convexity test.
- [[JensensInequality]] — a key consequence used in proofs.
- [[SaddlePoint]] — the *opposite* pathology that dominates nonconvex DL.
- [[LagrangeMultipliers]] — constraint handling in the convex setting.
- [[GradientDescent]] / [[StochasticGradientDescent]] — algorithms with convergence proofs *only* on convex objectives.
