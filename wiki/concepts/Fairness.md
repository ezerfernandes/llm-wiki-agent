---
name: Fairness
title: "Fairness (ML)"
type: concept
tags: [responsible-ai, fairness, evaluation, ethics]
sources: [mlsysbook-ch15-responsible-engineering]
last_updated: 2026-06-05
---

# Fairness (ML)

The property that an ML system produces equitable outcomes across user groups. Per [[mlsysbook-ch15-responsible-engineering|mlsysbook Vol 1 Ch 15]], fairness "has multiple conflicting mathematical definitions that *cannot* all be satisfied simultaneously" — making it a **constrained design choice**, not a single metric. It resists the simple formalization that traditional software correctness allows.

## Two families
- **Individual fairness** — similar individuals receive similar treatment (e.g. swapping "John" → "Jamal" should not change a loan decision; an [[InvarianceTesting|invariance test]]).
- **Group fairness** — equitable outcomes across demographic categories, computed from [[ConfusionMatrix|confusion matrices]]: [[DemographicParity|demographic parity]], [[EqualOpportunity|equal opportunity]], [[EqualizedOdds|equalized odds]], [[Calibration|calibration]].

These can conflict; choosing among them requires value judgments beyond optimization. The **impossibility theorem** (Kleinberg et al. 2016; Chouldechova 2017) proves that when group base rates differ, calibration and equalized odds cannot both hold (see [[COMPAS]]).

## Measurement
- Reveal disparities only through [[DisaggregatedEvaluation|disaggregated/intersectional evaluation]] — aggregate accuracy hides them ([[FlawOfAverages|Flaw of Averages]]; [[GenderShades|Gender Shades]] >43× error disparity).
- Industry starting thresholds: error-rate ratio <1.25× (high-stakes), FPR difference <5pp (screening), selection-rate ratio ≥0.8 (the four-fifths rule / [[DisparateImpact|disparate impact]] doctrine).
- The fairness-accuracy [[ParetoFrontier|Pareto frontier]] makes trade-offs explicit; a "sweet spot" often achieves large fairness gains with modest accuracy loss.

## Connections
- [[ResponsibleAI]] / [[ResponsibleAIEngineering]] — the broader discipline.
- [[AlgorithmicBias]] / [[ProxyVariable]] / [[DisparateImpact]] — failure modes that make systems unfair.
- [[DemographicParity]] / [[EqualOpportunity]] / [[EqualizedOdds]] / [[Calibration]] — the group-fairness metrics.
- [[ParetoFrontier]] — quantifies the fairness-accuracy trade-off.
- [[AdversarialDebiasing]] / [[Reweighting]] / [[ThresholdAdjustment]] — mitigation techniques.
- [[ModelCard]] — discloses disaggregated fairness results.
- [[mlsysbook-ch15-responsible-engineering]] — source.
