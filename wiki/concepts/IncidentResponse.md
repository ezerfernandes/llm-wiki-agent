---
title: "Incident Response"
type: concept
tags: [mlops, operations, reliability, on-call]
sources: [mlsysbook-ch14-ml-operations]
last_updated: 2026-06-05
---

# Incident Response (for ML Systems)

Structured processes for resolving production ML incidents, which differ from traditional software incidents because symptoms manifest as **accuracy degradation rather than explicit errors** — no stack trace, no crashed process, just a statistical signal. At 2 AM an on-call engineer facing a 12% click-through drop must distinguish among an upstream data-pipeline failure, model drift, a seasonal pattern, or statistical noise.

**Severity classification** ([[mlsysbook-ch14-ml-operations]]): P0 complete failure / serving errors (15 min response), P1 significant accuracy degradation > 10% (1 hr), P2 moderate/localized drift (4 hr, e.g. one feature PSI > 0.3), P3 minor anomaly (24 hr). The response checklist: detect → assess impact (% traffic) → review recent changes → evaluate mitigation (rollback, fallback, traffic reduction) → root-cause (model/data/infra). P0/P1 require postmortems naming the monitoring gap that let the issue reach production.

## Connections
- [[ModelDebugging]] — the diagnosis step (data-first decision tree).
- [[OnCallRotation]] — the human availability structure.
- [[RollbackStrategy]] — a primary mitigation.
- [[AlertFatigue]] — risk that erodes response effectiveness.
- [[ModelMonitoring]] / [[DriftDetection]] — the signals that trigger incidents.
- [[MLOps]] — production-operations practice.
- [[mlsysbook-ch14-ml-operations]] — source chapter.
