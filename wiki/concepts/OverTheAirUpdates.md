---
title: "Over-the-Air Updates"
type: concept
tags: [edge-ai, mlops, deployment, tinyml]
sources: [mlsysbook-ch14-ml-operations]
last_updated: 2026-06-05
---

# Over-the-Air (OTA) Updates

The mechanism for deploying and maintaining ML models on physically inaccessible edge/embedded devices without requiring direct host access. OTA pipelines must implement **secure model distribution** with cryptographic signatures and rollback mechanisms, using **differential compression** to transmit only parameter changes rather than complete model artifacts (80–95% payload reduction for constrained edge networks). Update scheduling must account for device connectivity patterns, power availability, and operational criticality.

A small model footprint from quantization and pruning is essential for OTA viability, and consistency is a critical concern: a single failed update can corrupt the on-device model, breaking the ML pipeline until the next connectivity window. In the [[OuraRing|Oura Ring]] case study ([[mlsysbook-ch14-ml-operations]]), OTA delivers quantized/pruned sleep-staging models to rings in the field.

## Connections
- [[EdgeML|Edge AI]] / [[TinyML]] — the deployment contexts requiring OTA.
- [[Quantization]] / [[Pruning]] — shrink models to make OTA payloads viable.
- [[RollbackStrategy]] — OTA must include rollback for failed updates.
- [[OuraRing]] — case study using OTA.
- [[mlsysbook-ch14-ml-operations]] — source chapter.
