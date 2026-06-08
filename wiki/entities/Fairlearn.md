---
title: "Fairlearn"
type: entity
tags: [responsible-ai, fairness, tooling, open-source]
sources: [mlsysbook-ch15-responsible-engineering]
last_updated: 2026-06-05
---

# Fairlearn

Fairlearn is Microsoft's open-source Python toolkit for assessing and improving the fairness of ML models, providing group-fairness metrics and mitigation algorithms. Cited in [[mlsysbook-ch15-responsible-engineering|mlsysbook Vol 1 Ch 15]] as a standard library for operationalizing fairness.

> Not to be confused with [[FairLearning]] (a copyright fair-use theory) — Fairlearn is a fairness-measurement software toolkit.

## Why it matters here
- Implements the chapter's fairness metrics ([[DemographicParity|demographic parity]], [[EqualizedOdds|equalized odds]], [[EqualOpportunity|equal opportunity]]) computed from confusion matrices, plus mitigations such as [[ThresholdAdjustment|threshold adjustment]] (Hardt et al. 2016) and [[Reweighting|reweighting]].
- Pairs with [[AIFairness360|AI Fairness 360]] as the chapter's example of production-ready fairness tooling.

## Connections
- [[AIFairness360]] — IBM's comparable fairness toolkit.
- [[Fairness]] / [[DisaggregatedEvaluation]] — what it measures.
- [[ThresholdAdjustment]] / [[Reweighting]] / [[AdversarialDebiasing]] — mitigations it supports.
- [[ResponsibleAIEngineering]] — the practice it supports.
- [[mlsysbook-ch15-responsible-engineering]] — source.
