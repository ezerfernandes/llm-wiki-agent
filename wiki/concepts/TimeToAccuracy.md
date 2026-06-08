---
title: "Time-to-Accuracy"
type: concept
tags: [benchmarking, training, metrics, mlperf, mlsysbook]
sources: [mlsysbook-ch12-benchmarking]
last_updated: 2026-06-05
---

# Time-to-Accuracy

The **primary training-benchmark metric**: the wall-clock time to reach a fixed quality target on a fixed dataset and model, formally

$$T_{\text{train}} = \arg\min_{t}\{\text{Accuracy}(t)\geq\text{target accuracy}\}$$

Per [[mlsysbook-ch12-benchmarking|mlsysbook Ch 12]], it is the corrective to raw throughput: a system processing 10,000 img/s that never reaches the **MLPerf ResNet-50 target of 75.9% top-1 on ImageNet** is an *invalid* result, while a slower system that converges efficiently is preferable. Holding model and target fixed, time-to-convergence varies **10–100×** across hardware-software stacks because it depends on the full pipeline (data loading, $\eta_{\text{hw}}$, gradient sync, fault recovery) — none of which a peak-FLOP/s spec captures.

Time-to-accuracy is what makes precision strategies comparable: TF32/mixed-precision may raise throughput but add iterations; fixing the accuracy target makes time-to-accuracy the comparable quantity regardless of precision. DAWNBench pioneered this metric; MLPerf adopted it.

## Connections

- [[MLPerf]] — codifies per-task accuracy targets; time-to-accuracy is its core training metric.
- [[IronLawOfMLSystems]] — the full-pipeline terms time-to-accuracy aggregates.
- [[ScalingEfficiency]] — the distributed-training companion metric.
- [[MFU]] — the $\eta_{\text{hw}}$ utilization that drives convergence speed.
- [[mlsysbook-ch12-benchmarking]] — source.
