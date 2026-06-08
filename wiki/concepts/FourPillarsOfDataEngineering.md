---
title: "Four Pillars of Data Engineering"
type: concept
tags: [ml-systems, mlsysbook, data-engineering, framework, foundations]
sources: [mlsysbook-ch04-data-engineering]
last_updated: 2026-06-05
---

# Four Pillars of Data Engineering

The organizing framework of Reddi's *Machine Learning Systems* ([[mlsysbook-ch04-data-engineering|Vol 1, Ch 4]]): every data-engineering decision — from storage formats to ingestion patterns — is evaluated against four interdependent dimensions.

- **Quality** — accuracy & fitness: correctness (are values right?), coverage (does data represent the deployment environment?), freshness (does the distribution still match production?).
- **Reliability** — consistency & fault tolerance: pipelines that keep operating under component failures, anomalies, and load spikes.
- **Scalability** — growth & performance (cost-effective): from gigabyte prototypes to petabyte production without redesign.
- **Governance** — ethics & compliance: privacy, regulatory compliance ([[GDPR]]), data ownership, provenance, auditability.

The pillars trade off against each other: validation overhead vs throughput, consistency vs distributed scale, privacy vs performance, bias mitigation vs data availability. Balancing these tensions is the core challenge.

**Diagnostic lens:** gradual accuracy decline → Quality ([[DataDrift|drift]]); intermittent crashes → Reliability; slow training despite hardware → Scalability; audit gaps → Governance. The chapter's key insight: data-infrastructure failures outnumber model failures by a wide margin, yet practitioners instinctively debug the model first.

## Connections

- [[DataEngineering]] — the discipline these pillars structure.
- [[DataCascade]] — the failure pattern the framework prevents.
- [[DataQuality]] / [[DataDrift]] — the Quality pillar's mechanisms.
- [[CircuitBreaker]] / [[DeadLetterQueue]] — Reliability primitives.
- [[DataGovernance]] / [[DataLineage]] — the Governance pillar.
- [[mlsysbook-ch04-data-engineering]] — source.
