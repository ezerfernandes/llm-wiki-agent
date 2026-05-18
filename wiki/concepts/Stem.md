---
title: "Stem (CNN)"
type: concept
tags: [deep-learning, cnn, architecture]
sources: [d2l-convolutional-modern]
last_updated: 2026-05-16
---

# Stem

The **stem** is the initial section of a modern CNN — the layers that ingest the raw image and produce a coarsened, channel-rich feature map suitable for the body's processing blocks. Popularized as a named architectural section by [[GoogLeNet]] ([[ChristianSzegedy|Szegedy]] et al. 2015) and adopted by every subsequent design ([[d2l-convolutional-modern]] §googlenet, §cnn-design).

## Typical structure

```
Conv 7×7 (or 3×3) [c₀ channels, stride 2]
BN + ReLU
MaxPool 3×3 (stride 2)   [optional]
```

The stem typically halves resolution (sometimes twice — once via stride-2 conv, once via stride-2 pool) and emits $c_0$ channels. [[ResNet]] / [[DenseNet]] use a $7\times7$ stride-2 conv; [[RegNet]] / AnyNet uses a $3\times3$ stride-2 conv.

## Stem / body / head decomposition

> "It was arguably also the first network that exhibited a clear distinction among the stem (data ingest), body (data processing), and head (prediction) in a CNN. This design pattern has persisted ever since in the design of deep networks." — [[d2l-convolutional-modern]] §googlenet

| Section | Job |
|---|---|
| **Stem** | Ingest raw image; produce $c_0$-channel feature map at $r/2 \times r/2$ resolution. |
| **Body** | Repeated stages of [[ConvolutionalLayer\|conv]] / [[ResidualBlock\|residual]] / [[Inception]] / [[ResNeXt]] blocks. Each stage halves resolution and increases channels. |
| **Head** | [[GlobalAveragePooling]] + FC(num_classes) — the classification readout. |

The same template applies to detection / segmentation networks — only the head changes.

## Connections

- [[d2l-convolutional-modern]] — canonical reference.
- [[NetworkHead]] — sibling section.
- [[GoogLeNet]] / [[ResNet]] / [[DenseNet]] / [[RegNet]] — all use the stem/body/head template.
- [[ConvolutionalLayer]] / [[MaxPooling]] / [[BatchNormalization]] — building blocks.
- [[CNN]] — parent family.
