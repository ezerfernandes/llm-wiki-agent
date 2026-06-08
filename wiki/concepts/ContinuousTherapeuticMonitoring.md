---
title: "Continuous Therapeutic Monitoring"
type: concept
tags: [mlops, healthcare, wearables, edge-ai]
sources: [mlsysbook-ch14-ml-operations]
last_updated: 2026-06-05
---

# Continuous Therapeutic Monitoring (CTM)

A healthcare approach using wearable sensors for real-time physiological/behavioral data collection and personalized treatment adjustments. CTM forces [[MLOps]] to confront constraints absent in typical deployments: feedback loops must include human-in-the-loop approval for safety-critical decisions, retraining requires clinician-validated labels (not implicit signals), and model updates must satisfy regulatory compliance before deployment. These constraints reshape every MLOps principle, making CTM a stress test for [[OperationalMaturity|operational maturity]].

The canonical example in [[mlsysbook-ch14-ml-operations]] is hypertension management — research systems estimate systolic blood pressure from ECG, PPG (photoplethysmography), pulse-transit-time, and heart-rate features, augmented by activity context and medication-adherence logs. CTM is operationalized through the [[ClinAIOps]] framework's three feedback loops.

## Connections
- [[ClinAIOps]] — the operating framework for CTM.
- [[MLOps]] — the discipline CTM stress-tests.
- [[EdgeML|Edge AI]] / [[FederatedLearning]] — wearable inference and privacy-preserving improvement.
- [[OuraRing]] — adjacent wearable-ML case study.
- [[mlsysbook-ch14-ml-operations]] — source chapter.
