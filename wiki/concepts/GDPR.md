---
title: "GDPR (General Data Protection Regulation)"
type: concept
tags: [privacy, regulation, deployment, mlsysbook]
sources: [mlsysbook-ch02-ml-systems, mlsysbook-ch15-responsible-engineering]
last_updated: 2026-06-05
---

# GDPR (General Data Protection Regulation)

The European privacy framework (2018) that, in [[VijayJanapaReddi|Reddi]]'s *Machine Learning Systems* ([[mlsysbook-ch02-ml-systems|Vol 1, Ch 2]]), is a **regulatory driver pushing ML computation toward the edge** and the first filter in the [[DeploymentDecisionFramework|deployment decision framework]].

Its "Right to be Forgotten" provision creates a systems constraint unique to ML: deleting a user's data may require **retraining or fine-tuning any model that learned from it**, because weight updates are not individually reversible. This turns a legal requirement into a compute cost that scales with model size and retraining frequency. Organizations subject to GDPR must process sensitive data locally rather than transmit it to remote data centers, mandating [[EdgeML|Edge ML]] / [[MobileML|Mobile ML]] / [[TinyML]] and motivating privacy-preserving techniques like [[FederatedLearning|federated learning]] and differential privacy.

## Connections

- [[DeploymentDecisionFramework]] — GDPR is its privacy-layer driver.
- [[HIPAA]] — the US healthcare analogue with its own infra overhead.
- [[EdgeML]] / [[MobileML]] / [[TinyML]] — the local-processing paradigms GDPR favors.
- [[FederatedLearning]] — a privacy-preserving response.
- [[CloudML]] — what GDPR can eliminate for sensitive data.
- [[mlsysbook-ch02-ml-systems]] — source.
- [[mlsysbook-ch15-responsible-engineering]] — mlsysbook Vol 1 Ch 15 turns GDPR into architecture constraints: Article 22 restricts solely-automated decisions, Article 15(1)(h) grants access to "meaningful information about the logic," and right-to-erasure (Art. 17) within 30 days drives [[DataLineage|lineage]]/[[AuditTrail|audit]] design; Meta's 2023 EUR 390M fine illustrates governance-evidence failure.
