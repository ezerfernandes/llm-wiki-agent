---
title: "Ablation Study"
type: concept
tags: [evaluation, experimentation, methodology, mlsysbook]
sources: [mlsysbook-ch03-ml-workflow]
last_updated: 2026-06-05
---

# Ablation Study

Named for surgical tissue removal, an ablation study **systematically disables individual components** to isolate each one's contribution to performance (Reddi, [[mlsysbook-ch03-ml-workflow|Vol 1, Ch 3]]).

The rigor matters because in high-stakes ML a **0.5% accuracy difference** can determine whether a model meets its clinical sensitivity threshold. Without ablation (and the surrounding scientific methodology — fixed random seeds, environment versioning, confounding-factor analysis, paired significance tests), a team cannot distinguish a genuine architectural improvement from noise introduced by a different random seed, wasting [[IterationTax|iteration]] cycles on phantom gains.

## Connections

- [[Reproducibility]] / [[ExperimentTracking]] — preconditions for trustworthy ablations.
- [[IterationTax]] — phantom gains waste the iteration budget.
- [[ABTesting]] — the live-traffic counterpart to offline paired tests.
- [[mlsysbook-ch03-ml-workflow]] — source.
