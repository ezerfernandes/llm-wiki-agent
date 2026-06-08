---
title: "Loss Function"
type: concept
tags: [learning-theory, optimization, training, foundational]
sources: [mml-ch08-when-models-meet-data, mml-book]
last_updated: 2026-06-04
---

# Loss Function

A function $\ell(y_n,\hat{y}_n)\ge 0$ that takes a ground-truth label $y_n$ and a prediction $\hat{y}_n=f(\mathbf{x}_n,\boldsymbol\theta)$ and returns a **non-negative number** measuring how much error was made on that one prediction ([[mml-book]] §8.2.2, p. 259). The training goal is to minimize the **average** loss over the $N$ examples — the [[EmpiricalRisk|empirical risk]].

## Role in empirical risk minimization

The loss function is the **second of the four design choices** in [[EmpiricalRiskMinimization|ERM]] ([[mml-book]] §8.2.2), after the [[HypothesisClass|hypothesis class]] and before [[Regularization|regularization]] and the search procedure. It is "how we measure how well the predictor performs on the training data."

| Loss $\ell(y,\hat y)$ | Recovers |
|---|---|
| Squared $(y-\hat y)^2$ | Least-squares regression (Example 8.2, the [[DesignMatrix\|design-matrix]] normal equations) |
| Zero-one $\mathbb{I}(y\neq\hat y)$ | Misclassification rate |
| $-\log p(y\mid f(\mathbf{x};\boldsymbol\theta))$ | [[MaximumLikelihoodEstimation\|MLE]] / [[NegativeLogLikelihood\|NLL]] |
| Cross-entropy | MLE under a categorical likelihood |
| Hinge | [[SupportVectorMachine\|SVM]] (the §8.2 motivating example) |

## The probabilistic counterpart: the likelihood

[[mml-book]] §8.3 makes the load-bearing analogy explicit: in the probabilistic route, **the likelihood is analogous to the loss function** of ERM, and the prior is analogous to the regularizer. Choosing a Gaussian likelihood and taking the [[NegativeLogLikelihood|negative log-likelihood]] recovers the squared loss exactly (Example 8.5).

## Loss vs performance measure

§8.2.2 (Remark, p. 261): in principle the loss should equal the task's performance metric (accuracy, RMSE, cost-sensitive cost); in practice there is often a mismatch — the loss is chosen for ease of implementation or efficiency of optimization, and a separate, possibly non-differentiable performance measure is reported.

## Connections

- [[mml-ch08-when-models-meet-data]] — §8.2.2 canonical reference.
- [[mml-book]] — §8.2.2 / §8.3.
- [[EmpiricalRisk]] — the average of the loss over the training set.
- [[EmpiricalRiskMinimization]] — minimizes the empirical risk built from this loss.
- [[NegativeLogLikelihood]] — the probabilistic loss that recovers MLE.
- [[Regularization]] — the penalty added to the loss to combat [[Overfitting]].
- [[MaximumLikelihoodEstimation]] — ERM with the NLL loss.
