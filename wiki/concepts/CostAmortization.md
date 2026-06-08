---
title: "Cost Amortization"
type: concept
tags: [ml-systems, data-selection, economics, mlsysbook]
sources: [mlsysbook-ch09-data-selection]
last_updated: 2026-06-05
---

# Cost Amortization

The economic structure underpinning [[SelfSupervisedLearning|self-supervised learning]] and the [[FoundationModel|foundation-model]] paradigm: an **expensive pretraining cost is paid once and reused across many downstream tasks** ([[mlsysbook-ch09-data-selection|Reddi Ch 9]]). Pretraining can cost >10,000× a single fine-tune, but the marginal per-task cost collapses. Worked 10-task example: labeling drops **100×** (from ~$1M to ~$10K), per-task marginal compute drops **20×** (1,000 → 50 GPU-hours), and deployment accelerates 20–50× per task; total compute becomes favorable past a crossover (~11 tasks). This asymmetry — "pretrain once, fine-tune many" — explains why fine-tuning dominates production ML. Also applies to data-selection infrastructure ([[DataSelectionCostModel|amortized ROI]]): a deduplication pipeline that loses money at 1 run is highly profitable across 50.

## Connections

- [[SelfSupervisedLearning]] / [[FoundationModel]] — the paradigm amortization enables.
- [[Pretraining]] / [[FineTuning]] / [[TransferLearning]] — the mechanism.
- [[DataSelectionCostModel]] — extends amortization to selection infrastructure ROI.
- [[mlsysbook-ch09-data-selection]] — source.
