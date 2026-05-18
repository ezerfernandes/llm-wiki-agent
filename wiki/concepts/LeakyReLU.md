---
title: "Leaky ReLU"
type: concept
tags: [activation-function, neural-networks, gan]
sources: [d2l-generative-adversarial-networks]
last_updated: 2026-05-16
---

# Leaky ReLU

Variant of [[ReLU]] that keeps a *non-zero* gradient for negative inputs. Given $\alpha \in [0, 1]$:

$$\textrm{leaky ReLU}(x) = \begin{cases} x & \textrm{if } x > 0 \\ \alpha x & \textrm{otherwise} \end{cases}$$

At $\alpha = 0$ this is the standard [[ReLU]]; at $\alpha = 1$ it is the identity function; for $\alpha \in (0, 1)$ it is a piecewise-linear nonlinearity with non-zero slope in *both* half-planes ([[d2l-generative-adversarial-networks]] §`dcgan`).

## Why it exists: the "dying ReLU" fix

Standard [[ReLU]] has gradient zero for $x < 0$. A neuron whose pre-activation lands in the negative half-plane across all training inputs receives zero gradient *forever* — it stops learning. This is the "dying ReLU" pathology, and it is acute in two regimes:

1. **Early training of any deep network** with large learning rates that can drive pre-activations sharply negative.
2. **[[Discriminator|GAN discriminators]] early in training**, where the generator's fakes are bad and the discriminator's pre-activations are mostly negative on the easy-to-classify fakes — exactly the regime D2L's `D_block` is designed for.

Leaky ReLU eliminates the pathology: the gradient is $\alpha$ (not 0) for $x < 0$, so the neuron can always escape.

## Default value: $\alpha = 0.2$

[[DCGAN]] standardized $\alpha = 0.2$ for the discriminator. The [[d2l-generative-adversarial-networks]] chapter explicitly visualizes the family $\alpha \in \{0, 0.2, 0.4, 0.6, 0.8, 1\}$ to show the smooth interpolation between ReLU and the identity. The discriminator's `D_block` in D2L's code is `Conv2d → BatchNorm2d → LeakyReLU(0.2, inplace=True)`.

## Where it lives in the modern stack

- **[[DCGAN]] discriminators** — the canonical use case; $\alpha = 0.2$ is the default.
- **Many subsequent GAN variants** (StyleGAN, BigGAN, etc.) — retain Leaky ReLU in $D$.
- **Some object-detection heads** (early YOLO variants) — Leaky ReLU throughout the backbone.

Note: most non-GAN modern architectures ([[ResNet]], [[Transformer]] FFNs) use standard [[ReLU]] or [[GELU]] / [[Swish|SiLU]]. Leaky ReLU is mostly a GAN-discriminator-specific tool.

## Variants

- **[[ReLU]]** — the $\alpha = 0$ special case.
- **pReLU** ([[KaimingHe|He]] et al. 2015) — same shape but $\alpha$ is *learned* per-channel.
- **ELU** (Clevert et al. 2015) — smooth exponential approach to $-1$ on the left half-plane; addresses the same "dying ReLU" problem with a saturating non-linearity.
- **[[GELU]]** — smooth standard-normal-CDF-weighted ReLU; default in [[Transformer]]s.

## Connections

- [[ReLU]] — parent activation.
- [[ActivationFunction]] — family.
- [[Discriminator]] — the GAN role this activation is built for.
- [[DCGAN]] — the canonical architecture that standardized $\alpha = 0.2$.
- [[VanishingGradient]] — the broader problem the dying-ReLU fix addresses.
- [[d2l-generative-adversarial-networks]] — canonical source.
