---
title: "Differential Privacy"
type: concept
tags: [cs324, llm, privacy, responsible-ai]
sources: [cs324-security, mlsysbook-ch15-responsible-engineering]
last_updated: 2026-06-05
---

Differential privacy is a formal, ε-parameterized guarantee that bounds the influence any single training record can have on a model's output, limiting what an adversary can infer about individuals. In deep learning it is applied via [[DP-SGD]], trading some accuracy for privacy.

## Connections
- [[Memorization]] — the leakage risk it mitigates
- [[DP-SGD]] — the training mechanism that achieves it
- [[cs324-security]] — discussed in this CS324 lecture
- [[mlsysbook-ch15-responsible-engineering]] — mlsysbook Vol 1 Ch 15 treats DP as a core privacy control in data governance: track the ε-budget, validate it empirically with [[MembershipInferenceAttack|membership inference]], and combine with [[FederatedLearning|federated learning]] because raw gradients still leak via reconstruction attacks.
