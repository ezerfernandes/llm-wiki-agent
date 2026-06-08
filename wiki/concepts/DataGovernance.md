---
title: "Data Governance"
type: concept
tags: [cs324, llm]
sources: [cs324-data, mlsysbook-ch04-data-engineering, mlsysbook-ch14-ml-operations]
last_updated: 2026-06-05
---

Data governance encompasses the organizational practices governing how data is created, documented, quality-controlled, licensed, and secured. For LLMs it covers rights and consent, dataset documentation, and access controls over training corpora.

In Reddi's *Machine Learning Systems* ([[mlsysbook-ch04-data-engineering|Vol 1, Ch 4]]) governance is the **fourth pillar** of [[DataEngineering|data engineering]] ("ethics & compliance"): privacy (GDPR/CCPA/HIPAA), regulatory compliance, clear data ownership, and the transparency/accountability ([[DataLineage|lineage]], provenance, data statements/data cards) needed to demonstrate compliance under audit. A perfectly scalable, reliable, high-quality pipeline that violates GDPR or perpetuates bias "creates liability rather than value."

## Connections
- [[Datasheets]] — documentation supporting governance
- [[FourPillarsOfDataEngineering]] — governance is the fourth pillar.
- [[DataLineage]] — the provenance/audit-trail mechanism.
- [[DataDebt]] — ungoverned systems accumulate documentation/governance debt.
- [[cs324-data]] / [[mlsysbook-ch04-data-engineering]] — sources.
- [[mlsysbook-ch14-ml-operations]] — mlsysbook Vol 1 Ch 14 frames governance across the full lifecycle (transparency, fairness, compliance) including post-deployment fairness-drift monitoring.

