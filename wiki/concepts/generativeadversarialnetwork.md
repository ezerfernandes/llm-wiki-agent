---
title: "Generative Adversarial Network (GAN)"
type: concept
tags: [generative-model, deep-learning]
sources: [d2l-introduction, d2l-generative-adversarial-networks]
last_updated: 2026-05-16
---

# Generative Adversarial Network (GAN)

[[IanGoodfellow|Goodfellow]], Pouget-Abadie, Mirza et al. 2014. A deep [[UnsupervisedLearning|unsupervised]] [[RepresentationLearning|representation-learning]] technique for **density estimation** in which the explicit probability distribution is replaced by an arbitrary differentiable generator $G$.

## The chapter's framing

[[d2l-introduction]]: "Traditionally, statistical methods for density estimation and generative models focused on finding proper probability distributions and (often approximate) algorithms for sampling from them. As a result, these algorithms were largely limited by the lack of flexibility inherent in the statistical models. The crucial innovation in generative adversarial networks was to replace the sampler by an arbitrary algorithm with differentiable parameters."

The [[Generator|generator]]'s parameters are then tuned so that a [[Discriminator|discriminator]] $D$ (effectively a two-sample test) cannot distinguish $G$'s outputs from real data. The two networks play a [[MinMaxGame|minimax game]].

## The full operational treatment

D2L's dedicated [[d2l-generative-adversarial-networks]] chapter operationalizes the framework end-to-end:

- **Objective.** $\min_D \max_G \{-E_{\mathbf{x}\sim\textrm{Data}} \log D(\mathbf{x}) - E_{\mathbf{z}\sim\textrm{Noise}} \log(1 - D(G(\mathbf{z})))\}$ — the canonical Goodfellow et al. 2014 [[MinMaxGame|minimax]] objective. At Nash equilibrium $D \equiv 1/2$ and $p_g \equiv p_{\textrm{data}}$.
- **Non-saturating $G$ loss.** Instead of the naive $\max_G$ form (which has vanishing gradients when $D(G(\mathbf{z}))$ is small), minimize $-\log D(G(\mathbf{z}))$ — feed fakes through $D$ with the *real* label $y=1$. The canonical reformulation every framework's GAN code uses.
- **[[DCGAN]] architecture** ([[AlecRadford|Radford]], Metz & Chintala 2015). All-convolutional [[Generator]] (4 [[TransposedConvolution|transposed convs]] + [[BatchNormalization|BN]] + [[ReLU]] + final $\tanh$) and mirror-image [[Discriminator]] (4 strided convs + BN + [[LeakyReLU]] $\alpha=0.2$). The first architecture to make GAN training reliably stable on natural images.
- **Training recipe.** [[Adam]] with $\beta_1 = 0.5$ (vs default $0.9$); same LR for $D$ and $G$; weights initialized from $\mathcal{N}(0, 0.02^2)$.
- **Dominant failure mode**: [[ModeCollapse|mode collapse]] — $G$ exploits a single mode and fools $D$ without matching the data distribution.

## Applications cited by D2L

- Photorealistic image synthesis from sketches (Park, Liu, Wang et al. 2019).
- Galloping zebras / style transfer (Zhu, Park, Isola et al. 2017 — CycleGAN).
- Fake celebrity faces (Karras, Aila, Laine et al. 2017 — ProGAN).
- 2-D Gaussian density-estimation toy ([[d2l-generative-adversarial-networks]] §`gan`); Pokémon-sprite image synthesis ([[d2l-generative-adversarial-networks]] §`dcgan`).

## Where they fit historically

[[d2l-introduction]] lists GANs among the early deep generative breakthroughs alongside [[VariationalAutoencoder|VAEs]] (Kingma & Welling 2014; Rezende & Mohamed 2014), with **normalizing flows** (Dinh et al. 2014/2017) and **[[DiffusionModel|diffusion models]]** (Sohl-Dickstein et al. 2015; Ho et al. 2020; Song et al. 2021) following. The chapter notes that diffusion models have **started to replace GANs** in production systems like DALL-E 2 (Ramesh et al. 2022) and Imagen (Saharia et al. 2022).

## Connections

- [[UnsupervisedLearning]] — parent paradigm.
- [[Generator]] / [[Discriminator]] / [[MinMaxGame]] / [[ModeCollapse]] — the four conceptual primitives.
- [[DCGAN]] — the canonical convolutional GAN architecture; the practical-reliability scale-up.
- [[IanGoodfellow]] — inventor; first author of Goodfellow et al. 2014.
- [[AlecRadford]] — [[DCGAN]] first author.
- [[TransposedConvolution]] / [[BatchNormalization]] / [[LeakyReLU]] / [[Adam]] — the four structural building blocks.
- [[DiffusionModel]] — successor generative-model family.
- [[Autoencoder]] — relative (VAEs share the encoder-decoder skeleton).
- [[d2l-introduction]] — corpus anchor introducing GAN history.
- [[d2l-generative-adversarial-networks]] — D2L's dedicated chapter; canonical operational reference.
