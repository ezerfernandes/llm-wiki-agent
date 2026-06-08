---
title: "Histogram of Oriented Gradients (HOG)"
type: concept
tags: [computer-vision, feature-engineering, classical-ml, history]
sources: [mlsysbook-ch05-neural-computation]
last_updated: 2026-06-05
---

# Histogram of Oriented Gradients (HOG)

An influential hand-crafted image feature descriptor (Dalal & Triggs 2005), the canonical example of classical-ML [[FeatureEngineering|feature engineering]] before deep learning. HOG identifies edges where brightness changes sharply, divides the image into fixed cells (e.g. 8×8 pixels), computes gradient magnitude and orientation per pixel, and bins them into orientation histograms per cell — turning raw pixels into shape descriptors robust to lighting variation and small positional shifts. Paired with a linear [[SupportVectorMachine|SVM]], it powered pedestrian/object detection in the 2000s.

## Systems contrast (mlsysbook Ch 5)

[[mlsysbook-ch05-neural-computation|mlsysbook Vol 1 Ch 5]] uses HOG as the *middle rung* in its MNIST paradigm ladder: classifying one 28×28 digit with HOG + SVM ≈ **8,000 operations / ~2 KB** — about 80× the rule-based cost (~100 comparisons) but still structured, predictable, and CPU-SIMD-friendly, vs **109,184 MACs** for a neural net (~1,092× rule-based). HOG's *fixed* computation graph runs efficiently on CPUs with predictable latency but requires expert tuning per domain; learned features need GPU parallelism but generalize without redesign. Deep learning's first convolutional layers learn filters resembling Gabor/HOG-like edge detectors — discovered automatically rather than hand-designed.

## Connections

- [[FeatureEngineering]] — HOG is the archetype of the hand-crafted-feature era.
- [[Histogram]] — the per-cell orientation binning.
- [[DeepLearning]] / [[Compositionality]] — the paradigm that replaced HOG with learned features.
- [[MNIST]] / [[mlsysbook-ch05-neural-computation]] — the running paradigm-cost comparison.
