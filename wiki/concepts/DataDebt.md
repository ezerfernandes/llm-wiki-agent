---
title: "Data Debt"
type: concept
tags: [ml-systems, mlsysbook, data-engineering, technical-debt, mlops]
sources: [mlsysbook-ch04-data-engineering]
last_updated: 2026-06-05
---

# Data Debt

The "compound interest of implicit coupling and missing documentation across the data stack" (Reddi, [[mlsysbook-ch04-data-engineering|Vol 1, Ch 4]]). Unlike code/technical debt — which manifests as slower development velocity — **data debt manifests as lower model accuracy even when the code is perfectly maintained**. It is a systems-architecture failure: the assumptions of the training distribution are no longer enforced at the system boundary.

Four categories:

- **Documentation debt** — unrecorded provenance, meaning, quality (missing data cards, unlabeled columns).
- **Schema debt** — accumulated workarounds (multiple date handlers, scattered null checks, version-specific parsing branches).
- **Quality debt** — known-but-uncorrected errors; a 3%-label-error dataset poisons every retrain, amplifying via feedback loops.
- **Freshness debt** — training distribution diverging from production over time (silent, gradual).

It compounds superlinearly: $\text{Debt}_n \approx \text{Debt}_0 (1+r)^n$ with $r$ ≈ 10–30%/period. Metric thresholds (warning/critical): data cards <80%/<50%; schema branches >3/>10; label error >1%/>5%; days since retrain >90/>365; [[PopulationStabilityIndex|PSI]] >0.1/>0.25. Remediation is budgeted, not heroic: documentation sprints (20/80 by usage), schema contracts ([[GreatExpectations|Great Expectations]]/Pandera), ~10% capacity for quality burn-down, and drift-triggered retraining. *Strategic* (conscious) debt is rational; *unconscious* untracked debt is the danger.

## Connections

- [[MLTechnicalDebt]] — the code-side analogue (Sculley et al.'s hidden technical debt).
- [[DataDrift]] / [[PopulationStabilityIndex]] — freshness-debt detection.
- [[DataQuality]] / [[DataLineage]] / [[DataGovernance]] — what the debt categories erode.
- [[FourPillarsOfDataEngineering]] — the framework debt accumulates against.
- [[mlsysbook-ch04-data-engineering]] — source.
