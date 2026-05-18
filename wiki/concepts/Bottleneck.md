---
title: "Bottleneck (CNN block)"
type: concept
tags: [deep-learning, cnn, architecture]
sources: [d2l-convolutional-modern]
last_updated: 2026-05-16
---

# Bottleneck

A **bottleneck block** sandwiches an expensive convolution (typically $3\times3$, possibly grouped) between two $1\times1$ convolutions: the first *reduces* channel count, the second *restores* it. The bottleneck is the dominant compute-frugality pattern in modern CNNs ([[d2l-convolutional-modern]] §resnet, §resnext).

## Structure

```
1×1 conv (c → b)        # reduce: b ≪ c
3×3 conv (b → b)        # expensive op at reduced width
1×1 conv (b → c)        # restore
```

`b` is the **bottleneck width**, often parameterized as `b = c × bot_mul` for a *bottleneck multiplier* `bot_mul ∈ (0, 1]`.

## Cost analysis

| Block | Cost per spatial location |
|---|---|
| Plain $3\times3$ at width $c$ | $\mathcal{O}(c^2 \cdot 9)$ |
| Bottleneck with width $b$ | $\mathcal{O}(c\cdot b + b^2\cdot 9 + b\cdot c) = \mathcal{O}(c\cdot b + 9b^2)$ |

For $b = c/4$ (the standard ResNet-50 ratio): $\mathcal{O}(c^2/4 + 9c^2/16) \approx \mathcal{O}(0.81 c^2)$ — much cheaper than the plain $9c^2$. The savings grow as $b$ shrinks.

## Used in

- **[[ResNet]]-50 / 101 / 152**: bottleneck residual blocks (without grouping).
- **[[ResNeXt]]**: bottleneck residual blocks *with grouped $3\times3$* — combines bottleneck and grouped-conv frugality.
- **[[Inception]] blocks**: branches 2 and 3 use $1\times1$ → $3\times3$ / $5\times5$ — a partial-bottleneck shape (no closing $1\times1$ on a per-branch basis).
- **[[RegNet]] / AnyNet**: bottleneck ratio is a top-level design knob (Radosavovic et al. find $k=1$ — *no bottleneck* — performs best on average).

## When bottlenecks are bad

> "We afford some number of channels, $c_i/k_i$, within each block for stage $i$ ... as the experiments show, this is not really effective and should be skipped." — [[d2l-convolutional-modern]] §cnn-design

The [[RegNet|design-space study]] (Radosavovic et al. 2020) found that **bottleneck ratio $k = 1$** (i.e., no bottleneck) performs best across compute budgets. The bottleneck is a useful compute trick but isn't a free lunch — it loses representational capacity at the inner layer.

## Connections

- [[d2l-convolutional-modern]] — canonical reference.
- [[ResNet]] / [[ResidualBlock]] — first widely-used implementation.
- [[ResNeXt]] — bottleneck + grouped conv.
- [[OneByOneConvolution]] — the flanking primitive.
- [[Inception]] — partial-bottleneck ancestor.
- [[RegNet]] — design-space finding that bottlenecks are suboptimal at the family level.
- [[CNN]] — parent family.
