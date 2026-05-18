---
title: "Min-Max Game (GAN Objective)"
type: concept
tags: [generative-model, gan, optimization, game-theory]
sources: [d2l-generative-adversarial-networks]
last_updated: 2026-05-16
---

# Min-Max Game (GAN Objective)

The two-player zero-sum game-theoretic framing of [[generativeadversarialnetwork|GAN]] training ([[IanGoodfellow|Goodfellow]], Pouget-Abadie, Mirza et al. 2014). The [[Discriminator]] $D$ and [[Generator]] $G$ optimize *opposite signs* of a single objective:

$$\min_D \max_G \big\{ -\mathbb{E}_{\mathbf{x} \sim \textrm{Data}} \log D(\mathbf{x}) - \mathbb{E}_{\mathbf{z} \sim \textrm{Noise}} \log(1 - D(G(\mathbf{z}))) \big\}$$

## The two views

- **Discriminator view:** standard [[BinaryCrossEntropy|BCE]] over real data (label 1) + fake data (label 0). $D$ wants to minimize the loss.
- **Generator view:** $D(G(\mathbf{z}))$ should be close to 1 (real), so $G$ wants to *maximize* the BCE loss when $y=0$ (i.e., the second term). Equivalently, $G$ wants to make $D$ misclassify fakes as real.

## Global equilibrium (Goodfellow et al. 2014 Theorem 1)

At the Nash equilibrium, the generator distribution equals the data distribution $p_g \equiv p_{\textrm{data}}$, and the discriminator collapses to $D(\mathbf{x}) \equiv 1/2$ everywhere — *informative no longer*, because real and fake are indistinguishable. The objective at equilibrium evaluates to $-\log 4$. This is the formal target the game pursues.

## The non-saturating reformulation

In practice the $\max_G$ form has a vanishing-gradient pathology when $D(G(\mathbf{z}))$ is small (which is exactly the regime early in training). [[d2l-generative-adversarial-networks]] §`gan` documents the canonical fix:

$$\min_G \{ -\log D(G(\mathbf{z})) \}$$

— *"feeding $\mathbf{x}' = G(\mathbf{z})$ into the discriminator but giving label $y=1$."* Same fixed point, well-conditioned gradients. Every framework's GAN training loop uses this form.

## Why this is not a standard supervised-learning problem

In supervised learning, the optimum is a *unique* minimum of a fixed objective over $\theta$. Here, the objective itself moves — $D$'s parameters and $G$'s parameters appear with opposite signs, and the "loss landscape" each network sees is reshaped by the other's updates. This is why standard convergence theory does not apply, and why GAN training is famously *unstable* (mode collapse, oscillation, divergence) without practical regularizers ([[BatchNormalization|BN]], [[Adam]] $\beta_1 = 0.5$, careful initialization).

## Connections

- [[generativeadversarialnetwork|GAN]] — the framework this objective defines.
- [[Generator]] / [[Discriminator]] — the two players.
- [[ModeCollapse]] — the dominant non-equilibrium failure mode.
- [[BinaryCrossEntropy|BCE]] / [[CrossEntropyLoss]] — the structural loss form.
- [[Adam]] — the canonical optimizer, with $\beta_1$ lowered to $0.5$ for GAN training.
- [[d2l-generative-adversarial-networks]] — canonical source.
- [[DCGAN]] — the architecture this objective is most often trained with.
