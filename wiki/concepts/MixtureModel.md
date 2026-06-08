---
title: "Mixture Model"
type: concept
tags: [probabilistic-models, density-estimation, foundational]
sources: [mml-ch11-density-estimation-gmm, mml-book]
last_updated: 2026-06-05
---

# Mixture Model

A convex combination of $K$ base distributions ([[mml-book]] §11.1):

$$p(\mathbf{x}) = \sum_{k=1}^K \pi_k\,p_k(\mathbf{x}), \quad 0\leq\pi_k\leq 1, \quad \sum_{k=1}^K\pi_k = 1.$$

The components $p_k$ come from a base family (Gaussian, Bernoulli, Categorical, Gamma, ...); the $\pi_k$ are *mixture weights*.

## Why mixtures matter

[[mml-book]] §11.1: "Mixture models are more expressive than the corresponding base distributions because they allow for multimodal data representations" — i.e., they describe datasets with multiple "clusters." A single base distribution can't represent more than one mode.

A mixture model is the simplest **latent variable model**: introduce $z\in\{1,\dots,K\}$ with $P(z=k)=\pi_k$ and let $\mathbf{x}\mid z=k\sim p_k$; marginalizing $z$ gives the mixture.

## Most-used members

- **[[GaussianMixtureModel|Gaussian mixture]]**: $p_k = \mathcal{N}(\boldsymbol\mu_k,\boldsymbol\Sigma_k)$ — the canonical [[mml-book]] example.
- **Mixture of Bernoullis**: e.g., topic models over binary feature vectors.
- **Mixture of Categoricals**: e.g., LDA's topic-word distributions.
- **Mixture of experts** (modern ML): each $p_k$ is a neural network, weights $\pi_k(\mathbf{x})$ are input-dependent. This is the supervised generalization that powers [[switchtransformer|Switch Transformer]] / Mixture-of-Experts LLMs.

## Fitting

The standard recipe is the [[EMAlgorithm]] — iterate between computing soft assignments ($r_{nk}$, the [[Responsibility]]) and updating component parameters by weighted MLE.

## Connection to Corpus II

[[2605.12966-agentic-ai-to-agi]] formalizes Mixture-of-Experts (Shazeer 2017, [[switchtransformer|Switch Transformer]]) as a **single-layer routing instance** of agentic AI. The mixture-model framing here is the static, density-estimation analogue — both partition the input space among specialized components, but mixture models are *generative* density models whereas MoE is a *discriminative* routing scheme.

## From [[mml-ch11-density-estimation-gmm|MML Ch 11]]

[[mml-ch11-density-estimation-gmm|MML §11.1]] introduces the mixture model as a **convex combination of $K$ simple (base) distributions** $p(\mathbf x)=\sum_{k=1}^K\pi_k p_k(\mathbf x)$ (Eq. 11.1) with [[MixtureWeight|mixture weights]] $0\le\pi_k\le1$, $\sum_k\pi_k=1$ (Eq. 11.2) — components $p_k$ being Gaussians, Bernoullis, or Gammas. The headline property: mixtures "are more expressive than the corresponding base distributions because they allow for multimodal data representations" (p. 349), modeling datasets with multiple clusters that a single base distribution cannot. The chapter develops the [[GaussianMixtureModel|Gaussian special case]] in full (the components are [[MixtureComponent|Gaussian components]] $\mathcal N(\boldsymbol\mu_k,\boldsymbol\Sigma_k)$), fitting it by the [[EMAlgorithm|EM algorithm]] via [[Responsibility|responsibilities]] because the mixture log-likelihood has no closed-form maximum. §11.4 reframes the mixture as a discrete [[LatentVariable|latent-variable]] model whose one-hot indicator $\mathbf z$ selects a component — the cleanest example of "a mixture model is the simplest latent-variable model."

## Connections

- [[mml-ch11-density-estimation-gmm]] — §11.1 per-chapter deep dive.
- [[mml-book]] — §11.1 canonical reference.
- [[GaussianMixtureModel]] — canonical example.
- [[MixtureWeight]] / [[MixtureComponent]] — the $\pi_k$ and the base distributions they weight.
- [[DensityEstimation]] — the pillar mixtures serve.
- [[EMAlgorithm]] — fitting algorithm.
- [[Responsibility]] — soft component assignment.
- [[LatentVariable]] — the one-hot indicator view (§11.4).
- [[MixtureOfExperts]] — supervised generalization.
- [[GaussianDistribution]] — most common base component.
