---
title: "Soft-Margin SVM"
type: concept
tags: [classification, classical-ml, convex-optimization, regularization, foundational]
sources: [mml-ch12-classification-svm, mml-book]
last_updated: 2026-06-05
---

# Soft-Margin SVM

The **violation-tolerant** [[SupportVectorMachine|SVM]] for data that is **not linearly separable**, obtained by relaxing the [[HardMarginSVM|hard-margin SVM]]'s constraints with [[SlackVariable|slack variables]] $\xi_n\ge0$ ([[mml-ch12-classification-svm|MML Ch 12]] §12.2.4, Eqs. 12.26a–c, p. 380):

$$\min_{\mathbf{w},b,\boldsymbol\xi}\ \tfrac12\|\mathbf{w}\|^2 + C\sum_{n=1}^N\xi_n \quad\text{s.t.}\quad y_n(\langle\mathbf{w},\mathbf{x}_n\rangle+b)\ge1-\xi_n,\ \ \xi_n\ge0.$$

Each $\xi_n$ measures how far example $\mathbf{x}_n$ intrudes past its margin boundary (Fig. 12.7): $\xi_n=0$ means correctly classified beyond the margin, $0<\xi_n\le1$ means inside the margin (still correct), $\xi_n>1$ means on the wrong side of the hyperplane. "The model that allows for some classification errors is called the soft margin SVM" (§12.2.4, p. 379).

## The regularization parameter $C$ (the "$C$-SVM")

$C>0$ "trades off the size of the margin and the total amount of slack that we have" ([[mml-ch12-classification-svm|MML Ch 12]] §12.2.4, p. 380). **Large $C$ = low regularization** — slack is penalized heavily, so the optimizer prioritizes correct classification over a wide margin; small $C$ permits more violations for a wider, smoother margin. This makes the soft-margin SVM also known as the **$C$-SVM**.

> **Quirk (inverse convention):** in the hinge-loss / [[EmpiricalRiskMinimization|ERM]] reading $C$ multiplies the *loss* term (Eq. 12.31), so it behaves as the **inverse** of the usual numerical-optimization regularization weight $\lambda$ that multiplies the *regularizer*. "Here a large value of $C$ implies low regularization" (§12.2.4 margin, p. 380). Roughly $C\leftrightarrow 1/(2\lambda)$.

The margin term $\frac12\|\mathbf{w}\|^2$ is the **regularizer**; this is the geometric-to-statistical bridge — "margin maximization can be interpreted as regularization" (§12.2.5, p. 382). Note that **$b$ is *not* regularized** (only $\mathbf{w}$), which "complicates theoretical analysis and decreases computational efficiency" (Steinwart & Christmann 2008; Fan et al. 2008).

## Equivalent to hinge-loss minimization

Substituting the slack out via $\xi_n=\max\{0,1-y_nf(\mathbf{x}_n)\}$ turns the soft-margin SVM into the unconstrained **regularized [[HingeLoss|hinge-loss]]** problem ([[mml-ch12-classification-svm|MML Ch 12]] §12.2.5, Eq. 12.31):

$$\min_{\mathbf{w},b}\ \tfrac12\|\mathbf{w}\|^2 + C\sum_{n=1}^N\max\{0,1-y_n(\langle\mathbf{w},\mathbf{x}_n\rangle+b)\}.$$

The equivalence holds because $\min_t\max\{0,1-t\}$ equals $\min_{\xi}\xi$ s.t. $\xi\ge0,\ \xi\ge1-t$ (Eqs. 12.32–12.33). This is the **loss-function-first** reading of the SVM and the form most naturally solved by [[StochasticGradientDescent|SGD]] on the subgradient (§12.5).

## Convex QP; solved via the dual

Like the hard-margin case, the soft-margin SVM is a **convex [[QuadraticProgramming|quadratic program]]** with no closed form. Its [[LagrangianDuality|Lagrangian dual]] is the [[DualSVM|dual SVM]] $\min_{\boldsymbol\alpha}\frac12\sum_{i,j}y_iy_j\alpha_i\alpha_j\langle\mathbf{x}_i,\mathbf{x}_j\rangle-\sum_i\alpha_i$ s.t. $\sum_iy_i\alpha_i=0$ and the **box constraint** $0\le\alpha_i\le C$ — the slack penalty $C$ becomes the upper bound on the dual multipliers ([[mml-ch12-classification-svm|MML Ch 12]] §12.3.1, Eq. 12.41). The convex-hull reading uses the **reduced hull** (§12.3.2): the bound on $\boldsymbol\alpha$ shrinks each class hull.

## Connections

- [[mml-ch12-classification-svm]] — §12.2.4 canonical reference.
- [[HardMarginSVM]] — the separable-data special case ($C\to\infty$, no slack).
- [[SlackVariable]] — the $\xi_n$ that measure violations.
- [[SupportVectorMachine]] — the umbrella method.
- [[HingeLoss]] — the equivalent unconstrained loss.
- [[DualSVM]] / [[SupportVector]] — the dual with box constraint $0\le\alpha_n\le C$.
- [[Regularization]] / [[ConvexOptimization]] / [[QuadraticProgramming]] — the optimization framing.
- [[SupportVectorClassifier]] — the ISLR name for the soft-margin classifier.
