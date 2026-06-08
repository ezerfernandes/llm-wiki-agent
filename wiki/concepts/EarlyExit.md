---
title: "Early Exit Architectures"
type: concept
tags: [model-compression, inference, dynamic-computation, mlsysbook]
sources: [mlsysbook-ch10-model-compression]
last_updated: 2026-06-05
---

# Early Exit Architectures

**Networks with multiple prediction points (lightweight classifiers attached at intermediate layers) that emit an output as soon as a confidence threshold is met, rather than completing the full forward pass for every input.** Per [[mlsysbook-ch10-model-compression|mlsysbook Ch 10]], a form of [[AdaptiveInference|adaptive inference]]: simple inputs exit early, complex inputs continue through deeper layers.

## Examples

- **BranchyNet** (Teerapittayanon 2016) — multiple exit points; terminates when intermediate-prediction confidence exceeds a threshold.
- **Multi-exit vision transformers** — lightweight classifiers at various transformer layers; some inputs exit after the first few layers.

On GPUs/TPUs, different exit paths can be evaluated concurrently to improve throughput while preserving the adaptive benefit. Inference-time reduction scales with input difficulty.

## Connections

- [[AdaptiveInference]] — the umbrella technique.
- [[ConditionalComputation]] — the complementary "which paths to activate" mechanism.
- [[ModelCompression]] — architectural-efficiency dimension.
- [[mlsysbook-ch10-model-compression]] — source.
