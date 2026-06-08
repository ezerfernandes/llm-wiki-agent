---
title: "Dual SVM"
type: concept
tags: [classification, classical-ml, duality, convex-optimization, quadratic-programming, kernel-methods, foundational]
sources: [mml-ch12-classification-svm, mml-book]
last_updated: 2026-06-05
---

# Dual SVM

The [[LagrangianDuality|Lagrangian dual]] of the [[SoftMarginSVM|soft-margin SVM]] — an equivalent optimization problem in the multiplier variables $\boldsymbol\alpha$ instead of the primal weights $(\mathbf{w},b,\boldsymbol\xi)$ ([[mml-ch12-classification-svm|MML Ch 12]] §12.3, Eq. 12.41, p. 385):

$$\min_{\boldsymbol\alpha}\ \tfrac12\sum_{i=1}^N\sum_{j=1}^N y_iy_j\alpha_i\alpha_j\langle\mathbf{x}_i,\mathbf{x}_j\rangle - \sum_{i=1}^N\alpha_i \quad\text{s.t.}\quad \sum_{i=1}^N y_i\alpha_i=0,\ \ 0\le\alpha_i\le C.$$

## Derivation

Form the [[Lagrangian]] of the soft-margin primal with multipliers $\alpha_n\ge0$ (classification constraint) and $\gamma_n\ge0$ (slack non-negativity) (Eq. 12.34). Differentiating and setting to zero gives the stationarity conditions: $\mathbf{w}=\sum_n\alpha_ny_n\mathbf{x}_n$ (Eq. 12.38, the **representer theorem**), $\sum_n\alpha_ny_n=0$ (Eq. 12.36), and $C-\alpha_n-\gamma_n=0$ (Eq. 12.37, which with $\gamma_n\ge0$ forces $\alpha_n\le C$). Substituting $\mathbf{w}$ back into $\mathfrak{L}$ eliminates the primal variables and yields Eq. 12.41. Because the primal is convex, [[Duality|strong duality]] holds and the dual optimum equals the primal optimum.

## Why the dual is the SVM's preferred form

- **Scales with examples, not features.** The primal SVM has $D{+}1{+}N$ variables (the weight $\mathbf{w}\in\mathbb{R}^D$ plus bias and slacks); the dual has just $N$ — "an equivalent optimization problem … which is independent of the number of features" ([[mml-ch12-classification-svm|MML Ch 12]] §12.3, p. 383). Ideal when $D\gg N$.
- **Box constraints.** The inequalities $0\le\alpha_i\le C$ confine $\boldsymbol\alpha$ to an axis-aligned box, "particularly efficient to implement in numerical solvers" (Dostál 2009).
- **Inner products only.** The objective touches the data *only* through $\langle\mathbf{x}_i,\mathbf{x}_j\rangle$ — never between examples and parameters. This is precisely the hook for the [[KernelTrick|kernel trick]]: replace each $\langle\mathbf{x}_i,\mathbf{x}_j\rangle$ by a [[KernelFunction|kernel]] $k(\mathbf{x}_i,\mathbf{x}_j)$ and the SVM becomes nonlinear without ever computing the [[FeatureMap|feature map]] $\boldsymbol\phi$ ([[mml-ch12-classification-svm|MML Ch 12]] §12.4).

## Support vectors and recovering $b$

[[KKTConditions|Complementary slackness]] makes most $\alpha_n=0$; the examples with $\alpha_n>0$ are the [[SupportVector|support vectors]] that define $\mathbf{w}^*=\sum_n\alpha_ny_n\mathbf{x}_n$. The bias is recovered from any margin-boundary support vector ($0<\alpha_n<C$): $b^*=y_n-\langle\mathbf{w}^*,\mathbf{x}_n\rangle$ (Eq. 12.42); in practice take the median over support vectors.

## Convex-hull interpretation

[[mml-ch12-classification-svm|MML Ch 12]] §12.3.2 gives a third reading: build the **[[ConvexHull|convex hull]]** of each class ($\mathrm{conv}(\mathbf{X})=\{\sum_n\alpha_n\mathbf{x}_n:\sum_n\alpha_n=1,\alpha_n\ge0\}$, Eq. 12.43), find the closest points $\mathbf{c}$ (positive hull) and $\mathbf{d}$ (negative hull), and the optimal hyperplane bisects $\mathbf{w}=\mathbf{c}-\mathbf{d}$. The hull-coefficient constraints $\sum\alpha_n^+=\sum\alpha_n^-=1$ reproduce the dual equality $\sum_ny_n\alpha_n=0$ (Eqs. 12.49–12.51). The soft-margin dual corresponds to the **reduced hull** (the $C$ bound shrinks each hull).

## Standard-form QP for solvers

The dual is a convex [[QuadraticProgramming|quadratic program]]; in matrix form $\min_{\boldsymbol\alpha}\frac12\boldsymbol\alpha^\top\mathbf{Y}\mathbf{K}\mathbf{Y}\boldsymbol\alpha-\mathbf{1}^\top\boldsymbol\alpha$ with $K_{ij}=k(\mathbf{x}_i,\mathbf{x}_j)$ and $\mathbf{Y}=\mathrm{diag}(\mathbf{y})$ ([[mml-ch12-classification-svm|MML Ch 12]] §12.5, Eq. 12.57). Solved by LIBSVM (Chang & Lin 2011) or SVMlight (Joachims 1999).

## Connections

- [[mml-ch12-classification-svm]] — §12.3 canonical reference.
- [[SupportVectorMachine]] — the method; this is its dual formulation.
- [[SoftMarginSVM]] / [[HardMarginSVM]] — the primal problems being dualized.
- [[SupportVector]] — the $\alpha_n>0$ examples the dual exposes.
- [[LagrangianDuality]] / [[Lagrangian]] / [[Duality]] / [[KKTConditions]] — the Ch 7 machinery.
- [[KernelTrick]] / [[KernelFunction|Kernel]] / [[GramMatrix]] — what the inner-product-only structure enables.
- [[QuadraticProgramming]] / [[ConvexOptimization]] — the problem class.
- [[ConvexHull]] — the §12.3.2 geometric reading.
