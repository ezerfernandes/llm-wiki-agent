---
title: "Support Vector Machine"
type: concept
tags: [classification, classical-ml, foundational]
sources: [madewithml-baselines, islr-seventh-printing, mml-book]
last_updated: 2026-05-16
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

## Connections

- [[mml-book]] — Ch 12 canonical reference.
- [[islr-seventh-printing]] — Ch 9 ISLR treatment.
- [[SeparatingHyperplane]] — geometric object.
- [[Margin]] — the quantity SVM maximizes.
- [[KernelTrick]] — non-linear extension.
- [[LagrangeMultipliers]] — dual derivation.
- [[ConvexOptimization]] — the problem class SVMs live in.
- [[MaximalMarginClassifier]] — hard-margin special case.
- [[LogisticRegression]] — hinge-loss SVM is equivalent to a $\ell_2$-regularized version with log loss.
