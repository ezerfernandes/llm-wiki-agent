---
title: "Filter (Convolutional)"
type: concept
tags: [deep-learning, cnn]
sources: [d2l-convolutional-neural-networks]
last_updated: 2026-05-16
---

# Filter

A **filter** (also called a **convolution kernel** or layer **weights**) is the small learnable tensor that a [[ConvolutionalLayer|convolutional layer]] slides across an input via [[CrossCorrelation|cross-correlation]]. In a multi-channel layer, the filter has shape $c_o\times c_i\times k_h\times k_w$ — one $c_i\times k_h\times k_w$ slice per output channel. Together with a scalar (or per-output-channel) bias, the filter is the *entire* parameter set of a convolutional layer.

## What filters learn

- **Low-level filters** (first layer): edge detectors (horizontal / vertical / diagonal), color blobs, simple textures. Famously rediscovers the [[ReceptiveField|receptive-field]] patterns Hubel & Wiesel observed in animal visual cortex.
- **Mid-level filters**: parts and textures (eyes, wheels, fur).
- **High-level filters**: object-shaped patterns, sometimes whole categories.

D2L §conv-layer demonstrates that a $1\times2$ filter `[1, -1]` is a *horizontal edge detector* (a finite-difference operator approximating $\partial_x$), and that gradient descent can **learn** exactly this filter from input/output pairs. This shifts the engineering job from "design clever filters" to "design a network architecture and a loss; let SGD find the filters."

## Initialization

Filters are typically initialized randomly with variance-scaled schemes — [[XavierInitialization|Xavier]] for sigmoid/tanh, [[HeInitialization|He]] for ReLU. See [[WeightInitialization]].

## Filter, kernel, weights — same thing

D2L: "$\mathbf V$ is referred to as a *convolution kernel*, a *filter*, or simply the layer's *weights* that are learnable parameters." Used interchangeably in the literature. The wiki collapses these onto this page; [[ConvolutionKernel]] redirects here.

## Connections

- [[Convolution]] / [[CrossCorrelation]] / [[ConvolutionalLayer]] — operator and layer the filter parameterizes.
- [[CNN]] — architecture that stacks filters.
- [[WeightInitialization]] / [[XavierInitialization]] / [[HeInitialization]] — how filters start.
- [[Backpropagation]] — how filters are learned.
- [[imlbook-cnn-features]] — interpretability of learned filters.
- [[d2l-convolutional-neural-networks]] — derivation + learning-a-kernel example.
- [[ReceptiveField]] — what a stacked-filter network "sees."
