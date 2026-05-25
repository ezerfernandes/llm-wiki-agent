---
name: StatelessRetraining
title: "Stateless Retraining"
type: concept
tags: [continual-learning, training]
sources: [dmls-ch08-distribution-shifts-monitoring, dmls-ch09-continual-learning]
last_updated: 2026-05-23
---

# Stateless Retraining

Retraining that **starts from scratch** (random weights or pretrained baseline) on a long historical window of data — the default ML retraining mode and the "stateless" half of the [[StatefulTraining|stateful-vs-stateless]] choice per [[ChipHuyen|Huyen]]'s [[dmls-ch09-continual-learning|DMLS Ch 9]].

## When it's the right call
- **Architecture change** ([[ModelIteration|model iteration]] vs [[DataIteration|data iteration]]): if you've changed the model definition, [[StatefulTraining|stateful training]] doesn't apply.
- **First training** of a new model.
- **Catastrophic [[DistributionShift|distribution shift]]**: when the historical-data prior is actively misleading, fresh-start retraining with a downweighted historical window is safer than fine-tuning.
- **Sample-efficiency-limited domains**: when the new-data window alone is too small to support stateful updates without [[CatastrophicForgetting|forgetting]].

## Cost
Significantly higher than [[StatefulTraining]]: [[Grubhub]] (DMLS Ch 9) reported 45× compute increase running stateless vs stateful daily retrains.

## Stages 1–2 of the continual-learning maturity model
Stateless retraining at increasing automation cadence:
1. **Manual** — DS triggers re-run on demand.
2. **Automatic** — scheduler ([[Airflow]] / [[ArgoWorkflows]]) triggers on a fixed cron.

Higher stages require [[StatefulTraining|stateful training]] + [[ModelLineage|model lineage]] tracking.

## Connections
- [[StatefulTraining]] — the incremental alternative.
- [[ContinualLearning]] — the broader umbrella.
- [[ModelIteration]] vs [[DataIteration]] — the architectural-change distinction that forces stateless.
- [[CatastrophicForgetting]] — the failure stateless retraining is immune to.
