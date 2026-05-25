---
name: StatefulTraining
title: "Stateful Training"
type: concept
tags: [continual-learning, training, fine-tuning]
sources: [dmls-ch08-distribution-shifts-monitoring, dmls-ch09-continual-learning]
last_updated: 2026-05-23
---

# Stateful Training

Retraining that **continues from the last checkpoint** on fresh data only, rather than training from scratch on combined historical + fresh data. Sometimes called **fine-tuning** in [[ChipHuyen|Huyen]]'s [[dmls-ch09-continual-learning|DMLS Ch 9]] usage. The "stateful" half of the [[StatelessRetraining|stateless-vs-stateful]] choice in production retraining.

## Why use it
- **Compute reduction**: [[Grubhub]] reported a 45× compute reduction by switching from stateless to stateful daily retraining (DMLS Ch 9).
- **Less data needed**: only the new examples, not the full historical corpus.
- **Faster turnaround**: enables higher update cadence (hourly, even minute-level for [[CTRPrediction|ad CTR]] systems).

## Stage in the continual-learning maturity ladder
Per [[dmls-ch09-continual-learning|Huyen]]'s four-stage model:
1. Manual stateless retraining (stage 1).
2. Automatic stateless retraining (stage 2 — scheduler-driven).
3. **Automatic stateful training (stage 3)** — requires [[ModelLineage|model lineage]] to track which base + which data produced each checkpoint.
4. Event-triggered [[ContinualLearning|continual learning]] (stage 4).

## Caveats
- Requires [[ModelLineage]] to be operationally sustainable.
- [[CatastrophicForgetting|Catastrophic forgetting]] risk if the new-data distribution drifts too far from historical.
- Only well-defined for [[ModelIteration|data iteration]] (same architecture, fresh data); does not apply to [[DataIteration|model iteration]] (architecture changes).
- [[CollaborativeFiltering|Matrix-factorization]] and similar approaches adapt poorly to incremental updates.

## Connections
- [[StatelessRetraining]] — the from-scratch alternative.
- [[ContinualLearning]] — the broader continuum stateful training lives within.
- [[FineTuning]] — overlapping term; Huyen uses it as a synonym for stateful retraining.
- [[ModelLineage]] — prerequisite for sustained stateful training in production.
- [[CatastrophicForgetting]] — the failure mode to monitor.
