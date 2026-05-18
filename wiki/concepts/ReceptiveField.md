---
title: "Receptive Field"
type: concept
tags: [deep-learning, cnn, neuroscience]
sources: [d2l-convolutional-neural-networks]
last_updated: 2026-05-16
---

# Receptive Field

In a [[CNN]], the **receptive field** of an element $x$ in some layer is the set of all input elements (from any preceding layer, ultimately the network input) whose values may affect $x$ during the forward pass. The term is borrowed from neurophysiology — Hubel & Wiesel's 1959–1968 experiments on the visual cortex of cats and primates showed that individual neurons respond to specific spatial patterns in a localized region of the visual field.

## How it grows

For a $k\times k$ convolution with stride 1, each output element sees a $k\times k$ patch of its immediate input. Stacking convolutions composes the receptive field:

- 1 layer of $3\times3$ conv → $3\times3$ receptive field.
- 2 layers of $3\times3$ conv → $5\times5$.
- 3 layers of $3\times3$ conv → $7\times7$.

In general, $n$ stacked $k\times k$ convs give a $(n(k-1)+1)\times(n(k-1)+1)$ receptive field. [[Stride|Strided]] convolutions and [[Pooling|pooling]] *multiplicatively* enlarge the receptive field — a stride-2 layer doubles the effective receptive-field expansion of every subsequent layer.

[[d2l-convolutional-neural-networks]] §conv-layer worked example: a $2\times2$ kernel followed by another $2\times2$ kernel gives the second output element a $3\times3$ receptive field on the original input.

## Why it matters

- **Global vs local features.** Early layers (small receptive field) detect edges and textures; later layers (large receptive field) detect objects and scenes. "Higher level vision in nature" works the same way.
- **Architecture design.** To answer global questions ("is there a cat in this image?"), the final layers must have a receptive field large enough to cover the whole input. Either go deeper, use larger kernels, use strided/pooled downsampling, or add global pooling at the end.
- **Effective vs theoretical RF.** The *theoretical* receptive field is the bound above; the *effective* receptive field (which inputs actually influence the output meaningfully) is typically smaller and Gaussian-shaped around the center (Luo et al. 2016).

## Connection to biology

Hubel & Wiesel observed that visual-cortex neurons have receptive fields with edge / orientation / motion selectivity — and that deeper visual-pathway neurons aggregate from earlier ones into larger, more complex receptive fields. Field (1987) showed that natural-image statistics align with convolutional-kernel-like sensors. Kuzovkin et al. (2018) extended this to deep CNN features. CNNs are not coincidentally biologically plausible — they were *modeled* on this hierarchical-receptive-field structure (Neocognitron, Fukushima 1982).

## Connections

- [[Convolution]] / [[ConvolutionalLayer]] / [[CNN]] — the operators whose stacking grows receptive fields.
- [[Pooling]] / [[Stride]] — accelerate receptive-field growth.
- [[FeatureMap]] — receptive fields *are* the inputs to a feature map's elements.
- [[d2l-convolutional-neural-networks]] — definition, worked example, biological context.
- [[Attention]] — the modern alternative for "global receptive field in one step" (every token attends to every other).
