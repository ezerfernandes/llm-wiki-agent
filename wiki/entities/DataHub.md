---
title: "DataHub"
type: entity
tags: [responsible-ai, governance, data-lineage, tooling, open-source]
sources: [mlsysbook-ch15-responsible-engineering]
last_updated: 2026-06-05
---

# DataHub

DataHub is an open-source metadata platform (originated at LinkedIn) for data discovery, observability, and [[DataLineage|lineage]] across data and ML assets. Cited in [[mlsysbook-ch15-responsible-engineering|mlsysbook Vol 1 Ch 15]] as a lineage/cataloging tool for ML governance.

## Why it matters here
- One of the chapter's two named lineage tools, alongside [[ApacheAtlas]]; integrated with orchestrators ([[Airflow]] / [[Kubeflow]]) it traces features back to source data and supports identifying artifacts for [[GDPR]] erasure requests.
- Underpins the **audit** and **compliance** domains of [[DataGovernance|data governance]].

## Connections
- [[DataLineage]] — the capability it provides.
- [[ApacheAtlas]] — comparable open-source lineage/governance tool.
- [[Airflow]] / [[Kubeflow]] — orchestrators it integrates with.
- [[DataGovernance]] / [[AuditTrail]] — the governance stack it supports.
- [[mlsysbook-ch15-responsible-engineering]] — source.
