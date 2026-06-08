---
title: "HIPAA (Health Insurance Portability and Accountability Act)"
type: concept
tags: [privacy, regulation, healthcare, deployment, mlsysbook]
sources: [mlsysbook-ch02-ml-systems, mlsysbook-ch15-responsible-engineering]
last_updated: 2026-06-05
---

# HIPAA (Health Insurance Portability and Accountability Act)

The US law governing healthcare data privacy that, in [[VijayJanapaReddi|Reddi]]'s *Machine Learning Systems* ([[mlsysbook-ch02-ml-systems|Vol 1, Ch 2]]), translates into **direct systems-level costs** for ML deployments and a [[DeploymentDecisionFramework|privacy-layer]] driver toward local processing.

HIPAA's mandates — isolated compute, immutable logging for every inference, and end-to-end data encryption — are nonnegotiable safeguards that typically add **15–30% to infrastructure and operational overhead** for a production ML system. This pushes healthcare ML toward [[EdgeML|Edge ML]] and on-device [[MobileML|mobile]]/[[TinyML]] processing: patient monitoring, surgical assistance, Apple Watch ECG, and FDA-cleared cardiac wearables maintain HIPAA compliance by keeping data local.

## Connections

- [[DeploymentDecisionFramework]] — HIPAA is a privacy-layer driver.
- [[GDPR]] — the European privacy analogue.
- [[EdgeML]] / [[MobileML]] / [[TinyML]] — the local-processing paradigms HIPAA favors.
- [[Apple]] — Apple Watch on-device ECG as a HIPAA-compliant example.
- [[mlsysbook-ch02-ml-systems]] — source.
- [[mlsysbook-ch15-responsible-engineering]] — mlsysbook Vol 1 Ch 15 turns HIPAA into governance architecture: PHI de-identification, **6-year audit-log retention** ([[AuditTrail|audit trail]]), and penalties up to $50K/violation ($1.5M/yr cap).
