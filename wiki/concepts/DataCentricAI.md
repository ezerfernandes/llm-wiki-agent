---
title: "Data-Centric AI"
type: concept
tags: [benchmarking, data-quality, datasets, mlsysbook]
sources: [mlsysbook-ch12-benchmarking]
last_updated: 2026-06-05
---

# Data-Centric AI

The development paradigm that **fixes the model and systematically improves the data**, contrasted with model-centric AI (fix the data, iterate on architecture). Per [[mlsysbook-ch12-benchmarking|mlsysbook Ch 12]], contemporary practice increasingly shows that *methodical dataset enhancement often yields greater performance gains than architectural refinement alone* — challenging the "more data is always better" assumption: **better datasets, not just larger ones**, produce more reliable, generalizable systems.

Evidence and benchmarks: **DataComp** inverts the standard benchmark by fixing model and training code and letting participants compete on dataset curation — a carefully filtered **30% subset matched models trained on 10× larger unfiltered data**, quantifying that engineering the data pipeline can beat scaling compute per dollar. DataPerf serves a similar role. Data benchmarking validates three things this paradigm depends on: **coverage** (class balance, subgroup/demographic representation, feature coverage), **quality** (3–6% label-error rates even in ImageNet; inter-annotator agreement; systematic vs. random errors), and **distribution alignment** (WILDS shows 90%+ in-distribution accuracy can drop to 60% under realistic shift).

## Connections

- [[DistributionShift]] — the failure mode data-centric validation targets.
- [[BenchmarkComponents]] — standardized datasets as the constraining benchmark ingredient.
- [[mlsysbook-ch09-data-selection]] — the data-selection optimizations (active learning, curation, augmentation) this paradigm operationalizes.
- [[Benchmarking]] — data benchmarking as the third evaluation dimension.
- [[mlsysbook-ch12-benchmarking]] — source.
