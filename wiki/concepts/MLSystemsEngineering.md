---
title: "ML Systems Engineering"
type: concept
tags: [ml-systems, discipline, ai-engineering, mlsysbook, foundations]
sources: [mlsysbook-ch01-introduction]
last_updated: 2026-06-05
---

# ML Systems Engineering

Reddi's *Machine Learning Systems* ([[mlsysbook-ch01-introduction|Vol 1, Ch 1]]) defines **AI Engineering** (used interchangeably with *ML systems engineering*) as:

> the engineering discipline of designing, deploying, and maintaining systems whose outputs are inherently probabilistic (stochastic) to meet deterministic reliability targets by simultaneously satisfying constraints on all three [[DAMTaxonomy|D·A·M]] axes (Data quality, Algorithm correctness, Machine efficiency) in production.

## How it differs from ML research

- **ML research** optimizes a *single* objective (validation loss) on a *static* dataset — primarily the Algorithm axis.
- **ML systems engineering** jointly optimizes a *multi-objective constraint surface* (latency, throughput, accuracy, cost, fairness, robustness) on a distribution that *shifts continuously after deployment*. A 95%-accurate model that violates a 100 ms p99 SLO is a **failed system**.

It is **not** "software engineering for ML": the system spec is probabilistic (statistically valid vs. a shifting distribution, not correct vs. a fixed contract), making continuous monitoring a *structural* requirement. The discipline mirrors how **Computer Engineering** formalized (Case Western, 1971) to bridge EE and CS — neither field alone addresses the integrated challenge under latency, power, and data-quality budgets.

> Note: this systems-physics definition is broader than [[ChipHuyen|Chip Huyen]]'s [[AIEngineering|"AI Engineering"]] (building applications on foundation models). See that page for the scope comparison.

## Connections

- [[DAMTaxonomy]] — the three axes the discipline balances.
- [[AIEngineering]] — the narrower foundation-model-application sense.
- [[IronLawOfMLSystems]] / [[EfficiencyFramework]] — its quantitative tools.
- [[FivePillarFramework]] — its operational structure.
- [[MachineLearningSystems]] — the systems it builds.
- [[mlsysbook-ch01-introduction]] — source.
