---
title: "ResNet"
type: concept
tags: [deep-learning, cnn, architecture, foundational]
sources: [d2l-convolutional-modern]
last_updated: 2026-05-16
---

# ResNet

The residual network by [[KaimingHe|He]], [[XiangyuZhang|Zhang]], [[ShaoqingRen|Ren]] & [[JianSun|Sun]] (2015) at Microsoft Research Asia — winner of **[[ImageNet|ILSVRC 2015]]** with depths up to 152 layers. ResNet introduced the **[[ResidualBlock|residual block]]** $f(\mathbf{x})=\mathbf{x}+g(\mathbf{x})$ — the single most-influential CNN-design idea after the convolutional layer itself, subsequently propagated into [[transformer|Transformers]], RNNs, graph neural networks, and beyond ([[d2l-convolutional-modern]] §resnet). "ResNet remains one of the most popular off-the-shelf architectures in computer vision."

## The motivating idea — nested function classes

For non-nested function classes, adding capacity does not guarantee strictly better fits: a larger $\mathcal{F}'$ may simply be *different*, not better. But if **every added layer can learn the identity function**, then $\mathcal{F}\subseteq\mathcal{F}'$ — strictly more powerful.

> "At the heart of their proposed *residual network* is the idea that every additional layer should more easily contain the identity function as one of its elements. These considerations are rather profound but they led to a surprisingly simple solution, a *residual block*." — [[d2l-convolutional-modern]] §resnet

## The residual block

Two $3\times3$ convolutions, each followed by [[BatchNormalization|BN]] and [[ReLU]] (with the second ReLU applied *after* the addition):

```
y = x
y = ReLU(BN(Conv3x3(y)))
y = BN(Conv3x3(y))
y = y + (x  [or 1x1-conv(x) if shape mismatch])
y = ReLU(y)
```

The **shortcut path** is the identity (when shapes match) or a $1\times1$ conv (when the block changes resolution or channel count). To halve resolution and double channels: `use_1x1conv=True, strides=2`.

If the identity mapping $f(\mathbf{x})=\mathbf{x}$ is optimal, learning it reduces to driving $g(\mathbf{x})\to 0$ — i.e., pushing one conv's weights to zero. **Much easier than learning the identity directly.**

## The degradation problem ResNet solved

Pre-ResNet: stacking more layers in plain CNNs *degraded training accuracy* — not from overfitting (training error went up), but from optimization difficulty. ResNet showed that 152-layer networks could be trained to *lower* training error than 20-layer plain CNNs once residual connections were added. Highway networks (Srivastava et al. 2015) anticipated the idea with gated bypass paths but lacked the elegant identity parametrization.

## ResNet-18 architecture (the D2L worked example)

- **Stem** (b1): $7\times7$ conv (64 ch, stride 2) → BN → ReLU → $3\times3$ max-pool (stride 2). Same as [[GoogLeNet]].
- **Body** (b2–b5): four modules, each with 2 residual blocks. First block of b3/b4/b5 uses `use_1x1conv=True, strides=2` to halve resolution and double channels. Module 1: 64 ch, 56×56. Module 4: 512 ch, 7×7.
- **Head**: global average pool → FC(num_classes).

Total: 18 conv-layer-equivalents (counted excluding the $1\times1$ shortcuts).

## ResNet family

| Variant | Depth | Block type |
|---|---|---|
| ResNet-18 / 34 | 18 / 34 | basic (two 3×3) |
| ResNet-50 / 101 / 152 | 50 / 101 / 152 | bottleneck ($1\times1\to3\times3\to1\times1$) |

The **bottleneck variant** (50+) sandwiches a $3\times3$ conv between two $1\times1$ convs that reduce + restore channel count — order-of-magnitude FLOP savings while preserving expressiveness. [[ResNeXt]] generalizes this with grouped convolutions.

## Pre-activation variant

A subsequent paper (He et al. 2016 "Identity mappings in deep residual networks") flipped the order to **BN → ReLU → Conv** inside the residual branch — see [[d2l-convolutional-modern]] §resnet exercise 4 and the [[DenseNet]] design that adopts it.

## Why ResNet became ubiquitous

> "Although the main architecture of ResNet is similar to that of GoogLeNet, ResNet's structure is simpler and easier to modify. All these factors have resulted in the rapid and widespread use of ResNet."

- Simpler than Inception (one block type, one stride knob).
- Naturally deep (152 layers worked out of the box).
- Residual connections drop into any architecture — RNNs, Transformers, graph nets.
- **Pretrained ResNet-50** is the standard CV transfer-learning starting point.

## Connections

- [[d2l-convolutional-modern]] — canonical reference.
- [[KaimingHe]] — first author.
- [[ResidualBlock]] / [[ResidualConnection]] / [[SkipConnection]] — the primitive.
- [[BatchNormalization]] / [[ReLU]] — used inside every residual block.
- [[OneByOneConvolution]] — the shortcut-shape adjuster and bottleneck primitive.
- [[CNN]] / [[AlexNet]] / [[VGG]] / [[GoogLeNet]] — predecessors.
- [[ResNeXt]] / [[DenseNet]] / [[RegNet]] — direct successors.
- [[transformer]] — adopted residual connections wholesale.
- [[microsoftresearch]] — institutional home (MSRA).
- [[ImageNet]] — the benchmark won (ILSVRC 2015).
