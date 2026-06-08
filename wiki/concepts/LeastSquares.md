---
title: "Least Squares"
type: concept
tags: [regression, optimization, least-squares, foundational]
sources: [mml-ch09-linear-regression, mml-book]
last_updated: 2026-06-04
---

# Least Squares (Ordinary / Regularized)

Fitting a model by **minimizing the sum of squared residuals**. For [[LinearRegression|linear regression]], ordinary least squares (OLS) minimizes

$$\mathcal{L}_{\text{OLS}}(\boldsymbol\theta) = \|\mathbf{y}-\boldsymbol\Phi\boldsymbol\theta\|^2 = \sum_{n=1}^N\big(y_n-\boldsymbol\phi^\top(\mathbf{x}_n)\boldsymbol\theta\big)^2,$$

solved in closed form by the [[NormalEquations|normal equations]] $\boldsymbol\theta_{\text{ML}}=(\boldsymbol\Phi^\top\boldsymbol\Phi)^{-1}\boldsymbol\Phi^\top\mathbf{y}$ ([[mml-ch09-linear-regression|MML Ch 9]] §9.2, Eqs. 9.10/9.19).

## Least squares = Gaussian MLE

Under additive zero-mean Gaussian [[NoiseModel|noise]] $\epsilon\sim\mathcal{N}(0,\sigma^2)$, the negative log-likelihood is $\mathcal{L}(\boldsymbol\theta)=\frac{1}{2\sigma^2}\|\mathbf{y}-\boldsymbol\Phi\boldsymbol\theta\|^2+\text{const}$ ([[mml-ch09-linear-regression|MML]] Eq. 9.10), so **minimizing squared error is exactly [[MaximumLikelihoodEstimation|maximum likelihood estimation]]** with fixed variance. The $\frac{1}{2\sigma^2}$ scaling does not change the minimizer — which is why the noise-free squared-error loss $\|\mathbf{y}-\boldsymbol\Phi\boldsymbol\theta\|^2$ and the NLL give the same $\boldsymbol\theta_{\text{ML}}$.

## RMSE — the reported error

The raw squared error has units of (target)$^2$ and scales with $N$. The [[RMSE|root mean square error]] $\sqrt{\frac1N\|\mathbf{y}-\boldsymbol\Phi\boldsymbol\theta\|^2}$ (MML Eq. 9.23) is normalized and unit-matched to the targets, so it can compare datasets of different sizes (the $\sigma^2$-scaled NLL is by contrast *unitless*).

## Regularized least squares (ridge / Tikhonov)

Adding an $\ell_2$ penalty gives **regularized least squares** $\|\mathbf{y}-\boldsymbol\Phi\boldsymbol\theta\|^2+\lambda\|\boldsymbol\theta\|_2^2$ (MML Eq. 9.32) with solution $\boldsymbol\theta_{\text{RLS}}=(\boldsymbol\Phi^\top\boldsymbol\Phi+\lambda\mathbf{I})^{-1}\boldsymbol\Phi^\top\mathbf{y}$ (Eq. 9.34) — see [[RidgeRegression]]. The data-fit term is also called the **misfit term**; the penalty is the **regularizer**. This is the [[MAPEstimation|MAP]] estimate under a Gaussian prior, and the [[Regularization|prior ↔ regularizer]] correspondence from [[mml-ch08-when-models-meet-data|MML Ch 8]]. With a general $p$-norm and $p=1$ it becomes [[Lasso|LASSO]] (sparse / variable selection).

## Geometry

OLS *is* an [[OrthogonalProjection|orthogonal projection]]: $\boldsymbol\Phi\boldsymbol\theta_{\text{ML}}$ is the projection of $\mathbf{y}$ onto the column space of the [[DesignMatrix|design matrix]] $\boldsymbol\Phi$ — the subspace point closest to $\mathbf{y}$ in squared distance ([[mml-ch09-linear-regression|MML]] §9.4, Eqs. 9.66–9.71).

## Connections

- [[mml-ch09-linear-regression]] / [[mml-book]] — §9.2 (OLS), §9.2.2 (RMSE), §9.2.4 (RLS), §9.4 (projection).
- [[NormalEquations]] — the closed-form solver.
- [[MaximumLikelihoodEstimation]] — least squares = Gaussian MLE.
- [[RidgeRegression]] / [[Regularization]] / [[Lasso]] — penalized variants.
- [[OrthogonalProjection]] — geometric meaning.
- [[MeanSquaredError]] / [[RMSE]] — the (normalized) error metrics.
- [[DesignMatrix]] / [[FeatureMap]] — the inputs.
- [[LinearRegression]] — the model.
