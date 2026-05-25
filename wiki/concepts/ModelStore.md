---
name: ModelStore
title: "Model Store"
type: concept
tags: [mlops, infrastructure, versioning]
sources: [dmls-ch09-continual-learning, dmls-ch10-infrastructure-mlops]
last_updated: 2026-05-23
---

# Model Store

Versioned artifact repository for trained ML models. Per [[ChipHuyen|Huyen]]'s [[dmls-ch10-infrastructure-mlops|DMLS Ch 10]], the **least mature** component of the typical [[MLPlatform]] — most companies in 2022 reduced it to "throw the binary on [[AmazonS3]]," which made rollback / lineage / reproducibility difficult.

## The 8 artifacts a model store should manage
Per Huyen (citing [[StefanKrawczyk|Krawczyk]]'s [[StitchFix|Stitch Fix]] [[CS329S]] slide):
1. **Model definition** — architecture (e.g., `nn.Module` class).
2. **Model parameters** — trained weights.
3. **Featurize function** — input → features mapping.
4. **Predict function** — model → output mapping.
5. **Dependencies** — Python / OS / framework versions.
6. **Data** — training dataset reference ([[DataVersioning|version]]).
7. **Model-generation code** — training script + git SHA.
8. **Experiment artifacts** — metrics, logs, checkpoints, [[ExperimentTracking|tracker]] run IDs.
9. **Tags** — owner, task type, business unit (categorization metadata).

## Concrete tools
- [[MLflow]] — most popular non-cloud model store ([[Databricks]] origin).
- [[AmazonSageMaker]] Model Registry — managed-cloud variant.
- [[WeightsAndBiases]] + [[CometML]] cover artifact subset #7-#8.
- [[DVC]] handles artifact #6 (data version).

## Why it matters in continual learning
[[dmls-ch09-continual-learning|DMLS Ch 9]] makes the model store **stage-2 prerequisite** for the four-stage continual-learning maturity model: you cannot do automatic stateless retraining without a versioned model store; you cannot do [[StatefulTraining|stateful training]] (stage 3) without [[ModelLineage|model lineage]] tracking which base + data produced each checkpoint.

## Connections
- [[ModelRegistry]] — partial overlap; registry is the lookup/promotion subset.
- [[MLPlatform]] — model store is one of the four canonical components.
- [[ModelLineage]] — finer-grained tracking of which base + which data produced each checkpoint.
- [[ExperimentTracking]] — sibling artifact class.
- [[Reproducibility]] — model store is the operational unit of reproducibility.
