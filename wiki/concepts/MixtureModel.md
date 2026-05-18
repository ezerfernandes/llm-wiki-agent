---
title: "Mixture Model"
type: concept
tags: [probabilistic-models, density-estimation, foundational]
sources: [mml-book]
last_updated: 2026-05-16
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

## Connections

- [[mml-book]] — §11.1 canonical reference.
- [[GaussianMixtureModel]] — canonical example.
- [[EMAlgorithm]] — fitting algorithm.
- [[Responsibility]] — soft component assignment.
- [[MixtureOfExperts]] — supervised generalization.
- [[GaussianDistribution]] — most common base component.
