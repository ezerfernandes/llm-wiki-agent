---
title: "ArchEHR-QA 2025"
type: concept
tags: [benchmark, clinical-qa, ehr, mimic, bionlp, shared-task]
sources: [2025-bionlp-archehr-qa-neural]
last_updated: 2026-05-22
---

# ArchEHR-QA 2025

**Grounded clinical question answering shared task** at the [[BioNLP2025]] workshop, organized by [[SarveshSoni|Soni]] & [[DinaDemnerFushman|Demner-Fushman]] (NIH/NLM, 2025). Provides 120 question-note cases derived from [[MIMIC]]-III/IV; each case bundles a **patient question** (often layperson phrasing), a **clinician-rewritten question** focused on the medical query, and a **relevant excerpt from the patient's EHR notes**. Notes are pre-segmented into numbered sentences, each labeled `essential` / `supplementary` / `not-relevant` for the question.

**Official split:** 20 cases dev / 100 cases test (hidden, Codabench). Submissions evaluated along two axes — **Factuality** (strict + lenient precision/recall/F1 over cited sentence indices vs. expert-annotated essential / essential+supplementary sets) and **Relevance** (mean of [[bleu|BLEU]], [[ROUGE]], [[SARI]], [[BERTScore]], [[AlignScore]], [[MEDCON]]).

## Top submissions (2025 test set)

| Place | Team | Overall | Fact | Rel |
|---|---|---|---|---|
| 🥇 | [[DMISLab]] | 53.7 | 58.6 | 48.8 |
| 🥈 | [[Ours_Neural\|Neural ([[universityofchicago]])]] | 51.5 | 59.3 | 43.7 |
| 🥉 | [[LAILab]] | 51.0 | 60.4 | 41.6 |
| 4 | [[LAMAR_BioNLP\|LAMAR]] | 49.1 | 56.9 | 41.4 |
| 5 | ssagarwal | 45.0 | 47.5 | 42.6 |

## Why it matters

- **Supervised data is scarce** — 20 dev cases force any system to either generalize a frontier-LM prompt or fine-tune on near-nothing. The benchmark **biases toward prompt-optimization** (e.g. [[MIPROv2]]) and **few-shot in-context learning** over weight fine-tuning.
- **Sentence-level evidence labels** make decomposition viable. [[2025-bionlp-archehr-qa-neural|Neural]] splits the task into evidence ID + answer synthesis; F1 on the first stage and composite reward on the second are independently optimizable.
- **The strict vs. lenient distinction matters.** Strict counts only `essential` citations; lenient also accepts `supplementary`. Systems that over-cite get penalized on precision; under-citing systems lose recall.

## Connections

- [[2025-bionlp-archehr-qa-neural]] — runner-up submission; [[MIPROv2]]-optimized two-stage pipeline on [[GPT4_1|GPT-4.1]].
- [[BioNLP2025]] — the workshop.
- [[SarveshSoni]] / [[DinaDemnerFushman]] — task organizers.
- [[MIMIC]] — source EHR corpus.
- [[emrQA]] — predecessor clinical-QA dataset (Pampari et al. 2018).
- [[EvidenceGroundedQA]] — the QA paradigm this task instantiates.
- [[F1Score]] / [[bleu|BLEU]] / [[ROUGE]] / [[SARI]] / [[BERTScore]] / [[AlignScore]] / [[MEDCON]] — evaluation metrics.
