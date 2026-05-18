---
title: "Convolution"
type: concept
tags: [deep-learning, math, cnn, signal-processing]
sources: [d2l-convolutional-neural-networks, madewithml-foundations-cnn]
last_updated: 2026-05-16
---

# Convolution

A **convolution** is the operation $(f*g)(\mathbf x)=\int f(\mathbf z)\,g(\mathbf x-\mathbf z)\,d\mathbf z$ in continuous form, or its discrete analog $\sum_a f(a)\,g(i-a)$. It measures the overlap between two functions when one is *flipped* and shifted. In deep learning, the operator deep-learning frameworks call "convolution" is actually [[CrossCorrelation|cross-correlation]] — the same arithmetic *without* the flip — but, because kernels are learned from data, the distinction is invisible to the trained network ([[d2l-convolutional-neural-networks]] §conv-layer).

## The two definitions

**True (mathematical) convolution, 2D discrete:**

$$(f*g)(i,j)=\sum_{a,b} f(a,b)\,g(i-a,\,j-b).$$

**Deep-learning "convolution" (actually cross-correlation):**

$$[\mathbf{H}]_{i,j}=u+\sum_{a,b}[\mathbf V]_{a,b}\,[\mathbf X]_{i+a,\,j+b}.$$

The only difference is $g(i-a,j-b)$ vs $g(i+a,j+b)$ — a horizontal+vertical kernel flip. Since CNN kernels are learned, the network simply learns the flipped version. D2L: "kernels are learned from data in deep learning, the outputs of convolutional layers remain unaffected no matter such layers perform either the strict convolution operations or the cross-correlation operations." See [[CrossCorrelation]] for the operator actually implemented.

## Why convolutions are everywhere in CNNs

Convolution is the *unique* linear operator on a 2D grid that is **translation-equivariant** ([[TranslationInvariance]]) and **local** ([[Locality]]) — exactly the two inductive biases [[d2l-convolutional-neural-networks]] argues images deserve. Replace a fully-connected layer with translation invariance + locality, and the math forces you to a convolution.

## Properties

- **Symmetric:** $f*g = g*f$ ([[d2l-convolutional-neural-networks]] §why-conv exercise).
- **Linear** in both operands.
- **Translation-equivariant:** shifting the input by $\delta$ shifts the output by $\delta$.
- **Parameter-sharing:** a single kernel reuses the same weights across all spatial locations — the source of CNNs' parameter efficiency.

## Connection to signal processing

Classical filters (edge detection, Gaussian blur, Sobel, finite-difference first/second derivatives) are convolutions with hand-designed kernels. The kernel `[[1, -1]]` is a horizontal finite-difference operator — an edge detector — and [[d2l-convolutional-neural-networks]] §conv-layer demonstrates that gradient descent can *learn* exactly this kernel from input/output pairs.

## In code

Frameworks expose convolution as `nn.Conv2d` ([[PyTorch]]), `nn.Conv2D` ([[MXNet]] / [[TensorFlow]]), `nn.Conv` ([[JAX]]/Flax). All compute cross-correlation under the hood.

## Connections

- [[CrossCorrelation]] — what frameworks actually compute.
- [[ConvolutionalLayer]] — the trainable layer wrapping the convolution operator + bias.
- [[CNN]] — the architecture that stacks convolutions.
- [[Filter]] / [[ConvolutionKernel]] — the kernel that gets convolved with the input.
- [[TranslationInvariance]] / [[Locality]] — the priors convolution encodes.
- [[d2l-convolutional-neural-networks]] — canonical derivation.
- [[Padding]] / [[Stride]] — operational knobs around the convolution.
- [[Channels]] / [[OneByOneConvolution]] — multi-channel variants.
- [[ReceptiveField]] — stacked-convolution consequence.
