---
title: "Ridge Regression"
type: concept
tags: [regularization, regression, shrinkage, least-squares]
sources: [islr-seventh-printing, d2l-linear-regression, mml-book, mml-ch09-linear-regression]
last_updated: 2026-06-04
---

# Ridge Regression

[[LinearRegression|Linear regression]] with an $\ell_2$ penalty (a.k.a. **Tikhonov regularization** / weight decay): minimize the [[LeastSquares|regularized least-squares]] loss

$$\|\mathbf{y}-\boldsymbol\Phi\boldsymbol\theta\|_2^2 + \lambda\|\boldsymbol\theta\|_2^2,\qquad \lambda\geq 0.$$

Shrinks all coefficients toward zero but never exactly to zero — no variable selection (that is [[Lasso|LASSO]], the $\ell_1$ counterpart). Trades a small increase in bias for a large decrease in variance; particularly effective when the number of predictors is comparable to $N$ or predictors are collinear. The strength $\lambda$ is tuned by [[CrossValidation]].

## Closed form & why it always exists

The [[NormalEquations|normal equations]] become $(\boldsymbol\Phi^\top\boldsymbol\Phi+\lambda\mathbf{I})\boldsymbol\theta=\boldsymbol\Phi^\top\mathbf{y}$, giving

$$\boldsymbol\theta_{\text{RLS}} = (\boldsymbol\Phi^\top\boldsymbol\Phi+\lambda\mathbf{I})^{-1}\boldsymbol\Phi^\top\mathbf{y}\qquad(\text{[[mml-ch09-linear-regression|MML]] Eq. 9.34}).$$

Unlike OLS, this **inverse always exists**: $\boldsymbol\Phi^\top\boldsymbol\Phi$ is only positive *semi*-definite, but adding $\lambda\mathbf{I}$ makes it strictly positive definite — so ridge also rescues the **under-determined** case ($N<K$, collinear columns) where OLS fails. This is the same $\epsilon\mathbf{I}$ "jitter" added for numerical stability in [[OrthogonalProjection|projection]] computations (MML §3.8.2).

## Ridge = MAP under a Gaussian prior

[[mml-ch09-linear-regression|MML Ch 9]] §9.2.3–9.2.4 derives the deep identity: ridge regression **is** [[MAPEstimation|MAP]] estimation with a zero-mean Gaussian prior $p(\boldsymbol\theta)=\mathcal{N}(\mathbf{0},b^2\mathbf{I})$. The penalty $\lambda\|\boldsymbol\theta\|_2^2$ is the negative log-prior $\frac{1}{2b^2}\|\boldsymbol\theta\|_2^2$ (Eq. 9.33), so $\boldsymbol\theta_{\text{RLS}}=\boldsymbol\theta_{\text{MAP}}$ when $\lambda=\frac{\sigma^2}{b^2}$ (matching MAP Eq. 9.31). This is the chapter's concrete instance of the [[Regularization|prior ↔ regularizer]] correspondence. Going one step further to the full posterior gives [[BayesianLinearRegression|Bayesian linear regression]], whose posterior precision $\mathbf{S}_N^{-1}=\mathbf{S}_0^{-1}+\sigma^{-2}\boldsymbol\Phi^\top\boldsymbol\Phi$ contains the same regularized Gram matrix.

## Notational note on $\lambda$

Conventions differ in the $\frac12$ and $\sigma^2$ bookkeeping: [[islr-seventh-printing|ISLR]] writes $\|y-X\beta\|_2^2+\lambda\|\beta\|_2^2$; MML's MAP uses prior variance $b^2$ giving the inverse term $\frac{\sigma^2}{b^2}\mathbf{I}$; the RLS↔neg-log-prior identity holds at $\lambda=\frac{1}{2b^2}$ (Eq. 9.33). When comparing $\lambda$ values across sources, check the loss scaling.

## Connections
- [[mml-ch09-linear-regression]] / [[mml-book]] — §9.2.3–9.2.4 (ridge = Gaussian-prior MAP, Eqs. 9.31–9.34).
- [[islr-seventh-printing]] — Ch. 6.2.1.
- [[d2l-linear-regression]] — §3.7 ([[WeightDecay|weight decay]]).
- [[MAPEstimation]] — ridge is MAP under a Gaussian prior.
- [[Lasso]] — $\ell_1$ counterpart that performs variable selection.
- [[NormalEquations]] / [[LeastSquares]] — the (regularized) solver and objective.
- [[BayesianLinearRegression]] — full-posterior generalization.
- [[Regularization]] — the broader family.
- [[CrossValidation]] — selects $\lambda$.
- [[LinearRegression]] — the unpenalized base model.
