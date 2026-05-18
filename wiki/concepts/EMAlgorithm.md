---
title: "EM Algorithm"
type: concept
tags: [optimization, density-estimation, foundational]
sources: [mml-book]
last_updated: 2026-05-16
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

## Connections

- [[mml-book]] — Ch 11 canonical reference.
- [[GaussianMixtureModel]] — most-cited application.
- [[Responsibility]] — soft assignment quantity.
- [[MaximumLikelihoodEstimation]] — what EM approximates.
- [[VariationalInference]] — generalizes the EM lower-bound argument.
