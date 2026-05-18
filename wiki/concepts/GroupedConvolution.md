---
title: "Grouped convolution"
type: concept
tags: [deep-learning, cnn, architecture]
sources: [d2l-convolutional-modern]
last_updated: 2026-05-16
---

# Grouped convolution

A **grouped convolution** partitions input and output channels into $g$ disjoint groups and applies an independent convolution within each group — reducing both parameters and FLOPs by factor $g$ at the cost of no information flow between groups. Introduced operationally in [[AlexNet]]'s dual-GPU split (Krizhevsky et al. 2012); popularized as a design knob by [[ResNeXt]] (Xie et al. 2017) ([[d2l-convolutional-modern]] §resnext).

## The arithmetic

A plain convolution from $c_i$ to $c_o$ channels with $k\times k$ kernel costs $\mathcal{O}(c_i \cdot c_o \cdot k^2)$ per spatial location. Splitting into $g$ groups of $c_i/g \to c_o/g$ each yields:

$$\mathcal{O}\bigl(g\cdot (c_i/g)\cdot (c_o/g)\cdot k^2\bigr) = \mathcal{O}(c_i\cdot c_o\cdot k^2 / g)$$

— a $g$-fold reduction in both parameters and FLOPs. Block-diagonal-weight-matrix interpretation: the unconstrained weight matrix is $c_o\times c_i$; the grouped version is block-diagonal with $g$ blocks of $(c_o/g)\times(c_i/g)$.

## Information flow caveat

> "The only challenge in this design is that no information is exchanged between the $g$ groups." — [[d2l-convolutional-modern]] §resnext

[[ResNeXt]] addresses this by sandwiching the grouped $3\times3$ between two ordinary (non-grouped) $1\times1$ convolutions — restoring cross-group mixing at the block boundaries.

## Special cases

- **$g=1$**: ordinary convolution.
- **$g=c_i=c_o$**: depthwise convolution (each channel processed independently). Used in MobileNet, Xception, EfficientNet.
- **Depthwise-separable**: depthwise + ordinary $1\times1$. Cheapest practical variant.

## API

PyTorch: `nn.Conv2d(in_channels, out_channels, kernel_size, groups=g)`. The constraint is that both `in_channels` and `out_channels` must be divisible by `groups`.

## Historical origin: AlexNet's dual-GPU split

> "Note that the idea of grouped convolutions dates back to the implementation of AlexNet. When distributing the network across two GPUs with limited memory, the implementation treated each GPU as its own channel with no ill effects." — [[d2l-convolutional-modern]] §resnext

[[AlexNet]] (2012) split channels across two GTX 580 GPUs (3 GB each) for *memory* reasons — accidentally producing the first grouped convolution. The two halves cross-mixed only at a few specific layers.

## Connections

- [[d2l-convolutional-modern]] — canonical reference.
- [[ResNeXt]] — the canonical user.
- [[AlexNet]] — historical origin (dual-GPU memory split).
- [[ConvolutionalLayer]] / [[Convolution]] — parent operations.
- [[Bottleneck]] — typically wrapped in $1\times1$ convs to recover cross-group mixing.
- [[OneByOneConvolution]] — the "no $k^2$ factor" counterpart frequently paired with grouped $3\times3$.
- [[CNN]] — parent family.
