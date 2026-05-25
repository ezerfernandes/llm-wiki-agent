---
title: "AlignScore"
type: concept
tags: [evaluation, metric, nlp, factual-consistency]
sources: [2025-bionlp-archehr-qa-neural, 2507.03152-medval]
last_updated: 2026-05-22
---

# AlignScore

Factual-consistency evaluation metric (Zha, Yang, Li & Hu, arXiv:2305.16739, 2023). Uses a **unified alignment function** trained on a large diverse alignment corpus to score whether a candidate generation is supported by a given source text. Designed to be **task-agnostic** — works across summarization, dialogue, QA — and to be more semantically faithful than [[bleu|BLEU]] / [[ROUGE]] for factuality-sensitive applications.

Used as the **factual-consistency** component of the relevance reward in [[2025-bionlp-archehr-qa-neural|ArchEHR-QA 2025 (Neural)]] — appropriate for clinical QA where surface lexical overlap (BLEU) under-rates correct medical paraphrases.

## Position vs MedVAL

[[2507.03152-medval|MedVAL (Aali et al. 2026)]] §3.7 directly benchmarks AlignScore against MedVAL on a `report2impression` subset ($n = 190$) using Pearson correlation with physician risk grades. **AlignScore reaches $r = 0.678$** — moderate but **substantially weaker than MedVAL** ($r = 0.825$ for GPT-4o, $r = 0.833$ for Qwen3-4B). The MedVAL paper concludes: *"Reference-based similarity is not a faithful proxy for reference-free, input-only clinical risk grading."* AlignScore is the **strongest reference-based prior-art baseline** the MedVAL paper compares against — its dependence on a reference output is a structural ceiling MedVAL is built to clear.

## Connections
- [[BERTScore]] / [[MEDCON]] / [[bleu|BLEU]] / [[ROUGE]] / [[SARI]] — sibling generation metrics.
- [[2025-bionlp-archehr-qa-neural]] — application: factual-alignment reward component.
- [[2507.03152-medval]] — benchmark comparison; MedVAL outperforms AlignScore on physician-correlation.
- [[MedVAL]] — the reference-free successor that MedVAL §3.7 shows correlates more strongly with physicians.
- [[EvidenceGroundedQA]] — task family this metric was designed to support.
