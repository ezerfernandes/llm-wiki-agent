---
name: Reweighting
title: "Reweighting (Bias Mitigation)"
type: concept
tags: [responsible-ai, fairness, bias-mitigation, training]
sources: [mlsysbook-ch15-responsible-engineering]
last_updated: 2026-06-05
---

# Reweighting (Bias Mitigation)

A **preprocessing** [[Fairness|fairness]]-mitigation technique rooted in importance sampling: samples from an underrepresented group receive higher loss weights during training, amplifying their influence on gradient updates **without removing any data**. Per [[mlsysbook-ch15-responsible-engineering|mlsysbook Vol 1 Ch 15]], Kamiran & Calders (2011) proved appropriately chosen weights can eliminate disparate impact from training data. Systems trade-off: shifting the loss landscape can reduce majority-group accuracy by **1–3%** to close disparity gaps — evaluated against the [[ParetoFrontier|Pareto frontier]].

## Connections
- [[Fairness]] / [[DisparateImpact]] — what it mitigates.
- [[AdversarialDebiasing]] / [[ThresholdAdjustment]] — sibling mitigation families (in- and post-processing).
- [[ParetoFrontier]] — the accuracy cost frame.
- [[mlsysbook-ch15-responsible-engineering]] — source.
