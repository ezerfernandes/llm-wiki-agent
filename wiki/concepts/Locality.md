---
title: "Locality (CNN Prior)"
type: concept
tags: [deep-learning, cnn, inductive-bias]
sources: [d2l-convolutional-neural-networks]
last_updated: 2026-05-16
---

# Locality

The prior that, in image data, **nearby pixels are more informative about each other than distant pixels** — so the earliest layers of a vision model should look at small local neighborhoods, not the whole image at once. Together with [[TranslationInvariance|translation invariance]], it is one of the two priors [[d2l-convolutional-neural-networks]] §why-conv uses to derive the [[ConvolutionalLayer|convolutional layer]] from a fully-connected layer.

## Mathematical statement

Take the translation-invariant layer

$$[\mathbf H]_{i,j} = u + \sum_{a,b}[\mathbf V]_{a,b}[\mathbf X]_{i+a,j+b}.$$

The locality prior says $[\mathbf V]_{a,b} = 0$ for $|a|>\Delta$ or $|b|>\Delta$. The sum collapses to a small window of size $(2\Delta+1)^2$:

$$[\mathbf H]_{i,j} = u + \sum_{a=-\Delta}^{\Delta}\sum_{b=-\Delta}^{\Delta}[\mathbf V]_{a,b}[\mathbf X]_{i+a,j+b}.$$

Parameter count drops from $4\times10^6$ (translation-invariant only) to $4\Delta^2$ (typically $\le100$) — four more orders of magnitude than translation invariance alone.

## Where locality breaks

Locality at *early* layers is the prior; *deeper* layers see larger receptive fields via stacking. D2L: "deeper layers should be able to capture longer-range features of the image, in a way similar to higher level vision in nature."

So locality is not "the network never sees far apart pixels" — it's "the network sees far apart pixels only through composed local interactions." A 10-layer CNN with $3\times3$ kernels has a $21\times21$ effective [[ReceptiveField|receptive field]].

When locality is the wrong prior:

- **Global structure matters at the lowest layer.** E.g., comparing two distant patches for a stereo task — better served by [[Attention]] or large-kernel convolutions.
- **[[VisionTransformer|ViT]] / [[Transformer]].** Drops locality entirely — every token attends to every other from layer 1. Works when data is plentiful; CNNs win at low data because locality is a useful prior.

## The pair: locality + translation invariance

Together these two priors *uniquely* determine the convolutional layer as a linear operator on a 2D grid:

- Linearity + translation invariance → convolution (any kernel).
- + locality → finite-support kernel.
- Drop either and you get a different (worse, on images) architecture.

## Connections

- [[TranslationInvariance]] — the sibling prior.
- [[Convolution]] / [[ConvolutionalLayer]] — what the priors force you to.
- [[ReceptiveField]] — the depth-grown version of locality.
- [[InductiveBias]] — the conceptual frame.
- [[CNN]] / [[d2l-convolutional-neural-networks]] — source.
- [[Attention]] / [[VisionTransformer]] — non-local alternative.
