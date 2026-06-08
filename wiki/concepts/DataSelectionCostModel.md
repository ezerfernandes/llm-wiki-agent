---
title: "Data Selection Cost Model"
type: concept
tags: [ml-systems, data-selection, economics, roi, mlsysbook]
sources: [mlsysbook-ch09-data-selection]
last_updated: 2026-06-05
---

# Data Selection Cost Model

The quantitative framework for deciding *whether* to invest in [[DataSelection|data selection]] ([[mlsysbook-ch09-data-selection|Reddi Ch 9]]). Total data cost spans the full lifecycle:

$$C_{\text{total}} = C_{\text{acquire}} + C_{\text{label}} + C_{\text{store}} + C_{\text{process}}$$

Labeling cost spans **three orders of magnitude** ($0.10–$100/sample, crowd vs expert), making it the component most amenable to optimization; in ImageNet-scale supervised training data costs ~81% vs ~19% compute (the ratio inverts for SSL on web data). Three decision tools:

- **ROI** = (Savings − Investment) / Investment. Deduplication has the highest ROI (minimal cost, immediate gains); active learning has the highest potential savings but most infrastructure.
- **Break-even** — the point where labeling reduction equals selection overhead.
- **Amortized ROI** = $(N_{\text{runs}}\times\text{per-run savings} − \text{one-time investment})/\text{investment}$. A $55K dedup pipeline is a net loss at 1 run but highly profitable across 50 — high-reuse, broad-transfer techniques amortize best.

High-ROI when labeling is expensive, data is redundant, or runs repeat; low-ROI for cheap-label, small/curated, one-off runs.

## Connections

- [[DataSelection]] — the discipline being justified; [[InformationComputeRatio]] — the compute-side metric this generalizes.
- [[CostAmortization]] — the temporal dimension (reuse across runs/tasks).
- [[ActiveLearning]] / [[DataDeduplication]] / [[CoresetSelection]] — techniques with distinct cost-benefit profiles.
- [[SamplesPerDollar]] — the cost-efficiency sibling metric.
- [[mlsysbook-ch09-data-selection]] — source.
