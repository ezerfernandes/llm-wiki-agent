---
title: "FDA (U.S. Food and Drug Administration)"
type: entity
tags: [regulator, healthcare, medical-ai, governance, mlsysbook]
sources: [mlsysbook-ch03-ml-workflow]
last_updated: 2026-06-05
---

# FDA (U.S. Food and Drug Administration)

The U.S. regulator of medical devices, including AI/ML-based systems. Reddi's *Machine Learning Systems* ([[mlsysbook-ch03-ml-workflow|Vol 1, Ch 3]]) cites the FDA as the reason **regulatory validation is a first-class engineering requirement** for clinical ML like [[DiabeticRetinopathyScreening|DR screening]].

Key points from the chapter:

- The FDA regulates AI/ML devices under the **Software as a Medical Device (SaMD)** framework and has authorized **1,000+** AI/ML-enabled devices (predominantly radiology and cardiology).
- Its **2021 AI/ML SaMD Action Plan** named draft guidance on **predetermined change control plans (PCCPs)** as a planned action; later guidance describes how manufacturers may propose bounded, prespecified model modifications and validation protocols in marketing submissions.
- This architecture directly constrains [[MLWorkflow|workflow]] design: it requires **versioned model artifacts, reproducible training pipelines, and audit trails at every lifecycle stage** — turning compliance into an engineering constraint rather than a paperwork afterthought.

## Connections

- [[ModelValidation]] — regulatory validation as a deployment gate.
- [[DiabeticRetinopathyScreening]] — the clinical case study subject to FDA clearance.
- [[DataLineage]] / [[Reproducibility]] / [[DataVersioning]] — the audit-trail requirements FDA imposes.
- [[mlsysbook-ch03-ml-workflow]] — source.
