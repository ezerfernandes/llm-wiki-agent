---
title: "Apache Atlas"
type: entity
tags: [responsible-ai, governance, data-lineage, tooling, open-source]
sources: [mlsysbook-ch15-responsible-engineering]
last_updated: 2026-06-05
---

# Apache Atlas

Apache Atlas is an open-source metadata and data-governance framework providing data cataloging, classification, and end-to-end [[DataLineage|lineage]] tracking. Cited in [[mlsysbook-ch15-responsible-engineering|mlsysbook Vol 1 Ch 15]] as a lineage backbone for ML governance.

## Why it matters here
- Combined with orchestrators ([[Airflow]] / [[Kubeflow]]), Atlas traces any feature back to its source data (e.g. raw audio in the [[LighthouseModel|Lighthouse KWS]] pipeline) and identifies every derived artifact to delete on a [[GDPR]] Article 17 erasure request (Article 30 record-keeping).
- One of the chapter's two named lineage tools, alongside [[DataHub]].

## Connections
- [[DataLineage]] — the capability it provides.
- [[DataHub]] — comparable open-source lineage/catalog tool.
- [[Airflow]] / [[Kubeflow]] — orchestrators it integrates with.
- [[DataGovernance]] / [[AuditTrail]] — the governance stack it supports.
- [[GDPR]] — erasure/record-keeping obligations lineage helps satisfy.
- [[mlsysbook-ch15-responsible-engineering]] — source.
