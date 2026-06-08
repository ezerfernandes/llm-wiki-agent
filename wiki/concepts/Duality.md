---
title: "Duality"
type: concept
tags: [optimization, duality, constrained-optimization, convex-optimization, foundational]
sources: [mml-ch07-continuous-optimization, mml-ch12-classification-svm, mml-book]
last_updated: 2026-06-05
---

# Duality

> "Duality in optimization is the idea of converting an optimization problem in one set of variables $\mathbf{x}$ (called the primal variables), into another optimization problem in a different set of variables $\boldsymbol\lambda$ (called the dual variables)." — [[mml-ch07-continuous-optimization|MML Ch 7]] §7.2, p. 234

[[mml-ch07-continuous-optimization|MML Ch 7]] introduces **two distinct dualities**:

1. **[[LagrangianDuality|Lagrangian duality]]** (§7.2) — builds the dual from the [[Lagrangian]] $\mathfrak{L}(\mathbf{x},\boldsymbol\lambda)$ of a *constrained* problem. Primal $\min_{\mathbf{x}}\max_{\boldsymbol\lambda\ge0}\mathfrak{L}$ vs dual $\max_{\boldsymbol\lambda\ge0}\min_{\mathbf{x}}\mathfrak{L}$.
2. **[[ConvexConjugate|Legendre–Fenchel duality]]** (§7.3.3) — builds a dual *without constraints*, via the convex conjugate $f^*(\mathbf{s})=\sup_{\mathbf{x}}(\langle\mathbf{s},\mathbf{x}\rangle-f(\mathbf{x}))$, describing a convex function by its tangent slopes.

For convex problems both routes yield matching primal/dual solutions (Example 7.9, Eq. 7.68 derives one via the other).

## Weak duality

From the **minimax inequality** $\max_{\mathbf{y}}\min_{\mathbf{x}}\varphi\le\min_{\mathbf{x}}\max_{\mathbf{y}}\varphi$ ([[mml-ch07-continuous-optimization|MML Ch 7]] Eq. 7.23), swapping min/max can only *shrink* the value. Applied to the Lagrangian (Eq. 7.27):

$$\underbrace{\min_{\mathbf{x}}\max_{\boldsymbol\lambda\ge0}\mathfrak{L}}_{\text{primal value }p^*}\;\geq\;\underbrace{\max_{\boldsymbol\lambda\ge0}\min_{\mathbf{x}}\mathfrak{L}}_{\text{dual value }d^*}.$$

**Weak duality: $p^*\ge d^*$ always** — the dual lower-bounds the primal. The difference $p^*-d^*\ge0$ is the **duality gap**. Weak duality holds even for *non-convex* problems, and since the dual is always a concave maximization, it gives a cheaply computable lower bound on any minimization.

## Strong duality

> "When $f(\cdot)$ is a convex function, and when the constraints involving $g(\cdot)$ and $h(\cdot)$ are convex sets … we have strong duality: The optimal solution of the dual problem is the same as the optimal solution of the primal problem." — [[mml-ch07-continuous-optimization|MML Ch 7]] §7.3, p. 236

**Strong duality: $p^*=d^*$** (zero duality gap). It is the defining payoff of [[ConvexOptimization|convex optimization]]: solve the easier dual and you have solved the primal. (Sufficient regularity such as Slater's condition is assumed.) This is exactly why the dual [[SupportVectorMachine|SVM]] (Ch 12) is solved instead of the primal.

## From [[mml-ch12-classification-svm|MML Ch 12]] — strong duality realized in the SVM

[[mml-ch12-classification-svm|MML Ch 12]] §12.3 is where the strong-duality promise pays off concretely: the [[SoftMarginSVM|soft-margin SVM]] primal is convex, so its [[DualSVM|dual]] (Eq. 12.41) attains the *same* optimum — solving the easier $N$-variable dual recovers the primal weight via $\mathbf{w}=\sum_n\alpha_ny_n\mathbf{x}_n$. §12.3.2 adds a *third* reading (neither Lagrangian nor Legendre–Fenchel): the dual as finding the closest points of the two class [[ConvexHull|convex hulls]] (Bennett & Bredensteiner 2000) — a reminder that "dual" descriptions of the same problem can be geometric as well as algebraic.

## Connections

- [[mml-ch07-continuous-optimization]] — §7.2 (Lagrangian) + §7.3.3 (Legendre–Fenchel) canonical reference.
- [[mml-ch12-classification-svm]] — §12.3 strong duality realized.
- [[LagrangianDuality]] — the constrained-problem route.
- [[ConvexConjugate]] / [[LegendreFenchelTransform]] — the constraint-free route.
- [[Lagrangian]] — the function underlying Lagrangian duality.
- [[ConvexOptimization]] — where weak duality strengthens to strong duality.
- [[KKTConditions]] — optimality conditions linking primal and dual optima.
- [[SupportVectorMachine]] / [[DualSVM]] — the flagship ML application of strong duality.
