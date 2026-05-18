---
title: "Margin"
type: concept
tags: [classification, geometry, foundational]
sources: [mml-book]
last_updated: 2026-05-16
---

# Margin

In binary classification, the margin of a [[SeparatingHyperplane]] is the distance from the hyperplane to the closest training example ([[mml-book]] §12.2.1).

For a hyperplane defined by $\langle\mathbf{w},\mathbf{x}\rangle + b = 0$ and a point $\mathbf{x}_n$ with label $y_n\in\{+1,-1\}$, the **signed distance** from $\mathbf{x}_n$ to the hyperplane is $\frac{y_n(\langle\mathbf{w},\mathbf{x}_n\rangle + b)}{\|\mathbf{w}\|}$ — positive when correctly classified.

## Two equivalent formulations

[[mml-book]] §12.2.3 proves these are the same problem:

**Formulation 1** (margin variable + unit-normal constraint):
$$\max_{\mathbf{w}, b, r}\, r \quad\text{s.t.}\quad y_n(\langle\mathbf{w},\mathbf{x}_n\rangle + b)\geq r,\;\|\mathbf{w}\|=1.$$

**Formulation 2** (scale-fixed margin = 1, minimize $\|\mathbf{w}\|^2$):
$$\min_{\mathbf{w}, b}\,\tfrac{1}{2}\|\mathbf{w}\|^2 \quad\text{s.t.}\quad y_n(\langle\mathbf{w},\mathbf{x}_n\rangle + b)\geq 1.$$

The second is the **hard-margin SVM** — a convex quadratic program with no closed form, solved via [[LagrangeMultipliers]] / [[ConvexOptimization]] (§12.3 dual SVM).

## Why "maximum margin" generalizes well

[[mml-book]] §12.2.1 marginal: "A classifier with large margin turns out to generalize well (Steinwart and Christmann, 2008)." More formally, Vapnik & Chervonenkis showed that the VC-dimension of margin-$\gamma$ linear classifiers grows like $R^2/\gamma^2$ (where $R$ bounds the input norm) — independent of dimension. So larger margins ⇒ lower generalization bounds, independent of $D$.

This is why SVMs were the dominant supervised method before deep learning: their generalization argument is *explicit and tight*.

## Soft margin

Real data isn't linearly separable. The **soft-margin SVM** ([[mml-book]] §12.2.4) introduces slack variables $\xi_n\geq 0$ allowing constraint violations, with a hinge-loss penalty:

$$\min\,\tfrac{1}{2}\|\mathbf{w}\|^2 + C\sum_n\xi_n \quad\text{s.t.}\quad y_n(\langle\mathbf{w},\mathbf{x}_n\rangle + b)\geq 1 - \xi_n.$$

$C$ trades off margin width against training-error tolerance — the SVM equivalent of an inverse-regularization parameter.

## Connections

- [[mml-book]] — §12.2 canonical reference.
- [[SupportVectorMachine]] — the algorithm that maximizes margin.
- [[SeparatingHyperplane]] — the geometric object whose distance defines margin.
- [[ConvexOptimization]] — the problem class margin maximization falls in.
- [[OrthogonalProjection]] — how distance to hyperplane is computed.
- [[MaximalMarginClassifier]] — earlier wiki page covering the same idea.
