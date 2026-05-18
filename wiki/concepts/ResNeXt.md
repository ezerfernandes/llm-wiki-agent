---
title: "ResNeXt"
type: concept
tags: [deep-learning, cnn, architecture]
sources: [d2l-convolutional-modern]
last_updated: 2026-05-16
---

# ResNeXt

The grouped-convolution generalization of [[ResNet]] by [[Xie|Xie]], [[RossGirshick|Girshick]], [[PiotrDollar|Dollár]] et al. (2017) at [[fair|FAIR]]. ResNeXt sandwiches a **grouped $3\times3$ convolution** between two $1\times1$ convolutions in a bottleneck block, trading channel count against FLOPs more favorably than plain ResNet ([[d2l-convolutional-modern]] §resnext).

## The grouped-convolution insight

A plain convolution from $c_i$ to $c_o$ channels costs $\mathcal{O}(c_i\cdot c_o)$ in both parameters and FLOPs. Splitting it into $g$ groups of $c_i/g \to c_o/g$ each yields:

$$\mathcal{O}\bigl(g\cdot (c_i/g)\cdot (c_o/g)\bigr) = \mathcal{O}(c_i\cdot c_o / g)$$

— a $g$-fold reduction in both parameters and FLOPs. The catch: no information flows between groups.

## The ResNeXt block

Two $1\times1$ convs flank a grouped $3\times3$ conv, restoring full cross-channel mixing at the ends:

```
y = x
y = ReLU(BN(Conv1x1(y, bot_channels)))      # reduce
y = ReLU(BN(Conv3x3(y, bot_channels, groups=bot_channels//groups)))  # grouped
y = BN(Conv1x1(y, num_channels))            # restore
y = y + x                                   # residual
y = ReLU(y)
```

- $b = $ `bot_channels` — bottleneck width. Often `bot_mul × num_channels`.
- $g = $ `groups` — group count for the $3\times3$.
- The $1\times1$ convs cost $\mathcal{O}(c\cdot b)$; the $3\times3$ costs $\mathcal{O}(b^2/g)$.

## Relationship to Inception

> "Different from the smorgasbord of transformations in Inception, ResNeXt adopts the *same* transformation in all branches, thus minimizing the need for manual tuning of each branch." — [[d2l-convolutional-modern]] §resnext

ResNeXt is "Inception with all branches identical." Easier to tune; cleaner ablations; same multi-branch benefit.

## Connection to AlexNet (full circle)

The idea of grouped convolutions dates back to [[AlexNet]]'s 1989 dual-GPU split — there, each GPU treated half the channels as "its own" with no cross-GPU mixing. AlexNet did this for *memory* reasons; ResNeXt does it for *compute* reasons.

## Significance

> "ResNeXt is an example for how the design of convolutional neural networks has evolved over time: by being more frugal with computation and trading it off against the size of the activations (number of channels), it allows for faster and more accurate networks at lower cost. An alternative way of viewing grouped convolutions is to think of a block-diagonal matrix for the convolutional weights." — [[d2l-convolutional-modern]] §resnext summary

ResNeXt's block becomes the **AnyNet** building block in the [[RegNet|RegNet design-space]] study (Radosavovic et al. 2020).

## Related efficient-CNN tricks

- **Depthwise-separable convolutions** (MobileNet, Xception): grouped conv with $g=c$ + $1\times1$ — the extreme of ResNeXt's idea.
- **ShiftNet** (Wu et al. 2018): mimics $3\times3$ by *shifting* channels — zero compute cost.

## Connections

- [[d2l-convolutional-modern]] — canonical reference.
- [[ResNet]] — direct parent.
- [[ResidualBlock]] / [[Bottleneck]] — the ResNeXt block is a grouped-bottleneck residual block.
- [[GroupedConvolution]] — the primitive.
- [[Inception]] — conceptual ancestor (multi-branch).
- [[OneByOneConvolution]] — the flanking primitive.
- [[RegNet]] — uses the ResNeXt block as its AnyNet building block.
- [[fair]] / [[meta]] — institutional home.
- [[AlexNet]] — historical precedent of grouped convolutions (dual-GPU split).
- [[CNN]] — parent family.
