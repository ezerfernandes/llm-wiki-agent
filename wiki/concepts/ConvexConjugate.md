---
title: "Convex Conjugate (Legendre–Fenchel Transform)"
type: concept
tags: [optimization, convex-optimization, duality, legendre-fenchel, foundational]
sources: [mml-ch07-continuous-optimization, mml-book]
last_updated: 2026-06-05
---

# Convex Conjugate / Legendre–Fenchel Transform

A second, **constraint-free** notion of [[Duality|duality]] ([[mml-ch07-continuous-optimization|MML Ch 7]] §7.3.3, distinct from the [[LagrangianDuality|Lagrangian duality]] of §7.2). It describes a [[ConvexFunction|convex function]] by a function of its **gradient/tangent slopes** rather than its values.

## Definition (Def. 7.4, Eq. 7.53)

The **convex conjugate** of $f:\mathbb{R}^D\to\mathbb{R}$ is

$$f^*(\mathbf{s})=\sup_{\mathbf{x}\in\mathbb{R}^D}\big(\langle\mathbf{s},\mathbf{x}\rangle-f(\mathbf{x})\big).$$

The transform from $f(\cdot)$ to $f^*(\cdot)$ is the **Legendre–Fenchel transform** (also called the convex conjugate; Hiriart-Urruty & Lemaréchal 2001). Note: it is a transform of the *function* $f$, depending on the tangent slopes $\mathbf{s}(\mathbf{x})=\nabla_{\mathbf{x}}f(\mathbf{x})$ — **not** of $\mathbf{x}$ or of $f$ evaluated at a point. The definition needs **neither convexity nor differentiability** of $f$.

## Geometric intuition (Eqs. 7.54–7.58)

A [[ConvexSet|convex set]] is equivalently described by its **supporting hyperplanes**; since the **epigraph** of a convex function is a convex set, a convex function is equivalently described by a function of its gradient. For the smooth 1-D case $f(x)=x^2$: a line $y=sx+c$ with slope $s$ "just touches" $f$ at the smallest intercept $c$; minimizing $-sx_0+f(x_0)$ over $x_0$ and negating gives $f^*(s)=sx_0-f(x_0)$ (Eq. 7.58) — Def. 7.4 without the supremum. For convex differentiable $f$ there is a **one-to-one correspondence** between $f$ and its Legendre transform (the classical Legendre transform); applying the conjugate **twice** recovers $f$ ("the slope of $f$ is $s$, the slope of $f^*$ is $x$").

## Physics note

Physics students meet the Legendre transform as relating the **Lagrangian and Hamiltonian** in classical mechanics ([[mml-ch07-continuous-optimization|MML Ch 7]] margin, p. 242).

## ML uses

- **Quadratic example** (Example 7.7, Eqs. 7.59–7.62): $f(\mathbf{y})=\tfrac{\lambda}{2}\mathbf{y}^\top\mathbf{K}^{-1}\mathbf{y}$ has conjugate $f^*(\boldsymbol\alpha)=\tfrac{1}{2\lambda}\boldsymbol\alpha^\top\mathbf{K}\boldsymbol\alpha$.
- **Sum of per-example losses** (Example 7.8, Eqs. 7.63a–d): the conjugate of $\mathfrak{L}(\mathbf{t})=\sum_i\ell_i(t_i)$ separates termwise, $\mathfrak{L}^*(\mathbf{z})=\sum_i\ell_i^*(z_i)$. "For convex loss functions that apply independently to each example, the conjugate loss is a convenient way to derive a dual problem" ([[mml-ch07-continuous-optimization|MML Ch 7]] p. 246) — the route to dual ML problems and a smooth surrogate for kinked losses like the hinge loss (Exercise 7.11).
- **Equivalence of the two dualities** (Example 7.9, Eq. 7.68): $\min_{\mathbf{x}} f(\mathbf{A}\mathbf{x})+g(\mathbf{x})=\max_{\mathbf{u}}-f^*(\mathbf{u})-g^*(-\mathbf{A}^\top\mathbf{u})$, proved by introducing a Lagrange multiplier $\mathbf{u}$ for $\mathbf{A}\mathbf{x}=\mathbf{y}$ and recognizing convex conjugates — under [[Duality|strong duality]] this matches the Lagrangian-dual answer. (For general inner products $\mathbf{A}^\top$ becomes the adjoint $\mathbf{A}^*$.)

## Connections

- [[mml-ch07-continuous-optimization]] — §7.3.3 Def. 7.4 canonical reference.
- [[LegendreFenchelTransform]] — synonym page.
- [[Duality]] — the umbrella (this is the constraint-free route).
- [[LagrangianDuality]] — the other duality route; coincides under strong duality.
- [[ConvexFunction]] / [[ConvexSet]] — described by tangents / supporting hyperplanes.
- [[Gradient]] — the conjugate is a function of the tangent slopes $\nabla f$.
- [[SupportVectorMachine]] — conjugate of the hinge loss → smooth dual (Ch 12).
</content>
