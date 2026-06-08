---
title: "Root Mean Square Error (RMSE)"
type: concept
tags: [regression, metrics, evaluation]
sources: [mml-ch09-linear-regression, mml-book]
last_updated: 2026-06-04
---

# Root Mean Square Error (RMSE)

A normalized, unit-matched regression error metric ([[mml-ch09-linear-regression|MML Ch 9]] §9.2.2, Eq. 9.23):

$$\text{RMSE} = \sqrt{\frac{1}{N}\,\|\mathbf{y}-\boldsymbol\Phi\boldsymbol\theta\|^2} = \sqrt{\frac{1}{N}\sum_{n=1}^N\big(y_n-\boldsymbol\phi^\top(\mathbf{x}_n)\boldsymbol\theta\big)^2}.$$

## Why RMSE rather than raw squared error

- **Normalized by $N$** — lets you compare errors across datasets of different sizes.
- **Same scale and units as the targets $y_n$** (MML margin: "the RMSE is normalized"). If a model maps (lat, lon) to house prices in EUR, the RMSE is in EUR, whereas the raw squared error is in EUR². By contrast the $\sigma^2$-scaled negative log-likelihood (MML Eq. 9.10b) is *unitless*.

## Use in model selection

Because RMSE (or the NLL) measures generalization on a held-out test set, sweeping it over a hyperparameter — e.g. the polynomial degree $M$ in [[PolynomialRegression|polynomial regression]] — exposes the [[Overfitting|overfitting]] curve: training RMSE falls monotonically with $M$, but test RMSE is U-shaped (minimized at $M=4$ in MML Fig. 9.6, then exploding). The minimizer of *test* RMSE is the selected model ([[ModelSelection]], §8.6).

## Connections

- [[mml-ch09-linear-regression]] / [[mml-book]] — §9.2.2 canonical reference (Eq. 9.23, Figs. 9.5–9.6).
- [[MeanSquaredError]] — RMSE is its square root.
- [[LeastSquares]] — the objective whose residuals RMSE summarizes.
- [[Overfitting]] / [[ModelSelection]] — RMSE as the generalization diagnostic.
- [[PolynomialRegression]] — degree selection via test RMSE.
