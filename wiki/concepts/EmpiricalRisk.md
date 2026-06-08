---
title: "Empirical Risk"
type: concept
tags: [learning-theory, optimization, foundational]
sources: [mml-ch08-when-models-meet-data, mml-book]
last_updated: 2026-06-04
---

# Empirical Risk

The **average [[LossFunction|loss]] over the finite training set** ([[mml-book]] §8.2.2, Eq. 8.6):

$$\mathbf{R}_{\text{emp}}(f,\mathbf{X},\mathbf{y})=\frac{1}{N}\sum_{n=1}^{N}\ell(y_n,\hat{y}_n),\qquad \hat{y}_n=f(\mathbf{x}_n,\boldsymbol\theta).$$

It depends on three arguments — the predictor $f$ and the data $\mathbf{X},\mathbf{y}$. Minimizing it is **[[EmpiricalRiskMinimization|empirical risk minimization]]**.

## Why the empirical mean is legitimate

The set of examples is assumed **[[IID|independent and identically distributed]]** ([[mml-book]] §6.4.5). Independence ⇒ the empirical mean is a good estimate of the population mean (§6.4.1), which is exactly the [[ExpectedRisk|expected risk]] $\mathbf{R}_{\text{true}}(f)$ that we actually care about.

## The gap that defines overfitting

Empirical risk is a **finite-sample proxy** for the [[ExpectedRisk|expected (true) risk]]. The trained predictor depends on the training set, so the training empirical risk $\mathbf{R}_{\text{emp}}(f,\mathbf{X}_{\text{train}},\mathbf{y}_{\text{train}})$ is a **biased** (optimistic) estimate of $\mathbf{R}_{\text{true}}(f)$. We estimate $\mathbf{R}_{\text{true}}$ with the empirical risk on a held-out **test set** $\mathbf{R}_{\text{emp}}(f,\mathbf{X}_{\text{test}},\mathbf{y}_{\text{test}})$; a test risk much larger than the training risk diagnoses [[Overfitting|overfitting]] ([[mml-book]] §8.2.3, p. 262).

## Connections

- [[mml-ch08-when-models-meet-data]] — §8.2.2 canonical reference (Eq. 8.6).
- [[mml-book]] — §8.2.2.
- [[ExpectedRisk]] — the population quantity this estimates; their difference is the [[GeneralizationGap]].
- [[EmpiricalRiskMinimization]] — minimizes this.
- [[LossFunction]] — what is averaged.
- [[Overfitting]] — diagnosed when training empirical risk ≪ test empirical risk.
- [[CrossValidation]] — averages empirical risk over multiple validation folds.
- [[Generalization]] — the broader goal empirical risk is a proxy for.
