---
title: "Polynomial Regression"
type: concept
tags: [nonlinear, regression, feature-map]
sources: [islr-seventh-printing, d2l-linear-regression, mml-book, mml-ch09-linear-regression]
last_updated: 2026-06-04
---

# Polynomial Regression

[[LinearRegression|Linear regression]] with a polynomial [[FeatureMap|feature / basis]] $\{1, x, x^2, \dots, x^{d}\}$. It captures global curvature with a single degree $d$, but behaves badly at boundary regions for large $d$ — [[RegressionSplines]] and local methods are usually preferable.

## Why it is still "linear" regression

[[mml-ch09-linear-regression|MML Ch 9]] (Example 9.3) uses polynomial regression as the canonical demonstration that linear regression means **linear in the parameters, not the inputs**. The feature map

$$\boldsymbol\phi(x) = [1,\,x,\,x^2,\,\dots,\,x^{K-1}]^\top \in\mathbb{R}^K\qquad(\text{Eq. 9.14})$$

"lifts" a 1-D input into a $K$-dim monomial space, so $f(x)=\sum_{k=0}^{K-1}\theta_k x^k=\boldsymbol\phi^\top(x)\boldsymbol\theta$ (Eq. 9.15) is a degree-$(K\!-\!1)$ polynomial that is *linear in $\boldsymbol\theta$* — hence fit by a single matrix inversion via the [[NormalEquations|normal equations]] $\boldsymbol\theta_{\text{ML}}=(\boldsymbol\Phi^\top\boldsymbol\Phi)^{-1}\boldsymbol\Phi^\top\mathbf{y}$, with the [[DesignMatrix|feature matrix]] $\boldsymbol\Phi$ collecting rows $\boldsymbol\phi^\top(x_n)$ (Example 9.4 shows the second-order case, rows $[1,x_n,x_n^2]$). The constant feature $\phi_0(x)=1$ is the intercept / bias term.

## The overfitting case study

Polynomial degree $M$ is MML's running [[Overfitting|overfitting]] example (§9.2.2, Figs. 9.5–9.6): training [[RMSE]] falls monotonically with $M$, while test RMSE is U-shaped — minimized at $M=4$ for the demo, then exploding from $M=6$; at $M=N-1$ the polynomial interpolates every point but oscillates wildly. [[MAPEstimation|MAP]] / [[RidgeRegression|ridge]] (§9.2.3) keeps high-degree fits smoother, and [[BayesianLinearRegression|Bayesian linear regression]] (§9.3) exposes their huge predictive uncertainty (degree-5 prior over functions, Example 9.7).

## Connections
- [[mml-ch09-linear-regression]] / [[mml-book]] — Example 9.3 (Eqs. 9.14–9.15), §9.2.2 overfitting demo.
- [[islr-seventh-printing]] — Ch. 7.1.
- [[FeatureMap]] / [[BasisFunctions]] — the lifting frame.
- [[LinearRegression]] — the underlying linear-in-parameters model.
- [[Overfitting]] / [[RMSE]] — degree-selection diagnostics.
- [[RegressionSplines]] — local, well-behaved alternative.
