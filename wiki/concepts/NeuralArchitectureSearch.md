---
title: "Neural architecture search (NAS)"
type: concept
tags: [deep-learning, automl, architecture, model-compression, mlsysbook]
sources: [d2l-convolutional-modern, mlsysbook-ch10-model-compression]
last_updated: 2026-06-05
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

## As structural compression ([[mlsysbook-ch10-model-compression|mlsysbook Ch 10]])

Ch 10 treats NAS as the structural-optimization technique that discovers architectures *efficient by construction* (vs pruning/distillation that compress a finished model), formalized as **bi-level optimization**: the outer loop searches architecture space $\mathcal{A}$, the inner loop trains each candidate. The inner loop is the cost: early RL-NAS (Zoph & Le 2017) ran **22,400 GPU-days (537,600 GPU-hours = 800 GPUs × 28 days, ~$50K–$100K)**; weight-sharing cut this ~1000×.

Search-strategy cost ladder: **RL** 400–1,000 GPU-days → **evolutionary** 200–500 → **[[DARTS|gradient-based DARTS]]** 1–4. **Hardware-aware NAS** (MnasNet) feeds measured device latency into the reward (accuracy × (target_latency/latency)^β), finding nets 1.8× faster than MobileNetV2. Recommended practice: *start with existing NAS-discovered architectures* ([[EfficientNet]], [[MobileNetV3]], MnasNet) rather than running NAS from scratch — reserve custom NAS for novel hardware or deployment scales that amortize the search. [[CompoundScaling]] (EfficientNet) is one of NAS's cleanest discoveries. [[mlsysbook-ch10-model-compression]]

## Connections

- [[d2l-convolutional-modern]] — canonical reference for NAS-vs-design-spaces framing.
- [[mlsysbook-ch10-model-compression]] — NAS as structural compression; cost ladder; hardware-aware NAS.
- [[EfficientNet]] / [[MobileNetV3]] / [[CompoundScaling]] / [[DARTS]] — NAS outputs and strategies covered there.
- [[RegNet]] — the design-space alternative.
- [[CNN]] — most NAS work targets CNN architectures.
- [[HyperparameterTuning]] — broader related field.
- [[ImageNet]] — the canonical NAS benchmark.
