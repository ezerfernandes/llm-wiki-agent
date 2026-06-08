---
name: RoleBasedAccessControl
title: "Role-Based Access Control (RBAC)"
type: concept
tags: [responsible-ai, security, governance]
sources: [mlsysbook-ch15-responsible-engineering]
last_updated: 2026-06-05
---

# Role-Based Access Control (RBAC)

An access-control model that grants data and system permissions according to a user's organizational role rather than identity, used in [[mlsysbook-ch15-responsible-engineering|mlsysbook Vol 1 Ch 15]] as the primary mechanism for **mapping organizational policy onto enforced database and storage permissions** — the security pillar of [[DataGovernance|data governance]].

## In the chapter's governance architecture
- Translates "who may see what" policy into S3 bucket policies, column-level security, and **separate feature-store read vs. write paths**.
- Works alongside [[Encryption|encryption]] (at rest + TLS 1.3 in transit) and an [[AuditTrail|audit trail]] that records every access decision.
- Part of the "security → privacy → compliance → audit" governance stack the chapter lays out.

## Connections
- [[DataGovernance]] — RBAC is the enforcement layer of its security domain.
- [[Encryption]] — confidentiality control paired with access control.
- [[AuditTrail]] — logs RBAC-mediated access for compliance.
- [[GDPR]] / [[HIPAA]] — compliance regimes RBAC helps satisfy.
- [[mlsysbook-ch15-responsible-engineering]] — source.
