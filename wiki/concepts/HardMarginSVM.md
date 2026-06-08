---
title: "Hard-Margin SVM"
type: concept
tags: [classification, classical-ml, convex-optimization, quadratic-programming, foundational]
sources: [mml-ch12-classification-svm, mml-book]
last_updated: 2026-06-05
---

# Hard-Margin SVM

The original, **no-violations** formulation of the [[SupportVectorMachine|support vector machine]] for **linearly separable** data ([[mml-ch12-classification-svm|MML Ch 12]] §12.2, Eqs. 12.18–12.19, p. 377):

$$\min_{\mathbf{w},b}\ \tfrac12\|\mathbf{w}\|^2 \quad\text{subject to}\quad y_n(\langle\mathbf{w},\mathbf{x}_n\rangle+b)\ge1 \ \text{ for all } n=1,\dots,N.$$

"The reason for the expression 'hard' is because the formulation does not allow for any violations of the margin condition" (§12.2, p. 377). Every example must lie on the correct side of the hyperplane *and* at least a unit margin away. The $\frac12$ factor "does not affect the optimal $\mathbf{w},b$ but yields a tidier form when we compute the gradient."

## Why this is the max-margin hyperplane

Because the [[Margin|margin]] is $r=1/\|\mathbf{w}\|$ ([[mml-ch12-classification-svm|MML Ch 12]] §12.2.1, Eq. 12.14), maximizing the margin is minimizing $\|\mathbf{w}\|$, hence minimizing $\frac12\|\mathbf{w}\|^2$. **Theorem 12.1** (§12.2.3) proves this objective is equivalent to the normalized formulation $\max_{\mathbf{w},b,r}r$ s.t. $y_n(\langle\mathbf{w},\mathbf{x}_n\rangle+b)\ge r$, $\|\mathbf{w}\|=1$ — fixing the scale so the margin equals $1$ is the same as constraining the weight to unit length. Among the infinitely many [[SeparatingHyperplane|separating hyperplanes]] of separable data (Fig. 12.3), this picks the unique maximum-margin one.

## It is a convex quadratic program

The objective $\frac12\|\mathbf{w}\|^2=\frac12\mathbf{w}^\top\mathbf{w}$ is a convex quadratic; the constraints are affine in $(\mathbf{w},b)$. So the hard-margin SVM is a **[[QuadraticProgramming|convex quadratic program]]** ([[mml-ch12-classification-svm|MML Ch 12]] margin note p. 377; this is the flagship ML QP promised in [[mml-ch07-continuous-optimization|MML Ch 7]] §7.3.2). It has **no analytic / closed-form solution** — unlike the [[LinearRegression|least-squares]] normal equations — so it is solved by [[ConvexOptimization|convex-optimization]] tooling. Its [[LagrangianDuality|Lagrangian dual]] is the [[DualSVM|dual SVM]], whose [[KKTConditions|complementary slackness]] exposes the [[SupportVector|support vectors]].

## The hard-margin loss

In the loss-function view ([[mml-ch12-classification-svm|MML Ch 12]] §12.2.5, Eq. 12.30), the hard-margin SVM corresponds to the loss $\ell(t)=0$ if $t\ge1$ else $\infty$ (where $t=y_nf(\mathbf{x}_n)$) — "this loss can be interpreted as never allowing any examples inside the margin." Relaxing the $\infty$ to the linearly-growing [[HingeLoss|hinge loss]] $\max\{0,1-t\}$ gives the [[SoftMarginSVM|soft-margin SVM]].

## Limitation → soft margin

Real data is rarely linearly separable, so the hard constraint is usually infeasible. The fix is the [[SoftMarginSVM|soft-margin SVM]] ([[mml-ch12-classification-svm|MML Ch 12]] §12.2.4), which adds [[SlackVariable|slack variables]] $\xi_n\ge0$ and a penalty $C\sum_n\xi_n$, allowing — but charging for — margin violations.

## Connections

- [[mml-ch12-classification-svm]] — §12.2 canonical reference.
- [[SupportVectorMachine]] — the umbrella method; hard-margin is its base case.
- [[Margin]] — $r=1/\|\mathbf{w}\|$; the maximized quantity.
- [[SeparatingHyperplane]] — the object chosen.
- [[SoftMarginSVM]] / [[SlackVariable]] — the relaxation for non-separable data.
- [[HingeLoss]] — the $\infty$-penalty limit is the hard-margin loss.
- [[DualSVM]] / [[SupportVector]] / [[KKTConditions]] — the dual and support vectors.
- [[QuadraticProgramming]] / [[ConvexOptimization]] — the problem class (no closed form).
- [[MaximalMarginClassifier]] — the ISLR name for the same idea.
