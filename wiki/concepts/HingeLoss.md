---
title: "Hinge Loss"
type: concept
tags: [classification, loss-function, classical-ml, convex-optimization, foundational]
sources: [mml-ch12-classification-svm, mml-book]
last_updated: 2026-06-05
---

# Hinge Loss

The loss function that defines the [[SupportVectorMachine|SVM]] in its **loss-function-first** reading ([[mml-ch12-classification-svm|MML Ch 12]] §12.2.5, Eq. 12.28, p. 381):

$$\ell(t)=\max\{0,\,1-t\}\qquad\text{where}\quad t=y\,f(\mathbf{x})=y(\langle\mathbf{w},\mathbf{x}\rangle+b).$$

The argument $t$ is the **margin score**: positive when the prediction is on the correct side of the hyperplane, $\ge1$ when it is correct *and* at least a unit margin away.

## Behaviour across the three regimes

- $t\ge1$ — correct and beyond the margin: $\ell=0$ (no penalty).
- $0<t<1$ — correct but *inside* the margin: $\ell=1-t>0$ (penalized despite being correct).
- $t<0$ — wrong side of the hyperplane: $\ell$ grows linearly, $\ell=1-t>1$.

"We pay a penalty once we are closer than the margin to the hyperplane, even if the prediction is correct, and the penalty increases linearly" ([[mml-ch12-classification-svm|MML Ch 12]] §12.2.5, p. 381).

## A convex upper bound on the zero-one loss

The ideal classification loss is the **zero-one loss** $\mathbf{1}(f(\mathbf{x}_n)\ne y_n)$, but it yields a combinatorial (NP-hard) optimization. The hinge loss is the SVM's **convex surrogate**: it is a convex upper bound on the zero-one loss (Fig. 12.8, p. 382), so minimizing it is a tractable convex program. The squared loss used for [[LinearRegression|regression]] (§9) "is not suitable for binary classification" — the hinge is the binary-classification-appropriate loss.

## Three equivalent forms

[[mml-ch12-classification-svm|MML Ch 12]] (§12.2.5, §12.6, p. 393) records three interchangeable expressions, each convenient for a different purpose:

1. **Max form** (Eq. 12.28): $\ell(t)=\max\{0,1-t\}$ — used when comparing the SVM loss against other losses.
2. **Two-piece form** (Eq. 12.29): $\ell(t)=0$ if $t\ge1$, else $1-t$ — convenient for subgradients, since each piece is linear.
3. **Slack / constrained form** (Eq. 12.33): $\min_\xi\xi$ s.t. $\xi\ge0,\ \xi\ge1-t$ — enables casting the SVM as a convex [[QuadraticProgramming|quadratic program]].

The hard-margin limit is $\ell(t)=0$ if $t\ge1$ else $\infty$ (Eq. 12.30) — "never allowing any examples inside the margin" ([[HardMarginSVM]]).

## Regularized empirical risk = the soft-margin SVM

Minimizing total hinge loss with an $\ell_2$ regularizer recovers the [[SoftMarginSVM|soft-margin SVM]] ([[mml-ch12-classification-svm|MML Ch 12]] Eq. 12.31):

$$\min_{\mathbf{w},b}\ \underbrace{\tfrac12\|\mathbf{w}\|^2}_{\text{regularizer}} + \underbrace{C\sum_{n=1}^N\max\{0,1-y_n(\langle\mathbf{w},\mathbf{x}_n\rangle+b)\}}_{\text{error / loss term}}.$$

This is a textbook [[EmpiricalRiskMinimization|ERM]] instance: hypothesis class = hyperplanes, loss = hinge, regularizer = margin term. "Margin maximization can be interpreted as regularization" (§12.2.5, p. 382).

## Numerical solution: the subgradient

The hinge is non-differentiable only at the kink $t=1$. Its **subgradient** ([[mml-ch12-classification-svm|MML Ch 12]] §12.5, Eq. 12.54) is $g(t)=-1$ for $t<1$, the interval $[-1,0]$ at $t=1$, and $0$ for $t>1$ — enabling [[GradientDescent|(sub)gradient descent]] / [[StochasticGradientDescent|SGD]].

## Connections

- [[mml-ch12-classification-svm]] — §12.2.5 canonical reference.
- [[SupportVectorMachine]] / [[SoftMarginSVM]] — the model the hinge loss defines.
- [[HardMarginSVM]] — the $\infty$-penalty limiting loss (Eq. 12.30).
- [[LossFunction]] — the parent concept.
- [[EmpiricalRiskMinimization]] — the framework (hinge as the loss term).
- [[Regularization]] — the margin term as $\ell_2$ regularizer.
- [[StochasticGradientDescent]] — solves the hinge objective via the subgradient.
- [[CrossEntropyLoss]] / [[LogisticRegression]] — the calibrated-probability alternative loss (§12.6).
- [[HingeLossRanking]] — the ranking-loss relative.
