---
title: "Cost Per Inference"
type: concept
tags: [serving, economics, infrastructure, mlsysbook]
sources: [mlsysbook-ch13-model-serving, mlsysbook-ch14-ml-operations]
last_updated: 2026-06-05
---

# Cost Per Inference

Serving's primary economic metric. Total serving cost decomposes into **compute time, accelerator memory, data transfer, and orchestration overhead** ([[mlsysbook-ch13-model-serving|mlsysbook Ch 13]]), and **scales with request volume** — unlike training cost, which scales with dataset size and model complexity.

The dominant component shifts with utilization: at high utilization, compute dominates (GPU stays busy); at low utilization, memory dominates (the GPU is reserved and billed while idle). So *throughput* improvements reduce compute cost per inference, while *utilization* improvements reduce idle-memory waste. ResNet-50 AWS 2026: c5.xlarge CPU ($0.17/h, 50 img/s) vs g4dn T4 GPU ($0.53/h, 400 img/s — **lowest cost per inference** despite higher hourly rate) vs p3 V100 ($3.06/h, 1,200 img/s — only worth its 5.8× price at very high sustained traffic). **Precision is a direct economic lever**: INT8 ≈ 3× FP32 throughput, so a 30-GPU FP32 fleet shrinks to 10 at INT8. For LLMs, $/million-tokens is set by prefill compute and decode bandwidth; **intelligence deflation** (~5.8× cheaper per 18 months) shrinks margins, making efficiency the survival lever ([[JevonsParadox|Jevons paradox]] then expands demand).

## Connections

- [[CapacityPlanning]] — aggregates cost-per-inference into a fleet specification.
- [[Quantization]] / [[InferenceRuntime]] — precision and runtime choices set the cost.
- [[JevonsParadox]] — why cheaper inference grows, not shrinks, total GPU demand.
- [[GPUUtilization]] — the utilization that determines idle-memory waste.
- [[LLMServing]] — the $/token and J/token economics for generative models.
- [[mlsysbook-ch13-model-serving]] — source.
- [[mlsysbook-ch14-ml-operations]] — mlsysbook Vol 1 Ch 14 tracks cost-per-1K-inferences over time as an efficiency-degradation signal (Hourly GPU cost × 1000 / inferences-per-hour).

