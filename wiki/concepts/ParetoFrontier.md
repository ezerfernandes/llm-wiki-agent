---
title: "Pareto Frontier"
type: concept
tags: [benchmarking, compression, trade-off, optimization, mlsysbook]
sources: [mlsysbook-ch12-benchmarking, mlsysbook-ch15-responsible-engineering, mlsysbook-ch16-conclusion]
last_updated: 2026-06-05
---

# Pareto Frontier

The set of solutions where improving one objective requires degrading another (named for economist Vilfredo Pareto). In [[mlsysbook-ch12-benchmarking|mlsysbook Ch 12]] it is the primary tool for **compression validation**: plotting accuracy against the target efficiency metric (latency, model size, energy) reveals the trade-off frontier. Models *on* the frontier cannot improve one metric without degrading the other; models *below* it are strictly **dominated** — they lose on both axes and represent wasted capacity.

The frontier's *shape* carries diagnostic information: a steep region means efficiency gains come cheaply (prune here), a flat region means further compression costs disproportionate accuracy (stop here). Different compression techniques fail differently along the frontier — [[Quantization|quantization]] degrades near decision boundaries (edge cases), [[Pruning|pruning]] loses capacity for rare features, distillation loses calibration. The **Lottery Ticket Hypothesis** supplies concrete frontier data: sparse "winning ticket" subnetworks can match full-network accuracy, but the acceptable sparsity point is empirical, not universal. Acceptable degradation is deployment-dependent (2% drop fine for recommendations, unacceptable for medical diagnosis) — define thresholds before compressing, then validate against them.

## Connections

- [[ModelCompression]] — the discipline this frontier validates.
- [[Quantization]] / [[Pruning]] / [[knowledgedistillation]] — the techniques whose trade-offs the frontier maps.
- [[ExpectedCalibrationError]] — a hidden frontier axis compression silently moves.
- [[mlsysbook-ch12-benchmarking]] — source.
- [[mlsysbook-ch15-responsible-engineering]] — mlsysbook Vol 1 Ch 15 reuses the same Pareto machinery for the **fairness-accuracy** trade-off (exponential, not linear): a "sweet spot" of ~3.6× fairer at ~1% accuracy cost shows the "price of fairness" is a system constraint, not a bug ([[Fairness]]).
- [[mlsysbook-ch16-conclusion]] — the conclusion makes the Pareto frontier invariant #5 of the [[ThirteenQuantitativeInvariants|thirteen]] ("no universal optimum; every gain trades against another"), and uses it to debunk the "single accuracy metric captures quality" fallacy — for [[AGI]] the frontier expands from ~3 metrics to dozens (safety, fairness, factuality), which is part of why [[CompoundAISystems|compound systems]] are needed.
