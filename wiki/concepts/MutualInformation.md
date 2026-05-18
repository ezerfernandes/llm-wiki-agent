---
title: "Mutual Information"
type: concept
tags: [information-theory, foundational]
sources: [d2l-appendix-mathematics]
last_updated: 2026-05-16
---

# Mutual Information

The amount of information shared between two random variables — the reduction in uncertainty about one from observing the other ([[d2l-appendix-mathematics]] §information-theory). Defined symmetrically as

$$I(X; Y) = H(X) + H(Y) - H(X, Y) = H(X) - H(X\mid Y) = H(Y) - H(Y\mid X).$$

Equivalently, the [[KullbackLeiblerDivergence|KL divergence]] between the joint and the product of marginals:

$$I(X; Y) = D_{KL}\!\big(P(X, Y)\,\|\,P(X)\,P(Y)\big) = \sum_{x,y} p(x,y)\log\frac{p(x,y)}{p(x)\,p(y)}.$$

## Properties

- **Non-negative**: $I(X; Y) \geq 0$, with equality iff $X\perp Y$.
- **Symmetric**: $I(X; Y) = I(Y; X)$ — unlike KL divergence and conditional entropy.
- **Invariant** under invertible reparametrizations of either $X$ or $Y$.
- **Data-processing inequality**: if $X\to Y\to Z$ is a Markov chain, $I(X; Z)\leq I(X; Y)$.

## ML uses

- **[[InfoMax]] / [[InfoNCE]] / [[ContrastiveLearning|contrastive]] representation learning** (SimCLR, MoCo, CLIP): maximize $I(\text{view}_1; \text{view}_2)$ between augmented views of the same example — the formal objective underneath every modern self-supervised vision encoder.
- **[[InformationBottleneck|Information bottleneck]]** (Tishby et al. 1999): find a representation $T$ minimizing $I(X; T) - \beta\,I(T; Y)$ — preserve task-relevant info while compressing input.
- **Feature selection / dependency screening**: pick features $X_j$ with high $I(X_j; Y)$ to the target $Y$.
- **Disentanglement / [[VariationalAutoencoder|VAE]] regularization**: ELBO surgery often introduces an $I(X; Z)$ term to control how much input information leaks into latents.
- **[[ChainOfThought]] / reasoning interpretability**: $I(\text{prompt}; \text{answer})$ vs $I(\text{prompt}; \text{trace})$ measures how much intermediate reasoning communicates beyond the final output.

## Estimation in high dimensions is hard

Naïve plug-in estimators are biased and high-variance in continuous / high-dimensional settings. Modern alternatives: **MINE** (Belghazi et al. 2018, Donsker-Varadhan lower bound), **[[InfoNCE]]** (van den Oord et al. 2018 — provably lower-bounds $I$), **DV-style neural estimators** in general. The empirical fact that these "MI lower bounds" power modern self-supervised learning is one of the strongest practical applications of information theory in deep learning.

## Connections

- [[d2l-appendix-mathematics]] — §information-theory canonical reference.
- [[Entropy]] — building block.
- [[KullbackLeiblerDivergence]] — alternative MI definition.
- [[ConditionalEntropy]] — $I(X; Y) = H(X) - H(X\mid Y)$.
- [[InfoNCE]] — practical neural-network MI lower bound underpinning contrastive learning.
- [[InformationBottleneck]] — uses MI directly as a training objective.
- [[InformationTheory]] — parent field.
