---
title: "Gaussian Mixture Model"
type: concept
tags: [density-estimation, probabilistic-models, foundational]
sources: [mml-ch11-density-estimation-gmm, mml-book, d2l-appendix-mathematics]
last_updated: 2026-06-05
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

## From [[mml-ch11-density-estimation-gmm|MML Ch 11]]

[[mml-ch11-density-estimation-gmm|MML §11.1]] defines the GMM as a [[DensityEstimation|density-estimation]] model combining $K$ Gaussians (Eq. 11.3), the parameters collected as $\boldsymbol\theta=\{\boldsymbol\mu_k,\boldsymbol\Sigma_k,\pi_k:k=1,\dots,K\}$ — per-component [[MixtureComponent|means/covariances]] plus [[MixtureWeight|mixture weights]]. It is the **third of the four ML pillars** (density estimation), the latent-variable peer of [[mml-ch10-dimensionality-reduction-pca|Ch 10's PPCA]] (discrete one-hot latent vs PPCA's continuous $\mathbf z$). The chapter's running 1-D example ($\mathcal X=\{-3,-2.5,-1,0,2,4,5\}$, $K=3$) is carried through Examples 11.1–11.6.

The three **M-step updates** are responsibility-weighted estimates ([[mml-ch11-density-estimation-gmm|MML]] Thms 11.1–11.3):

$$\boldsymbol\mu_k^{\text{new}}=\tfrac1{N_k}\textstyle\sum_n r_{nk}\mathbf x_n\ \text{(Eq. 11.20)},\quad \boldsymbol\Sigma_k^{\text{new}}=\tfrac1{N_k}\textstyle\sum_n r_{nk}(\mathbf x_n-\boldsymbol\mu_k)(\mathbf x_n-\boldsymbol\mu_k)^\top\ \text{(Eq. 11.30)},\quad \pi_k^{\text{new}}=\tfrac{N_k}{N}\ \text{(Eq. 11.42)},$$

with $N_k=\sum_n r_{nk}$ the effective count. The **mean update is an importance-weighted Monte Carlo estimate** (p. 354); the **weight update needs a [[LagrangeMultipliers|Lagrange multiplier]]** for $\sum_k\pi_k=1$ (§7.2). All three couple through $r_{nk}$, which is **exactly why there is no closed-form joint MLE** (Remarks after Thms 11.1–11.3). §11.4 re-derives everything from the discrete latent indicator $\mathbf z$, giving $r_{nk}=p(z_{nk}=1\mid\mathbf x_n)$ a principled reading as a posterior (Eq. 11.72b). §11.5 records the GMM-as-generative-model framing (ancestral sampling generated Fig. 11.1), the $K$-must-be-chosen caveat (nested CV, §8.6.1), the singularity/overfitting pathology (a component collapsing onto one point sends the likelihood to $+\infty$), and the **soft-vs-hard** statement: $K$-means makes hard assignments, the GMM soft ones (MacKay 2003).

## Connections

- [[mml-ch11-density-estimation-gmm]] — Ch 11 per-chapter deep dive.
- [[mml-book]] — Ch 11 canonical reference.
- [[GaussianDistribution]] — base component.
- [[EMAlgorithm]] — fitting algorithm.
- [[Responsibility]] — soft assignment.
- [[MixtureModel]] — broader family (Bernoulli mixtures, Categorical mixtures, etc.).
- [[MixtureWeight]] / [[MixtureComponent]] — the $\pi_k$ and the per-component Gaussians.
- [[DensityEstimation]] — the pillar this model serves.
- [[LatentVariable]] — the one-hot generative view (§11.4).
- [[MaximumLikelihoodEstimation]] — what EM iteratively maximizes.
