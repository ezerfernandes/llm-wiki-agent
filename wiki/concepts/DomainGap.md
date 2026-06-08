---
title: "Domain Gap"
type: concept
tags: [ml-systems, synthetic-data, data-selection, mlsysbook]
sources: [mlsysbook-ch09-data-selection]
last_updated: 2026-06-05
---

# Domain Gap

The statistical divergence between **synthetic (generated) data and real-world data** distributions, the chief limitation of [[SyntheticDataGeneration|synthetic data generation]] ([[mlsysbook-ch09-data-selection|Reddi Ch 9]]). A model trained only on synthetic data learns a decision boundary optimized for the wrong distribution — performing well on synthetic test data while failing silently on real deployment data, a form of [[TrainingServingSkew|training-serving skew]] that is hard to detect. Measurable via Maximum Mean Discrepancy (MMD) or Fréchet Inception Distance (FID); visual domain-adaptation studies show 20–40% accuracy loss across domains (e.g. webcam → DSLR). Bridged by [[DomainRandomization|domain randomization]] and [[DomainAdaptation|domain adaptation]]; best results come from mixing **50–80% synthetic + 20–50% real**.

## Connections

- [[SyntheticDataGeneration]] / [[SyntheticData]] — the source of the gap.
- [[DomainRandomization]] / [[DomainAdaptation]] — the two bridging strategies.
- [[TrainingServingSkew]] — the production failure mode it creates.
- [[mlsysbook-ch09-data-selection]] — source.
