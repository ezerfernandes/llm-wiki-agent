---
title: "Lagrangian"
type: concept
tags: [optimization, constrained-optimization, duality, foundational]
sources: [mml-ch07-continuous-optimization, mml-book]
last_updated: 2026-06-05
---

# Lagrangian

The scalar function that turns a **constrained** minimization into something tractable by **relaxing the constraints into a linear penalty** ([[mml-ch07-continuous-optimization|MML Ch 7]] §7.2, Eq. 7.20). For the problem $\min_{\mathbf{x}} f(\mathbf{x})$ subject to $g_i(\mathbf{x})\le 0$ ($i=1,\dots,m$), introduce non-negative **[[LagrangeMultipliers|Lagrange multipliers]]** $\lambda_i\ge 0$ and define

$$\mathfrak{L}(\mathbf{x},\boldsymbol\lambda)=f(\mathbf{x})+\sum_{i=1}^m\lambda_i\,g_i(\mathbf{x})=f(\mathbf{x})+\boldsymbol\lambda^\top\mathbf{g}(\mathbf{x}),$$

stacking the constraints into $\mathbf{g}(\mathbf{x})$ and the multipliers into $\boldsymbol\lambda\in\mathbb{R}^m$.

## Why it works

The naive way to enforce constraints is an **indicator penalty** $J(\mathbf{x})=f(\mathbf{x})+\sum_i\mathbf{1}(g_i(\mathbf{x}))$ with $\mathbf{1}(z)=0$ for $z\le0$ and $\infty$ otherwise ([[mml-ch07-continuous-optimization|MML Ch 7]] Eqs. 7.18–7.19). That infinite step is as hard to optimize as the original problem. The Lagrangian **replaces the step function with a linear function** $\lambda_i g_i(\mathbf{x})$ — for $\boldsymbol\lambda\ge\mathbf{0}$ it is a *lower bound* on $J(\mathbf{x})$, and $J(\mathbf{x})=\max_{\boldsymbol\lambda\ge\mathbf{0}}\mathfrak{L}(\mathbf{x},\boldsymbol\lambda)$ (Eq. 7.25).

## Two key structural facts

- $\mathfrak{L}$ is **affine in $\boldsymbol\lambda$** (Eq. 7.20b). Hence the dual function $\mathfrak{D}(\boldsymbol\lambda)=\min_{\mathbf{x}}\mathfrak{L}(\mathbf{x},\boldsymbol\lambda)$ — a pointwise minimum of affine functions — is **concave** even when $f,g_i$ are non-convex.
- For fixed $\boldsymbol\lambda$, $\min_{\mathbf{x}}\mathfrak{L}$ is an **unconstrained** problem — solvable by setting $\nabla_{\mathbf{x}}\mathfrak{L}=\mathbf{0}$ when $f,g_i$ are differentiable.

## Equality constraints

Add $h_j(\mathbf{x})=0$ by modeling each as $h_j\le0$ and $h_j\ge0$; the resulting multipliers come out **unconstrained** ([[mml-ch07-continuous-optimization|MML Ch 7]] Eqs. 7.28, Remark p. 235–236). Rule: **non-negative multipliers for inequalities, free $\mathbb{R}$ multipliers for equalities**. The fuller form $\mathfrak{L}=f+\sum_i\lambda_i g_i+\sum_j\nu_j h_j$ appears on [[LagrangeMultipliers]].

## Notation quirk

MML Ch 7 writes the Lagrangian as fraktur $\mathfrak{L}$ and the dual function as $\mathfrak{D}$; most other references (and [[LagrangeMultipliers]] / the Ch 12 [[SupportVectorMachine|SVM]] derivation) use $\mathcal{L}$. Same object.

## Connections

- [[mml-ch07-continuous-optimization]] — §7.2 canonical reference.
- [[LagrangeMultipliers]] — the multipliers $\boldsymbol\lambda$ and the KKT/geometry view.
- [[LagrangianDuality]] — the primal/dual problem built from $\mathfrak{L}$.
- [[KKTConditions]] — optimality conditions on $\mathfrak{L}$ at the optimum.
- [[Duality]] — the umbrella idea (primal ↔ dual variables).
- [[ConvexConjugate]] — the *other* duality (Legendre–Fenchel) introduced in §7.3.3.
- [[LinearProgramming]] / [[QuadraticProgramming]] — Lagrangians derived explicitly (Eqs. 7.40, 7.48).
- [[SupportVectorMachine]] — the dual SVM is a Lagrangian-duality construction.
</content>
