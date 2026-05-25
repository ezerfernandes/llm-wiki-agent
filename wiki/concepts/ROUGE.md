---
title: "ROUGE"
type: concept
tags: [evaluation, metric, summarization]
sources: [2025-bionlp-archehr-qa-neural, 2507.03152-medval, hands-on-llm-ch12-fine-tuning-generation-models]
last_updated: 2026-05-24
---

# ROUGE

**Recall-Oriented Understudy for Gisting Evaluation** — family of overlap-based summarization metrics (Lin, *Text Summarization Branches Out*, ACL 2004). Most-used variants:
- **ROUGE-N** — n-gram recall of reference against candidate.
- **ROUGE-L** — longest common subsequence based F1.
- **ROUGE-Lsum** — sentence-level ROUGE-L summed; the variant reported in the [[ArchEHRQA2025]] table.

Recall-biased complement to precision-biased [[bleu|BLEU]]. Known limitations: surface lexical overlap, poor with paraphrases, n-gram-length blind.

Used as the **lexical-overlap** component of the relevance reward in [[2025-bionlp-archehr-qa-neural|ArchEHR-QA 2025 (Neural)]] alongside [[bleu|BLEU]] / [[SARI]] / [[BERTScore]] / [[AlignScore]] / [[MEDCON]].

## Position vs MedVAL — weak physician correlation

[[2507.03152-medval|MedVAL (Aali et al. 2026)]] §3.7 reports ROUGE-L Pearson correlation with physician risk grades at $r = 0.259$ on a 190-example radiology subset — **weak**. Compares against [[AlignScore]] ($r = 0.678$) and MedVAL itself ($r = 0.825$ for GPT-4o). The MedVAL paper uses ROUGE as the surface-overlap floor against which embedding ([[BERTScore]]) and learned-alignment ([[AlignScore]]) metrics improve, but all three reference-based metrics remain decisively weaker than the reference-free MedVAL on physician correlation.

## Connections
- [[bleu|BLEU]] — precision-biased sibling.
- [[BERTScore]] — embedding-based semantic alternative.
- [[AlignScore]] — learned-alignment alternative; stronger physician correlation but still beaten by MedVAL.
- [[2025-bionlp-archehr-qa-neural]] — application.
- [[2507.03152-medval]] — physician-correlation benchmark; ROUGE-L is weak ($r = 0.259$).
- [[MedVAL]] — reference-free successor.

## From [[hands-on-llm-ch12-fine-tuning-generation-models|Hands-On LLMs Ch 12]]

Ch 12 of *Hands-On LLMs* names ROUGE (Lin 2004) as one of **four canonical word-level metrics** for generative-LLM evaluation — alongside [[Perplexity]], [[bleu|BLEU]], and [[BERTScore]]. The chapter's framing: ROUGE is a *"classic token-level metric comparing reference vs generated text"* but does *"not account for consistency, fluency, creativity, or even correctness of the generated text"* — motivating Ch 12's pivot to public benchmarks, LLM-as-a-judge, and human evaluation as more capable downstream eval methodologies.
