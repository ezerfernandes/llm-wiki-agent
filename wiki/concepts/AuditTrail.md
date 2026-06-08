---
name: AuditTrail
title: "Audit Trail"
type: concept
tags: [responsible-ai, governance, compliance, security]
sources: [mlsysbook-ch15-responsible-engineering]
last_updated: 2026-06-05
---

# Audit Trail

An immutable, append-only record of every consequential event in an ML system — predictions served, data accessed, models deployed, erasure requests fulfilled — so that lawful processing can be *demonstrated*, not merely asserted ([[mlsysbook-ch15-responsible-engineering|mlsysbook Vol 1 Ch 15]]). One of the four interlocking [[DataGovernance|data-governance]] domains (security, privacy, compliance, audit).

## How it is built
- Immutable stores (Apache Iceberg, Delta Lake, hash chains) prevent retroactive tampering; see the related [[hashchainedaudit|hash-chained audit]] pattern.
- High volume: a large platform may log **>50 billion events/day**.
- Retention is regulation-driven — **HIPAA mandates 6-year retention**.

## Why it matters
- Meta's Jan 2023 EUR 390M fine came from *insufficient governance infrastructure to demonstrate lawful processing*, not a breach — audit trails are the evidence regulators demand.
- Distinct from but fed by [[DataLineage|data lineage]], which traces *where* a feature came from; the audit trail records *what happened to it*.

## Connections
- [[DataGovernance]] — the umbrella practice; audit is one of its four domains.
- [[DataLineage]] — complementary: lineage = provenance, audit = event history.
- [[hashchainedaudit]] — a tamper-evident implementation pattern.
- [[GDPR]] / [[HIPAA]] — mandate retention and demonstrable compliance.
- [[RoleBasedAccessControl]] / [[Encryption]] — the security controls audit trails record access against.
- [[mlsysbook-ch15-responsible-engineering]] — source.
