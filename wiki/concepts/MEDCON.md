---
title: "MEDCON"
type: concept
tags: [evaluation, metric, clinical-nlp, medical-concept-coverage]
sources: [2025-bionlp-archehr-qa-neural]
last_updated: 2026-05-22
---

# MEDCON

Medical-concept-coverage metric introduced with the AciBench corpus ([[WenwaiYim|Yim]], Fu, Ben Abacha, Snider, Lin & Yetisgen, *Scientific Data* 10(1):586, 2023). Extracts the set of medical concepts (UMLS-mapped) in candidate vs. reference generations and reports F1 over the concept sets. The clinical-NLP-domain analogue of [[BERTScore]] — measures **medical-concept overlap** rather than generic token / embedding overlap, so it stays sensitive to clinically-load-bearing terms even when phrasing diverges.

Used as the **medical-concept-coverage** component of the relevance reward in [[2025-bionlp-archehr-qa-neural|ArchEHR-QA 2025 (Neural)]].

## Connections
- [[BERTScore]] / [[AlignScore]] / [[bleu|BLEU]] / [[ROUGE]] / [[SARI]] — sibling generation metrics.
- [[2025-bionlp-archehr-qa-neural]] — application: medical-concept reward component.
- [[WenwaiYim]] — first author of the AciBench paper.
