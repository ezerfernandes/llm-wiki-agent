---
title: "Gaussian Distribution"
type: concept
tags: [probability, distributions, foundational]
sources: [mml-book, d2l-appendix-mathematics, mml-ch06-probability-and-distributions, mml-ch11-density-estimation-gmm]
last_updated: 2026-06-05
---

# Gaussian Distribution

The univariate Gaussian (or normal) density:

$$p(x\mid\mu,\sigma^2) = \frac{1}{\sqrt{2\pi\sigma^2}}\exp\!\left(-\frac{(x-\mu)^2}{2\sigma^2}\right).$$

The multivariate Gaussian on $\mathbb{R}^D$:

$$p(\mathbf{x}\mid\boldsymbol\mu,\boldsymbol\Sigma) = (2\pi)^{-D/2}\,|\boldsymbol\Sigma|^{-1/2}\,\exp\!\left(-\tfrac{1}{2}(\mathbf{x}-\boldsymbol\mu)^\top\boldsymbol\Sigma^{-1}(\mathbf{x}-\boldsymbol\mu)\right).$$

Parameterized by mean $\boldsymbol\mu\in\mathbb{R}^D$ and symmetric positive-definite covariance $\boldsymbol\Sigma\in\mathbb{R}^{D\times D}$ ([[mml-book]] §6.5).

## Why Gaussians are everywhere in ML

- **Closure under marginalization, conditioning, and linear transformations**: every operation a probabilistic ML algorithm needs on a Gaussian yields another Gaussian in closed form. This is the property that makes Bayesian linear regression, Kalman filters, and Gaussian processes analytically tractable.
- **Conjugate to itself for the mean**: Gaussian likelihood × Gaussian prior on the mean = Gaussian posterior (§6.6) — see [[ConjugatePrior]].
- **Maximum-entropy distribution** given a fixed mean and variance: the "least committal" choice under those constraints.
- **Central limit theorem**: sums of independent RVs converge to a Gaussian — the empirical justification for using it as a noise model.

## Standard ML uses

- **[[LinearRegression]]** ([[mml-book]] Ch 9): the noise model $\epsilon\sim\mathcal{N}(0,\sigma^2)$ makes least-squares = MLE.
- **[[GaussianMixtureModel|GMM]]** (Ch 11): mixtures of Gaussians give multimodal density estimates.
- **[[BayesianLinearRegression]]** (§9.3): Gaussian prior + Gaussian likelihood ⇒ closed-form Gaussian posterior.
- **[[VariationalAutoencoder|VAE]]** prior + posterior ansatz.
- **Score matching / diffusion models**: Gaussian noise schedule with closed-form perturbation kernels.

## Sampling and density evaluation

- **Sampling**: factor $\boldsymbol\Sigma = \mathbf{L}\mathbf{L}^\top$ via [[CholeskyDecomposition]]; sample $\mathbf{z}\sim\mathcal{N}(\mathbf{0},\mathbf{I})$; return $\boldsymbol\mu + \mathbf{L}\mathbf{z}$.
- **Log-density** is quadratic in $\mathbf{x}$ ⇒ minimizing NLL = solving a least-squares / quadratic problem.

## From [[mml-ch06-probability-and-distributions|MML Ch 6]]

[[mml-book]] §6.5 (book pp. 197–204) develops the Gaussian as *the* continuous distribution of ML, prized for its closed-form behaviour under every operation inference needs. Univariate density Eq. 6.62; multivariate Eq. 6.63 (with $\boldsymbol\mu=\mathbf 0,\boldsymbol\Sigma=\mathbf I$ the **standard normal**). It "arises naturally when we consider sums of i.i.d. random variables — the central limit theorem" (margin, p. 197).

- **Marginals and conditionals are Gaussian** (§6.5.1). For a joint $\mathcal{N}\big(\big[\begin{smallmatrix}\boldsymbol\mu_x\\\boldsymbol\mu_y\end{smallmatrix}\big],\big[\begin{smallmatrix}\boldsymbol\Sigma_{xx}&\boldsymbol\Sigma_{xy}\\\boldsymbol\Sigma_{yx}&\boldsymbol\Sigma_{yy}\end{smallmatrix}\big]\big)$ (Eq. 6.64): the **conditional** $p(\mathbf x\mid\mathbf y)=\mathcal{N}(\boldsymbol\mu_{x\mid y},\boldsymbol\Sigma_{x\mid y})$ with $\boldsymbol\mu_{x\mid y}=\boldsymbol\mu_x+\boldsymbol\Sigma_{xy}\boldsymbol\Sigma_{yy}^{-1}(\mathbf y-\boldsymbol\mu_y)$ (Eq. 6.66) and $\boldsymbol\Sigma_{x\mid y}=\boldsymbol\Sigma_{xx}-\boldsymbol\Sigma_{xy}\boldsymbol\Sigma_{yy}^{-1}\boldsymbol\Sigma_{yx}$ (Eq. 6.67); the **marginal** $p(\mathbf x)=\mathcal{N}(\boldsymbol\mu_x,\boldsymbol\Sigma_{xx})$ just reads off the relevant block (Eq. 6.68). The **Kalman filter** is "nothing but computing Gaussian conditionals" (p. 199); Gaussian processes condition jointly Gaussian function values on data.
- **Product of two Gaussian densities is a scaled Gaussian** (§6.5.2). $\mathcal{N}(\mathbf x\mid\mathbf a,\mathbf A)\mathcal{N}(\mathbf x\mid\mathbf b,\mathbf B)=c\,\mathcal{N}(\mathbf x\mid\mathbf c,\mathbf C)$ with $\mathbf C=(\mathbf A^{-1}+\mathbf B^{-1})^{-1}$, $\mathbf c=\mathbf C(\mathbf A^{-1}\mathbf a+\mathbf B^{-1}\mathbf b)$, scaling $c=\mathcal{N}(\mathbf a\mid\mathbf b,\mathbf A+\mathbf B)$ (Eqs. 6.74–6.77) — the likelihood×prior step behind Gaussian conjugacy.
- **Sums and linear transforms stay Gaussian** (§6.5.3). For independent Gaussians $p(\mathbf x+\mathbf y)=\mathcal{N}(\boldsymbol\mu_x+\boldsymbol\mu_y,\boldsymbol\Sigma_x+\boldsymbol\Sigma_y)$ (Eq. 6.78); **any** affine map $\mathbf y=\mathbf A\mathbf x$ gives $p(\mathbf y)=\mathcal{N}(\mathbf A\boldsymbol\mu,\mathbf A\boldsymbol\Sigma\mathbf A^\top)$ (Eqs. 6.86–6.88). Theorem 6.12 gives the mean/variance of a *mixture* and surfaces the **law of total variance** (Eq. 6.85c).
- **Sampling** (§6.5.4): uniform PRNG → Box–Müller → $\mathcal{N}(\mathbf 0,\mathbf I)$; then factor $\boldsymbol\Sigma=\mathbf A\mathbf A^\top$ via [[CholeskyDecomposition|Cholesky]] and return $\mathbf y=\mathbf A\mathbf x+\boldsymbol\mu$.
- **As an exponential-family member** (§6.6.3, Example 6.13): sufficient statistics $\boldsymbol\phi(x)=[x,x^2]^\top$, [[NaturalParameters|natural parameters]] $\boldsymbol\theta=[\mu/\sigma^2,-1/(2\sigma^2)]^\top$.

Because a Gaussian is fully specified by its [[Mean|mean]] and [[CovarianceMatrix|covariance]], transformations are often computed by transforming just those two moments — variable transformations (§6.7) are frequently unnecessary.

## From [[mml-ch11-density-estimation-gmm|MML Ch 11]] (the Gaussian as a mixture base component)

[[mml-ch11-density-estimation-gmm|MML Ch 11]] uses the Gaussian as the **base component of a [[GaussianMixtureModel|mixture]]** (Eq. 11.3), explicitly because a single Gaussian has "limited modeling capabilities" — it is unimodal and cannot represent the clustered Fig. 11.1 data (p. 348–349). The log-density form $\log\mathcal N(\mathbf x\mid\boldsymbol\mu,\boldsymbol\Sigma)=-\tfrac D2\log(2\pi)-\tfrac12\log\det\boldsymbol\Sigma-\tfrac12(\mathbf x-\boldsymbol\mu)^\top\boldsymbol\Sigma^{-1}(\mathbf x-\boldsymbol\mu)$ (Eq. 11.11) is precisely what makes **single**-Gaussian MLE closed-form — and its inability to simplify the *mixture* log-likelihood (the $\log$ stuck outside the sum over components) is what forces the [[EMAlgorithm|EM algorithm]]. Each [[MixtureComponent|component]]'s mean and covariance are then re-estimated by responsibility-weighted Gaussian MLE in the M-step (Thms 11.1–11.2). The matrix-calculus derivative of the Gaussian's $\det(\boldsymbol\Sigma)^{-1/2}$ and quadratic form (Eqs. 11.33–11.34) drives the covariance update.

## Connections

- [[mml-ch06-probability-and-distributions]] — §6.5 deep dive.
- [[mml-ch11-density-estimation-gmm]] — Ch 11, the Gaussian as a GMM base component.
- [[mml-book]] — §6.5 canonical reference.
- [[CovarianceMatrix]] / [[Mean]] — the two parameters that fully specify it.
- [[ConjugatePrior]] — Gaussians are self-conjugate.
- [[ExponentialFamily]] — Gaussian is the prototypical exponential-family member.
- [[NaturalParameters]] — its natural-parameter form.
- [[CholeskyDecomposition]] — sampling primitive.
- [[GaussianMixtureModel]] — multimodal extension.
- [[ChangeOfVariables]] — closed under linear transforms (Example 6.17).
- [[BayesianLinearRegression]] — Gaussian-conjugacy application.
