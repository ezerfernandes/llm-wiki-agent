---
title: "Lagrange Multipliers"
type: concept
tags: [optimization, foundational]
sources: [mml-book]
last_updated: 2026-05-16
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

## Connections

- [[mml-book]] — §7.2 canonical reference.
- [[lagrangetheorem]] — earlier wiki stub on the same topic.
- [[ConvexOptimization]] — guarantees strong duality.
- [[SupportVectorMachine]] — most important ML application.
- [[PrincipalComponentAnalysis]] — eigenvalue derivation route.
