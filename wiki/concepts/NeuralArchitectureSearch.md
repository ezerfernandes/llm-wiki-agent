---
title: "Neural architecture search (NAS)"
type: concept
tags: [deep-learning, automl, architecture]
sources: [d2l-convolutional-modern]
last_updated: 2026-05-16
---

# Neural architecture search

A family of **automatic architecture-design methods** that search a predefined space of network configurations for one that maximizes a target metric (typically validation accuracy at a fixed compute / latency budget). NAS was the dominant alternative to manual architecture design in the late 2010s; [[d2l-convolutional-modern]] §cnn-design positions it explicitly as the foil for the *design-space* approach that produced [[RegNet]].

## How it works (generically)

1. **Search space.** Define the menu of architectural choices (e.g. AnyNet's 17 hyperparameters; cell-search spaces; macro-search over depth/width).
2. **Search strategy.** Sample candidates via reinforcement learning (Zoph & Le 2016), evolution (AmoebaNet — Real et al. 2018), gradient-based methods (DARTS — Liu et al. 2018), or random search.
3. **Performance estimation.** Train each candidate (perhaps with proxy tasks, fewer epochs, smaller datasets) and score it.
4. **Output.** A *single network instance* maximizing the metric.

## Notable outputs

- **EfficientNet** (Tan & Le 2019) — found via NAS; the compound-scaling rule (depth × width × resolution coupled by a single coefficient) is one of NAS's cleanest contributions.
- **MobileNet v3** (Howard et al. 2019) — NAS-tuned mobile-efficient CNN.
- **NASNet, AmoebaNet, DARTS** — historically important but expensive.

## Costs and limitations

> "Up to now we have omitted networks obtained via *neural architecture search* (NAS). We chose to do so since their cost is usually enormous, relying on brute-force search, genetic algorithms, reinforcement learning, or some other form of hyperparameter optimization." — [[d2l-convolutional-modern]] §cnn-design

- **Compute.** Original NAS papers consumed thousands of GPU-days. Even DARTS / proxy-task methods are expensive.
- **Single-instance output.** You get *one* network. If your compute budget or input resolution changes, you re-run NAS.
- **No transferable insight.** NAS outputs an architecture but not *why* it's good. Re-running on a related task starts from scratch.

## The design-space alternative

[[RegNet]] (Radosavovic et al. 2020) is positioned by [[d2l-convolutional-modern]] as the third path — optimize over *distributions* of networks, not a single network — that:

- Is computationally cheaper than NAS.
- Yields scientific insights ("tie bottleneck ratios; tie group widths; increase channels and depths across stages").
- Outputs a *family* of networks transferable across compute budgets.

## Connections

- [[d2l-convolutional-modern]] — canonical reference for NAS-vs-design-spaces framing.
- [[RegNet]] — the design-space alternative.
- [[CNN]] — most NAS work targets CNN architectures.
- [[HyperparameterTuning]] — broader related field.
- [[ImageNet]] — the canonical NAS benchmark.
