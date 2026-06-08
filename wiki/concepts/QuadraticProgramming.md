---
title: "Quadratic Programming"
type: concept
tags: [optimization, convex-optimization, quadratic-programming, duality, foundational]
sources: [mml-ch07-continuous-optimization, mml-ch12-classification-svm, mml-book]
last_updated: 2026-06-05
---

# Quadratic Programming

The convex-optimization sub-class with a **convex quadratic objective** and **affine constraints** ([[mml-ch07-continuous-optimization|MML Ch 7]] §7.3.2, Eq. 7.45):

$$\min_{\mathbf{x}\in\mathbb{R}^d}\ \tfrac12\mathbf{x}^\top\mathbf{Q}\mathbf{x}+\mathbf{c}^\top\mathbf{x}\quad\text{subject to}\quad\mathbf{A}\mathbf{x}\leq\mathbf{b},$$

where $\mathbf{Q}\in\mathbb{R}^{d\times d}$ is symmetric **positive definite** (so the objective is convex), $\mathbf{A}\in\mathbb{R}^{m\times d}$, $\mathbf{c}\in\mathbb{R}^d$ — $d$ variables, $m$ linear constraints. The contour lines are ellipses; the optimum lies in the feasible polytope (Example 7.6, Fig. 7.4).

## The dual QP (via [[LagrangianDuality|Lagrangian duality]])

[[Lagrangian]]: $\mathfrak{L}=\tfrac12\mathbf{x}^\top\mathbf{Q}\mathbf{x}+\mathbf{c}^\top\mathbf{x}+\boldsymbol\lambda^\top(\mathbf{A}\mathbf{x}-\mathbf{b})$ (Eq. 7.48a). Setting $\partial_{\mathbf{x}}\mathfrak{L}=\mathbf{0}$ gives $\mathbf{Q}\mathbf{x}+(\mathbf{c}+\mathbf{A}^\top\boldsymbol\lambda)=\mathbf{0}$ (Eq. 7.49); since $\mathbf{Q}$ is positive definite (hence invertible), $\mathbf{x}=-\mathbf{Q}^{-1}(\mathbf{c}+\mathbf{A}^\top\boldsymbol\lambda)$ (Eq. 7.50). Back-substituting yields the **dual program** (Eqs. 7.51–7.52):

$$\max_{\boldsymbol\lambda\in\mathbb{R}^m}\ -\tfrac12(\mathbf{c}+\mathbf{A}^\top\boldsymbol\lambda)^\top\mathbf{Q}^{-1}(\mathbf{c}+\mathbf{A}^\top\boldsymbol\lambda)-\boldsymbol\lambda^\top\mathbf{b}\quad\text{subject to}\quad\boldsymbol\lambda\geq\mathbf{0}.$$

## Flagship ML application

"We will see an application of quadratic programming in machine learning in Chapter 12" ([[mml-ch07-continuous-optimization|MML Ch 7]] p. 242). The **hard-margin** [[SupportVectorMachine|SVM]] $\min\tfrac12\|\mathbf{w}\|^2$ s.t. $y_n(\langle\mathbf{w},\mathbf{x}_n\rangle+b)\ge1$ ([[HardMarginSVM]]) is exactly a QP; its dual exposes the support vectors via [[KKTConditions|complementary slackness]]. (Exercise 7.7 derives the dual of Example 7.6; Exercise 7.8 derives the Lagrangian dual of a minimal hard-margin-like QP.)

## From [[mml-ch12-classification-svm|MML Ch 12]] — the SVM as a QP

[[mml-ch12-classification-svm|MML Ch 12]] cashes in the Ch 7 forward-ref: **both the primal and the dual SVM are convex quadratic programs**. The [[HardMarginSVM|hard-margin SVM]] $\min\frac12\|\mathbf{w}\|^2$ s.t. $y_n(\langle\mathbf{w},\mathbf{x}_n\rangle+b)\ge1$ is a QP with no closed form (margin note, p. 377); §12.5 (Eqs. 12.55–12.56) writes the [[SoftMarginSVM|soft-margin]] primal in standard form over $[\mathbf{w}^\top,b,\boldsymbol\xi^\top]^\top\in\mathbb{R}^{D+1+N}$, and the [[DualSVM|dual]] (Eq. 12.57) as $\min_{\boldsymbol\alpha}\frac12\boldsymbol\alpha^\top\mathbf{Y}\mathbf{K}\mathbf{Y}\boldsymbol\alpha-\mathbf{1}^\top\boldsymbol\alpha$ over $N$ box-constrained variables ($\mathbf{Q}=\mathbf{Y}\mathbf{K}\mathbf{Y}$ here). The dual's equality constraint $\sum_n y_n\alpha_n=0$ is encoded as two inequalities to match the §7.3.2 standard form (Eq. 12.58). Solved by off-the-shelf QP solvers — LIBSVM (Chang & Lin 2011), SVMlight (Joachims 1999) — though "expressing the SVM problem in standard convex optimization form is not often used in practice" (§12.5, p. 392); specialized SMO-style solvers dominate.

## Connections

- [[mml-ch07-continuous-optimization]] — §7.3.2 canonical reference.
- [[mml-ch12-classification-svm]] — §12.5 the SVM-as-QP application.
- [[ConvexOptimization]] — QP is the convex-quadratic special case.
- [[LinearProgramming]] — the all-linear sibling.
- [[LagrangianDuality]] / [[Duality]] — source of the dual QP.
- [[Lagrangian]] — the function used to derive the dual.
- [[SupportVectorMachine]] / [[HardMarginSVM]] / [[SoftMarginSVM]] / [[DualSVM]] — the headline ML QP (Ch 12).
