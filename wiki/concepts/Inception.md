---
title: "Inception block"
type: concept
tags: [deep-learning, cnn, architecture]
sources: [d2l-convolutional-modern]
last_updated: 2026-05-16
---

# Inception block

The multi-branch CNN module at the heart of [[GoogLeNet]] (Szegedy et al. 2015). The block stems from the *Inception* movie meme "we need to go deeper" and *concatenates* (rather than chooses between) multi-scale convolutions ([[d2l-convolutional-modern]] §googlenet).

## Structure

Four parallel branches operating on the same input; outputs concatenated along the channel axis at the end.

| Branch | Operation |
|---|---|
| 1 | $1\times1$ conv → channels $c_1$ |
| 2 | $1\times1$ conv → $c_{2,0}$ → $3\times3$ conv → channels $c_{2,1}$ |
| 3 | $1\times1$ conv → $c_{3,0}$ → $5\times5$ conv → channels $c_{3,1}$ |
| 4 | $3\times3$ max-pool (stride 1) → $1\times1$ conv → channels $c_4$ |

Total output channels = $c_1 + c_{2,1} + c_{3,1} + c_4$.

All branches use padding to keep spatial dimensions identical so concatenation is well-defined.

## Why it works

- **Multi-scale feature extraction.** "Details at different extents can be recognized efficiently by filters of different sizes." Rather than committing to one kernel size (like [[VGG]]'s universal $3\times3$), Inception lets gradient descent allocate capacity across branches.
- **Channel-reduction bottlenecks.** Branches 2 and 3 use $1\times1$ convolutions to *reduce* the channel count before applying the expensive $3\times3$ / $5\times5$ kernels. This is the same trick [[ResNet]] later adopts for its bottleneck blocks. Result: GoogLeNet is **cheaper** than [[AlexNet]] / [[VGG]] while being more accurate.
- **Pool branch.** Branch 4 is a max-pool followed by a $1\times1$ conv — gives the block translation-invariant features and channel reshape in one cheap path.

## Hyperparameters

Per-block: the four channel counts $(c_1, (c_{2,0},c_{2,1}), (c_{3,0},c_{3,1}), c_4)$ — i.e., **how to allocate capacity among convolutions of different size**. In GoogLeNet, the third branch ($3\times3$) gets the largest allocation, then the first ($1\times1$), then the fifth ($5\times5$), then the pool branch. The hand-picking of these numbers was a major motivator for later [[NeuralArchitectureSearch|NAS]] and [[RegNet|design-space]] approaches.

## Successor variants

- **Inception-v2/v3** (Szegedy et al. 2016): factorizes $n\times n$ into $1\times n$ + $n\times1$ convs (e.g. $5\times5$ → two $3\times3$ — borrowed from VGG); adds [[BatchNormalization]] and label smoothing.
- **Inception-v4 / Inception-ResNet** (Szegedy et al. 2017): adds residual connections.
- **ResNeXt** (Xie et al. 2017): the multi-branch idea generalized to *grouped convolutions* with all branches identical — see [[ResNeXt]].
- The **residual block** is "a special case of the multi-branch Inception block: it has two branches, one of which is the identity mapping" ([[d2l-convolutional-modern]] §resnet).

## Connections

- [[d2l-convolutional-modern]] — canonical reference.
- [[GoogLeNet]] — the architecture built from Inception blocks.
- [[ChristianSzegedy]] — first author.
- [[OneByOneConvolution]] — the channel-reduction primitive central to Inception.
- [[ResNet]] / [[ResNeXt]] / [[Bottleneck]] — successors that inherit the multi-branch + bottleneck idea.
- [[NetworkInNetwork]] — direct predecessor for $1\times1$ convs.
- [[CNN]] — parent family.
