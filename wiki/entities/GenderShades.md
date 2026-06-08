---
title: "Gender Shades"
type: entity
tags: [responsible-ai, fairness, case-study, computer-vision, audit]
sources: [mlsysbook-ch15-responsible-engineering]
last_updated: 2026-06-05
---

# Gender Shades

Gender Shades is the landmark 2018 audit study by [[JoyBuolamwini|Joy Buolamwini]] and [[TimnitGebru|Timnit Gebru]] ([[MITMediaLab|MIT Media Lab]]) of commercial facial-analysis systems from Microsoft, IBM, and Face++. It is the canonical [[DisaggregatedEvaluation|disaggregated-evaluation]] case study in [[mlsysbook-ch15-responsible-engineering|mlsysbook Vol 1 Ch 15]].

## Why it matters here
- Evaluated on the Fitzpatrick skin-tone scale, gender-classification error ranged from **0.8% (light-skinned males) to 34.7% (dark-skinned females)** — a **>43× disparity** completely invisible in aggregate accuracy.
- "The measurement methodology *was* the intervention": after publication, Microsoft cut worst-case error **~20×** (below 2% for all groups; Raji et al. 2019).
- Illustrates the **statistics of representation** — validating a 1%-of-population subgroup needs ~100× more data than the majority under random sampling, so fairness requires intentional data engineering, not just more data.

## Connections
- [[JoyBuolamwini]] / [[TimnitGebru]] — the authors.
- [[MITMediaLab]] — where the study was conducted.
- [[DisaggregatedEvaluation]] / [[FlawOfAverages]] — the methodology it pioneered.
- [[AlgorithmicBias]] / [[Fairness]] — the harm it exposed.
- [[microsoft|Microsoft]] — one of the audited vendors, which later reduced error ~20×.
- [[mlsysbook-ch15-responsible-engineering]] — source.
