---
title: "Weak Supervision"
type: concept
tags: [ml-systems, mlsysbook, data-engineering, labeling]
sources: [mlsysbook-ch04-data-engineering]
last_updated: 2026-06-05
---

# Weak Supervision

A "data programming" labeling paradigm that replaces individual human annotations with **programmatic labeling functions** — rule-based heuristics, knowledge bases, and existing model outputs (Reddi, [[mlsysbook-ch04-data-engineering|Vol 1, Ch 4]]). It trades per-label accuracy for orders-of-magnitude throughput gains.

The motivating observation: domain experts write heuristic rules faster than they label examples. The cost trade-off is structural — manual labeling cost scales linearly with dataset size, whereas a labeling function involves upfront authoring effort and then labels millions of points at near-zero marginal cost. [[Snorkel]] is the canonical framework. Weak supervision sits below semi-supervised learning in the [[AIAssistedLabeling|AI-assisted labeling]] hierarchy (lower precision, higher abstraction level / throughput).

## Connections

- [[AIAssistedLabeling]] — the parent hierarchy.
- [[Snorkel]] — the canonical programmatic-labeling framework.
- [[SemiSupervisedLearning]] / [[ActiveLearning]] — sibling strategies.
- [[DataLabeling]] — the stage it scales.
- [[mlsysbook-ch04-data-engineering]] — source.
