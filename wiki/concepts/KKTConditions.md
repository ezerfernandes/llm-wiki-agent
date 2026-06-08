---
title: "KKT Conditions"
type: concept
tags: [optimization, constrained-optimization, duality, foundational]
sources: [mml-ch07-continuous-optimization, mml-ch12-classification-svm, mml-book]
last_updated: 2026-06-05
---

# KKT Conditions (Karush–Kuhn–Tucker)

The first-order **necessary conditions for optimality** of a constrained problem $\min_{\mathbf{x}} f(\mathbf{x})$ subject to $g_i(\mathbf{x})\le0$ and $h_j(\mathbf{x})=0$ ([[mml-ch07-continuous-optimization|MML Ch 7]] §7.2; full treatment Boyd & Vandenberghe 2004, ch. 4). They are the conditions a candidate $(\mathbf{x}^*,\boldsymbol\lambda^*,\boldsymbol\nu^*)$ must satisfy on the [[Lagrangian]] $\mathfrak{L}=f+\sum_i\lambda_i g_i+\sum_j\nu_j h_j$:

1. **Stationarity** — $\nabla_{\mathbf{x}}\mathfrak{L}(\mathbf{x}^*,\boldsymbol\lambda^*,\boldsymbol\nu^*)=\mathbf{0}$. The objective gradient is a combination of constraint gradients.
2. **Primal feasibility** — $g_i(\mathbf{x}^*)\le0$ and $h_j(\mathbf{x}^*)=0$.
3. **Dual feasibility** — $\lambda_i\ge0$ for the inequality multipliers ($\nu_j\in\mathbb{R}$ free for equalities, per [[mml-ch07-continuous-optimization|MML Ch 7]] Eq. 7.28 Remark).
4. **Complementary slackness** — $\lambda_i\,g_i(\mathbf{x}^*)=0$ for every $i$.

## Complementary slackness, intuitively

For each inequality constraint, *either* the constraint is **active** ($g_i(\mathbf{x}^*)=0$, the optimum sits on its boundary) *or* its multiplier vanishes ($\lambda_i=0$, the constraint is **inactive / slack** and exerts no force). Both cannot be "on" at once. This is precisely what identifies the **support vectors** in the dual [[SupportVectorMachine|SVM]]: only training points with $\lambda_n>0$ (active margin constraints) matter.

## Geometric reading

At the optimum the negative objective gradient $-\nabla f$ is a non-negative combination of the active constraint gradients — you cannot decrease $f$ without violating a constraint ([[LagrangeMultipliers]] geometry).

## Sufficiency

For **[[ConvexOptimization|convex problems]]** (convex $f,g_i$; affine $h_j$) satisfying a constraint qualification (e.g. Slater's condition), the KKT conditions are also **sufficient** for global optimality, and primal/dual optima coincide ([[Duality|strong duality]]).

## From [[mml-ch12-classification-svm|MML Ch 12]] — complementary slackness ⇒ support vectors

[[mml-ch12-classification-svm|MML Ch 12]] §12.3 is the canonical worked example of complementary slackness. After dualizing the [[SoftMarginSVM|soft-margin SVM]], the multiplier $\alpha_n$ on each example's margin constraint is positive **iff that constraint is active** — i.e. iff $\mathbf{x}_n$ lies on (or violates) its margin boundary. Examples with $\alpha_n=0$ "do not contribute to the solution $\mathbf{w}$ at all"; those with $\alpha_n>0$ are the [[SupportVector|support vectors]] that "support the hyperplane" (§12.3.1 Remark, p. 384). The box constraint $0\le\alpha_n\le C$ refines this into three KKT regimes: $\alpha_n=0$ (interior, ignored), $0<\alpha_n<C$ (exactly on the margin — used to recover $b^*=y_n-\langle\mathbf{w}^*,\mathbf{x}_n\rangle$, Eq. 12.42), $\alpha_n=C$ (inside the margin or misclassified, $\xi_n>0$). The margin note on p. 385 attributes the "$0<\alpha_n<C$ ⇒ on the margin" fact directly to the KKT conditions (Schölkopf & Smola 2002).

## Connections

- [[mml-ch07-continuous-optimization]] — §7.2 reference (Lagrangian + dual feasibility).
- [[mml-ch12-classification-svm]] — §12.3 the support-vector application.
- [[Lagrangian]] — the function the conditions are stated on.
- [[LagrangeMultipliers]] — the multipliers $\boldsymbol\lambda,\boldsymbol\nu$ and geometric picture.
- [[LagrangianDuality]] / [[Duality]] — KKT links primal and dual optima.
- [[ConvexOptimization]] — where KKT becomes sufficient.
- [[SupportVectorMachine]] / [[DualSVM]] / [[SupportVector]] — complementary slackness ⇒ support vectors.
