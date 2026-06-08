---
title: "Slack Variable"
type: concept
tags: [classification, classical-ml, convex-optimization, constrained-optimization, foundational]
sources: [mml-ch12-classification-svm, mml-book]
last_updated: 2026-06-05
---

# Slack Variable

A non-negative auxiliary variable $\xi_n\ge0$ introduced — one per example–label pair $(\mathbf{x}_n,y_n)$ — to **relax a hard constraint** into a soft, penalized one. In the [[SoftMarginSVM|soft-margin SVM]] it lets a training example sit inside the margin or even on the wrong side of the [[SeparatingHyperplane|hyperplane]], at a cost ([[mml-ch12-classification-svm|MML Ch 12]] §12.2.4, p. 379–380).

## In the soft-margin SVM

The [[HardMarginSVM|hard-margin]] constraint $y_n(\langle\mathbf{w},\mathbf{x}_n\rangle+b)\ge1$ becomes

$$y_n(\langle\mathbf{w},\mathbf{x}_n\rangle+b)\ge 1-\xi_n,\qquad \xi_n\ge0,$$

with a penalty $C\sum_n\xi_n$ added to the objective (Eqs. 12.26a–c). "We subtract the value of $\xi_n$ from the margin, constraining $\xi_n$ to be non-negative" ([[mml-ch12-classification-svm|MML Ch 12]] p. 380).

## Geometric meaning

$\xi_n$ measures the distance of $\mathbf{x}_n$ past its correct margin boundary (Fig. 12.7):

- $\xi_n=0$ — correctly classified, on or beyond the margin (no penalty).
- $0<\xi_n\le1$ — inside the margin but still correctly classified.
- $\xi_n>1$ — on the wrong side of the hyperplane (misclassified).

At the optimum the slack is exactly the [[HingeLoss|hinge loss]] of that example: $\xi_n=\max\{0,1-y_nf(\mathbf{x}_n)\}$. Eliminating the slacks this way is what turns the constrained soft-margin SVM (Eq. 12.26a) into the unconstrained regularized-hinge problem (Eq. 12.31) — the equivalence $\min_t\max\{0,1-t\}=\min_\xi\xi$ s.t. $\xi\ge0,\xi\ge1-t$ (Eqs. 12.32–12.33).

## In the dual

Slack non-negativity carries its own Lagrange multiplier $\gamma_n\ge0$ in the [[DualSVM|dual]] derivation; the stationarity condition $C-\alpha_n-\gamma_n=0$ (Eq. 12.37) makes the slack terms vanish from the dual objective and produces the **box constraint** $0\le\alpha_n\le C$ on the classification multipliers ([[mml-ch12-classification-svm|MML Ch 12]] §12.3.1).

## General pattern

The slack-variable trick is a standard [[ConvexOptimization|convex-optimization]] device for converting inequality-violating objectives (like a non-differentiable max) into smooth constrained programs amenable to [[QuadraticProgramming|QP]] solvers — used well beyond the SVM.

## Connections

- [[mml-ch12-classification-svm]] — §12.2.4 canonical reference.
- [[SoftMarginSVM]] — the model that introduces $\xi_n$.
- [[HardMarginSVM]] — the unrelaxed ($\xi_n\equiv0$) special case.
- [[HingeLoss]] — equals the optimal slack per example.
- [[DualSVM]] — slacks → box constraint $0\le\alpha_n\le C$.
- [[ConvexOptimization]] / [[QuadraticProgramming]] — the optimization framing.
- [[Regularization]] — the penalty $C\sum_n\xi_n$ as the loss/error term.
