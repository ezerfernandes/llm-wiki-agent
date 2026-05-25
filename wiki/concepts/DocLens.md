---
title: "DocLens"
type: concept
tags: [evaluation, metric, medical-nlp, prior-art, stub]
sources: [2507.03152-medval]
last_updated: 2026-05-22
---

# DocLens

**Multi-aspect fine-grained evaluation for medical text generation** — Xie, Zhang, Cheng et al., arXiv:2311.09581 (2023). Ref [36] in [[2507.03152-medval]].

Introduces three metrics for medical text generation:
- **Completeness** — how much of the required information appears.
- **Conciseness** — the inverse, surface compression.
- **Attribution** — whether generated claims are grounded in the source.

Reports higher physician-assessment agreement than prior generic metrics, but **relies on the availability of reference outputs**. [[2507.03152-medval]] §4 contrasts MedVAL as reference-free and broader-tasked.

## Connections
- [[2507.03152-medval]] — the paper that contrasts with DocLens.
- [[MedVAL]] — the reference-free successor.
- [[BERTScore]] / [[ROUGE]] — sibling reference-based generation metrics.
- [[MedicalTextValidation]] — the parent task family.
