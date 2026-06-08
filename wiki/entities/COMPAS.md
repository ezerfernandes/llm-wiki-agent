---
title: "COMPAS"
type: entity
tags: [responsible-ai, fairness, case-study, criminal-justice]
sources: [mlsysbook-ch15-responsible-engineering]
last_updated: 2026-06-05
---

# COMPAS

COMPAS (Correctional Offender Management Profiling for Alternative Sanctions) is a proprietary recidivism-risk scoring tool by Northpointe (now Equivant) used in US criminal sentencing and parole decisions. It is the canonical **Algorithm-axis** fairness case study in [[mlsysbook-ch15-responsible-engineering|mlsysbook Vol 1 Ch 15]].

## Why it matters here
- [[ProPublica]] (Angwin et al. 2016) found that while COMPAS was **calibrated** (a score of 7 meant the same re-offend probability across groups), its *errors* were skewed: Black defendants who did **not** re-offend were flagged high-risk at nearly **2× the White rate (44.9% vs. 23.5%)**, while White re-offenders were mislabeled low-risk far more often (47.7% vs. 28%).
- It satisfied calibration but violated [[EqualizedOdds|equalized odds]] — the empirical anchor for the **Impossibility Theorem of Fairness** (Chouldechova 2017; Kleinberg et al. 2016): when base rates differ, calibration and equalized odds cannot both hold.

## Connections
- [[EqualizedOdds]] / [[Calibration]] — the two criteria COMPAS could not jointly satisfy.
- [[AlgorithmicBias]] / [[DisparateImpact]] — the harm it illustrates.
- [[ProPublica]] — the investigative outlet that audited it.
- [[Fairness]] — the impossibility theorem it motivates.
- [[DAMTaxonomy]] — classified as an Algorithm-axis failure.
- [[mlsysbook-ch15-responsible-engineering]] — source.
