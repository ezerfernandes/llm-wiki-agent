---
name: InvarianceTesting
title: "Invariance Testing"
type: concept
tags: [responsible-ai, fairness, testing, evaluation]
sources: [mlsysbook-ch15-responsible-engineering]
last_updated: 2026-06-05
---

# Invariance Testing

A behavioral test that checks whether a model's prediction **changes when it should not**. Per [[mlsysbook-ch15-responsible-engineering|mlsysbook Vol 1 Ch 15]], replacing "John" with "Jamal" in a loan application should not change approval likelihood if the feature is not legitimate for the decision — a direct operationalization of *individual* [[Fairness|fairness]]. Behavioral frameworks such as **CheckList** (Ribeiro et al. 2020) organize tests around model capabilities and invariance-style expectations rather than accuracy alone.

It complements other responsible-testing strategies: [[DisaggregatedEvaluation|slice-based]] evaluation, boundary testing (edges of input distributions), stress testing (corrupted/adversarial inputs, distribution shift), and stakeholder [[RedTeaming|red-teaming]].

## Connections
- [[Fairness]] — individual-fairness operationalization.
- [[DisaggregatedEvaluation]] / [[RedTeaming]] — sibling responsible-testing strategies.
- [[ResponsibleAIEngineering]] — turns fairness goals into testable invariants.
- [[mlsysbook-ch15-responsible-engineering]] — source.
