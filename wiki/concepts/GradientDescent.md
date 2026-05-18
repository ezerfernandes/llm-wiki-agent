---
title: "Gradient Descent"
type: concept
tags: [optimization, deep-learning, foundational]
sources: [mml-book, d2l-linear-regression, d2l-optimization, d2l-appendix-mathematics]
last_updated: 2026-05-16
---

# Gradient Descent

The first-order optimization procedure that iteratively steps parameters in the **negative** [[Gradient]] direction scaled by a [[LearningRate|step-size]] $\gamma$ ([[mml-book]] §7.1):

$$\mathbf{x}_{i+1} = \mathbf{x}_i - \gamma_i\,(\nabla f(\mathbf{x}_i))^\top.$$

The negative gradient points in the direction of *steepest descent*; for a sufficiently small step-size the function value decreases monotonically.

## Three key variants

| Variant | Update | Best for |
|---|---|---|
| Batch GD ([[mml-book]] §7.1) | full-data gradient | small datasets, convex problems |
| GD with momentum (§7.1.2) | $\boldsymbol\Delta\mathbf{x}_i = \alpha\boldsymbol\Delta\mathbf{x}_{i-1} - \gamma(\nabla f)^\top$ | poorly-conditioned objectives, "heavy-ball" averaging |
| Stochastic GD (§7.1.3) | gradient of *one* (or a mini-batch) loss term | large datasets, ML at scale |

## Convergence depends on the condition number

[[mml-book]] §7.1.1 Remark: convergence speed depends on $\kappa = \sigma_{\max}(\mathbf{A})/\sigma_{\min}(\mathbf{A})$ — the [[ConditionNumber]] of the Hessian. Ill-conditioned problems "zigzag" (Fig 7.3). Preconditioners $\mathbf{P}^{-1}$ solve $\mathbf{P}^{-1}(\mathbf{A}\mathbf{x}-\mathbf{b})=\mathbf{0}$ to lower the effective condition number.

## Connections

- [[mml-book]] — §7.1 canonical reference.
- [[Gradient]] — what GD consumes.
- [[Momentum]] — the noise-smoothing extension.
- [[StochasticGradientDescent]] — mini-batch variant.
- [[ConditionNumber]] — controls convergence speed.
- [[Backpropagation]] — how the gradient is computed.
- [[Adam]] — adaptive-step-size variant.
- [[ConvexOptimization]] — when GD reaches the global minimum.
