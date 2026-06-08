---
name: RedTeaming
title: "Red Teaming"
type: concept
tags: [responsible-ai, security, testing, evaluation]
sources: [mlsysbook-ch15-responsible-engineering]
last_updated: 2026-06-05
---

# Red Teaming

Adversarial probing of a system to surface failure modes before deployment. Per [[mlsysbook-ch15-responsible-engineering|mlsysbook Vol 1 Ch 15]], **stakeholder red-teaming** engages domain experts and affected community members to "identify scenarios that engineers may not anticipate but users will encounter, surfacing failure modes that no automated test can discover because they require lived experience to imagine."

It sits alongside [[InvarianceTesting|invariance]], slice-based ([[DisaggregatedEvaluation|disaggregated]]), boundary, and stress testing as a responsible-testing strategy that complements (does not replace) traditional software verification.

## Connections
- [[DisaggregatedEvaluation]] / [[InvarianceTesting]] — sibling responsible-testing methods.
- [[Fairness]] / [[ResponsibleAIEngineering]] — what red-teaming protects.
- [[mlsysbook-ch15-responsible-engineering]] — source.
