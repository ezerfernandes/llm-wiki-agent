---
title: "EM Algorithm"
type: concept
tags: [optimization, density-estimation, foundational]
sources: [mml-ch11-density-estimation-gmm, mml-book]
last_updated: 2026-06-05
---

# Expectation-Maximization (EM) Algorithm

An iterative scheme for **maximum-likelihood estimation under latent variables**. [[mml-book]] Ch 11 develops EM as the workaround for the no-closed-form MLE of [[GaussianMixtureModel|GMMs]]: the log-likelihood $\sum_n\log\sum_k\pi_k\mathcal{N}(\mathbf{x}_n\mid\boldsymbol\mu_k,\boldsymbol\Sigma_k)$ can't have the log enter the sum over $k$ (p. 351), so no closed form exists.

## The two steps

For GMM specifically ([[mml-book]] §11.2–11.3):

**E-step** — given current parameters $\boldsymbol\theta = \{\pi_k, \boldsymbol\mu_k, \boldsymbol\Sigma_k\}$, compute the **[[Responsibility|responsibilities]]** (soft cluster assignments):

$$r_{nk} = \frac{\pi_k\,\mathcal{N}(\mathbf{x}_n\mid\boldsymbol\mu_k, \boldsymbol\Sigma_k)}{\sum_{j=1}^K\pi_j\,\mathcal{N}(\mathbf{x}_n\mid\boldsymbol\mu_j, \boldsymbol\Sigma_j)}.$$

**M-step** — given the responsibilities, update parameters in closed form (treating $r_{nk}$ as fixed importance weights):

$$\boldsymbol\mu_k^{\text{new}} = \frac{\sum_n r_{nk}\mathbf{x}_n}{\sum_n r_{nk}}, \quad \boldsymbol\Sigma_k^{\text{new}} = \frac{\sum_n r_{nk}(\mathbf{x}_n-\boldsymbol\mu_k)(\mathbf{x}_n-\boldsymbol\mu_k)^\top}{\sum_n r_{nk}}, \quad \pi_k^{\text{new}} = \frac{1}{N}\sum_n r_{nk}.$$

Iterate to convergence.

## What EM actually does

EM optimizes a **lower bound** on the log-likelihood (the ELBO, Evidence Lower Bound), tightening it at each iteration. Convergence is monotone — the log-likelihood never decreases — but only to a *local* optimum. Initialization matters: $k$-means is a common warm-start.

EM is general: it works for any latent-variable model where the *complete-data* MLE (i.e., MLE if the latent assignments were observed) has a closed form. The Gaussian mixture is the cleanest example because the M-step is just weighted Gaussian MLE.

## Other applications

- **$k$-means**: the hard-assignment limit of GMM-EM (responsibilities $\in\{0,1\}$, isotropic equal-variance Gaussians).
- **Hidden Markov Models**: EM = Baum-Welch algorithm.
- **Factor analysis** / **PPCA**: EM derivation in [[mml-book]] §10.7.
- **Mixture-of-experts** training in modern ML.

## From [[mml-ch11-density-estimation-gmm|MML Ch 11]]

[[mml-ch11-density-estimation-gmm|MML §11.3]] introduces EM (Dempster et al. 1977) as "a general iterative scheme for learning parameters (maximum likelihood or MAP) in mixture models and, more generally, latent-variable models." The concrete GMM instantiation (p. 361): **(1)** initialize $\boldsymbol\mu_k,\boldsymbol\Sigma_k,\pi_k$; **(2) E-step** — evaluate $r_{nk}$ (Eq. 11.53); **(3) M-step** — re-estimate $\boldsymbol\mu_k,\boldsymbol\Sigma_k,\pi_k$ (Eqs. 11.54–11.56), where the **newly updated means (11.54) feed the covariance update (11.55)** (margin note, p. 361). "Every step in the EM algorithm increases the log-likelihood function (Neal and Hinton, 1999)" (p. 361) — but only to a **local** maximum, so multiple random initializations are used to avoid bad optima (§11.4.5, p. 367). On the running example EM converges in **5 iterations** (Eq. 11.57); on the Fig. 11.1 2-D data, **62 iterations** (Figs. 11.8–11.10), the negative log-likelihood dropping monotonically.

§11.4.5 gives the **principled, latent-variable derivation**: the E-step forms the **expected complete-data log-likelihood** $Q(\boldsymbol\theta\mid\boldsymbol\theta^{(t)})=\mathbb E_{\mathbf z\mid\mathbf x,\boldsymbol\theta^{(t)}}[\log p(\mathbf x,\mathbf z\mid\boldsymbol\theta)]$ (Eqs. 11.73a–b) — the expectation taken under the latent posterior at the current parameters — and the M-step maximizes $Q$ over $\boldsymbol\theta$ to get $\boldsymbol\theta^{(t+1)}$. (Note: the chapter proves the monotone-increase claim via the $Q$-function and cites Neal & Hinton 1999; it does **not** itself derive the ELBO/free-energy lower bound, though that is the standard general justification — Bishop 2006.)

## Connections

- [[mml-ch11-density-estimation-gmm]] — §11.3 / §11.4.5 per-chapter deep dive.
- [[mml-book]] — Ch 11 canonical reference.
- [[GaussianMixtureModel]] — most-cited application.
- [[Responsibility]] — soft assignment quantity (the E-step output).
- [[LatentVariable]] — EM's general setting (§11.4.5).
- [[MaximumLikelihoodEstimation]] — what EM approximates.
- [[VariationalInference]] — generalizes the EM lower-bound argument.
