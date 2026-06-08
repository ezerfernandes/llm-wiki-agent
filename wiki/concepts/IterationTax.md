---
title: "Iteration Tax"
type: concept
tags: [ml-systems, mlsysbook, workflow, iteration-velocity, foundations]
sources: [mlsysbook-ch03-ml-workflow]
last_updated: 2026-06-05
---

# Iteration Tax

The compounding cost of **slow iteration**: a system whose development loop is slow loses, over time, to one whose loop is fast — even if the slow system starts from a better model (Reddi, [[mlsysbook-ch03-ml-workflow|Vol 1, Ch 3]]). The chapter's worked example: over a 26-week window, a large model at **1 experiment/week** (start 95%, +0.15 pp/iter, diminishing returns) reaches ~98.9%, while a lightweight model iterating **hourly** (start 90%, +0.1 pp/iter, capped at ~100 effective experiments) reaches the 99% ceiling. Rapid cycles create far more chances to discover better architectures, data augmentations, and hyperparameters.

> "Iteration velocity is a feature. A system that allows ten experiments/day will almost always eventually outperform a system that allows one experiment/week, even if the latter starts with a better model."

This explains why fast-iterating startups often out-execute larger teams bound by slow, rigid pipelines, and why investment in iteration infrastructure (job scheduling, caching, early stopping, automated resource optimization) recovers its cost within a few experiment cycles. Iteration velocity is therefore a **systems feature**, not merely a productivity metric.

## Connections

- [[MLWorkflow]] — the discipline that prizes iteration velocity.
- [[ConstraintPropagationPrinciple]] — the complementary law (cost of *late* discovery vs. cost of *slow* iteration).
- [[ExperimentTracking]] / [[Reproducibility]] — prerequisites for trustworthy fast iteration.
- [[mlsysbook-ch03-ml-workflow]] — source.
