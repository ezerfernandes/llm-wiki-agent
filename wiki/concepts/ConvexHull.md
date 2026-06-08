---
title: "Convex Hull"
type: concept
tags: [convex-optimization, geometry, classification, foundational]
sources: [mml-ch12-classification-svm, mml-book]
last_updated: 2026-06-05
---

# Convex Hull

The **smallest convex set containing a given set of points** — equivalently, the set of all their convex combinations ([[mml-ch12-classification-svm|MML Ch 12]] §12.3.2, Eq. 12.43, p. 386):

$$\mathrm{conv}(\mathbf{X})=\left\{\sum_{n=1}^N\alpha_n\mathbf{x}_n\ :\ \sum_{n=1}^N\alpha_n=1,\ \alpha_n\ge0\right\}.$$

A convex combination $\alpha_1\mathbf{x}_1+\alpha_2\mathbf{x}_2$ ($\alpha_1+\alpha_2=1$, $\alpha_i\ge0$) traces the line segment between two points; three points span the filled triangle; $N$ points give a convex polytope. As the number of points exceeds the dimension, some points fall *inside* the hull (Fig. 12.9a).

## The SVM convex-hull view

[[mml-ch12-classification-svm|MML Ch 12]] §12.3.2 uses convex hulls to give a **third interpretation of the [[DualSVM|dual SVM]]** (alongside the Lagrangian-dual and primal-geometric views). For separable data, form the convex hull of each class; since the classes are separable, the hulls do not overlap. Pick the closest pair of points — $\mathbf{c}$ in the positive hull, $\mathbf{d}$ in the negative hull — and the maximum-margin [[SeparatingHyperplane|separating hyperplane]] **bisects** the difference vector

$$\mathbf{w}:=\mathbf{c}-\mathbf{d}\qquad(\text{Eq. } 12.44).$$

Minimizing $\frac12\|\mathbf{w}\|^2$ (Eq. 12.45) with $\mathbf{c}=\sum_{n:y_n=+1}\alpha_n^+\mathbf{x}_n$ and $\mathbf{d}=\sum_{n:y_n=-1}\alpha_n^-\mathbf{x}_n$ recovers exactly the dual SVM; the hull constraints $\sum\alpha_n^+=\sum\alpha_n^-=1$ reproduce the dual equality $\sum_ny_n\alpha_n=0$ (Eqs. 12.49–12.51, Bennett & Bredensteiner 2000a).

## Reduced hull (soft margin)

For the [[SoftMarginSVM|soft-margin SVM]] the relevant object is the **reduced hull**: the box bound $\alpha_n\le C$ caps each coefficient, shrinking the convex hull to a smaller volume so the two (possibly overlapping) class clouds can still be separated ([[mml-ch12-classification-svm|MML Ch 12]] §12.3.2 Remark, p. 388; Bennett & Bredensteiner 2000b).

## Connections

- [[mml-ch12-classification-svm]] — §12.3.2 canonical reference.
- [[DualSVM]] — the convex-hull view is the third reading of the dual.
- [[SeparatingHyperplane]] — bisects $\mathbf{c}-\mathbf{d}$.
- [[SoftMarginSVM]] — uses the reduced hull.
- [[ConvexSet]] / [[ConvexOptimization]] — the hull is the smallest convex set containing the points.
- [[SupportVector]] — the closest-points $\mathbf{c},\mathbf{d}$ are convex combinations of support vectors.
