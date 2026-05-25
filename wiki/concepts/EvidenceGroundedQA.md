---
title: "Evidence-Grounded QA"
type: concept
tags: [qa, retrieval, citation, grounded-generation]
sources: [2025-bionlp-archehr-qa-neural]
last_updated: 2026-05-22
---

# Evidence-Grounded QA

QA paradigm where **every claim in the answer must cite a supporting span from a provided source document**. Systems are scored along two complementary axes:

1. **Factuality / citation correctness** — does the cited evidence actually support the claim? Operationalized as precision / recall / F1 of the cited-span set against an expert-annotated gold-evidence set.
2. **Relevance / answer quality** — is the synthesized answer fluent, complete, on-topic? Operationalized via surface metrics ([[bleu|BLEU]], [[ROUGE]], [[SARI]]) + semantic metrics ([[BERTScore]], [[AlignScore]]) + domain-specific concept-coverage ([[MEDCON]] for clinical).

Distinct from open-domain QA (no fixed evidence corpus) and reading-comprehension QA (no required citation). The [[ArchEHRQA2025]] shared task is the canonical clinical instance; [[2025-bionlp-archehr-qa-neural|Reddy et al. 2025]] decompose the task into separately-optimized **evidence retrieval** and **answer synthesis** stages — a natural fit for [[LMProgram|multi-stage LM programs]] and [[MIPROv2|MIPROv2]]-style per-stage prompt optimization.

## Connections
- [[ArchEHRQA2025]] — canonical clinical instance.
- [[2025-bionlp-archehr-qa-neural]] — decomposed two-stage MIPROv2 pipeline.
- [[emrQA]] — earlier large-scale clinical-QA dataset.
- [[LMProgram]] — natural target abstraction.
- [[MIPROv2]] — per-stage prompt optimizer fit.
- [[AlignScore]] / [[MEDCON]] — factual-consistency metrics designed for this paradigm.
