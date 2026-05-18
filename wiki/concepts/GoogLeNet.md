---
title: "GoogLeNet"
type: concept
tags: [deep-learning, cnn, architecture, computer-vision]
sources: [d2l-convolutional-modern]
last_updated: 2026-05-16
---

# GoogLeNet

The 22-layer CNN by [[ChristianSzegedy|Szegedy]] et al. (2015) at [[google|Google]] that won **[[ImageNet|ILSVRC 2014]]** ([[VGG]] was runner-up). Built from a stack of nine **[[Inception|Inception blocks]]** — multi-branch concatenation modules combining $1\times1$, $3\times3$, $5\times5$ convolutions and $3\times3$ max-pooling in parallel ([[d2l-convolutional-modern]] §googlenet). GoogLeNet was the first widely-known CNN to exhibit a clean **stem / body / head** decomposition — a design template adopted by every subsequent architecture in the chapter.

## Stem / body / head template

GoogLeNet established the now-universal CNN structure:

- **Stem** (b1, b2): initial $7\times7$ stride-2 conv + max-pool, then $1\times1$ → $3\times3$ → max-pool. Halves resolution; produces 192 channels.
- **Body** (b3, b4, b5): three groups of [[Inception]] blocks (2 + 5 + 2 = 9 total) separated by max-pool downsampling. Channels grow stage-wise: 256 → 480 → 512..832 → 832..1024.
- **Head**: global average pool + fully-connected output layer.

## Inception block (see [[Inception]])

Four parallel branches, concatenated along the channel axis:

1. $1\times1$ conv
2. $1\times1$ conv → $3\times3$ conv
3. $1\times1$ conv → $5\times5$ conv
4. $3\times3$ max-pool → $1\times1$ conv

Branches 2 and 3 use $1\times1$ convs as **channel-reduction bottlenecks** before the expensive larger kernels — drastically reducing FLOPs.

## Significance

> "A key feature of GoogLeNet is that it is actually *cheaper* to compute than its predecessors while simultaneously providing improved accuracy. This marks the beginning of a much more deliberate network design that trades off the cost of evaluating a network with a reduction in errors. It also marks the beginning of experimentation at a block level with network design hyperparameters." — [[d2l-convolutional-modern]] §googlenet discussion

- First CNN to *explicitly* trade compute for accuracy.
- First widespread use of the stem/body/head pattern that persists in every modern CNN.
- The "let training allocate capacity across all kernel sizes" philosophy replaced the "pick the right kernel size" debate.

## Successor variants

- **Inception-v2/v3** (Szegedy, Vanhoucke, Ioffe et al. 2016): adds [[BatchNormalization|BN]] and label smoothing; factorizes $n\times n$ into $1\times n$ + $n\times1$.
- **Inception-v4 / Inception-ResNet** (Szegedy, Ioffe, Vanhoucke et al. 2017): adds residual connections.
- **Xception** (Chollet 2017): replaces Inception modules with depthwise-separable convolutions.

## Notable caveats

GoogLeNet has many seemingly-arbitrary hyperparameters (channel counts per branch, number of blocks per stage, etc.) — a relic of pre-NAS, pre-automatic-shape-inference manual design. Subsequent architectures ([[ResNet]] / [[RegNet]]) chose more uniform, explicable design rules.

## Connections

- [[d2l-convolutional-modern]] — canonical reference.
- [[ChristianSzegedy]] — first author.
- [[Inception]] — the multi-branch building block.
- [[google]] — institutional home.
- [[CNN]] / [[AlexNet]] / [[VGG]] / [[NetworkInNetwork]] — predecessors.
- [[ResNet]] / [[DenseNet]] / [[RegNet]] — successors.
- [[Stem]] / [[NetworkHead]] — the template GoogLeNet popularized.
- [[OneByOneConvolution]] — the bottleneck primitive in branches 2 and 3.
- [[GlobalAveragePooling]] — head replacement adopted from NiN.
- [[ImageNet]] — the benchmark won.
