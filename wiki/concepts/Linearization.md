---
title: "Linearization"
type: concept
tags: [vector-calculus, approximation, foundational]
sources: [mml-ch05-vector-calculus, mml-book]
last_updated: 2026-06-04
---

# Linearization

First-order [[TaylorSeries]] approximation $f(\mathbf{x}+\boldsymbol\delta)\approx f(\mathbf{x})+\nabla f(\mathbf{x})\boldsymbol\delta$ of a function near $\mathbf{x}$. [[mml-book]] §5.8.

## From [[mml-ch05-vector-calculus|MML Ch 5]]

§5.8 (Eq. 5.148) writes the linearization of $f$ around $\mathbf{x}_0$ as

$$f(\mathbf{x}) \approx f(\mathbf{x}_0) + (\nabla_\mathbf{x} f)(\mathbf{x}_0)(\mathbf{x}-\mathbf{x}_0),$$

approximating $f$ by a straight line / tangent hyperplane through $\mathbf{x}_0$ (Fig. 5.12 linearizes a curve at $x_0=-2$). It is the **degree-1 [[TaylorPolynomial|Taylor polynomial]]** — keeping only the first two terms of the multivariate Taylor series (Def 5.7). MML: *"This approximation is locally accurate, but the farther we move away from $\mathbf{x}_0$ the worse the approximation gets."*

### Where it is used (§5.9)

Linearization is how nonlinear functions are made tractable inside otherwise-intractable expectations $\mathbb{E}_\mathbf{x}[f(\mathbf{x})]=\int f(\mathbf{x})p(\mathbf{x})\,\mathrm{d}\mathbf{x}$ (Eq. 5.181): a first-order Taylor expansion of $f$ around $\boldsymbol\mu$ linearizes it, and for a Gaussian $p$ the mean and covariance of a *linear* $f$ are then exact (§6.5). This underlies the **extended Kalman filter** (Maybeck 1979) for online state estimation in nonlinear dynamical systems. The second-order analogue — keeping the [[Hessian]] term — is the [[LaplaceApproximation|Laplace approximation]]. (A gradient-free alternative is the *unscented transform*, Julier & Uhlmann 1997.)

## Connections

- [[mml-ch05-vector-calculus|MML Ch 5]] — §5.8 Eq. 5.148 canonical reference.
- [[TaylorSeries]] / [[TaylorPolynomial]] — the degree-1 truncation.
- [[Gradient]] / [[Jacobian]] — the first-order coefficient.
- [[Hessian]] — the next term up (second-order).
- [[LaplaceApproximation]] — the second-order density approximation.
