---
title: "Five-Pillar Framework"
type: concept
tags: [ml-systems, framework, mlsysbook, foundations]
sources: [mlsysbook-ch01-introduction]
last_updated: 2026-06-05
---

# Five-Pillar Framework

The organizing structure of Reddi's *Machine Learning Systems* ([[mlsysbook-ch01-introduction|Vol 1, Ch 1]]): **five interconnected engineering disciplines**, each owning a distinct challenge category, resting on a shared foundation of physical and economic constraints.

1. **Data Engineering** — owns failures where data quality or [[DistributionShift|distribution shift]] determines behavior; pipelines, versioning, quality monitoring, drift detection, privacy-preserving processing. ([[DataEngineering]])
2. **Training Systems** — owns the model-complexity/scale problems from the [[BitterLesson|bitter lesson]]; distributed training, parallelization, failure recovery, hyperparameter tuning at scale.
3. **Deployment Infrastructure** — owns the [[TrainingServingSkew|training-serving divide]] and inference performance across tiers; benchmarking, latency analysis, MLPerf scenarios.
4. **Operations & Monitoring** — owns [[SilentDegradation|silent degradation]]; four-dimensional monitoring (infrastructure, model performance, data quality, business impact), alerting, incident response. ([[MLOps]])
5. **Ethics & Governance** — owns fairness, transparency, privacy, and safety; made *explicit* so it isn't dropped under deadline pressure. ([[ResponsibleAI]])

The framework was chosen to mirror how industry teams organize. Teams lacking expertise in any pillar face **60–85% project failure rates**. The five pillars map onto the book's four parts (Foundations, Build, Optimize, Deploy).

## Connections

- [[DataEngineering]] — pillar 1.
- [[MLOps]] / [[ModelMonitoring]] — pillar 4.
- [[ResponsibleAI]] — pillar 5.
- [[DAMTaxonomy]] / [[MLSystemLifecycle]] — the framework emerges from these.
- [[MLSystemsEngineering]] — the discipline the pillars structure.
- [[mlsysbook-ch01-introduction]] — source.
