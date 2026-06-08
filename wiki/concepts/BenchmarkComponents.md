---
title: "Benchmark Components"
type: concept
tags: [benchmarking, ml-systems, methodology, reproducibility, mlsysbook]
sources: [mlsysbook-ch12-benchmarking]
last_updated: 2026-06-05
---

# Benchmark Components

The seven ingredients every ML benchmark — at any [[BenchmarkGranularity|granularity]] — must specify so its result is interpretable ([[mlsysbook-ch12-benchmarking|mlsysbook Ch 12]]). The critical property is **serial dependency**: each component constrains the next, so a decision at any point propagates forward and narrows every subsequent choice (illustrated by the chapter's nine-stage audio anomaly-detection workflow).

1. **Problem definition** — input spec, output spec, and quantitative performance spec.
2. **Standardized datasets** — ImageNet/COCO/CIFAR-10 (vision), SQuAD/[[GLUE]]/WikiText (NLP), ToyADMOS (anomaly). Without them every team evaluates on private data and cross-lab comparison is impossible. Beware domain gaps (ToyADMOS 95%+ AUC → 70–80% on factory floors).
3. **Model selection** — baselines from linear/logistic regression up to [[bert|BERT]] (chosen as MLPerf NLP reference because its constant-cost forward pass isolates hardware variability). Must control for framework (PyTorch vs. TensorFlow can differ 0.1–0.5%).
4. **Evaluation metrics** — accuracy (Top-1/5, mAP, BLEU, perplexity), throughput (samples/s, tokens/s, time-to-train), latency (p50/p99, first-token), efficiency (samples/s/W, accuracy/FLOP, TCO/inference). Report both atomic and compound metrics.
5. **Benchmark harness** — delivers inputs (Poisson arrivals for servers; sequential injection for mobile), collects measurements, ensures reproducibility without perturbing the system under test.
6. **System specifications** — full hardware + software stack (a model can train 10× faster on H100 than V100), framework versions, compiler flags, containers.
7. **Run rules** — fixed seeds, controlled data ordering, hyperparameter documentation, code provenance, containerized environments — taming stochasticity (weight init, shuffling, dropout).

## Connections

- [[Benchmarking]] / [[BenchmarkGranularity]] — the discipline and the orthogonal scope dimension.
- [[Reproducibility]] / [[ReproducibilityInML]] — run rules and harness exist to guarantee it.
- [[TailLatency]] — the percentile metrics the metric set must include.
- [[BenchmarkEngineering]] — gaming exploits underspecified components.
- [[mlsysbook-ch12-benchmarking]] — source.
