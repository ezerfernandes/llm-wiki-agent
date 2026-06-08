---
title: "Compositionality"
type: concept
tags: [deep-learning, neural-networks, representation-learning, foundational]
sources: [mlsysbook-ch05-neural-computation]
last_updated: 2026-06-05
---

# Compositionality

The principle that explains *why depth matters* in [[DeepLearning|deep learning]]: complex patterns decompose into simpler patterns that themselves decompose further. In vision, pixels → edges → textures → parts → objects. This hierarchical decomposition reflects the structure of the world and is what earns "deep" learning its name.

Per [[mlsysbook-ch05-neural-computation|mlsysbook Vol 1 Ch 5]], compositionality gives deep networks two advantages over shallow ones:

- **Exponential representational capacity, linear parameter growth.** Each layer builds on the previous, so a k-layer network composes k stages of learned abstraction; for certain function classes, a deep net represents functions that would require *exponentially* more neurons in a single hidden layer (the exponential-advantage result, Telgarsky 2016). This is the constructive answer to the [[UniversalApproximationTheorem|universal approximation theorem]]'s non-constructive guarantee.
- **Parameter reuse.** The edge detectors learned for a "7" also detect edges in every other digit, so a deep 100K-parameter net can represent patterns that would need millions of parameters in a shallow pixel-to-label mapping.

## Depth vs width trade-off

Depth and width are *not* symmetric. Adding depth increases representational power but adds sequential dependencies (layer ℓ+1 waits for ℓ, limiting parallelism), lengthens the gradient path (risking [[VanishingGradient|vanishing]]/[[ExplodingGradient|exploding]] gradients), and forces storage of more intermediate activations for [[Backpropagation|backprop]]. Widening allows all neurons in a layer to compute simultaneously. Ten layers of 100 neurons vs two layers of 500 share 1,000 hidden neurons but have very different compute characteristics.

## Connections

- [[DeepLearning]] — the paradigm compositionality justifies.
- [[UniversalApproximationTheorem]] — depth trades exponential width for polynomial depth.
- [[CompositionalCapacity]] — related capacity framing.
- [[NeuralNetwork]] / [[CNN]] — architectures encoding hierarchical structure.
- [[VanishingGradient]] / [[ExplodingGradient]] — the engineering cost of depth.
- [[mlsysbook-ch05-neural-computation]] — source.
