---
title: "Lagrangian Duality"
type: concept
tags: [optimization, constrained-optimization, duality, foundational]
sources: [mml-ch07-continuous-optimization, mml-ch12-classification-svm, mml-book]
last_updated: 2026-06-05
---

# Lagrangian Duality

One of the two notions of **[[Duality|duality]]** in [[mml-ch07-continuous-optimization|MML Ch 7]] (the other is [[ConvexConjugate|Legendre–Fenchel duality]], §7.3.3). It converts a constrained **primal** problem in the variables $\mathbf{x}$ into a **dual** problem in the multiplier variables $\boldsymbol\lambda$ ([[mml-ch07-continuous-optimization|MML Ch 7]] §7.2, Def. 7.1).

## Primal and dual problems

Given the [[Lagrangian]] $\mathfrak{L}(\mathbf{x},\boldsymbol\lambda)=f(\mathbf{x})+\boldsymbol\lambda^\top\mathbf{g}(\mathbf{x})$:

- **Primal problem** (Eq. 7.21): $\min_{\mathbf{x}} f(\mathbf{x})$ subject to $g_i(\mathbf{x})\le 0$ — over the *primal variables* $\mathbf{x}$.
- **Dual problem** (Eq. 7.22): $\max_{\boldsymbol\lambda\in\mathbb{R}^m}\mathfrak{D}(\boldsymbol\lambda)$ subject to $\boldsymbol\lambda\ge\mathbf{0}$, where the **dual function** $\mathfrak{D}(\boldsymbol\lambda)=\min_{\mathbf{x}\in\mathbb{R}^d}\mathfrak{L}(\mathbf{x},\boldsymbol\lambda)$.

Convention: **minimize the primal, maximize the dual** ([[mml-ch07-continuous-optimization|MML Ch 7]] margin, p. 239).

## The minimax inequality → weak duality

The **minimax inequality** (Eq. 7.23): for any $\varphi(\mathbf{x},\mathbf{y})$,

$$\max_{\mathbf{y}}\min_{\mathbf{x}}\varphi(\mathbf{x},\mathbf{y})\;\leq\;\min_{\mathbf{x}}\max_{\mathbf{y}}\varphi(\mathbf{x},\mathbf{y})$$

("the maximin is less than the minimax"). Since the primal equals $\min_{\mathbf{x}}\max_{\boldsymbol\lambda\ge0}\mathfrak{L}$ (Eq. 7.26), swapping order gives **[[Duality|weak duality]]** (Eq. 7.27):

$$\underbrace{\min_{\mathbf{x}}\max_{\boldsymbol\lambda\ge0}\mathfrak{L}}_{\text{primal}}\;\geq\;\underbrace{\max_{\boldsymbol\lambda\ge0}\min_{\mathbf{x}}\mathfrak{L}}_{\text{dual}}.$$

**Primal optimal value ≥ dual optimal value, always.** The gap can be positive (a *duality gap*).

## Why the dual is easy

For fixed $\boldsymbol\lambda$, $\min_{\mathbf{x}}\mathfrak{L}$ is *unconstrained*. Because $\mathfrak{L}$ is **affine in $\boldsymbol\lambda$**, $\mathfrak{D}(\boldsymbol\lambda)$ is a pointwise minimum of affine functions — hence **concave** — *even if $f$ and $g_i$ are non-convex*. So the outer maximization is a concave program and can be solved efficiently. When $f,g_i$ are differentiable, derive the dual by $\nabla_{\mathbf{x}}\mathfrak{L}=\mathbf{0}$ and substituting back (worked for LP, Eqs. 7.40–7.43, and QP, Eqs. 7.48–7.52).

## Strong duality

For **[[ConvexOptimization|convex problems]]** (convex $f$, convex feasible set), **[[Duality|strong duality]]** typically holds — the primal and dual optimal values are *equal* (the duality gap is zero), so solving the easier dual recovers the primal solution ([[mml-ch07-continuous-optimization|MML Ch 7]] §7.3, p. 236). This is the engine behind the dual [[SupportVectorMachine|SVM]] (Ch 12).

## From [[mml-ch12-classification-svm|MML Ch 12]] — the dual SVM

[[mml-ch12-classification-svm|MML Ch 12]] §12.3 is the flagship application: "the following subsections are essentially an application of convex duality, which we discussed in Section 7.2" (p. 383). The [[SoftMarginSVM|soft-margin]] primal in $(\mathbf{w},b,\boldsymbol\xi)$ is dualized with multipliers $\alpha_n\ge0$ (classification constraint) and $\gamma_n\ge0$ (slack-nonnegativity); SVM literature uses $\alpha,\gamma$ where Ch 7 used $\lambda$ (margin note, p. 383). The [[Lagrangian]] (Eq. 12.34) → stationarity (Eqs. 12.35–12.37) → substituting $\mathbf{w}=\sum_n\alpha_ny_n\mathbf{x}_n$ back in yields the [[DualSVM|dual SVM]] (Eq. 12.41), an $N$-variable convex [[QuadraticProgramming|QP]]. Because the primal is convex, **strong duality** holds and solving the dual recovers the primal optimum; [[KKTConditions|complementary slackness]] makes most multipliers zero, exposing the [[SupportVector|support vectors]] ($\alpha_n>0$). This is the concrete payoff of the "minimize the primal, maximize the dual" convention recorded above.

## Connections

- [[mml-ch07-continuous-optimization]] — §7.2 canonical reference.
- [[mml-ch12-classification-svm]] — §12.3 the dual-SVM application.
- [[Lagrangian]] — the function $\mathfrak{L}$ this duality is built from.
- [[LagrangeMultipliers]] — the dual variables $\boldsymbol\lambda$ (SVM: $\alpha,\gamma$).
- [[Duality]] — the umbrella concept (weak vs strong; two routes: Lagrangian + Legendre–Fenchel).
- [[ConvexOptimization]] — where strong duality holds.
- [[KKTConditions]] — characterize when primal/dual optima are attained.
- [[ConvexConjugate]] — the alternative (constraint-free) duality, §7.3.3.
- [[SupportVectorMachine]] / [[DualSVM]] / [[SupportVector]] — flagship ML use of Lagrangian duality.
