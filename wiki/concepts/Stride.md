---
title: "Stride"
type: concept
tags: [deep-learning, cnn]
sources: [d2l-convolutional-neural-networks]
last_updated: 2026-05-16
---

# Stride

The **stride** of a [[Convolution|convolution]] or [[Pooling|pooling]] operator is how many input elements the window advances between successive output positions. With stride $s_h\times s_w$ and padding $p_h\times p_w$ on an $n_h\times n_w$ input with $k_h\times k_w$ kernel, the output shape is

$$\left\lfloor\frac{n_h - k_h + p_h + s_h}{s_h}\right\rfloor \times \left\lfloor\frac{n_w - k_w + p_w + s_w}{s_w}\right\rfloor.$$

When $p=k-1$ and the input dims are divisible by the strides, this simplifies to $(n_h/s_h)\times(n_w/s_w)$ — i.e., stride-$s$ exactly downsamples by factor $s$.

## Why use stride > 1

- **Downsampling.** Cheaper than [[Pooling|pooling]] for the same downsampling factor; the conv layer itself reduces resolution.
- **Larger effective receptive field.** Each output pixel covers more of the input with fewer layers.
- **Computational saving.** Output is $1/s^2$ the size; the next layer is correspondingly cheaper.

## Defaults

- **[[ConvolutionalLayer|Convolutional layers]]:** stride defaults to 1.
- **[[Pooling|Pooling layers]]:** framework default is *stride = window size* (non-overlapping windows). Override explicitly if you want overlapping pooling.

## Concrete: stride-2 conv

Setting `stride=2, padding=1, kernel_size=3` is the classic "halve resolution" convolution used in ResNet's "bottleneck" downsampling and many other architectures.

## Connections

- [[Padding]] — sibling output-shape knob.
- [[Convolution]] / [[ConvolutionalLayer]] / [[Pooling]] — operators that take stride.
- [[CNN]] / [[LeNet]] — LeNet uses stride-2 average pooling (the original downsampler).
- [[d2l-convolutional-neural-networks]] — output-shape formula derivation.
