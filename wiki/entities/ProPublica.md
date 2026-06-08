---
title: "ProPublica"
type: entity
tags: [responsible-ai, fairness, journalism, audit]
sources: [mlsysbook-ch15-responsible-engineering]
last_updated: 2026-06-05
---

# ProPublica

ProPublica is a nonprofit investigative-journalism organization whose 2016 "Machine Bias" investigation (Angwin, Larson, Mattu & Kirchner) audited the [[COMPAS]] recidivism-scoring tool — a foundational external algorithmic audit cited in [[mlsysbook-ch15-responsible-engineering|mlsysbook Vol 1 Ch 15]].

## Why it matters here
- ProPublica's analysis showed COMPAS satisfied **calibration** yet violated [[EqualizedOdds|equalized odds]]: Black defendants who did not re-offend were flagged high-risk at nearly 2× the White rate.
- The investigation became the empirical case behind the **Impossibility Theorem of Fairness** and a model for independent, data-driven accountability journalism on ML systems.

## Connections
- [[COMPAS]] — the system it audited.
- [[EqualizedOdds]] / [[Fairness]] — the criteria its analysis exposed.
- [[AlgorithmicBias]] / [[DisparateImpact]] — the harm documented.
- [[mlsysbook-ch15-responsible-engineering]] — source.
