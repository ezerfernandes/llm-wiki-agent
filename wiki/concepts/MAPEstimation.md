---
title: "MAP Estimation"
type: concept
tags: [bayesian-inference, foundational, parameter-estimation]
sources: [mml-book, mml-ch08-when-models-meet-data, mml-ch09-linear-regression]
last_updated: 2026-06-04
---

# Maximum A Posteriori (MAP) Estimation

A point estimate of the parameters $\boldsymbol\theta$ that maximizes the **posterior** $p(\boldsymbol\theta\mid\mathcal{D})$ instead of the likelihood $p(\mathcal{D}\mid\boldsymbol\theta)$ ([[mml-book]] §8.3):

$$\boldsymbol\theta_{\text{MAP}} = \arg\max_{\boldsymbol\theta}\,p(\boldsymbol\theta\mid\mathcal{D}) = \arg\max_{\boldsymbol\theta}\,[\log p(\mathcal{D}\mid\boldsymbol\theta) + \log p(\boldsymbol\theta)].$$

## MAP vs MLE

MAP differs from [[MaximumLikelihoodEstimation|MLE]] by the additional $\log p(\boldsymbol\theta)$ term — the log-prior. As prior beliefs become more diffuse (i.e., approach uniform), MAP collapses to MLE.

## MAP ≡ regularized MLE

The most useful reading of MAP for ML practitioners:

| Prior on $\boldsymbol\theta$ | MAP recovers |
|---|---|
| Gaussian $\mathcal{N}(\mathbf{0}, \sigma_0^2\mathbf{I})$ | **Ridge regression** ($\ell_2$ weight decay) |
| Laplace prior | **Lasso** ($\ell_1$ sparsity) |
| Uniform / improper flat | MLE |

The "regularization strength" hyperparameter $\lambda$ is the variance of the prior in disguise (with $\lambda\propto 1/\sigma_0^2$).

## MAP vs full Bayesian inference

MAP is a **point estimate** — it picks a single $\boldsymbol\theta$ and discards the rest of the posterior. Full Bayesian inference instead retains $p(\boldsymbol\theta\mid\mathcal{D})$ and integrates it into predictions:

$$p(\mathbf{x}_*\mid\mathcal{D}) = \int p(\mathbf{x}_*\mid\boldsymbol\theta)\,p(\boldsymbol\theta\mid\mathcal{D})\,d\boldsymbol\theta.$$

MAP underestimates predictive uncertainty because it ignores parameter uncertainty. [[BayesianLinearRegression]] ([[mml-book]] §9.3) is the worked example of going beyond MAP to the full integral — analytically tractable when priors are conjugate.

## From [[mml-ch08-when-models-meet-data|MML Ch 8]]

[[mml-ch08-when-models-meet-data|MML Ch 8]] §8.3.2 derives MAP from Bayes' theorem (Eq. 8.19): with a [[Prior|prior]] $p(\boldsymbol\theta)$ multiplied onto the [[Likelihood|likelihood]], the [[Posterior|posterior]] is $p(\boldsymbol\theta\,|\,\mathbf{x})=\frac{p(\mathbf{x}\,|\,\boldsymbol\theta)p(\boldsymbol\theta)}{p(\mathbf{x})}$; since the denominator $p(\mathbf{x})$ is independent of $\boldsymbol\theta$, maximizing the posterior reduces to $p(\boldsymbol\theta\,|\,\mathbf{x})\propto p(\mathbf{x}\,|\,\boldsymbol\theta)p(\boldsymbol\theta)$ (Eq. 8.20), i.e. **minimizing the negative log-posterior** (the [[NegativeLogLikelihood|NLL]] plus a negative-log-prior). The chapter's load-bearing analogy: **the prior is to MAP what [[Regularization|regularization]] is to [[EmpiricalRiskMinimization|ERM]]** (§8.3 intro). Example 8.6 uses a zero-mean Gaussian prior (conjugate to the Gaussian likelihood) so the posterior is Gaussian; Fig. 8.6 shows the prior biasing the regression slope flatter and the intercept toward zero. MML states the role precisely: *"Maximum a posteriori estimation can be considered to bridge the non-probabilistic and probabilistic worlds as it explicitly acknowledges the need for a prior distribution but it still only produces a point estimate of the parameters"* (§8.3.2, p. 269) — full [[BayesianInference|Bayesian inference]] (§8.4) takes the next step of integrating over $\boldsymbol\theta$.

## From [[mml-ch09-linear-regression|MML Ch 9]]

[[mml-ch09-linear-regression|MML Ch 9]] §9.2.3–9.2.4 is the **worked closed-form MAP** for linear regression and its identification with ridge regression. With a conjugate Gaussian prior $p(\boldsymbol\theta)=\mathcal{N}(\mathbf{0},b^2\mathbf{I})$, the negative log-posterior is $\frac{1}{2\sigma^2}\|\mathbf{y}-\boldsymbol\Phi\boldsymbol\theta\|^2+\frac{1}{2b^2}\boldsymbol\theta^\top\boldsymbol\theta+\text{const}$ (Eq. 9.28); zeroing its gradient gives
$$\boldsymbol\theta_{\text{MAP}}=\left(\boldsymbol\Phi^\top\boldsymbol\Phi+\tfrac{\sigma^2}{b^2}\mathbf{I}\right)^{-1}\boldsymbol\Phi^\top\mathbf{y}\quad(\text{Eq. 9.31}).$$
The **only difference from the [[MaximumLikelihoodEstimation|MLE]]** (Eq. 9.19) is the $\frac{\sigma^2}{b^2}\mathbf{I}$ term, which makes the matrix strictly positive definite (so the inverse always exists, even when $\boldsymbol\Phi^\top\boldsymbol\Phi$ is only PSD / underdetermined) and reflects the regularizer. §9.2.4 then shows this **equals [[RidgeRegression|regularized least squares]]** $\boldsymbol\theta_{\text{RLS}}=(\boldsymbol\Phi^\top\boldsymbol\Phi+\lambda\mathbf{I})^{-1}\boldsymbol\Phi^\top\mathbf{y}$ (Eq. 9.34) at $\lambda=\frac{\sigma^2}{b^2}$, with the regularizer $\lambda\|\boldsymbol\theta\|_2^2$ identified as a negative-log Gaussian prior (Eq. 9.33). The §9.3 [[BayesianLinearRegression|Bayesian]] posterior is Gaussian, so $\boldsymbol\theta_{\text{MAP}}=\mathbf{m}_N$ (its mean) and the MAP prediction equals the [[PosteriorPredictiveDistribution|posterior-predictive]] mean (p. 308) — MAP is the point-estimate shadow of the full posterior.

## Connections

- [[mml-book]] — §8.3 canonical reference.
- [[mml-ch09-linear-regression]] — §9.2.3–9.2.4 closed-form MAP = ridge (Eq. 9.31).
- [[MaximumLikelihoodEstimation]] — MAP collapses to this under uniform prior.
- [[BayesianLinearRegression]] — full-Bayesian alternative.
- [[ConjugatePrior]] — when the full Bayesian integral has a closed form.
- [[RidgeRegression]] — MAP with Gaussian prior.
- [[EmpiricalRiskMinimization]] — MAP can be cast as regularized ERM.
