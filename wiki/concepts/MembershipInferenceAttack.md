---
name: MembershipInferenceAttack
title: "Membership Inference Attack"
type: concept
tags: [responsible-ai, privacy, security, differential-privacy]
sources: [mlsysbook-ch15-responsible-engineering]
last_updated: 2026-06-05
---

# Membership Inference Attack

A privacy attack that determines whether a specific individual's data was in a model's training set, by exploiting the fact that models behave differently (e.g. higher confidence) on examples they were trained on ([[mlsysbook-ch15-responsible-engineering|mlsysbook Vol 1 Ch 15]]). It is the canonical empirical test that a privacy defense actually works.

## Role in the governance toolkit
- Used to **validate** a [[DifferentialPrivacy|differential-privacy]] ε-budget: if membership can still be inferred, the ε is too loose.
- Motivates combining [[FederatedLearning|federated learning]] with differential privacy — raw gradients leak training data via reconstruction attacks, so FedAvg alone is insufficient.
- Demonstrates why syntactic anonymization ([[KAnonymity|k-anonymity]], l-diversity, t-closeness) fails against ML adversaries.

## Connections
- [[DifferentialPrivacy]] — the defense membership inference tests.
- [[FederatedLearning]] — data-minimization architecture that still needs DP because of gradient leakage.
- [[KAnonymity]] — syntactic privacy that membership inference defeats.
- [[DataGovernance]] — privacy is one of its four domains.
- [[mlsysbook-ch15-responsible-engineering]] — source.
