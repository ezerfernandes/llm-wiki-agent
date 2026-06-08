---
title: "Data Wall"
type: concept
tags: [ml-systems, data-selection, scaling, mlsysbook]
sources: [mlsysbook-ch09-data-selection]
last_updated: 2026-06-05
---

# Data Wall

The structural asymmetry in which **compute supply outgrows the supply of high-quality human-generated data**, making data — not GPUs — the binding constraint on frontier ML. In [[mlsysbook-ch09-data-selection|Reddi Ch 9]], GPU compute grows ~10× every 3 years while high-quality training web text grows only ~2× every 5 years (labeled data ~1.5× / 5 yr); synthetic data is nominally unbounded but bounded by generator quality and [[ModelCollapse|model collapse]]. [[EpochAI|Epoch AI]] projected exhaustion of high-quality public text on a near-term (years) horizon.

Consequence: the field is **compute-rich and data-poor**, inverting the optimization priority from "get more data" to "get more from existing data" — the rationale for [[DataSelection|data selection]]. Mathematically tied to the [[InformationComputeRatio|ICR]] decay ($I(D)\sim\log D$ while cost is linear) and the [[ChinchillaScalingLaw|Chinchilla]] result that compute-optimal token demand grows as $\sqrt C$, still outpacing supply.

## Connections

- [[DataSelection]] — the discipline the data wall motivates.
- [[InformationComputeRatio]] — the metric whose decay defines the "data tax" region beyond the wall.
- [[ChinchillaScalingLaw]] / [[ScalingLaws]] — quantify the data-compute balance.
- [[EpochAI]] — data-exhaustion projections.
- [[SyntheticDataGeneration]] / [[SelfSupervisedLearning]] — partial escape routes (with caveats).
- [[mlsysbook-ch09-data-selection]] — source.
