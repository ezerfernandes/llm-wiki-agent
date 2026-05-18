---
title: "Residual connection"
type: concept
tags: [deep-learning, architecture, foundational]
sources: [d2l-convolutional-modern]
last_updated: 2026-05-16
---

# Residual connection

A **residual connection** (or *shortcut connection*) is a path through a neural network that adds the input of a block directly to its output: $f(\mathbf{x})=\mathbf{x}+g(\mathbf{x})$ where $g$ is the block's learnable transformation. Introduced by [[KaimingHe|He]] et al. (2015) in [[ResNet]]; "had a major influence on the design of subsequent deep neural networks, of either convolutional or sequential nature" ([[d2l-convolutional-modern]] §resnet).

## Why it works

- **Easy identity.** If $g(\mathbf{x})=0$ then $f(\mathbf{x})=\mathbf{x}$. Driving the block's weights to zero is much easier than learning the identity function with a stack of convs + nonlinearities. Adding layers cannot make the function class strictly smaller — so increasing depth is "safe."
- **Solves the degradation problem.** Plain (residual-free) very-deep CNNs *train* worse than shallow ones — an optimization failure, not overfitting. Residual connections eliminate this.
- **Gradient flow.** The shortcut path is a $\partial f/\partial \mathbf{x} = I + \partial g/\partial \mathbf{x}$ derivative — never vanishes (the $I$ floor). Combats [[VanishingGradient]] in deep stacks.
- **Forward propagation.** "Inputs can forward propagate faster through the residual connections across layers."

## Shape matching

The addition $\mathbf{x}+g(\mathbf{x})$ requires shape compatibility. When $g$ changes resolution or channel count, a $1\times1$ conv (sometimes also strided) is inserted on the shortcut path:

```
y = g(x)
x' = 1x1_conv(x) if shape_mismatch else x
return y + x'
```

## Used in

- **[[ResNet]] / [[ResNeXt]]** — the original CNNs.
- **[[transformer|Transformers]]** (Vaswani et al. 2017) — every sub-layer (multi-head attention + FFN) is wrapped in `LayerNorm(x + sublayer(x))` (post-LN) or `x + sublayer(LayerNorm(x))` (pre-LN). Without residuals, deep Transformers wouldn't train.
- **RNNs** — Prakash et al. 2016, Kim et al. 2017.
- **Graph neural networks** — Kipf & Welling 2016 graph convolutions adopt the same pattern.
- **Inception-ResNet** — Szegedy et al. 2017 adds residual connections to Inception.

## Precursors and variants

- **Highway networks** (Srivastava et al. 2015) — predates ResNet; adds a *gated* bypass $f(\mathbf{x})=T(\mathbf{x})\cdot g(\mathbf{x}) + (1-T(\mathbf{x}))\cdot \mathbf{x}$ where $T$ is learned. ResNet simplifies to the identity-only case.
- **Pre-activation residuals** (He et al. 2016 v2) — order BN → ReLU → conv → add (instead of conv → BN → ReLU → add). Marginally better for very deep nets.
- **[[DenseNet]]** — concatenates instead of adds: $\mathbf{x}\to[\mathbf{x},g(\mathbf{x})]$. Stronger feature reuse, more memory.

## Connections

- [[d2l-convolutional-modern]] — canonical reference.
- [[ResNet]] / [[ResidualBlock]] — the canonical residual construction.
- [[KaimingHe]] — ResNet's first author.
- [[VanishingGradient]] — the problem residuals partially address.
- [[BatchNormalization]] — typically paired inside residual blocks.
- [[transformer]] / [[Attention]] — heavy users of residuals.
- [[DenseNet]] — concat variant.
- [[SkipConnection]] — synonym; also used for U-Net-style long-range copies.
- [[CNN]] — the architecture family ResNet introduced this in.
