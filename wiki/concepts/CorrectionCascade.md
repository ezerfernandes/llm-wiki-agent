---
title: "Correction Cascade"
type: concept
tags: [mlops, technical-debt, model-dependencies]
sources: [mlsysbook-ch14-ml-operations]
last_updated: 2026-06-05
---

# Correction Cascade

An ML [[TechnicalDebt|technical-debt]] pattern in which fixing one component introduces problems elsewhere, requiring additional fixes that themselves cause further problems. In ML systems these cascades are severe because changes propagate through *statistical* dependencies rather than explicit code paths: retraining to fix one failure mode degrades previously working cases; adjusting thresholds to cut false positives raises false negatives; adding features introduces destabilizing correlations.

A common source is sequential model development — reusing or fine-tuning existing models embeds earlier assumptions (feature encodings, labeling criteria) as implicit constraints on future models. Mitigation balances reuse against redesign: loose coupling, clear version boundaries, and design for independent evolution.

**Canonical failure:** [[Zillow]]'s Zestimate iBuying venture — valuation errors propagated into purchasing decisions; retroactive corrections triggered systemic instability requiring full rollback; iBuying shut down 2021 (> $500M losses, ~2,000 layoffs).

Defined in [[mlsysbook-ch14-ml-operations]] (mlsysbook Vol 1, Ch 14), following Sculley et al. 2015.

## Connections
- [[TechnicalDebt]] — parent pattern family.
- [[BoundaryErosion]] — sibling pattern (the *how* of structural decay; cascades are the *what* of repair).
- [[FeedbackLoop]] — related self-reinforcing dynamic.
- [[Zillow]] — the canonical case study.
- [[mlsysbook-ch14-ml-operations]] — source chapter.
