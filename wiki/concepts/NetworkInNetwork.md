---
title: "Network in Network (NiN)"
type: concept
tags: [deep-learning, cnn, architecture]
sources: [d2l-convolutional-modern]
last_updated: 2026-05-16
---

# Network in Network (NiN)

A CNN design by [[MinLin|Lin]], Chen & Yan (2013) that introduced two innovations that propagated through every subsequent architecture: **$1\times1$ convolutions** ([[OneByOneConvolution|per-pixel FC over channels]]) and **[[GlobalAveragePooling|global average pooling]]** (replacing the expensive FC classification head). NiN is "the alternative" to VGG/AlexNet's FC-heavy design — capable of solving both the FC-parameter-explosion problem and the inability-to-add-nonlinearity-mid-network problem in one strategy ([[d2l-convolutional-modern]] §nin).

## Motivation

VGG-11's first FC layer alone occupies ~400 MB in FP32 — a "significant impediment to computation, in particular on mobile and embedded devices." At VGG's time the iPhone 4S had 512 MB total RAM. Furthermore, you *can't* simply add FC layers earlier in the network — they would destroy spatial structure and explode memory further.

## NiN block

```
Conv k×k (initial — varies per block) + ReLU
Conv 1×1 + ReLU
Conv 1×1 + ReLU
```

The **$1\times1$ convolutions** act as a tiny MLP at every spatial location — adding "local nonlinearities across the channel activations" without spatial mixing. "The idea behind NiN is to apply a fully connected layer at each pixel location."

## NiN network

Initial kernel sizes match AlexNet: $11\times11$, $5\times5$, $3\times3$. Three NiN blocks each followed by $3\times3$ max-pool (stride 2). Then **no FC head** — a final NiN block with `num_classes` output channels, followed by **global average pooling** and flatten. The output is directly a vector of logits.

```
nin_block(96, 11, stride 4)
MaxPool 3×3 stride 2
nin_block(256, 5)
MaxPool 3×3 stride 2
nin_block(384, 3)
MaxPool 3×3 stride 2
Dropout 0.5
nin_block(num_classes, 3)
GlobalAvgPool
Flatten
```

## Influence

- **$1\times1$ convolutions** — appropriated by [[GoogLeNet]] / [[Inception]] (bottleneck branches), [[ResNet]] (bottleneck residual blocks), [[ResNeXt]] (group-then-restore), [[DenseNet]] (transition layers). Most modern CNN FLOPs are spent in $1\times1$ convolutions.
- **Global average pooling** — adopted by [[GoogLeNet]] / [[ResNet]] / [[DenseNet]] / [[RegNet]] / ViT and is now the default classification head. Replaces the FC head's ~hundred MB of parameters with zero parameters.

## Trade-offs

> "NiN has dramatically fewer parameters than AlexNet and VGG. This stems primarily from the fact that it needs no giant fully connected layers. ... What surprised researchers at the time was the fact that this averaging operation did not harm accuracy. Note that averaging across a low-resolution representation (with many channels) also adds to the amount of translation invariance that the network can handle." — [[d2l-convolutional-modern]] §nin summary

Cost: dropping the FC head can increase *training time* (the averaging is a fixed operation; the FC head it replaces was a parameterized one that could learn).

## Connections

- [[d2l-convolutional-modern]] — canonical reference.
- [[OneByOneConvolution]] — the canonical NiN primitive.
- [[GlobalAveragePooling]] — NiN's FC-head replacement.
- [[CNN]] / [[AlexNet]] / [[VGG]] — predecessors.
- [[GoogLeNet]] / [[Inception]] / [[ResNet]] / [[DenseNet]] — successors that adopted NiN's two innovations.
- [[ConvolutionalLayer]] / [[MaxPooling]] / [[Dropout]] — building blocks.
