---
title: "Lagrange Multipliers"
type: concept
tags: [optimization, constrained-optimization, foundational]
sources: [mml-ch07-continuous-optimization, mml-book]
last_updated: 2026-06-05
---

# Lagrange Multipliers

The standard technique for **constrained optimization** ([[mml-book]] §7.2). To minimize $f(\mathbf{x})$ subject to $g_i(\mathbf{x})\leq 0$ and $h_j(\mathbf{x})=0$, form the **Lagrangian**

$$\mathcal{L}(\mathbf{x},\boldsymbol\lambda,\boldsymbol\nu) = f(\mathbf{x}) + \sum_i \lambda_i\,g_i(\mathbf{x}) + \sum_j \nu_j\,h_j(\mathbf{x})$$

with **Lagrange multipliers** $\lambda_i\geq 0$ (inequality) and $\nu_j\in\mathbb{R}$ (equality). The Karush-Kuhn-Tucker (KKT) conditions at the optimum are:

1. **Stationarity**: $\nabla_\mathbf{x}\mathcal{L} = \mathbf{0}$.
2. **Primal feasibility**: $g_i(\mathbf{x}^*)\leq 0$, $h_j(\mathbf{x}^*)=0$.
3. **Dual feasibility**: $\lambda_i\geq 0$.
4. **Complementary slackness**: $\lambda_i\,g_i(\mathbf{x}^*) = 0$ — either the constraint is active ($g_i=0$) or its multiplier vanishes.

## Geometric reading

At the optimum, the negative gradient $-\nabla f$ is a non-negative combination of constraint gradients $\nabla g_i, \nabla h_j$ — the objective can't decrease without violating a constraint.

## ML uses

- **[[SupportVectorMachine|SVM]]** ([[mml-book]] §12.3): the dual SVM formulation comes from applying Lagrange multipliers to the hard-margin / soft-margin primal — and the multipliers $\alpha_n$ identify the *support vectors* (those with $\alpha_n>0$).
- **[[PrincipalComponentAnalysis|PCA]]** ([[mml-book]] §10.2.1): maximizing variance subject to $\|\mathbf{b}_1\|=1$ is a constrained problem; the Lagrange-multiplier $\lambda_1$ turns out to be the eigenvalue, giving PCA's eigenvalue-equation derivation.
- **[[GaussianMixtureModel|GMM]] mixture-weight updates** ([[mml-book]] §11.2): maximizing the log-likelihood subject to $\sum_k\pi_k=1$ uses a Lagrange multiplier.
- **Information-theoretic objectives** (Lagrangians for constrained entropy / KL minimization).

## Connection to duality

When the primal problem is convex, *strong duality* holds: the optimal primal value equals the optimal dual value (Slater's condition). The dual problem $\max_{\boldsymbol\lambda\geq 0,\boldsymbol\nu}\min_\mathbf{x}\mathcal{L}$ is often easier than the primal — this is the basis of the dual SVM formulation.

## From [[mml-ch07-continuous-optimization|MML Ch 7]]

§7.2 (pp. 233–236) is the canonical derivation. The motivation is concrete: the naive way to enforce $g_i(\mathbf{x})\le0$ is an **indicator penalty** $J(\mathbf{x})=f(\mathbf{x})+\sum_i\mathbf{1}(g_i(\mathbf{x}))$ with $\mathbf{1}(z)=0$ for $z\le0$ else $\infty$ (Eqs. 7.18–7.19) — "equally difficult to optimize." Lagrange multipliers **replace that step function with a linear function** $\lambda_i g_i$, giving the [[Lagrangian]] $\mathfrak{L}=f+\boldsymbol\lambda^\top\mathbf{g}$ (Eq. 7.20). The chapter then builds **[[LagrangianDuality|Lagrangian duality]]**: primal $\min_{\mathbf{x}}\max_{\boldsymbol\lambda\ge0}\mathfrak{L}$ (Eq. 7.26) vs dual $\max_{\boldsymbol\lambda\ge0}\min_{\mathbf{x}}\mathfrak{L}$, related by the minimax inequality (Eq. 7.23) and **weak duality** $p^*\ge d^*$ (Eq. 7.27). For **equality** constraints, modeling $h_j=0$ as $h_j\le0\wedge h_j\ge0$ shows their multipliers are **unconstrained** — hence the rule used by the [[KKTConditions|KKT conditions]]: non-negative multipliers for inequalities, free $\mathbb{R}$ multipliers for equalities (Eq. 7.28, Remark). The four KKT conditions listed above are the standard optimality conditions for this setup.

> Notation: MML §7.2 writes the Lagrangian as fraktur $\mathfrak{L}$ and the dual function as $\mathfrak{D}$, with $\boldsymbol\lambda\in\mathbb{R}^m$ for inequalities; this page uses $\mathcal{L}$ and splits $\lambda_i,\nu_j$ to match the Ch 12 SVM derivation. Same math.

## Connections

- [[mml-ch07-continuous-optimization]] — §7.2 canonical deep dive.
- [[mml-book]] — umbrella source.
- [[Lagrangian]] — the function $\mathfrak{L}$ built from the multipliers.
- [[LagrangianDuality]] / [[Duality]] — primal/dual construction.
- [[KKTConditions]] — the optimality conditions.
- [[lagrangetheorem]] — earlier wiki stub on the same topic.
- [[ConvexOptimization]] — guarantees strong duality.
- [[SupportVectorMachine]] — most important ML application.
- [[PrincipalComponentAnalysis]] — eigenvalue derivation route.
