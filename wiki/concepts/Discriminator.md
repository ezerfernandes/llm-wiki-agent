---
title: "Discriminator (GAN)"
type: concept
tags: [generative-model, gan, deep-learning]
sources: [d2l-generative-adversarial-networks]
last_updated: 2026-05-16
---

# Discriminator (GAN)

The "two-sample classifier" half of a [[generativeadversarialnetwork|GAN]]: a binary classifier $D: \mathbf{x} \mapsto [0, 1]$ trained to distinguish real data ($y=1$) from generator outputs ($y=0$), providing the training signal for the [[Generator]] ([[IanGoodfellow|Goodfellow]], Pouget-Abadie, Mirza et al. 2014; [[d2l-generative-adversarial-networks]] §`gan`).

## Training objective

Standard [[BinaryCrossEntropy|BCE]] / [[CrossEntropyLoss|cross-entropy]] over real + fake samples:

$$\min_D \{-y \log D(\mathbf{x}) - (1-y) \log(1 - D(\mathbf{x}))\}$$

In code, this is `(loss(D(real), ones) + loss(D(fake.detach()), zeros)) / 2`. The `.detach()` is essential — the discriminator update should *not* backpropagate through $G$ (we have separate `update_D` and `update_G` functions per [[d2l-generative-adversarial-networks]] §`gan`).

## Architecture taxonomy

| Architecture | Discriminator structure | D2L reference |
|---|---|---|
| **MLP discriminator** | 3-layer MLP with [[Tanh]] activations (e.g., $2 \to 5 \to 3 \to 1$) | §`gan` 2-D Gaussian toy |
| **[[DCGAN]] discriminator** | 4 strided-conv "blocks" (each = [[ConvolutionalLayer|Conv2d]] stride 2 + [[BatchNormalization|BN]] + [[LeakyReLU]] $\alpha=0.2$) halving spatial dims and doubling channels each step; final $4\!\times\!4$ conv → single logit | §`dcgan` (canonical reference) |

## Why "a bit more discriminating"

[[d2l-generative-adversarial-networks]] §`gan` deliberately gives $D$ a 3-layer MLP while $G$ is a single linear layer in the toy example — *"For the discriminator we will be a bit more discriminating: we will use an MLP with 3 layers to make things a bit more interesting."* A weak discriminator gives the generator no useful gradient; this asymmetry is structural to early-training GAN dynamics.

## Why [[LeakyReLU]] (not [[ReLU]]) for $D$

DCGAN discriminators activate via [[LeakyReLU]] $\alpha=0.2$ rather than standard [[ReLU]] specifically to fix the "dying ReLU" pathology — early in training, many of the discriminator's pre-activations are negative (because the generator's fakes are bad and easy to classify), and a standard ReLU would silently zero out gradients in those units. Leaky ReLU keeps a non-zero gradient flowing, letting $D$ continue to update through bad initial regimes ([[d2l-generative-adversarial-networks]] §`dcgan`).

## Output: logits, not probabilities

D2L's `nn.BCEWithLogitsLoss` consumes raw logits and fuses sigmoid + BCE for numerical stability (see [[LogSumExp]] trick). The final layer of `net_D` is a Linear (or Conv) with no activation; the loss applies the sigmoid internally.

## Connections

- [[generativeadversarialnetwork|GAN]] — parent framework.
- [[Generator]] — adversarial counterpart.
- [[MinMaxGame]] — the formal game-theoretic framing.
- [[BinaryCrossEntropy|BCE]] / [[CrossEntropyLoss]] — the training objective.
- [[LeakyReLU]] — the activation that distinguishes DCGAN discriminators from standard CNNs.
- [[BatchNormalization]] / [[ConvolutionalLayer]] — structural building blocks of DCGAN-style discriminators.
- [[DCGAN]] — the canonical convolutional discriminator architecture.
- [[d2l-generative-adversarial-networks]] — canonical source.
