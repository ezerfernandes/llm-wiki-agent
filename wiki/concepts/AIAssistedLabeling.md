---
title: "AI-Assisted Labeling"
type: concept
tags: [ml-systems, mlsysbook, data-engineering, labeling, scalability]
sources: [mlsysbook-ch04-data-engineering]
last_updated: 2026-06-05
---

# AI-Assisted Labeling

Using automation as a **force multiplier** for human [[DataLabeling|labeling]] — handling clear cases automatically while preserving human judgment for ambiguous or high-stakes ones (Reddi, [[mlsysbook-ch04-data-engineering|Vol 1, Ch 4]]). It occupies the space between fully manual annotation (max precision, min throughput) and fully automated labeling (lacks nuanced judgment).

The decision hierarchy trades precision for throughput: **traditional supervision → [[SemiSupervisedLearning|semi-supervised learning]] → [[WeakSupervision|weak supervision]] ([[Snorkel]] labeling functions) → [[TransferLearning|transfer learning]]**, with [[ActiveLearning|active learning]] as the cost-saving alternative. Three primary mechanisms:

- **Pre-annotation** — AI generates preliminary labels humans verify/correct (cuts manual effort 50–80% for many CV tasks).
- **Weak supervision** — programmatic labeling functions ([[Snorkel]]) generate labels at scale.
- **LLM labeling** — rich descriptions and explained reasoning, but $0.01–$1/example, 100–10,000 req/min limits, and a need for output validation.

Quality control monitors model confidence calibration (95% reported confidence but 75% actual accuracy misleads reviewers) and human-AI agreement rates. The common pattern across domains is **tiered escalation**: automation handles clear cases, humans handle ambiguous ones, monitoring keeps the boundary adaptive.

## Connections

- [[DataLabeling]] — the parent stage.
- [[WeakSupervision]] / [[SemiSupervisedLearning]] / [[TransferLearning]] / [[ActiveLearning]] — the strategy hierarchy.
- [[Snorkel]] — the canonical weak-supervision framework.
- [[mlsysbook-ch04-data-engineering]] — source.
