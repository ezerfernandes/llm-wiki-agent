---
title: "VGG"
type: concept
tags: [deep-learning, cnn, architecture, computer-vision]
sources: [d2l-convolutional-modern]
last_updated: 2026-05-16
---

# VGG

A family of CNN architectures by [[KarenSimonyan|Simonyan]] & [[AndrewZisserman|Zisserman]] (2014) at the **Visual Geometry Group**, [[oxforduniversity|Oxford]]. VGG popularized **blocks of multiple small $3\times3$ convolutions** as the basic CNN building block and the doctrine "**deep and narrow beats shallow**" — set deep learning on a quest for ever-deeper networks ([[d2l-convolutional-modern]] §vgg). Runner-up to [[GoogLeNet]] at ILSVRC 2014 but became, alongside [[ResNet]], one of the two dominant pre-2020 CNN backbones for transfer learning.

## VGG block

```
[Conv 3×3 (pad 1) + ReLU] × num_convs
MaxPool 2×2 (stride 2)
```

Each block preserves resolution through `num_convs` convs (because of pad 1) then halves resolution via max-pool. Output channels typically double from one block to the next: 64 → 128 → 256 → 512 → 512.

## Why two $3\times3$ convs beat one $5\times5$

Two stacked $3\times3$ convolutions cover the same receptive field as one $5\times5$ but:

- **Parameters:** $2\cdot 9c^2 = 18c^2$ vs. $25c^2$ for $5\times5$.
- **Nonlinearities:** two interleaved ReLUs vs. one.
- **Implementations:** $3\times3$ kernels are heavily GPU-optimized (cuDNN, Winograd).

Three $3\times3$ convs ≈ one $7\times7$ — same logic. This is **why $3\times3$ became the universal CNN kernel size** until ConvNeXt revisited the choice (Liu et al. 2022).

## VGG-11 / 16 / 19

The "-N" suffix counts weight layers (conv + FC). VGG-11 = 8 conv + 3 FC. VGG-16 / VGG-19 add more convs per block.

The **convolutional part** is parameterized by an `arch` list of `(num_convs, num_channels)` tuples — D2L: `arch=((1,64),(1,128),(2,256),(2,512),(2,512))` gives VGG-11. The **dense head** is identical to AlexNet's: Flatten → FC(4096) → ReLU → Dropout 0.5 → FC(4096) → ReLU → Dropout 0.5 → FC(num_classes).

## Significance

> "One might argue that VGG is the first truly modern convolutional neural network. While AlexNet introduced many of the components of what make deep learning effective at scale, it is VGG that arguably introduced key properties such as blocks of multiple convolutions and a preference for deep and narrow networks. It is also the first network that is actually an entire family of similarly parametrized models, giving the practitioner ample trade-off between complexity and speed." — [[d2l-convolutional-modern]] §vgg summary

The shift from "design individual layers" to "design blocks, iterate" was a paradigm shift in CNN engineering — mirroring VLSI design progressing from transistors to logic blocks. Every subsequent architecture in [[d2l-convolutional-modern]] follows the block paradigm.

## Costs

- **Compute:** much slower than [[AlexNet]]; FC layers dominate parameters (~400 MB FP32 for VGG-11's first FC layer alone).
- **Memory:** the FC head is the bottleneck. [[NetworkInNetwork|NiN]] kills this by replacing the FC head with global average pooling.

## Connections

- [[d2l-convolutional-modern]] — canonical reference.
- [[KarenSimonyan]] / [[AndrewZisserman]] — authors.
- [[oxforduniversity]] — Visual Geometry Group's institutional home.
- [[CNN]] / [[AlexNet]] — predecessors.
- [[NetworkInNetwork]] / [[GoogLeNet]] / [[ResNet]] — successors that kept the block paradigm.
- [[ConvolutionalLayer]] / [[MaxPooling]] — the building blocks of VGG blocks.
- [[Dropout]] — used in the FC head.
- [[ImageNet]] — VGG was ILSVRC 2014 runner-up.
