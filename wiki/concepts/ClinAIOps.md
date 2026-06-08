---
title: "ClinAIOps"
type: concept
tags: [mlops, healthcare, governance, feedback-loops, case-study]
sources: [mlsysbook-ch14-ml-operations]
last_updated: 2026-06-05
---

# ClinAIOps

A framework (Chen et al. 2023) for operationalizing AI in clinical environments, where standard [[MLOps]] is insufficient because healthcare requires extensive human oversight, domain-specific evaluation, and ethical governance. ClinAIOps reframes [[FeedbackLoop|feedback loops]] *as beneficial architecture* rather than technical debt, designing them into the system via **three interlocking loops**:

- **Patient treatment loop** — wearable sensors capture physiological data; tiered AI recommendations within clinician-defined safety thresholds enable bounded self-management.
- **Clinician oversight loop** — clinicians review AI recommendations (accept/reject/modify) and set approval limits, preserving accountability.
- **Developer feedback loop** — patient + clinician signals inform model, interface, and workflow improvement.

Applied to [[ContinuousTherapeuticMonitoring|continuous therapeutic monitoring]] (e.g., hypertension management with PPG/ECG/pulse-transit-time BP estimation and tiered medication titration). ClinAIOps differs from MLOps across 8 dimensions: it optimizes *patient outcomes* (not model metrics), coordinates patients/clinicians/developers (not just data scientists/engineers), and centers privacy, ethics, and clinical validation. One of two case studies in [[mlsysbook-ch14-ml-operations]] (with the [[OuraRing|Oura Ring]]).

## Connections
- [[ContinuousTherapeuticMonitoring]] — the healthcare paradigm ClinAIOps serves.
- [[MLOps]] — the framework it extends for clinical/regulatory needs.
- [[FeedbackLoop]] — reframed from debt to deliberate architecture.
- [[GracefulDegradation]] — made mandatory by regulatory requirements (human-in-the-loop).
- [[OuraRing]] — the companion edge case study.
- [[mlsysbook-ch14-ml-operations]] — source chapter.
