---
title: "Channels (CNN)"
type: concept
tags: [deep-learning, cnn]
sources: [d2l-convolutional-neural-networks]
last_updated: 2026-05-16
---

# Channels

A **channel** is the third axis of an image tensor — the one orthogonal to height and width. RGB images have $c=3$ channels (red, green, blue); grayscale has $c=1$; hyperspectral satellite imagery has tens to hundreds. In a [[CNN]], hidden-layer feature maps also have a channel axis — typically much wider than the input's (6, 16, 64, 128, 256, …), with each channel encoding a different learned feature.

## Multi-channel convolution arithmetic

Notation: $c_i$ = input channels, $c_o$ = output channels, $k_h\times k_w$ = kernel spatial size.

- A [[ConvolutionalLayer|convolutional layer]] with $c_i$ input and $c_o$ output channels has a kernel tensor of shape **$c_o\times c_i\times k_h\times k_w$**.
- For *each* output channel $d\in\{1,\dots,c_o\}$, the layer cross-correlates the input with a $c_i\times k_h\times k_w$ slice and *sums* the $c_i$ resulting 2D maps into one 2D output channel.
- The $c_o$ output channels are stacked into a 3D output of shape $c_o\times h'\times w'$.

[[d2l-convolutional-neural-networks]] §channels:

$$[\mathsf H]_{i,j,d} = \sum_{a,b}\sum_{c=1}^{c_i}[\mathsf V]_{a,b,c,d}\,[\mathsf X]_{i+a,\,j+b,\,c}.$$

## Why deeper layers have more channels

D2L's design principle: "In the most popular neural network architectures, we actually increase the channel dimension as we go deeper in the neural network, typically downsampling to trade off spatial resolution for greater channel depth." LeNet: $1\to6\to16$. VGG/ResNet: $3\to64\to128\to256\to512$.

Intuition: channels carry features. Lower layers need few channels because they detect simple low-level features (edges, blobs). Higher layers need many channels to represent compositions of features (object parts, textures, semantic concepts).

## Channels are jointly optimized, not factorized

A naive interpretation is "channel $k$ detects feature $k$." D2L is careful: "channels are optimized to be jointly useful. This means that rather than mapping a single channel to an edge detector, it may simply mean that some direction in channel space corresponds to detecting edges." Cross-channel patterns matter; per-channel interpretability is approximate.

## Pooling vs. convolution on channels

| Operator | Behavior across channels |
|---|---|
| [[Convolution|Conv]] | sums over input channels (per output channel) |
| [[Pooling|Pool]] | acts per channel — channel count preserved |
| [[OneByOneConvolution|$1\times1$ conv]] | pure channel mixing, no spatial mixing |

## Cost

Total cost of a conv layer: $\mathcal O(h\cdot w\cdot k^2\cdot c_i\cdot c_o)$. Doubling both $c_i$ and $c_o$ quadruples the cost — hence depth-wise / grouped / [[ResNeXt|ResNeXt-style]] convolutions that constrain the cross-channel pattern.

## Connections

- [[Convolution]] / [[ConvolutionalLayer]] — operates over channels.
- [[OneByOneConvolution]] — pure-channel-mixing special case.
- [[FeatureMap]] — each channel is a feature map.
- [[CNN]] — the architecture whose channel-progression principle this article documents.
- [[Pooling]] — preserves channels.
- [[d2l-convolutional-neural-networks]] — canonical derivation.
- [[ResNeXt]] / [[DepthwiseConvolution]] — exploit channel structure for efficiency.
