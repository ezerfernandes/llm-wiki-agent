---
name: AlgorithmicBias
title: "Algorithmic Bias"
type: concept
tags: [responsible-ai, fairness, bias, ethics]
sources: [mlsysbook-ch15-responsible-engineering]
last_updated: 2026-06-05
---

# Algorithmic Bias

Systematic, unfair disparity in an ML system's outputs across groups, arising when a model "faithfully learns and reproduces whatever patterns exist in its training distribution, including patterns of historical injustice that no one intended to encode" ([[mlsysbook-ch15-responsible-engineering|mlsysbook Vol 1 Ch 15]]). The model is not malfunctioning — it optimizes a flawed specification correctly (verification passes, validation fails).

## Sources of bias (D·A·M)
- **Data axis** — biased historical signal (e.g. [[Amazon]]'s 2014 recruiting tool trained on ~10 years of mostly-male resumes; the "Fuel" is corrupted).
- **Algorithm axis** — a proxy objective that optimizes for harm (e.g. engagement → polarization; the "Blueprint").
- See [[DAMTaxonomy|D·A·M taxonomy]] for the diagnostic framework.

## Why it is hard to remove
- Removing protected attributes is insufficient: models reconstruct them from [[ProxyVariable|proxy variables]] (ZIP code ↔ race, names ↔ gender, cost ↔ need) at **70–90% accuracy** — "fairness laundering."
- It manifests as [[DisparateImpact|disparate impact]] (unintentional statistical harm) even absent discriminatory intent — legal liability under *Griggs v. Duke Power* / the four-fifths rule.
- Detection requires [[DisaggregatedEvaluation|disaggregated evaluation]]; [[GenderShades|Gender Shades]] showed >43× error disparity hidden by aggregate accuracy.

## Connections
- [[Fairness]] — the property bias violates.
- [[ProxyVariable]] — the mechanism that defeats attribute removal.
- [[DisparateImpact]] — the legal/statistical framing.
- [[FeedbackLoop]] / [[GoodhartsLaw]] — amplification mechanisms.
- [[COMPAS]] / [[GenderShades]] — canonical bias case studies.
- [[ResponsibleAI]] — the broader practice.
- [[mlsysbook-ch15-responsible-engineering]] — source.
