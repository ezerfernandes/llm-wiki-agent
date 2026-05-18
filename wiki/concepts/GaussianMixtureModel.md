---
title: "Gaussian Mixture Model"
type: concept
tags: [density-estimation, probabilistic-models, foundational]
sources: [mml-book, d2l-appendix-mathematics]
last_updated: 2026-05-16
---

# Gaussian Mixture Model (GMM)

A density model that mixes $K$ Gaussian components ([[mml-book]] Ch 11):

$$p(\mathbf{x}\mid\boldsymbol\theta) = \sum_{k=1}^K \pi_k\,\mathcal{N}(\mathbf{x}\mid\boldsymbol\mu_k,\boldsymbol\Sigma_k), \quad 0\leq\pi_k\leq 1, \quad \sum_{k=1}^K\pi_k = 1.$$

Parameters $\boldsymbol\theta = \{\pi_k, \boldsymbol\mu_k, \boldsymbol\Sigma_k\}_{k=1}^K$.

## Why mixtures over single Gaussians

A single [[GaussianDistribution]] is unimodal — useless for clustered data ([[mml-book]] Fig 11.1 shows a clearly bimodal sample that any Gaussian fit smears across both clusters). GMM gains multimodality at the cost of a non-convex log-likelihood.

## Why MLE has no closed form

The log-likelihood is

$$\mathcal{L}(\boldsymbol\theta) = \sum_{n=1}^N \log\sum_{k=1}^K \pi_k\,\mathcal{N}(\mathbf{x}_n\mid\boldsymbol\mu_k, \boldsymbol\Sigma_k).$$

The log can't move inside the sum over $k$ ([[mml-book]] p. 351–352) — so unlike single-Gaussian MLE there is no clean closed form. The remedy is the iterative [[EMAlgorithm]].

## Latent-variable interpretation

Introduce a categorical latent $z_n\in\{1,\dots,K\}$ that indicates which component generated $\mathbf{x}_n$. The joint is $p(\mathbf{x}_n, z_n=k) = \pi_k\,\mathcal{N}(\mathbf{x}_n\mid\boldsymbol\mu_k,\boldsymbol\Sigma_k)$. Marginalizing $z_n$ recovers the mixture. The **posterior** $p(z_n=k\mid\mathbf{x}_n)$ is the [[Responsibility]] $r_{nk}$ — soft cluster assignment.

## Hard cluster limit: $k$-means

Take the responsibilities to be one-hot (the most-likely component) and force $\boldsymbol\Sigma_k = \sigma^2\mathbf{I}$ with $\sigma\to 0$. GMM-EM degenerates to $k$-means. So $k$-means is GMM-EM under maximally-restrictive assumptions; full GMM allows ellipsoidal clusters of varying sizes and orientations.

## Use cases

- **Generative classifiers** (one GMM per class).
- **Speaker / phoneme modeling** in classical speech.
- **Anomaly detection**: low density under the GMM ⇒ outlier.
- **Background modeling** in computer vision.

## Limitations

- $K$ must be chosen (model selection problem — typically by held-out likelihood or BIC).
- Local optima — initialization matters, $k$-means warm-start is standard.
- Singularities — a component collapsing onto a single point sends covariance determinant to zero and the log-likelihood to $+\infty$. Regularization or restricted covariance structures (diagonal, tied) prevent this.

## Connections

- [[mml-book]] — Ch 11 canonical reference.
- [[GaussianDistribution]] — base component.
- [[EMAlgorithm]] — fitting algorithm.
- [[Responsibility]] — soft assignment.
- [[MixtureModel]] — broader family (Bernoulli mixtures, Categorical mixtures, etc.).
- [[MaximumLikelihoodEstimation]] — what EM iteratively maximizes.
