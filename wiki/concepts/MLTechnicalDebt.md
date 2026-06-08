---
title: "ML Technical Debt"
type: concept
tags: [ml-systems, mlsysbook, mlops, maintainability, foundations]
sources: [mlsysbook-ch03-ml-workflow]
last_updated: 2026-06-05
---

# ML Technical Debt

ML systems accumulate technical debt **faster** than traditional software through three mechanisms (Reddi, [[mlsysbook-ch03-ml-workflow|Vol 1, Ch 3]], building on Sculley et al.'s "Hidden Technical Debt in ML Systems"):

- **Entanglement** — changing one feature affects all others, because the model learned joint distributions ("Changing Anything Changes Everything").
- **Hidden feedback loops** — predictions influence the future training data.
- **Undeclared consumers** — downstream systems depend on model outputs without contracts.

The systems consequence: **ML code is less than 5% of a production system**; the remaining ~95% (configuration, pipelines, infrastructure) is where debt compounds silently, which is why late-discovered constraints propagate so expensively. Reproducibility makes the debt diagnosable: without lineage tracking, a team cannot tell whether a 2% accuracy regression came from a code change, a data change, or a random seed.

## Connections

- [[ConstraintPropagationPrinciple]] — debt is what makes late discoveries expensive.
- [[DataCascade]] — debt propagation through data-quality channels.
- [[TechnicalDebt]] — the general software concept.
- [[Reproducibility]] / [[DataLineage]] / [[ExperimentTracking]] — the disciplines that bound the debt.
- [[MLOps]] — where the 95% of non-model system lives.
- [[mlsysbook-ch03-ml-workflow]] — source.
