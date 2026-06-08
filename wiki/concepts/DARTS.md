---
title: "DARTS (Differentiable Architecture Search)"
type: concept
tags: [model-compression, nas, automl, mlsysbook]
sources: [mlsysbook-ch10-model-compression]
last_updated: 2026-06-05
---

# DARTS (Differentiable Architecture Search)

**A gradient-based [[NeuralArchitectureSearch|NAS]] strategy (Liu et al. 2019) that relaxes the discrete architecture-search space into a continuous one where all candidate operations are weighted combinations, then optimizes architecture weights and model weights jointly by gradient descent.** Per [[mlsysbook-ch10-model-compression|mlsysbook Ch 10]], DARTS slashes search cost from hundreds of GPU-days (RL/evolutionary NAS) to just **1–4 GPU-days**.

## Trade-off

The continuous relaxation may converge to suboptimal local minima and miss discrete architectural patterns that explicit discrete search would find. Recommended when the compute budget is only a few GPU-days, but still best justified by deployment scale.

## Connections

- [[NeuralArchitectureSearch]] — DARTS is the cheapest of the three main search strategies (vs RL, evolutionary).
- [[ModelCompression]] — structural optimization.
- [[mlsysbook-ch10-model-compression]] — source.
