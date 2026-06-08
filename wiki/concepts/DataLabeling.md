---
title: "Data Labeling"
type: concept
tags: [ml-systems, mlsysbook, data-engineering, labeling, supervised-learning]
sources: [mlsysbook-ch04-data-engineering]
last_updated: 2026-06-05
---

# Data Labeling

Producing the **ground truth** that tells a supervised model what patterns to learn — "the most expensive, most human-dependent, and most error-prone stage of the entire pipeline" (Reddi, [[mlsysbook-ch04-data-engineering|Vol 1, Ch 4]]). Ground truth is a *proxy* for reality, not reality itself, so label-quality errors propagate silently into every downstream metric.

**Label types** scale in cost and storage: classification (1 scalar) → bounding box (4 coords/object, 10–20× slower to annotate than classification) → segmentation mask (~2.1M pixel labels for a 1080p image, ~50,000× more scalar entries than 10 boxes) → caption → transcription. Some fraction of labels is always wrong; the goal is to **measure and manage** error rates, not eliminate them.

**Quality control** uses consensus: collect 3–5 labels per example and compute Fleiss' κ (a multi-rater [[CohensKappa|Cohen's κ]]); route low-agreement cases (κ<0.4, often 5–15% of examples) to expert review. Experts cost 10–50× crowdsourcing, but forcing nonexpert majority votes on genuinely ambiguous cases produces systematically biased labels — hence **tiered escalation**. Scaling beyond manual work uses [[AIAssistedLabeling|AI-assisted labeling]] and automated [[ForcedAlignment|forced alignment]].

## Connections

- [[DataAnnotation]] — the FM-era labeling treatment (Huyen Ch 8).
- [[CohensKappa]] — inter-annotator agreement (and its Fleiss' κ generalization).
- [[AIAssistedLabeling]] / [[WeakSupervision]] / [[ActiveLearning]] — scaling strategies.
- [[ForcedAlignment]] — automated word-level labeling for KWS corpora.
- [[DataAcquisition]] — labeling as an acquisition channel.
- [[mlsysbook-ch04-data-engineering]] — source.
