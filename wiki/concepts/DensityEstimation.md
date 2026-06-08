---
title: "Density Estimation"
type: concept
tags: [density-estimation, probabilistic-models, unsupervised, foundational]
sources: [mml-ch11-density-estimation-gmm, mml-book]
last_updated: 2026-06-05
---

# Density Estimation

The problem of **representing a dataset compactly by estimating the probability density $p(\mathbf x)$ that generated it**, given i.i.d. samples $\mathcal X=\{\mathbf x_1,\dots,\mathbf x_N\}$ from an unknown distribution. It is the **third of the four ML pillars** in [[mml-book|Mathematics for Machine Learning]] ([[mml-ch11-density-estimation-gmm|Ch 11]]), alongside regression ([[mml-ch09-linear-regression|Ch 9]]), dimensionality reduction ([[mml-ch10-dimensionality-reduction-pca|Ch 10]]), and classification (Ch 12). The estimated density lets us treat the dataset "as a typical realization from this distribution if we were to sample from it" ([[mml-ch11-density-estimation-gmm|MML §11]], p. 348).

## Why estimate a density at all

Taking the raw data points *as* the representation is unhelpful "if the dataset is huge or if we are interested in representing characteristics of the data" ([[mml-ch11-density-estimation-gmm|MML §11]], p. 348). A density gives a compact, generative summary: the mean and variance of a fitted [[GaussianDistribution|Gaussian]] capture the data's location and spread; a richer model captures multimodality, supports sampling new data, and yields a notion of *how typical* a point is (low density ⇒ outlier).

## Parametric vs nonparametric

- **Parametric** — assume a fixed-form family $p(\mathbf x\mid\boldsymbol\theta)$ and fit $\boldsymbol\theta$ by [[MaximumLikelihoodEstimation|MLE]] / MAP. A single Gaussian is the simplest; the [[GaussianMixtureModel|Gaussian mixture model]] (a [[MixtureModel|mixture]] of $K$ Gaussians) is the workhorse multimodal choice ([[mml-ch11-density-estimation-gmm|MML §11.1]]). The number of parameters is fixed in advance.
- **Nonparametric** — the model complexity grows with the data; no fixed parametric form.
  - **[[Histogram|Histograms]]** (Pearson 1895): bin the space and count; a step-function estimate whose **bin size** is the critical hyperparameter ([[mml-ch11-density-estimation-gmm|MML §11.5]]).
  - **[[KernelDensityEstimation|Kernel density estimation]]** (Rosenblatt 1956; Parzen 1962): $p(\mathbf x)=\tfrac1{Nh}\sum_{n=1}^N k\!\big(\tfrac{\mathbf x-\mathbf x_n}{h}\big)$ — place a kernel on every data point; **bandwidth $h$** plays the bin-size role but yields a *smooth* estimate (MML Eq. 11.74).

Cross-validation (§8.2.4 / §8.6.1) chooses the hyperparameters: the bin size, the bandwidth $h$, or the number of mixture components $K$.

## From [[mml-ch11-density-estimation-gmm|MML Ch 11]]

Chapter 11 develops density estimation primarily through the **[[GaussianMixtureModel|GMM]]** (book pp. 348–369). A single Gaussian has "limited modeling capabilities" — it cannot represent the bimodal Fig. 11.1 data — so the chapter moves to the more expressive mixture family $p(\mathbf x)=\sum_{k=1}^K\pi_k\mathcal N(\mathbf x\mid\boldsymbol\mu_k,\boldsymbol\Sigma_k)$ (Eq. 11.3). Because the resulting log-likelihood has **no closed-form maximum** (the $\log$ cannot enter the sum over components, p. 351–352), fitting is done iteratively by the [[EMAlgorithm|EM algorithm]] via [[Responsibility|responsibilities]] (soft cluster assignments). The chapter closes (§11.5) by situating the GMM among the broader density-estimation toolkit — histograms and KDE — and notes that MLE density estimation inherits the standard MLE pathologies (overfitting/singularities; a point estimate with no parameter uncertainty, motivating Bayesian/variational treatments).

## Connections

- [[mml-ch11-density-estimation-gmm]] — canonical reference (the third pillar).
- [[mml-book]] — Ch 11.
- [[GaussianMixtureModel]] — the parametric multimodal workhorse.
- [[MixtureModel]] — the parametric family GMMs belong to.
- [[GaussianDistribution]] — the simplest parametric density.
- [[KernelDensityEstimation]] / [[Histogram]] — the nonparametric alternatives.
- [[MaximumLikelihoodEstimation]] — the fitting principle for parametric densities.
- [[EMAlgorithm]] — fits the GMM when MLE has no closed form.
- [[DensityBasedClustering]] — clustering built on local density estimates.
