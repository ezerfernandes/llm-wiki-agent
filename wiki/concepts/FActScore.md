---
title: "FActScore"
type: concept
tags: [evaluation, metric, factuality, llm, prior-art]
sources: [2507.03152-medval]
last_updated: 2026-05-22
---

# FActScore

**Fine-grained atomic evaluation of factual precision** in long-form text generation. Min, Krishna, Lyu, Lewis, Yih, Koh, Iyyer, Zettlemoyer & Hajishirzi, arXiv:2305.14251 (2023). Ref [30] in [[2507.03152-medval]].

## Mechanism

1. Decompose long-form generated text into **atomic facts** (single-claim units).
2. For each atomic fact, retrieve relevant evidence from a structured knowledge base (e.g. Wikipedia).
3. Score each atomic fact as supported / not-supported.
4. Aggregate to a precision score over the full generation.

## Why MedVAL contrasts itself with FActScore

[[2507.03152-medval]] (§4 Discussion) positions [[MedVAL]] as a successor that drops two FActScore constraints:
- **No domain-specific extractors needed.** FActScore relies on domain-specific atomic-fact extractors; MedVAL is end-to-end (input + output → risk grade + error list).
- **No structured knowledge base needed.** FActScore relies on KB lookup for evidence; MedVAL is reference-free.

The MedVAL paper acknowledges FActScore's value but situates it as part of the family of methods that "lack the necessary nuance for clinically focused error assessment" in medicine, where errors are often cloaked in jargon and the right-wrong continuum is graded.

## Connections

- [[2507.03152-medval]] — the paper that contrasts with FActScore.
- [[Hallucination]] — the failure mode FActScore was designed to detect.
- [[MedVAL]] — the successor framework for the medical domain.
- [[MedicalTextValidation]] — the task family.
- [[LLMAsAJudge]] — the parent paradigm.
