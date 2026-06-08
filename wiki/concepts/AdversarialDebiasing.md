---
name: AdversarialDebiasing
title: "Adversarial Debiasing"
type: concept
tags: [responsible-ai, fairness, bias-mitigation, training]
sources: [mlsysbook-ch15-responsible-engineering]
last_updated: 2026-06-05
---

# Adversarial Debiasing

An **in-processing** [[Fairness|fairness]]-mitigation technique that trains the primary model alongside an adversary which tries to predict the protected attribute from the model's representation; the primary model is penalized when the adversary succeeds, discouraging it from encoding group membership. Per [[mlsysbook-ch15-responsible-engineering|mlsysbook Vol 1 Ch 15]], the representation pressure can improve robustness to some distribution shifts but does **not** provide a general fairness guarantee under arbitrary deployment shift. Cost: typically **+20–50% training time and 1–3% accuracy reduction**.

It is one of three mitigation families, each with distinct trade-offs:
- **Preprocessing** — [[Reweighting|reweighting]] training samples.
- **In-processing** — adversarial debiasing, fairness constraints in the loss.
- **Postprocessing** — [[ThresholdAdjustment|threshold adjustment]] (per-group, no retraining).

## Connections
- [[Fairness]] — the property being enforced.
- [[Reweighting]] / [[ThresholdAdjustment]] — sibling mitigation families.
- [[ParetoFrontier]] — the fairness-accuracy trade-off it navigates.
- [[ProxyVariable]] — what it tries to prevent the model from reconstructing.
- [[mlsysbook-ch15-responsible-engineering]] — source.
