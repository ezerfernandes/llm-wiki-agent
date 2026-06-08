---
title: "Probabilistic PCA"
type: concept
tags: [dimensionality-reduction, latent-variable-models, probabilistic-modeling, generative-model, pca, gaussian]
sources: [mml-ch10-dimensionality-reduction-pca, mml-book]
last_updated: 2026-06-05
---

# Probabilistic PCA (PPCA)

A **continuous-latent-variable generative model** that recovers [[PrincipalComponentAnalysis|PCA]] as the maximum-likelihood solution in a noise-free limit, proposed by **Tipping & Bishop (1999)** ([[mml-book]] §10.7). PPCA replaces the deterministic linear coder/decoder of classical PCA with an explicit probabilistic model, giving a likelihood, a generative process, posteriors, and Bayesian extensions.

## The generative model ([[mml-ch10-dimensionality-reduction-pca|MML §10.7.1]])

A latent variable $\mathbf z\in\mathbb R^M$ with a standard-normal prior, mapped linearly/affinely to the observed $\mathbf x\in\mathbb R^D$ with isotropic Gaussian noise (Eqs. 10.63–10.66):

$$\mathbf z\sim\mathcal N(\mathbf 0,\mathbf I),\qquad \mathbf x=\mathbf B\mathbf z+\boldsymbol\mu+\boldsymbol\epsilon,\qquad \boldsymbol\epsilon\sim\mathcal N(\mathbf 0,\sigma^2\mathbf I),$$

so $p(\mathbf x\mid\mathbf z,\mathbf B,\boldsymbol\mu,\sigma^2)=\mathcal N(\mathbf x\mid\mathbf B\mathbf z+\boldsymbol\mu,\sigma^2\mathbf I)$ (Eq. 10.64). Parameters: loading matrix $\mathbf B\in\mathbb R^{D\times M}$, mean $\boldsymbol\mu\in\mathbb R^D$, noise variance $\sigma^2$. **Ancestral sampling** generates a typical point: draw $\mathbf z_n\sim p(\mathbf z)$, then $\mathbf x_n\sim p(\mathbf x\mid\mathbf z_n,\dots)$. The directed [[DirectedGraphicalModel|graphical model]] (Fig. 10.14) has arrow $\mathbf z\to\mathbf x$: a **low-dimensional latent *cause*** for high-dimensional observations.

## The marginal likelihood ([[mml-ch10-dimensionality-reduction-pca|MML §10.7.2]])

Integrating out the latent (the [[LatentVariable|latent-variable]] marginalization of §8.4.3) gives a Gaussian whose covariance is the model's signature (Eqs. 10.68–10.70):

$$p(\mathbf x\mid\mathbf B,\boldsymbol\mu,\sigma^2)=\int\mathcal N(\mathbf x\mid\mathbf B\mathbf z+\boldsymbol\mu,\sigma^2\mathbf I)\,\mathcal N(\mathbf z\mid\mathbf 0,\mathbf I)\,d\mathbf z=\mathcal N\!\bigl(\mathbf x\mid\boldsymbol\mu,\;\mathbf B\mathbf B^\top+\sigma^2\mathbf I\bigr).$$

Only this marginal (not the conditional 10.64, which still depends on $\mathbf z$) can be used for MLE/MAP, because the estimation objective must depend on the data and parameters but **not** on the latents.

## Posterior over latents ([[mml-ch10-dimensionality-reduction-pca|MML §10.7.3]])

Gaussian conditioning (§6.5.1) yields $p(\mathbf z\mid\mathbf x)=\mathcal N(\mathbf z\mid\mathbf m,\mathbf C)$ with (Eqs. 10.74–10.75)

$$\mathbf m=\mathbf B^\top(\mathbf B\mathbf B^\top+\sigma^2\mathbf I)^{-1}(\mathbf x-\boldsymbol\mu),\qquad \mathbf C=\mathbf I-\mathbf B^\top(\mathbf B\mathbf B^\top+\sigma^2\mathbf I)^{-1}\mathbf B.$$

The posterior covariance $\mathbf C$ is **independent of the observed data** and quantifies embedding confidence (small $\det\mathbf C$ ⇒ a confident latent embedding).

## Maximum likelihood & the link to classical PCA ([[mml-ch10-dimensionality-reduction-pca|MML §10.8]])

The MLE parameters (Tipping & Bishop 1999, Eqs. 10.77–10.79):

$$\boldsymbol\mu_{\text{ML}}=\tfrac1N\textstyle\sum_n\mathbf x_n,\qquad \mathbf B_{\text{ML}}=\mathbf T(\boldsymbol\Lambda-\sigma^2\mathbf I)^{1/2}\mathbf R,\qquad \sigma^2_{\text{ML}}=\tfrac1{D-M}\textstyle\sum_{j=M+1}^D\lambda_j,$$

where $\mathbf T$ holds $M$ eigenvectors of the [[DataCovarianceMatrix|data covariance]] $\mathbf S$, $\boldsymbol\Lambda=\mathrm{diag}(\lambda_1,\dots,\lambda_M)$, and $\mathbf R$ is **an arbitrary orthogonal matrix** — so $\mathbf B_{\text{ML}}$ is unique only up to rotation (Eq. 10.78 is essentially an SVD). The noise variance estimate is the **average leftover variance in the [[OrthogonalComplement|orthogonal complement]]** of the principal subspace. In the **noise-free limit $\sigma\to0$**, $\mathbf B\mathbf B^\top=\mathbf T\boldsymbol\Lambda\mathbf T^{-1}=\mathrm{Cov}[\mathcal X]$ (Eqs. 10.80–10.81), recovering classical PCA — confirming that **(P)PCA performs a decomposition of the data covariance matrix**.

## Why bother (advantages over classical PCA)

A likelihood function for noisy observations; Bayesian model comparison via the [[MarginalLikelihood|marginal likelihood]]; a generative model to simulate new data and detect novelty; principled handling of missing dimensions via Bayes; a route to mixtures of PCA; and a fully Bayesian treatment ([[mml-book]] §10.7, p. 339–340). In a streaming setting, the [[EMAlgorithm|EM]] algorithm (Roweis 1998) is recommended for the MLE.

## Relatives

- **Bayesian PCA** (Bishop 1999) — places a prior $p(\boldsymbol\mu,\mathbf B,\sigma^2)$ and integrates parameters out, giving automatic selection of latent dimensionality $M$ (MCMC / variational inference).
- **[[FactorAnalysis|Factor analysis]]** — per-dimension noise $\sigma_d^2$ instead of isotropic $\sigma^2$; no closed-form MLE.
- **[[IndependentComponentAnalysis|ICA]]** — same model with a non-Gaussian latent prior.
- **GP-LVM** (Lawrence 2005) — replaces the linear $\mathbf z\to\mathbf x$ map with a Gaussian process.

## Connections

- [[mml-ch10-dimensionality-reduction-pca|MML Ch 10]] — §10.7–10.8 canonical reference.
- [[PrincipalComponentAnalysis]] — the noise-free special case.
- [[LatentVariable]] — PPCA is the headline continuous-latent example (Ch 8 §8.4.3 machinery).
- [[GaussianDistribution]] — the entire model is Gaussian algebra (marginal, joint, posterior).
- [[DataCovarianceMatrix]] — what (P)PCA ultimately decomposes.
- [[MaximumLikelihoodEstimation]] / [[MAPEstimation]] / [[EMAlgorithm]] — parameter estimation.
- [[DirectedGraphicalModel]] — Fig. 10.14, arrow $\mathbf z\to\mathbf x$.
- [[GaussianMixtureModel]] — the Ch 11 discrete-latent peer.
- [[FactorAnalysis]] / [[IndependentComponentAnalysis]] — close linear-Gaussian relatives.
- [[Autoencoder]] — PPCA's deterministic limit is the linear auto-encoder.
