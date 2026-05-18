---
title: "Generator (GAN)"
type: concept
tags: [generative-model, gan, deep-learning]
sources: [d2l-generative-adversarial-networks]
last_updated: 2026-05-16
---

# Generator (GAN)

The "fake-sample synthesizer" half of a [[generativeadversarialnetwork|GAN]]: a differentiable function $G: \mathbf{z} \mapsto \mathbf{x}'$ that maps a noise vector $\mathbf{z} \sim \mathcal{N}(0, I)$ (the *latent variable*) to a sample $\mathbf{x}' = G(\mathbf{z})$ aimed at matching the data distribution. Co-defined with the [[Discriminator]] inside the [[MinMaxGame|minimax]] adversarial training framework ([[IanGoodfellow|Goodfellow]], Pouget-Abadie, Mirza et al. 2014).

## Training objective

The naive maximization $\max_G \{-\log(1 - D(G(\mathbf{z})))\}$ has a vanishing-gradient pathology when the discriminator is good (i.e., $D(G(\mathbf{z}))$ is small), which happens early in training. The standard non-saturating reformulation ([[d2l-generative-adversarial-networks]] §`gan`) is:

$$\min_G \{-\log D(G(\mathbf{z}))\}$$

— literally *"feeding $\mathbf{x}' = G(\mathbf{z})$ into the discriminator but giving label $y=1$"*. Same fixed point, well-behaved gradients. Every framework's GAN training loop uses this form.

## Architecture taxonomy

| Architecture | Generator structure | D2L reference |
|---|---|---|
| **MLP generator** | Single linear or shallow MLP layer mapping noise → output | §`gan` toy 2-D Gaussian example (single Linear $\mathbb{R}^2\!\to\!\mathbb{R}^2$) |
| **[[DCGAN]] generator** | 4 transposed-conv "blocks" (each = [[TransposedConvolution]] + [[BatchNormalization|BN]] + [[ReLU]]) upsampling from $1{\times}1{\times}100$ noise through $4 \to 8 \to 16 \to 32 \to 64$ spatial resolution; final [[TransposedConvolution]] → 3 channels + $\tanh$ to map to $[-1, 1]$ | §`dcgan` (canonical reference) |

## Why a deliberately *small* generator in the toy example

[[d2l-generative-adversarial-networks]] §`gan` uses a single linear layer for $G$ on the 2-D Gaussian toy — because the data *is* a linear transformation of Gaussian noise, $G$ literally only needs to learn the parameters to fake things perfectly. This pedagogical choice keeps the minimax dynamics in front of the reader without confounding it with capacity issues.

## The "$G$ wins" failure mode

If $G$ wins decisively, $D \equiv 1/2$ (the global Nash equilibrium) — *desired*. If $G$ wins on a single mode while ignoring the others, that is [[ModeCollapse|mode collapse]] — undesired. The chapter's exercise *"does an equilibrium exist where the generator wins?"* points at this distinction.

## Connections

- [[generativeadversarialnetwork|GAN]] — parent framework.
- [[Discriminator]] — adversarial counterpart.
- [[MinMaxGame]] — the formal game-theoretic framing.
- [[ModeCollapse]] — the dominant failure mode of generator training.
- [[TransposedConvolution]] — the structural upsampling primitive for image-generator architectures.
- [[BatchNormalization]] / [[ReLU]] — structural building blocks of DCGAN-style generators.
- [[DCGAN]] — the canonical convolutional generator architecture.
- [[d2l-generative-adversarial-networks]] — canonical source.
