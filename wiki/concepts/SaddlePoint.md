---
title: "Saddle Point"
type: concept
tags: [optimization, deep-learning, mathematics]
sources: [d2l-optimization]
last_updated: 2026-05-16
---

# Saddle Point

A point where all gradients vanish ($\nabla f = \mathbf{0}$) but which is **neither a local minimum nor a local maximum** — the function increases in some directions and decreases in others. In high dimensions, saddle points are **exponentially more common** than local minima, and they are the dominant stalling pathology for [[GradientDescent|gradient descent]] in deep-learning loss landscapes.

## Definition

Formally, at a saddle point $\mathbf{x}^*$, $\nabla f(\mathbf{x}^*) = \mathbf{0}$ and the [[Hessian]] $\nabla^2 f(\mathbf{x}^*)$ has **eigenvalues of mixed sign** — some positive (corresponding to local minimum directions) and some negative (corresponding to local maximum directions).

## Why they dominate in high dimensions

At any zero-gradient point in $\mathbb{R}^d$, the Hessian has $d$ eigenvalues. The Hessian is a true local minimum iff *all* $d$ eigenvalues are positive. Under reasonable distributions of eigenvalue signs (e.g. each independently positive with probability $\approx 0.5$ in the symmetric-random-matrix regime, [[d2l-optimization]] §saddle-points), the probability of all $d$ being positive shrinks **exponentially** in $d$. For deep nets with $d \sim 10^9$, true local minima are vanishingly rare; saddle points dominate.

> "For high-dimensional problems the likelihood that at least *some* of the eigenvalues are negative is quite high. This makes saddle points more likely than local minima." — [[d2l-optimization]] §optimization-intro

## Canonical example: $f(x, y) = x^2 - y^2$

The origin is a saddle point: a **minimum in $x$** (gradient pushes toward $x=0$ along the $x$-axis) and a **maximum in $y$** (gradient pushes away from $y=0$ along the $y$-axis). The surface resembles a horse saddle — origin of the name.

The 1D example $f(x) = x^3$ has $f'(0) = f''(0) = 0$ — optimization stalls at $x = 0$ even though it is not a minimum.

## Why they stall optimization

[[GradientDescent]] follows $-\nabla f$; at a saddle point the gradient is zero, so the update vanishes. Optimization stalls until **noise** in [[StochasticGradientDescent|SGD]] / [[MinibatchSGD]] perturbs the iterate off the saddle in the negative-eigenvalue direction. This is one of the deep reasons SGD's noise is *productive*: it dislodges parameters from saddles where deterministic GD would freeze.

[[Momentum|Momentum]] also helps escape saddles by accumulating velocity over multiple steps; an iterate with non-zero velocity continues moving even if the instantaneous gradient is zero.

## Connections

- [[d2l-optimization]] — canonical reference (§optimization-intro).
- [[Hessian]] — eigenvalue signs characterize saddle / min / max.
- [[GradientDescent]] — stalls at saddles.
- [[StochasticGradientDescent]] / [[MinibatchSGD]] — noise dislodges from saddles.
- [[Momentum]] — velocity carries iterate through saddles.
- [[VanishingGradient]] — sibling pathology: gradient becomes zero from activation saturation rather than landscape geometry.
- [[Convexity]] — convex functions have no saddle points (Hessian is PSD everywhere).
- [[NewtonsMethod]] — explicitly *attracts* iterates to saddles when the Hessian has negative eigenvalues.
