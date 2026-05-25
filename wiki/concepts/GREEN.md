---
title: "GREEN"
type: concept
tags: [evaluation, metric, radiology, medical-nlp, prior-art]
sources: [2507.03152-medval]
last_updated: 2026-05-22
---

# GREEN — Generative Radiology Report Evaluation and Error Notation

Ostmeier, Xu, Chen, Varma, Blankemeier, Bluethgen, Michalson, Moseley, Langlotz & Chaudhari, arXiv:2405.03595 (2024). Ref [40] in [[2507.03152-medval]]. Notably shares **multiple authors with MedVAL** ([[ChristianBluethgen|Bluethgen]], [[CurtisLangloo|Langlotz]], [[AkshayChaudhari|Chaudhari]], Sophie Ostmeier, Maya Varma) — same Stanford research lineage.

## Scope

Generative evaluation method specifically for **radiology reports** — identifies significant errors and produces an error notation that radiologists can interpret. Operates on reference-output-based comparison of generated vs ground-truth reports.

## Relation to MedVAL

[[2507.03152-medval]] (§4 Discussion) positions GREEN as **radiology-only prior art** that MedVAL generalizes beyond. While GREEN provides high-fidelity error notation for chest X-ray reports, it **relies on reference outputs** and is **restricted to one sub-specialty**.

MedVAL extends the same research-lab line of thinking into:
- **6 diverse tasks**, only 3 of which are radiology (report2impression, impression2simplified, report2simplified).
- **Reference-free** validation using only the input.
- **Multilingual** ($bhc2spanish$ — English → Spanish translation).

## Connections

- [[2507.03152-medval]] — the successor framework.
- [[ChristianBluethgen]] / [[CurtisLangloo]] / [[AkshayChaudhari]] — co-authors of both GREEN and MedVAL.
- [[MedVAL]] — the cross-specialty successor.
- [[ReXTrust]] / [[ReXErr]] / [[FineRadScore]] — sibling radiology-only error-evaluation prior art.
- [[Openi]] / [[MIMICIV]] — the radiology data sources MedVAL inherits from this lineage.
