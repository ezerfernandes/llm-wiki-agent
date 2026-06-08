---
name: KAnonymity
title: "k-Anonymity"
type: concept
tags: [responsible-ai, privacy, security]
sources: [mlsysbook-ch15-responsible-engineering]
last_updated: 2026-06-05
---

# k-Anonymity

A syntactic privacy guarantee in which every record is indistinguishable from at least *k − 1* others on its quasi-identifiers (e.g. ZIP, age, gender), achieved through generalization and suppression ([[mlsysbook-ch15-responsible-engineering|mlsysbook Vol 1 Ch 15]]). Refinements l-diversity and t-closeness add constraints on sensitive-attribute distributions within each equivalence class.

## Limitation emphasized in Ch 15
- k-anonymity (and l-diversity / t-closeness) **fail against ML attacks** — high-dimensional models can re-identify individuals or infer membership despite the guarantee. The chapter contrasts this syntactic family with the formal, attack-resistant guarantee of [[DifferentialPrivacy|differential privacy]], validated empirically via [[MembershipInferenceAttack|membership inference]].

## Connections
- [[DifferentialPrivacy]] — the stronger, formal alternative the chapter recommends.
- [[MembershipInferenceAttack]] — the attack class that defeats k-anonymity.
- [[DataGovernance]] — privacy domain.
- [[GDPR]] / [[HIPAA]] — de-identification regimes that motivate anonymization.
- [[mlsysbook-ch15-responsible-engineering]] — source.
