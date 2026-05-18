---
title: "Global average pooling"
type: concept
tags: [deep-learning, cnn, architecture]
sources: [d2l-convolutional-modern]
last_updated: 2026-05-16
---

# Global average pooling

A pooling operator that **averages each channel over its entire spatial extent**, producing a single value per channel. For an input of shape $(N, C, H, W)$, output shape is $(N, C, 1, 1)$ (or $(N, C)$ after flatten). Introduced by [[MinLin|Lin]], Chen & Yan in [[NetworkInNetwork|NiN]] (2013); now the **default classification-head replacement** in modern CNNs ([[d2l-convolutional-modern]] §nin).

## Mechanically

```
GlobalAvgPool(X)[n, c] = (1 / (H × W)) × Σᵢ Σⱼ X[n, c, i, j]
```

Equivalent to an [[AveragePooling|average pooling]] layer with window size = full spatial extent. PyTorch idiom: `nn.AdaptiveAvgPool2d((1, 1))`. Flax: `nn.avg_pool(x, window_shape=x.shape[1:3], strides=x.shape[1:3])`.

## What it replaces

The traditional CNN classification head — `Flatten → FC(num_features → 4096) → ReLU → Dropout → FC(4096 → 4096) → ReLU → Dropout → FC(4096 → num_classes)` — has tens to hundreds of millions of parameters dominated by the first FC layer. Global average pooling replaces all of this with:

```
GlobalAvgPool → Flatten → FC(num_channels → num_classes)
```

— ~0% of the parameter count.

## Why it works

- **Zero parameters.** Cannot overfit by itself.
- **Translation invariance.** Averaging over an entire channel is maximally translation-invariant — sliding the input by any amount gives nearly the same output.
- **Forces channel-as-feature.** Combined with a NiN-style block that outputs `num_classes` channels (or a ResNet/DenseNet-style end-of-body channel count), the network is *encouraged* to compute "class evidence" channel-by-channel — interpretable, semi-attention-like.

> "Note that averaging across a low-resolution representation (with many channels) also adds to the amount of translation invariance that the network can handle." — [[d2l-convolutional-modern]] §nin summary

## Used in

- [[NetworkInNetwork]] — originator.
- [[GoogLeNet]] / [[Inception]] — adopted from NiN.
- [[ResNet]] / [[ResNeXt]] / [[DenseNet]] / [[RegNet]] — universal head choice.
- [[VisionTransformer|ViT]] — uses a special `[CLS]` token instead, but its mean-pooled-patch variant is equivalent in spirit.

## Connections

- [[d2l-convolutional-modern]] — canonical reference.
- [[NetworkInNetwork]] — origin.
- [[AveragePooling]] — the per-window version.
- [[Pooling]] — parent operation.
- [[CNN]] — architectural context.
- [[ResNet]] / [[GoogLeNet]] / [[DenseNet]] / [[RegNet]] — adopters.
