---
title: "Ensemble Learning"
type: concept
tags: [ml-engineering, model-composition, accuracy-deployment-tradeoff, mlsysbook]
sources: [mlsysbook-ch03-ml-workflow]
last_updated: 2026-06-05
---

# Ensemble Learning

Combining predictions from multiple models to achieve better accuracy than any single model. Three families (Reddi, [[mlsysbook-ch03-ml-workflow|Vol 1, Ch 3]]): **bagging** (train models on different data subsets), **boosting** (sequentially train models to correct prior errors), and **stacking** (a meta-model combines base predictions).

From a [[MLWorkflow|workflow]] perspective, ensembles embody an **accuracy-vs-deployment trade-off**: every constituent model multiplies inference latency, memory footprint, and serving cost. Competition winners typically ensemble **10–50 models**. The canonical cautionary tale is the **Netflix Prize** (2006–2009): BellKor's ensemble cut RMSE 10.06% and won $1M, but Netflix **never deployed it** because serving 800+ models exceeded the business value — simpler models plus better data infrastructure delivered more production value.

## Connections

- [[ModelEnsemble]] — the closely related composition concept.
- [[MLWorkflow]] — accuracy gains weighed against deployment feasibility.
- [[ModelCompression]] — the alternative path to deployable accuracy.
- [[Netflix]] — the competition-production-gap case.
- [[mlsysbook-ch03-ml-workflow]] — source.
