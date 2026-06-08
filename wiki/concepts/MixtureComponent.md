---
title: "Mixture Component"
type: concept
tags: [density-estimation, probabilistic-models, mixture-model, latent-variable]
sources: [mml-ch11-density-estimation-gmm, mml-book]
last_updated: 2026-06-05
---

# Mixture Component

One of the $K$ base distributions $p_k(\mathbf x)$ combined in a [[MixtureModel|mixture model]] $p(\mathbf x)=\sum_{k=1}^K\pi_k\,p_k(\mathbf x)$ ([[mml-ch11-density-estimation-gmm|MML §11.1]], Eq. 11.1). Each component is paired with a [[MixtureWeight|mixture weight]] $\pi_k$; together the components and their weights specify the full density. The components are drawn from a basic distributional family — Gaussians, Bernoullis, Categoricals, Gammas — and each can be thought of as describing one "cluster" or mode of the data.

## In a Gaussian mixture model

For a [[GaussianMixtureModel|GMM]] each component is a [[GaussianDistribution|Gaussian]] $p_k(\mathbf x)=\mathcal N(\mathbf x\mid\boldsymbol\mu_k,\boldsymbol\Sigma_k)$ with its own **mean $\boldsymbol\mu_k$** and **covariance $\boldsymbol\Sigma_k$** ([[mml-ch11-density-estimation-gmm|MML §11.1]], Eq. 11.3). The full GMM parameter set is therefore the per-component triple collected over all components, $\boldsymbol\theta=\{\pi_k,\boldsymbol\mu_k,\boldsymbol\Sigma_k:k=1,\dots,K\}$. A single Gaussian is the $K=1$ degenerate case; using $K>1$ ellipsoidal components is what gives the GMM its multimodal expressiveness over a single Gaussian.

## Component parameter updates (M-step)

Given the [[Responsibility|responsibilities]] $r_{nk}$ (the soft assignment of points to components) and the effective count $N_k=\sum_n r_{nk}$, each component's parameters are updated by responsibility-weighted MLE ([[mml-ch11-density-estimation-gmm|MML]] Theorems 11.1–11.2):

$$\boldsymbol\mu_k^{\text{new}}=\frac1{N_k}\sum_{n=1}^N r_{nk}\mathbf x_n,\qquad \boldsymbol\Sigma_k^{\text{new}}=\frac1{N_k}\sum_{n=1}^N r_{nk}(\mathbf x_n-\boldsymbol\mu_k)(\mathbf x_n-\boldsymbol\mu_k)^\top.$$

Each is an **importance-weighted estimate** in which a data point contributes to component $k$ in proportion to how responsible that component is for it. Because the responsibilities depend on *all* components' parameters, the components cannot be fit independently — they are updated jointly and iteratively by the [[EMAlgorithm|EM algorithm]].

## Latent-variable reading

Under the generative view (§11.4), the conditional $p(\mathbf x\mid z_k=1)=\mathcal N(\mathbf x\mid\boldsymbol\mu_k,\boldsymbol\Sigma_k)$ (MML Eq. 11.58) *is* the $k$th component: the one-hot indicator $\mathbf z$ selects which component generates a point, and ancestral sampling draws $\mathbf x$ from the selected component. Each component thus has the dual identity of a term in the density and a conditional distribution in the generative process.

## Connections

- [[mml-ch11-density-estimation-gmm]] — §11.1, §11.2, §11.4 canonical reference.
- [[mml-book]] — Ch 11.
- [[MixtureModel]] — the sum the components belong to.
- [[MixtureWeight]] — the $\pi_k$ paired with each component.
- [[GaussianMixtureModel]] — components are Gaussians.
- [[GaussianDistribution]] — the per-component density in a GMM.
- [[Responsibility]] — the soft assignment driving each component's update.
- [[CovarianceMatrix]] — the $\boldsymbol\Sigma_k$ per component.
- [[EMAlgorithm]] — fits all components jointly.
