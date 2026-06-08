---
title: "EfficientNet"
type: concept
tags: [deep-learning, cnn, efficient-architecture, nas, mlsysbook]
sources: [mlsysbook-ch10-model-compression]
last_updated: 2026-06-05
---

# EfficientNet

**A NAS-discovered CNN family (Tan & Le 2019) whose key insight is [[CompoundScaling|compound scaling]] — scaling depth, width, and resolution with fixed coefficients.** Per [[mlsysbook-ch10-model-compression|mlsysbook Ch 10]], one of the recommended "start here" NAS-discovered architectures (vs running NAS from scratch).

## Pareto frontier

EfficientNet quantifies how steep the accuracy-efficiency trade-off becomes: **B0 (77.1% accuracy, 390M FLOPs) → B7 (84.4%, 37B FLOPs)** — a 95× compute increase for 7.3 percentage points. The family spans mobile to cloud deployment from a single scaling recipe.

## Connections

- [[CompoundScaling]] — its defining principle.
- [[NeuralArchitectureSearch]] — discovered it; [[MobileNetV3]] / MnasNet are sibling NAS architectures.
- [[ModelCompression]] — efficient-by-construction structural optimization.
- [[mlsysbook-ch10-model-compression]] — source.
