---
title: "AI Fairness 360"
type: entity
tags: [responsible-ai, fairness, tooling, open-source]
sources: [mlsysbook-ch15-responsible-engineering]
last_updated: 2026-06-05
---

# AI Fairness 360

AI Fairness 360 (AIF360) is IBM's open-source toolkit providing fairness metrics and bias-mitigation algorithms across the ML pipeline. Cited in [[mlsysbook-ch15-responsible-engineering|mlsysbook Vol 1 Ch 15]] as one of the standard libraries that operationalize fairness measurement and mitigation.

## Why it matters here
- Packages the [[Fairness|fairness]] metrics ([[DemographicParity|demographic parity]], [[EqualizedOdds|equalized odds]], [[EqualOpportunity|equal opportunity]]) and mitigations ([[Reweighting|reweighting]], [[AdversarialDebiasing|adversarial debiasing]], [[ThresholdAdjustment|threshold adjustment]]) the chapter describes, so teams can compute and remediate disparities without reimplementing them.
- Alongside [[Fairlearn]], it is the chapter's example of fairness tooling moving from research to production checklists.

## Connections
- [[Fairlearn]] — Microsoft's comparable fairness toolkit.
- [[Fairness]] / [[DisaggregatedEvaluation]] — what it measures.
- [[Reweighting]] / [[AdversarialDebiasing]] / [[ThresholdAdjustment]] — mitigations it implements.
- [[ResponsibleAIEngineering]] — the practice it supports.
- [[mlsysbook-ch15-responsible-engineering]] — source.
