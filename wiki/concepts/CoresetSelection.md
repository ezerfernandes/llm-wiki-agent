---
title: "Coreset Selection"
type: concept
tags: [ml-systems, data-selection, coreset, mlsysbook]
sources: [mlsysbook-ch09-data-selection]
last_updated: 2026-06-05
---

# Coreset Selection

A [[StaticDataPruning|static-pruning]] technique that turns dataset reduction into a **coverage problem**: keep the smallest subset that preserves the statistical properties of the full dataset ([[mlsysbook-ch09-data-selection|Reddi Ch 9]]). The name comes from computational geometry, where a coreset approximates the geometry of the full point set within a $(1+\varepsilon)$ factor — a provable bound that distinguishes it from random downsampling.

The systems decision is **where to spend the selection budget** (cheap coverage metrics vs costlier training-dynamics scores):

| Method | Cost | Needs training | Best for | Limitation |
|---|---|---|---|---|
| k-Center | $\mathcal{O}(D^2)$/$\mathcal{O}(DK)$ | No | Coverage | Ignores labels |
| Herding | $\mathcal{O}(DK)$ | No | Distribution match | Gaussian-ish |
| [[GraNd]] | $\mathcal{O}(\text{epochs}\times D)$ | Few epochs | Decision boundaries | Needs proxy |
| [[ForgettingEvents]] | full training | Yes | Hard examples | Expensive |
| [[EL2N]] | $\mathcal{O}(\text{epochs}\times D)$ | Few epochs | Uncertainty | Best with proxy |

Gradient methods beat geometry methods but need a **proxy model** — scores transfer across architectures (ResNet-18 → ResNet-50), so a 5-epoch proxy can curate data for a 90-epoch run. On ImageNet a 50% EL2N coreset gives ~1.8× higher [[InformationComputeRatio|ICR]].

## Connections

- [[StaticDataPruning]] — parent stage; [[DataSelection]] — discipline.
- [[EL2N]] / [[GraNd]] / [[ForgettingEvents]] — gradient-based scoring methods.
- [[InformationComputeRatio]] — coresets raise ICR by targeting the decision boundary.
- [[DataDeduplication]] / [[DataPruning]] — complementary static-pruning techniques.
- [[mlsysbook-ch09-data-selection]] — source.
