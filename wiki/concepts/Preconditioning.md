---
title: "Preconditioning"
type: concept
tags: [optimization, mathematics]
sources: [d2l-optimization]
last_updated: 2026-05-16
---

# Preconditioning

Reshaping an optimization problem so that all directions have comparable scale — equivalently, reducing the **[[ConditionNumber|condition number]]** $\kappa = \lambda_{\max}/\lambda_{\min}$ of the [[Hessian]]. For ill-conditioned objectives, plain [[GradientDescent]] oscillates in steep directions and crawls in flat ones; preconditioning eliminates this zigzag.

## The ideal

If $\mathbf{Q} = \mathbf{U}^\top \boldsymbol{\Lambda}\mathbf{U}$ is the eigendecomposition, the change of variables $\mathbf{z} = \boldsymbol{\Lambda}^{1/2}\mathbf{U}\mathbf{x}$ would make all eigenvalues equal to 1 — the optimization problem becomes a sphere instead of an ellipsoid. But computing eigenvalues is $\mathcal{O}(d^3)$ — more expensive than solving the problem.

## Cheap approximations

1. **Diagonal preconditioning** (D2L §gd-preconditioning): use only $\textrm{diag}(\mathbf{Q})$.
   $$\tilde{\mathbf{Q}} = \textrm{diag}^{-1/2}(\mathbf{Q})\,\mathbf{Q}\,\textrm{diag}^{-1/2}(\mathbf{Q}),\quad \tilde{\mathbf{Q}}_{ii} = 1.$$
   Update: $\mathbf{x}\leftarrow\mathbf{x}-\eta\,\textrm{diag}(\mathbf{H})^{-1}\nabla f$. Effectively a *per-coordinate learning rate*.

2. **Gradient-magnitude proxy** (D2L §adagrad): use accumulated squared gradients $\mathbf{s}_t$ as a stand-in for $\textrm{diag}(\mathbf{H})$. This is the conceptual foundation of [[Adagrad]] / [[RMSProp]] / [[Adam]].

## Why diagonal preconditioning works

D2L's pedagogical example: if one variable is in millimeters and another in kilometers, the natural-meter scales differ by $10^6$ — a terrible parametrization mismatch. Diagonal preconditioning rescales each coordinate, eliminating this artificial ill-conditioning. The general principle: preconditioning is **invariant under coordinate rescaling**, so the optimizer no longer cares about the units of each parameter.

## Connection to [[NewtonsMethod]]

Diagonal preconditioning is the affordable middle ground between [[GradientDescent]] (no curvature info) and full Newton (intractable $\mathcal{O}(d^2)$ Hessian). Adagrad's $\mathbf{s}_t = \sum_t \mathbf{g}_t^2$ further replaces the Hessian-diagonal computation with a cumulative gradient-magnitude one — yielding a fully gradient-only second-order proxy that costs the same as plain SGD.

## Connections

- [[d2l-optimization]] — canonical reference (§gd-preconditioning, §adagrad-preconditioning).
- [[Hessian]] / [[ConditionNumber]] — what preconditioning targets.
- [[NewtonsMethod]] — the expensive full-curvature version.
- [[GradientDescent]] — what preconditioning improves.
- [[Adagrad]] / [[RMSProp]] / [[Adadelta]] / [[Adam]] — gradient-based diagonal preconditioners.
- [[BatchNormalization]] — an architectural form of preconditioning that rescales activations.
