---
title: "Newton's Method"
type: concept
tags: [optimization, mathematics]
sources: [d2l-optimization]
last_updated: 2026-05-16
---

# Newton's Method

Second-order optimization method: instead of the first-order Taylor expansion that yields [[GradientDescent]], use the **second-order** expansion to find the minimum of the quadratic approximation in one step.

## Derivation

For $f: \mathbb{R}^d \to \mathbb{R}$:

$$f(\mathbf{x} + \boldsymbol{\epsilon}) \approx f(\mathbf{x}) + \boldsymbol{\epsilon}^\top \nabla f(\mathbf{x}) + \tfrac{1}{2}\boldsymbol{\epsilon}^\top \mathbf{H}\,\boldsymbol{\epsilon},$$

where $\mathbf{H} = \nabla^2 f(\mathbf{x})$ is the [[Hessian]]. Setting the derivative with respect to $\boldsymbol{\epsilon}$ to zero:

$$\nabla f + \mathbf{H}\boldsymbol{\epsilon} = \mathbf{0} \quad\Longrightarrow\quad \boldsymbol{\epsilon} = -\mathbf{H}^{-1}\nabla f.$$

The Newton update is therefore $\mathbf{x} \leftarrow \mathbf{x} - \mathbf{H}^{-1}\nabla f$ ([[d2l-optimization]] §gd-newton).

## The good

- **One-step convergence on quadratics.** For $f(x) = \frac{1}{2}x^2$, the Taylor expansion is exact and $\mathbf{H} = 1$ gives $\epsilon = -x$ — perfect convergence in one step.
- **Quadratic convergence near a strict local minimum.** $|e^{(k+1)}| \leq c\,|e^{(k)}|^2$ — the error squares each iteration once close enough.
- **Curvature-aware.** Steps are short where the function curves rapidly and long where it is flat — automatically handling ill-conditioned objectives.

## The bad

- **Hessian inversion is $\mathcal{O}(d^3)$ work, $\mathcal{O}(d^2)$ storage.** For $d \sim 10^9$ DL parameters, completely infeasible.
- **Fatal flaw on nonconvex problems.** When $\mathbf{H}$ has negative eigenvalues, the Newton update points *toward* a maximum or [[SaddlePoint|saddle point]] rather than a minimum. D2L's worked example $f(x) = x\cos(cx)$ diverges spectacularly.

## Practical fixes (used in DL-adjacent contexts)

1. **Use $|\mathbf{H}|$ instead of $\mathbf{H}$.** Flip negative eigenvalues; preserves descent direction.
2. **Reintroduce a learning rate $\eta < 1$.** Trust the second-order direction but limit step size — D2L shows $\eta = 0.5$ recovers stability on nonconvex problems while preserving the curvature awareness.
3. **[[Preconditioning|Diagonal preconditioning]].** Use only $\textrm{diag}(\mathbf{H})$ — much cheaper and the dominant DL-era compromise. This is the conceptual root of [[Adagrad]] / [[RMSProp]] / [[Adam]], which use gradient magnitudes as a cheaper-still proxy for the diagonal Hessian.
4. **Quasi-Newton (BFGS, L-BFGS).** Maintain a low-rank approximation to $\mathbf{H}^{-1}$ from gradient differences across iterations. L-BFGS is occasionally used for small-scale problems (logistic regression, fine-tuning) but rarely for full DL training.

## Why DL almost never uses Newton's method directly

The combination of $\mathcal{O}(d^2)$ storage, $\mathcal{O}(d^3)$ inversion, sensitivity to nonconvexity, and the fact that one only has *stochastic* (minibatch) gradient estimates anyway — makes Newton's method strictly worse than first-order alternatives in the modern DL regime.

## Connections

- [[d2l-optimization]] — canonical reference (§gd-newton).
- [[GradientDescent]] — first-order counterpart.
- [[Hessian]] — what Newton's method uses (and what makes it expensive).
- [[Preconditioning]] — the diagonal-only DL-friendly approximation.
- [[Adagrad]] / [[RMSProp]] / [[Adam]] — algorithms that use gradient magnitudes as a Hessian-diagonal proxy.
- [[ConvexOptimization]] — where Newton's method's quadratic convergence is guaranteed.
- [[SaddlePoint]] — the failure mode Newton's method does not handle.
