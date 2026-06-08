---
title: "Factor Analysis"
type: concept
tags: [dimensionality-reduction, latent-variable-models, probabilistic-modeling, statistics]
sources: [mml-ch10-dimensionality-reduction-pca, mml-book]
last_updated: 2026-06-05
---

# Factor Analysis (FA)

A **latent-variable model for linear dimensionality reduction** (Spearman 1904; Bartholomew et al. 2011) that generalizes [[ProbabilisticPCA|probabilistic PCA]] by allowing **each observation dimension its own noise variance** ([[mml-book]] §10.8, p. 346).

## How it differs from PPCA ([[mml-ch10-dimensionality-reduction-pca|MML §10.8]])

PPCA assumes the linear-Gaussian model $p(\mathbf x_n\mid\mathbf z_n)=\mathcal N(\mathbf x_n\mid\mathbf B\mathbf z_n+\boldsymbol\mu,\sigma^2\mathbf I)$ with prior $p(\mathbf z_n)=\mathcal N(\mathbf 0,\mathbf I)$ — **isotropic** noise: every dimension shares one variance $\sigma^2$. Factor analysis instead lets dimension $d$ have its own variance $\sigma_d^2$, i.e. the noise covariance is a general diagonal matrix $\boldsymbol\Psi=\mathrm{diag}(\sigma_1^2,\dots,\sigma_D^2)$. This gives the likelihood "more flexibility than PPCA, but still forces the data to be explained by the model parameters $\mathbf B,\boldsymbol\mu$."

## Consequences

- **No closed-form MLE** — unlike PPCA (which has the closed form of Eqs. 10.77–10.79), FA requires an iterative scheme such as the [[EMAlgorithm|EM algorithm]].
- **Not all stationary points are global optima** — in PPCA every stationary point is a global optimum; this guarantee is lost in FA.
- **Invariance behavior is the mirror image of PCA**: FA does **not** change if you scale the data, but it **does** return different solutions if you rotate the data. (PCA / PPCA is invariant to rotation but not to scaling.)

## Connections

- [[mml-ch10-dimensionality-reduction-pca|MML Ch 10]] — §10.8 canonical reference (p. 346).
- [[ProbabilisticPCA]] — the isotropic-noise special case.
- [[PrincipalComponentAnalysis]] — the noise-free / rotation-invariant cousin.
- [[IndependentComponentAnalysis]] — the non-Gaussian-prior cousin.
- [[LatentVariable]] / [[EMAlgorithm]] — the latent-variable machinery FA needs.
- [[DimensionalityReduction]] — one of the three linear methods (PCA, FA, ICA).
