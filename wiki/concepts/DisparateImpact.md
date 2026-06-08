---
name: DisparateImpact
title: "Disparate Impact"
type: concept
tags: [responsible-ai, fairness, regulation, legal]
sources: [mlsysbook-ch15-responsible-engineering]
last_updated: 2026-06-05
---

# Disparate Impact

A legal doctrine and statistical test for unintentional discrimination. Per [[mlsysbook-ch15-responsible-engineering|mlsysbook Vol 1 Ch 15]], it originates in *Griggs v. Duke Power Co.* (US Supreme Court, 1971), which held that practices "fair in form, but discriminatory in operation" violate civil rights law **even absent intent**.

## Disparate impact vs. disparate treatment
- **Disparate impact** — unintentional statistical harm. ML models routinely produce it through [[ProxyVariable|proxy variables]], creating liability even when engineers never encoded protected attributes.
- **Disparate treatment** — intentional discrimination.

## The four-fifths rule
Codified in the 1978 Uniform Guidelines on Employee Selection Procedures (EEOC, DoL, DoJ): a selection rate for any protected group below **80% of the highest group's rate** is prima facie evidence of adverse impact (if 60% of one group passes, ≥48% of any other group must pass). For ML systems this becomes automated monitoring that alerts when per-group selection ratios fall below 0.8 — a concrete threshold where most [[Fairness|fairness metrics]] stay qualitative.

## Connections
- [[Fairness]] / [[AlgorithmicBias]] — the broader property and failure mode.
- [[ProxyVariable]] — the mechanism that produces unintentional disparate impact.
- [[DemographicParity]] — the metric closest to the selection-rate test.
- [[EUAIAct]] / [[GDPR]] — modern regulatory layers atop sectoral anti-discrimination law.
- [[COMPAS]] — disparate impact in criminal-justice risk scoring.
- [[mlsysbook-ch15-responsible-engineering]] — source.
