---
name: DisaggregatedEvaluation
title: "Disaggregated Evaluation"
type: concept
tags: [responsible-ai, fairness, evaluation, testing]
sources: [mlsysbook-ch15-responsible-engineering]
last_updated: 2026-06-05
---

# Disaggregated Evaluation

Reporting model metrics **separately for each relevant subgroup** instead of (only) in aggregate. Per [[mlsysbook-ch15-responsible-engineering|mlsysbook Vol 1 Ch 15]], it is the central methodology for detecting hidden [[Fairness|fairness]] failures — the antidote to the [[FlawOfAverages|Flaw of Averages]]. The [[GenderShades|Gender Shades]] study established it as the standard, showing a single aggregate accuracy number can conceal **>43× error-rate disparities** across intersectional subgroups.

## Practices
- **Slice-based evaluation** — partition test data into meaningful subgroups (e.g. low-income, rural); a 95% aggregate model may be 78% on a slice.
- **Intersectional analysis** — combinations of attributes (harms concentrate at intersections; e.g. dark-skinned females).
- **Confidence intervals** — small subgroups yield unreliable estimates; validating a 1%-of-population group needs ~100× more data under random sampling → **intentional data engineering** (stratified sampling).
- **Temporal monitoring** — track subgroup performance over time (drift hits some populations first).
- Complements [[InvarianceTesting|invariance]], boundary, stress, and stakeholder [[RedTeaming|red-team]] testing.

## Connections
- [[Fairness]] / [[FlawOfAverages]] — the property and the fallacy it counters.
- [[GenderShades]] — the audit that canonized the method.
- [[ConfusionMatrix]] / [[TruePositiveRate]] / [[FalsePositiveRate]] — per-slice metrics.
- [[ModelCard]] — discloses disaggregated results.
- [[ModelMonitoring]] — production subgroup-parity tracking.
- [[Fairlearn]] / [[AIFairness360]] — tooling.
- [[mlsysbook-ch15-responsible-engineering]] — source.
