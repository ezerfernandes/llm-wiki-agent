---
title: "Useful Gradient Identities"
type: concept
tags: [vector-calculus, matrix-calculus, foundational, reference]
sources: [mml-ch05-vector-calculus, mml-book]
last_updated: 2026-06-04
---

# Useful Gradient Identities

A reference table of closed-form gradients that recur in ML derivations, so one can look them up instead of re-deriving via the [[ChainRule|chain rule]] each time. [[mml-ch05-vector-calculus|MML Ch 5]] §5.5 (Eqs. 5.99–5.108) reproduces a subset, citing **Petersen & Pedersen's *Matrix Cookbook* (2012)** as the comprehensive source. Uses $\operatorname{tr}(\cdot)$ ([[Trace]]), $\det(\cdot)$ ([[Determinant]]), and matrix inverses; all in MML's [[Gradient|numerator layout]].

## Matrix-function identities

$$\frac{\partial}{\partial\mathbf{X}}\mathbf{f}(\mathbf{X})^\top = \left(\frac{\partial\mathbf{f}(\mathbf{X})}{\partial\mathbf{X}}\right)^\top \quad (5.99)$$

$$\frac{\partial}{\partial\mathbf{X}}\operatorname{tr}(\mathbf{f}(\mathbf{X})) = \operatorname{tr}\left(\frac{\partial\mathbf{f}(\mathbf{X})}{\partial\mathbf{X}}\right) \quad (5.100)$$

$$\frac{\partial}{\partial\mathbf{X}}\det(\mathbf{f}(\mathbf{X})) = \det(\mathbf{f}(\mathbf{X}))\operatorname{tr}\left(\mathbf{f}(\mathbf{X})^{-1}\frac{\partial\mathbf{f}(\mathbf{X})}{\partial\mathbf{X}}\right) \quad (5.101)$$

$$\frac{\partial}{\partial\mathbf{X}}\mathbf{f}(\mathbf{X})^{-1} = -\mathbf{f}(\mathbf{X})^{-1}\frac{\partial\mathbf{f}(\mathbf{X})}{\partial\mathbf{X}}\mathbf{f}(\mathbf{X})^{-1} \quad (5.102)$$

## Linear / quadratic forms

$$\frac{\partial\mathbf{a}^\top\mathbf{X}^{-1}\mathbf{b}}{\partial\mathbf{X}} = -(\mathbf{X}^{-1})^\top\mathbf{a}\mathbf{b}^\top(\mathbf{X}^{-1})^\top \quad (5.103)$$

$$\frac{\partial\mathbf{x}^\top\mathbf{a}}{\partial\mathbf{x}} = \mathbf{a}^\top, \qquad \frac{\partial\mathbf{a}^\top\mathbf{x}}{\partial\mathbf{x}} = \mathbf{a}^\top \quad (5.104,\ 5.105)$$

$$\frac{\partial\mathbf{a}^\top\mathbf{X}\mathbf{b}}{\partial\mathbf{X}} = \mathbf{a}\mathbf{b}^\top \quad (5.106)$$

$$\frac{\partial\mathbf{x}^\top\mathbf{B}\mathbf{x}}{\partial\mathbf{x}} = \mathbf{x}^\top(\mathbf{B}+\mathbf{B}^\top) \quad (5.107)$$

$$\frac{\partial}{\partial\mathbf{s}}(\mathbf{x}-\mathbf{A}\mathbf{s})^\top\mathbf{W}(\mathbf{x}-\mathbf{A}\mathbf{s}) = -2(\mathbf{x}-\mathbf{A}\mathbf{s})^\top\mathbf{W}\mathbf{A}\quad\text{for symmetric }\mathbf{W} \quad (5.108)$$

The last identity is exactly the gradient of a **weighted least-squares / Mahalanobis residual** — the workhorse for the [[Gradient|gradient]] of a regression loss (cf. MML Example 5.11, where the $\mathbf{W}=\mathbf{I}$ case yields the Ch 9 normal equations).

## Tensor caveat

MML §5.5 Remark: these identities use the matrix trace and transpose, but gradients can be higher-order [[Tensor|tensors]] where neither is defined. The trace of a $D\times D\times E\times F$ tensor is an $E\times F$ matrix (a *tensor contraction*); "transpose" means swapping the first two dimensions.

## Connections

- [[mml-ch05-vector-calculus|MML Ch 5]] — §5.5 canonical reference (subset of Petersen & Pedersen 2012).
- [[Gradient]] / [[Jacobian]] — the objects being tabulated (numerator layout).
- [[Trace]] / [[Determinant]] — appear in the matrix-function identities.
- [[ChainRule]] — what these identities save you from re-deriving.
- [[Tensor]] — the higher-order caveat.
