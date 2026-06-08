---
title: "Support Vector Machine"
type: concept
tags: [classification, classical-ml, foundational]
sources: [madewithml-baselines, islr-seventh-printing, mml-ch12-classification-svm, mml-book]
last_updated: 2026-06-05
---

# Support Vector Machine (SVM)

A classical binary classifier that finds the **maximum-margin** [[SeparatingHyperplane]] between two classes ([[mml-book]] Ch 12; [[islr-seventh-printing|ISLR]] Ch 9). Hard-margin (linearly separable) → soft-margin (slack variables for non-separable) → kernel SVM (non-linear decision surfaces via [[KernelTrick]]). Strong baseline for small/medium datasets; available in [[scikitlearn]].

## The three formulations [[mml-book]] develops

1. **Geometric / primal** (§12.2): $\min \tfrac{1}{2}\|\mathbf{w}\|^2$ s.t. $y_n(\langle\mathbf{w},\mathbf{x}_n\rangle + b)\geq 1$. Convex quadratic program — no closed form.
2. **Loss / hinge** (§12.2.5): equivalent reformulation as $\min \sum_n \max(0, 1 - y_n(\langle\mathbf{w},\mathbf{x}_n\rangle + b)) + \tfrac{1}{2C}\|\mathbf{w}\|^2$ — the hinge loss + $\ell_2$ regularization view.
3. **Dual** (§12.3): apply [[LagrangeMultipliers]] to the primal. Get $\max_{\boldsymbol\alpha\geq 0}\sum_n \alpha_n - \tfrac{1}{2}\sum_{n,m}\alpha_n\alpha_m y_n y_m \langle\mathbf{x}_n,\mathbf{x}_m\rangle$ s.t. $\sum_n\alpha_n y_n=0$. The dual depends on data only through pairwise inner products — which is what lets the [[KernelTrick]] (§12.4) work.

## Why SVMs were *the* method for ~15 years

- **Convex** — no local minima, unique solution.
- **Sparse** — only the support vectors (training points with $\alpha_n > 0$) affect the decision boundary.
- **Margin-based generalization bounds** — Vapnik-Chervonenkis theory shows VC-dimension scales as $R^2/\gamma^2$ (margin $\gamma$, ball radius $R$), independent of input dimension.
- **Kernels** — can fit arbitrarily non-linear boundaries without explicit feature engineering.

Largely displaced for high-data regimes by deep learning circa 2012, but still the right baseline whenever data is scarce, features are well-engineered, or the problem is genuinely linear / mildly non-linear.

## From [[mml-ch12-classification-svm|MML Ch 12]]

[[mml-ch12-classification-svm|MML Ch 12]] is the canonical per-chapter deep dive (book pp. 370–394). It frames the SVM as the **geometric / loss-function-first counterpart to probabilistic linear regression** ([[mml-ch09-linear-regression|Ch 9]]): where MLE *proposes a probabilistic model and derives an optimization problem*, the SVM *starts from a loss to minimize* (max [[Margin|margin]]) following [[EmpiricalRiskMinimization|ERM]] (§8.2), and is chosen as one of the four pillars precisely because its optimization has **no analytic solution** (§12, p. 371). The build order is exact:

- **§12.1** — [[SeparatingHyperplane|separating hyperplane]] $\langle\mathbf{w},\mathbf{x}\rangle+b=0$ as decision boundary ($\mathbf{w}$ normal), classify by $\mathrm{sign}\,f(\mathbf{x})$; the two correctness conditions collapse into $y_n(\langle\mathbf{w},\mathbf{x}_n\rangle+b)\ge0$ (Eq. 12.7).
- **§12.2** — margin $r=1/\|\mathbf{w}\|$ (Eq. 12.14) via [[OrthogonalProjection|orthogonal projection]]; [[HardMarginSVM|hard-margin]] $\min\frac12\|\mathbf{w}\|^2$ s.t. $y_n(\langle\mathbf{w},\mathbf{x}_n\rangle+b)\ge1$ (Eqs. 12.18–12.19); Theorem 12.1 proves the "$\|\mathbf{w}\|=1$" and "margin$=1$" formulations equivalent.
- **§12.2.4–5** — [[SoftMarginSVM|soft-margin]] with [[SlackVariable|slack]] $\xi_n$ and box parameter $C$ (Eqs. 12.26a–c); the [[HingeLoss|hinge loss]] $\max\{0,1-y_nf(\mathbf{x}_n)\}$ as a convex upper bound on zero-one loss, giving the regularized-ERM form (Eq. 12.31) — margin term = $\ell_2$ regularizer.
- **§12.3** — the [[DualSVM|dual]] (Eq. 12.41) via [[LagrangianDuality|Lagrangian duality]]; representer theorem $\mathbf{w}=\sum_n\alpha_ny_n\mathbf{x}_n$ (Eq. 12.38); [[KKTConditions|complementary slackness]] ⇒ [[SupportVector|support vectors]] ($\alpha_n>0$); box constraint $0\le\alpha_n\le C$; the [[ConvexHull|convex-hull]] reading (§12.3.2).
- **§12.4** — the [[KernelTrick|kernel trick]]: the dual sees data only through inner products, so $\langle\mathbf{x}_i,\mathbf{x}_j\rangle\to k(\mathbf{x}_i,\mathbf{x}_j)$ ([[KernelFunction|PSD kernel]], [[RBFKernel|RBF]]/polynomial) lifts to nonlinear classifiers without computing $\boldsymbol\phi$; the hypothesis class stays linear (Fig. 12.10).
- **§12.5** — numerical solution: subgradient/[[StochasticGradientDescent|SGD]] on the hinge (Eq. 12.54), or standard-form [[QuadraticProgramming|QP]] (Eqs. 12.55–12.57; LIBSVM / SVMlight). §12.6 notes the SVM has **no native probabilities** — calibration (Platt scaling) or [[LogisticRegression|logistic regression]] is the probabilistic cousin.

## Connections

- [[mml-ch12-classification-svm]] — canonical per-chapter deep dive (book pp. 370–394).
- [[mml-book]] — umbrella source.
- [[islr-seventh-printing]] — Ch 9 ISLR treatment.
- [[SeparatingHyperplane]] — geometric object.
- [[Margin]] — the quantity SVM maximizes.
- [[HardMarginSVM]] / [[SoftMarginSVM]] / [[SlackVariable]] — the two primal formulations.
- [[HingeLoss]] — the loss-function-first reading.
- [[DualSVM]] / [[SupportVector]] — the dual program and the $\alpha_n>0$ examples.
- [[KernelTrick]] / [[KernelFunction|Kernel]] — non-linear extension.
- [[LagrangianDuality]] / [[LagrangeMultipliers]] / [[KKTConditions]] — dual derivation + support-vector sparsity.
- [[ConvexOptimization]] / [[QuadraticProgramming]] — the problem class SVMs live in.
- [[MaximalMarginClassifier]] — hard-margin special case.
- [[LogisticRegression]] — hinge-loss SVM is equivalent to a $\ell_2$-regularized version with log loss.
