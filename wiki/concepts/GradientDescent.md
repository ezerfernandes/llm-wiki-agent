---
title: "Gradient Descent"
type: concept
tags: [optimization, deep-learning, foundational]
sources: [mml-ch07-continuous-optimization, mml-book, d2l-linear-regression, d2l-optimization, d2l-appendix-mathematics, mlsysbook-ch05-neural-computation]
last_updated: 2026-06-05
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

## From [[mml-ch07-continuous-optimization|MML Ch 7]]

§7.1 (pp. 227–233) is the canonical treatment. Key points beyond the table above:

- **Steepest descent + orthogonality to contours.** The negative gradient $-((\nabla f)(\mathbf{x}_0))^\top$ is the direction of steepest descent and is *orthogonal to the contour lines* $f(\mathbf{x})=c$. The update $\mathbf{x}_{i+1}=\mathbf{x}_i-\gamma_i((\nabla f)(\mathbf{x}_i))^\top$ (Eq. 7.6) carries an explicit **transpose** because MML uses the **row-vector gradient convention** ([[mml-ch05-vector-calculus|Ch 5]] Eq. 5.40) — DL texts omit it (column-vector convention).
- **Worked 2-D quadratic** (Example 7.1): from $\mathbf{x}_0=[-3,-1]^\top$ with $\gamma=0.085$ the iterates zigzag toward the minimum (Fig. 7.3) — the canonical illustration of GD on a poorly conditioned quadratic.
- **Slow near the minimum** (Remark, p. 229): GD's asymptotic convergence rate is inferior to many methods; on long thin valleys it "zigzags as the gradients point nearly orthogonally to the shortest direction" — i.e. governed by the [[ConditionNumber|condition number]] $\kappa=\sigma_{\max}/\sigma_{\min}$, remediable by a [[Preconditioner|preconditioner]] (§7.1.1 Remark).
- **Adaptive step-size heuristics** (Toussaint 2012): if the function value rose, the step was too large — undo it and shrink $\gamma$ (guarantees monotonic convergence); if it fell, try a larger $\gamma$. See [[LearningRate]].
- **Least-squares as GD** (Example 7.2): minimizing $\|\mathbf{A}\mathbf{x}-\mathbf{b}\|^2$ has gradient $2(\mathbf{A}\mathbf{x}-\mathbf{b})^\top\mathbf{A}$ (Eq. 7.10) — usable in GD, though it has the analytic least-squares solution (forward to Ch 9 / [[LinearRegression]]).

## Connections

- [[mml-ch07-continuous-optimization]] — §7.1 canonical deep dive.
- [[mml-book]] — umbrella source.
- [[Gradient]] — what GD consumes.
- [[Momentum]] — the noise-smoothing extension.
- [[StochasticGradientDescent]] — mini-batch variant.
- [[ConditionNumber]] — controls convergence speed.
- [[Backpropagation]] — how the gradient is computed.
- [[Adam]] — adaptive-step-size variant.
- [[ConvexOptimization]] — when GD reaches the global minimum.
- [[MiniBatchGradientDescent]] — the standard NN training form.
- [[mlsysbook-ch05-neural-computation]] — systems view: GD *applies* the update (not [[Backpropagation|backprop]], which computes the gradient); the optimizer choice sets training-memory overhead — vanilla SGD stores only the gradient, [[Adam]] adds two moment buffers → ~16 bytes/param mixed precision, ~8× the FP16 inference weight. NN loss landscapes are nonconvex; GD finds low-loss regions that generalize, not the global min.
