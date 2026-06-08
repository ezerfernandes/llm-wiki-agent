---
title: "Preconditioner"
type: concept
tags: [optimization, numerical-linear-algebra, gradient-descent, foundational]
sources: [mml-ch07-continuous-optimization, mml-book]
last_updated: 2026-06-05
---

# Preconditioner

A matrix $\mathbf{P}$ used to **improve the [[ConditionNumber|condition number]]** of a problem so that [[GradientDescent|gradient descent]] (or an iterative linear solver) converges faster ([[mml-ch07-continuous-optimization|MML Ch 7]] §7.1.1, Remark p. 230).

## The idea

Gradient descent on $\mathbf{A}\mathbf{x}=\mathbf{b}$ (i.e. minimizing $\|\mathbf{A}\mathbf{x}-\mathbf{b}\|^2$) converges slowly when $\mathbf{A}$ is **ill-conditioned** — a large $\kappa=\sigma_{\max}/\sigma_{\min}$ means a long, thin valley, and the iterates "zigzag" (Fig. 7.3). Instead of solving $\mathbf{A}\mathbf{x}-\mathbf{b}=\mathbf{0}$ directly, solve the **preconditioned system**

$$\mathbf{P}^{-1}(\mathbf{A}\mathbf{x}-\mathbf{b})=\mathbf{0}.$$

## The design trade-off

Choose $\mathbf{P}$ so that:

1. $\mathbf{P}^{-1}\mathbf{A}$ has a **better (smaller) condition number** than $\mathbf{A}$ — faster convergence; and
2. $\mathbf{P}^{-1}$ is **cheap to compute/apply** — otherwise the preconditioning costs more than it saves.

(The two extremes: $\mathbf{P}=\mathbf{I}$ does nothing; $\mathbf{P}=\mathbf{A}$ gives the perfect condition number $1$ but requires solving the original problem.) Further reading: Boyd & Vandenberghe (2004, ch. 9).

## Connection to ML optimizers

Preconditioning is the conceptual ancestor of **adaptive / per-parameter step-size** methods — [[Adam]], [[RMSProp]], AdaGrad, and natural-gradient methods all rescale the gradient by (an approximation of) curvature, i.e. an implicit preconditioner. [[Momentum]] addresses the same ill-conditioning pathology by a different mechanism (leaky averaging).

## Connections

- [[mml-ch07-continuous-optimization]] — §7.1.1 Remark canonical reference.
- [[ConditionNumber]] — what a preconditioner reduces.
- [[GradientDescent]] — the algorithm whose convergence it accelerates.
- [[Momentum]] — alternative remedy for ill-conditioning.
- [[Adam]] / [[RMSProp]] — adaptive methods that act as implicit preconditioners.
- [[SingularValueDecomposition]] — $\kappa$ is the ratio of singular values (§4.5).
</content>
