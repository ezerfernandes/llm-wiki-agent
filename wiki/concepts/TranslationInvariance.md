---
title: "Translation Invariance"
type: concept
tags: [deep-learning, cnn, inductive-bias, computer-vision]
sources: [d2l-convolutional-neural-networks]
last_updated: 2026-05-16
---

# Translation Invariance

The property that a function's response to an input pattern does not depend on *where* in the input that pattern occurs. In computer vision: if you see a pig at the bottom of an image, you should recognize a pig that's been shifted to the top of the image the same way.

Formally, $f$ is **translation invariant** if $f(T_\delta \mathbf x) = f(\mathbf x)$ for any shift $T_\delta$ (the function's output is unchanged by input shifts); $f$ is **translation equivariant** if $f(T_\delta \mathbf x) = T_\delta f(\mathbf x)$ (the output shifts by the same amount as the input). [[Convolution|Convolutional layers]] are translation *equivariant*; [[Pooling|max-pooling]] adds local translation *invariance*; the final FC + softmax of a CNN classifier is translation *invariant* over the receptive field of its inputs.

## Why it matters for CNNs

It's one of the two priors that [[d2l-convolutional-neural-networks]] §why-conv derives the [[ConvolutionalLayer|convolutional layer]] from:

> "In the earliest layers, our network should respond similarly to the same patch, regardless of where it appears in the image. This principle is called translation invariance (or translation equivariance)."

Imposed mathematically: in the fully-connected formulation $[\mathbf H]_{i,j}=u+\sum_{a,b}[\mathsf V]_{i,j,a,b}[\mathbf X]_{i+a,j+b}$, translation invariance forces $\mathsf V$ to not depend on $(i,j)$. The result $[\mathbf V]_{a,b}$ — a position-independent kernel — *is* a convolution.

## Trade-off: an inductive bias, not a free lunch

[[d2l-convolutional-neural-networks]]: "All learning depends on imposing inductive bias. When that bias agrees with reality, we get sample-efficient models that generalize well to unseen data. But of course, if those biases do not agree with reality, e.g., if images turned out not to be translation invariant, our models might struggle even to fit our training data."

Cases where translation invariance is *wrong*:

- **Spatial-context-dependent features.** "Sky pixels are at the top of images" — a violation of translation invariance that real CNNs implicitly learn around via [[Padding|zero-padding]] "where the whitespace is."
- **Document understanding.** Position of text on a page matters for layout-aware tasks.
- **Astrophysical / medical imaging.** Anatomical position is informative.

Architectures that need explicit position information add it back: [[VisionTransformer|ViT]] uses positional embeddings; CoordConv (Liu et al. 2018) concatenates explicit $(x,y)$ channels.

## Translation equivariance vs invariance

- **Conv layer:** equivariant — shifting input shifts the feature map by the same amount.
- **Max-pool over a $k\times k$ window:** locally invariant to shifts $<k$ within the window.
- **Global average pool / global max pool:** strictly invariant over the entire input.
- **Final softmax classifier:** strictly invariant (classification doesn't change with translation).

## Connections

- [[Locality]] — the *other* CNN-motivating prior.
- [[Convolution]] / [[ConvolutionalLayer]] — what translation equivariance forces you to.
- [[Pooling]] / [[MaxPooling]] — what adds local translation *invariance* on top of equivariance.
- [[InductiveBias]] — the conceptual frame.
- [[CNN]] / [[d2l-convolutional-neural-networks]] — derivation source.
- [[VisionTransformer]] — alternative that doesn't bake in translation equivariance.
