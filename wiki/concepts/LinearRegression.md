---
title: "Linear Regression"
type: concept
tags: [classical-ml, regression]
sources: [islr-seventh-printing, mml-book, mml-ch09-linear-regression, d2l-linear-regression]
last_updated: 2026-05-16
---

# Linear Regression

A model predicting a continuous target as a linear combination of features ($\hat y = \mathbf{w}^\top\mathbf{x} + b$), fit either by the closed-form normal equation $\mathbf{w}^* = (\mathbf{X}^\top\mathbf{X})^{-1}\mathbf{X}^\top\mathbf{y}$ (requires full column rank) or by minibatch [[StochasticGradientDescent|SGD]] minimizing [[MeanSquaredError|squared loss]]. The simplest interpretable baseline; foundational to [[statsmodels]], extends to [[LogisticRegression]] for classification.

## Three corpora, one model

- **[[islr-seventh-printing|ISLR]] Ch.3** — "fundamental starting point for all regression methods"; paired with [[KNearestNeighbors]] as the parametric / non-parametric contrast (§3.5).
- **[[mml-book|MML]] §9** — derives the closed form from Gaussian-NLL minimization; explicit gradient-zero derivation (§9.2.1, Eq. 9.12c).
- **[[d2l-linear-regression|D2L]] §3** — the canonical *neural-network-style* introduction: linear regression as a single-layer fully-connected net, motivating [[MinibatchSGD|minibatch SGD]] as the universal DL optimizer even on a problem with a closed-form solution. Introduces D2L's [[Module]] / [[DataModule]] / [[Trainer]] OO scaffold here.

## The probabilistic motivation

Under additive Gaussian noise $y = \mathbf{w}^\top\mathbf{x} + b + \epsilon,\ \epsilon\sim\mathcal{N}(0,\sigma^2)$, minimizing [[MeanSquaredError|MSE]] is exactly [[MaximumLikelihoodEstimation|maximum likelihood estimation]] — the link to [[GeneralizedLinearModels|GLMs]] and the bridge to classification via [[LogisticRegression]].

## From [[mml-ch09-linear-regression|MML Ch 9]]

[[mml-ch09-linear-regression|MML Ch 9]] is the book's full deep-dive — linear regression as the **first of the four ML pillars**, fusing all six mathematical foundations. The defining claim: linear regression means **"linear in the parameters, not the inputs"** (§9.2, p. 295) — an arbitrary nonlinear [[FeatureMap|feature map]] $\boldsymbol\phi(\mathbf{x})$ (e.g. polynomial monomials) keeps the model linear-in-$\boldsymbol\theta$ and closed-form-solvable. The chapter builds the full inferential ladder on the Gaussian [[NoiseModel|noise model]] $p(y\mid\mathbf{x},\boldsymbol\theta)=\mathcal{N}(\boldsymbol\phi^\top(\mathbf{x})\boldsymbol\theta,\sigma^2)$:

1. **[[MaximumLikelihoodEstimation|MLE]] = [[LeastSquares|least squares]]**, via the [[NormalEquations|normal equations]] $\boldsymbol\theta_{\text{ML}}=(\boldsymbol\Phi^\top\boldsymbol\Phi)^{-1}\boldsymbol\Phi^\top\mathbf{y}$ (§9.2.1, Eqs. 9.12/9.19) — unique global minimum since the Hessian $\boldsymbol\Phi^\top\boldsymbol\Phi$ is PD.
2. **[[Overfitting|Overfitting]]** of high-degree [[PolynomialRegression|polynomial]] MLE (§9.2.2; test [[RMSE]] minimized at degree $M=4$, Fig. 9.6) motivates
3. **[[MAPEstimation|MAP]] = [[RidgeRegression|ridge / regularized least squares]]** $\boldsymbol\theta_{\text{MAP}}=(\boldsymbol\Phi^\top\boldsymbol\Phi+\tfrac{\sigma^2}{b^2}\mathbf{I})^{-1}\boldsymbol\Phi^\top\mathbf{y}$ (§9.2.3–9.2.4, Eq. 9.31), the regularizer being a negative-log Gaussian prior.
4. **[[BayesianLinearRegression]]** (§9.3) integrates $\boldsymbol\theta$ out entirely — closed-form Gaussian posterior, [[PosteriorPredictiveDistribution|posterior predictive]] with calibrated uncertainty, and the [[MarginalLikelihood|marginal likelihood]].
5. **MLE *is* [[OrthogonalProjection|orthogonal projection]]** of $\mathbf{y}$ onto $\text{col}(\boldsymbol\Phi)$ (§9.4, geometric reading).

MML's model is **bias-free** ($f(\mathbf{x})=\mathbf{x}^\top\boldsymbol\theta$, lines through the origin) — an intercept is recovered only by the §8.1 augmentation $\phi_0\equiv 1$, unlike the explicit-$b$ convention of [[d2l-linear-regression|D2L]]/[[islr-seventh-printing|ISLR]].

## Connections
- [[mml-ch09-linear-regression]] — canonical book deep-dive (§9.1–9.5).
- [[MeanSquaredError]] — the loss function.
- [[StochasticGradientDescent]] / [[MinibatchSGD]] — practical optimizer.
- [[MaximumLikelihoodEstimation]] — squared loss as Gaussian MLE.
- [[NormalEquations]] / [[LeastSquares]] — closed-form solver + objective.
- [[RidgeRegression]] / [[WeightDecay]] / [[Lasso]] — regularized variants.
- [[BayesianLinearRegression]] — full-posterior counterpart.
- [[PolynomialRegression]] — basis-expanded variant.
- [[OrthogonalProjection]] — geometric reading of the MLE.
