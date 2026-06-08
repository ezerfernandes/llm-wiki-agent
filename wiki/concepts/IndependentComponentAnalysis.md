---
title: "Independent Component Analysis"
type: concept
tags: [dimensionality-reduction, latent-variable-models, signal-processing, blind-source-separation, statistics]
sources: [mml-ch10-dimensionality-reduction-pca, mml-book]
last_updated: 2026-06-05
---

# Independent Component Analysis (ICA)

A latent-variable method "closely related to [[PrincipalComponentAnalysis|PCA]]" (Hyvärinen et al. 2001) that keeps the same linear-Gaussian *likelihood* as [[ProbabilisticPCA|PPCA]] but **changes the prior on the latents $\mathbf z$ to a non-Gaussian distribution** ([[mml-book]] §10.8, pp. 346–347).

## The model & why the prior matters ([[mml-ch10-dimensionality-reduction-pca|MML §10.8]])

Starting from the latent-variable model $p(\mathbf x_n\mid\mathbf z_n)=\mathcal N(\mathbf x_n\mid\mathbf B\mathbf z_n+\boldsymbol\mu,\sigma^2\mathbf I)$, ICA replaces the standard-normal prior $p(\mathbf z_n)=\mathcal N(\mathbf 0,\mathbf I)$ with a **non-Gaussian** $p(\mathbf z)$. This single change is decisive: under the Gaussian model the PCA/PPCA solution is **invariant to any rotation** of the latent space, so PCA "can identify the best lower-dimensional subspace in which the signals live, but not the signals themselves." A non-Gaussian prior **breaks the rotation symmetry**, letting ICA recover the actual latent sources.

## Blind-source separation

ICA's headline use is **blind-source separation** — the "cocktail-party problem": in a busy train station many people talk simultaneously; the microphones (your ears) record linear mixtures of the speech signals, and the goal is to recover the individual constituent signals from the mixture. Because PCA only finds the subspace (not the sources), ICA is the tool that disentangles the mixed signals.

## Place among linear dimensionality-reduction methods

PCA, [[FactorAnalysis|factor analysis]], and ICA are the **three examples of dimensionality reduction with linear models** (Cunningham & Ghahramani 2015): PCA/PPCA (isotropic Gaussian noise, Gaussian prior), FA (per-dimension Gaussian noise), and ICA (non-Gaussian prior).

## Connections

- [[mml-ch10-dimensionality-reduction-pca|MML Ch 10]] — §10.8 canonical reference (pp. 346–347).
- [[ProbabilisticPCA]] — same likelihood, Gaussian prior.
- [[PrincipalComponentAnalysis]] — rotation-invariant, so cannot identify sources.
- [[FactorAnalysis]] — the per-dimension-noise sibling.
- [[LatentVariable]] / [[GaussianDistribution]] — the modeling substrate.
- [[DimensionalityReduction]] — one of the three linear methods.
