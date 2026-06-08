---
name: Encryption
title: "Encryption"
type: concept
tags: [responsible-ai, security, governance, privacy]
sources: [mlsysbook-ch15-responsible-engineering]
last_updated: 2026-06-05
---

# Encryption

Rendering data unreadable without a key, applied across an ML system to enforce confidentiality as part of the **security** pillar of [[DataGovernance|data governance]] ([[mlsysbook-ch15-responsible-engineering|mlsysbook Vol 1 Ch 15]]).

## In the chapter's governance architecture
- **At rest** — managed via cloud key services (AWS / GCP KMS).
- **In transit** — **TLS 1.3**.
- **Edge model updates** — code-signing to authenticate and protect model artifacts pushed to devices (e.g. the [[LighthouseModel|Lighthouse KWS]] device fleet).
- Pairs with [[RoleBasedAccessControl|RBAC]], column-level security, and separate feature-store read/write paths to map organizational policy onto enforced database permissions.

## Connections
- [[DataGovernance]] — encryption is part of its security domain.
- [[RoleBasedAccessControl]] — access control complements encryption.
- [[AuditTrail]] — records access to encrypted resources.
- [[DifferentialPrivacy]] / [[FederatedLearning]] — privacy techniques layered above transport/storage encryption.
- [[mlsysbook-ch15-responsible-engineering]] — source.
