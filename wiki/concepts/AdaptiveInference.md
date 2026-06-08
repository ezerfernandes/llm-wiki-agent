---
title: "Adaptive Inference"
type: concept
tags: [model-compression, inference, dynamic-computation, mlsysbook]
sources: [mlsysbook-ch10-model-compression]
last_updated: 2026-06-05
---

# Adaptive Inference

**Varying the amount of computation a model performs on a per-input basis, spending compute proportional to input difficulty rather than applying a uniform budget to every input.** Per [[mlsysbook-ch10-model-compression|mlsysbook Ch 10]], an architectural-efficiency technique: a cat on a plain background needs less analysis than a cat hidden in clutter, and many real-world inputs classify correctly with a fraction of the full network.

## Mechanisms

- **[[EarlyExit|Early-exit architectures]]** (BranchyNet, multi-exit ViTs) — emit a prediction at an intermediate layer when confidence exceeds a threshold.
- **[[ConditionalComputation]]** (SkipNet gating, dynamic routing) — activate only some layers/paths.
- **Dynamic layer scaling / Fast Neural Networks** — continuously modulate depth based on uncertainty estimates.

## Costs

Variable inference time complicates real-time SLOs; gating overhead can offset savings; irregular execution paths hurt accelerator utilization; rare-but-important inputs may get under-served (bias risk); standard FLOPs/latency benchmarks don't capture adaptive scaling.

## Connections

- [[EarlyExit]] / [[ConditionalComputation]] — discrete adaptive mechanisms.
- [[MixtureOfExperts]] / [[SwitchTransformer]] — gate-based conditional computation at scale.
- [[ModelCompression]] — the architectural-efficiency dimension.
- [[mlsysbook-ch10-model-compression]] — source.
