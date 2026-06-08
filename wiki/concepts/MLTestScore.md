---
title: "ML Test Score"
type: concept
tags: [mlops, testing, technical-debt, production-readiness]
sources: [mlsysbook-ch14-ml-operations]
last_updated: 2026-06-05
---

# ML Test Score

A systematic rubric (Breck et al. 2017) for evaluating production readiness of ML systems and quantifying [[TechnicalDebt|technical debt]]. It defines **28 tests** grouped into four sections of seven tests each:

- **Data tests** — feature expectations captured in schema, all features beneficial, no feature whose cost exceeds its benefit, privacy controls.
- **Model tests** — model spec reviewed/version-controlled, offline-online metric correlation, all hyperparameters tuned, staleness bounded.
- **Infrastructure tests** — reproducible training, rollback capability, training-serving consistency tested, validation gates before serving.
- **Monitoring tests** — alerts on dependency changes, data invariants hold, no training-serving skew, staleness triggers retraining.

Readiness is tracked **by section, not by grand total**: a system with strong model tests but weak monitoring still carries production risk. Quarterly audits prioritizing the most frequent incident types reveal where operational investment yields the highest reliability gains.

Discussed in [[mlsysbook-ch14-ml-operations]] (mlsysbook Vol 1, Ch 14).

## Connections
- [[TechnicalDebt]] — the rubric makes ML debt explicit.
- [[OperationalMaturity]] — complements maturity assessment (practices vs. integration).
- [[TrainingServingSkew]] / [[ModelMonitoring]] / [[DataQuality]] — categories it tests.
- [[GreatExpectations]] / [[TensorFlowExtended]] — implementation tools for data tests.
- [[mlsysbook-ch14-ml-operations]] — source chapter.
