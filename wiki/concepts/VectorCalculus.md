---
title: "Vector Calculus"
type: concept
tags: [vector-calculus, calculus, foundational]
sources: [mml-ch05-vector-calculus, mml-book, matrix-calculus-for-deep-learning]
last_updated: 2026-06-04
---

# Vector Calculus

Calculus on multivariate functions: [[PartialDerivative]], [[Gradient]], [[Jacobian]], [[Hessian]], [[ChainRule]], [[TaylorSeries]], [[Backpropagation]]. Covered in [[mml-book]] Ch 5, and rederived from Calculus 1 for a deep-learning audience in [[matrix-calculus-for-deep-learning|Parr & Howard]] (gradient → Jacobian → element-wise diagonal Jacobians → the three chain-rule variants → neuron and loss gradients).

## From [[mml-ch05-vector-calculus|MML Ch 5]]

Ch 5 is the canonical wiki reference for this concept — the **gradient-machinery chapter** whose explicit purpose is to build the differential-calculus tooling that ML optimizers consume (gradient descent §7.1, regression Ch 9, auto-encoders Ch 10, GMMs Ch 11). Its conceptual spine (Fig. 5.2 mind map):

1. **[[DifferenceQuotient|Difference quotient]]** (§5.1, Def 5.1) → **[[derivatives|derivative]]** (Def 5.2) as its limit; the [[DifferentiationRules|differentiation rules]] (§5.1.2) and the [[TaylorSeries|Taylor series]] / [[TaylorPolynomial|Taylor polynomial]] (§5.1.1).
2. **[[PartialDerivative|Partial derivatives]]** (§5.2, Def 5.5) collected into the **[[Gradient|gradient as a row vector]]** (Eq. 5.40 — the deliberate [[Gradient|row-vector convention]]).
3. The **[[Jacobian]]** $m\times n$ matrix for vector-valued functions (§5.3, Def 5.6, numerator layout); its determinant scales volumes (change-of-variables, §6.7).
4. Gradients of matrices → higher-order [[Tensor|tensors]] (§5.4); the [[UsefulGradientIdentities|useful-identities table]] (§5.5).
5. **[[Backpropagation]]** = [[ReverseModeAutodiff|reverse-mode]] [[AutomaticDifferentiation|automatic differentiation]] over a [[ComputationalGraph|computation graph]] (§5.6).
6. The **[[Hessian]]** and higher-order derivatives (§5.7); [[Linearization]] and the multivariate Taylor series (§5.8).

The chapter is **pen-and-paper** (no notebooks) and motivates every object by where it is *used* downstream (Chs 6, 7, 9–12).

## Convention note

MML (and [[matrix-calculus-for-deep-learning|Parr & Howard]]) use the **row-vector gradient / numerator-layout Jacobian** convention; Murphy, Goodfellow et al., and [[d2l-preliminaries|D2L]] use the **column-vector** convention. Same math, transpose-different shapes — see [[Gradient]] / [[Jacobian]].
