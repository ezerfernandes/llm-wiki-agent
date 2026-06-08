---
title: "Margin"
type: concept
tags: [classification, geometry, foundational]
sources: [mml-ch12-classification-svm, mml-book]
last_updated: 2026-06-05
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

## From [[mml-ch12-classification-svm|MML Ch 12]]

§12.2.1 (book pp. 374–377) derives the central identity **$r=1/\|\mathbf{w}\|$** (Eq. 12.14). Take $\mathbf{x}_a$ at distance $r$ from the hyperplane; its [[OrthogonalProjection|orthogonal projection]] $\mathbf{x}_a'$ satisfies $\mathbf{x}_a=\mathbf{x}_a'+r\frac{\mathbf{w}}{\|\mathbf{w}\|}$ (Eq. 12.8, since $\mathbf{w}$ is the orthogonal direction, §3.8). Substituting into $\langle\mathbf{w},\mathbf{x}_a'\rangle+b=0$ (Eq. 12.11) and using $\langle\mathbf{w},\mathbf{w}\rangle=\|\mathbf{w}\|^2$ (Eq. 3.16) plus the scale fix $\langle\mathbf{w},\mathbf{x}_a\rangle+b=1$ collapses to $r=1/\|\mathbf{w}\|$. **Theorem 12.1** (§12.2.3, pp. 378–379) proves the two formulations on this page are *the same problem*: scaling so the margin equals $1$ (then minimizing $\frac12\|\mathbf{w}\|^2$) is equivalent to constraining $\|\mathbf{w}\|=1$ (then maximizing $r$). The chapter then makes the deep statistical reading explicit — **the margin term $\frac12\|\mathbf{w}\|^2$ *is* the regularizer**, so "margin maximization can be interpreted as regularization" (§12.2.5, p. 382). The generalization remark (§12.2.1, p. 376) attributes the large-margin → low-complexity argument to Vapnik & Chervonenkis (Vapnik 2000; Steinwart & Christmann 2008; Shalev-Shwartz & Ben-David 2014).

## Connections

- [[mml-ch12-classification-svm]] — §12.2 canonical per-chapter reference.
- [[mml-book]] — umbrella source.
- [[SupportVectorMachine]] — the algorithm that maximizes margin.
- [[HardMarginSVM]] / [[SoftMarginSVM]] — the formulations; [[HingeLoss]] — the loss-first view.
- [[SeparatingHyperplane]] — the geometric object whose distance defines margin.
- [[ConvexOptimization]] — the problem class margin maximization falls in.
- [[OrthogonalProjection]] — how distance to hyperplane is computed.
- [[MaximalMarginClassifier]] — earlier wiki page covering the same idea.
