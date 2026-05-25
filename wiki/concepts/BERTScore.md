---
title: "BERTScore"
type: concept
tags: [evaluation, metric, nlp, semantic-similarity]
sources: [2025-bionlp-archehr-qa-neural, 2507.03152-medval, hands-on-llm-ch12-fine-tuning-generation-models]
last_updated: 2026-05-24
---

# BERTScore

Automatic generation-evaluation metric ([[TianyiZhang|Zhang]], Kishore, Wu, Weinberger & Artzi, ICLR 2020). Computes pairwise cosine similarity between contextual [[bert|BERT]] embeddings of candidate and reference tokens, then aggregates via greedy matching into precision / recall / F1. Captures **semantic similarity** in ways [[bleu|BLEU]] / [[ROUGE]] miss (paraphrase, synonymy), at the cost of model-dependence (the embedding model matters) and higher compute.

Used in the relevance-side reward composite for [[2025-bionlp-archehr-qa-neural|ArchEHR-QA 2025 (Neural)]] alongside [[bleu|BLEU]] / [[ROUGE]] / [[SARI]] / [[AlignScore]] / [[MEDCON]].

## Position vs MedVAL — weak physician correlation

[[2507.03152-medval|MedVAL (Aali et al. 2026)]] §3.7 measures Pearson correlation between metrics and physician risk grades on a 190-example radiology subset. **BERTScore F1 correlates with physicians at $r = 0.141$ — weak.** For comparison: [[AlignScore]] $r = 0.678$, MedVAL GPT-4o $r = 0.825$, MedVAL Qwen3-4B $r = 0.833$. The MedVAL paper uses this as evidence that **embedding-based surface similarity is not a faithful proxy for reference-free clinical risk grading** — BERTScore is sensitive to embedding-space neighborhood but blind to clinically-load-bearing distinctions like *"no pleural effusion"* vs *"small pleural effusion"* when surface forms are similar.

## Connections
- [[TianyiZhang]] — first author.
- [[bert|BERT]] — the embedding substrate.
- [[bleu|BLEU]] / [[ROUGE]] / [[SARI]] / [[AlignScore]] / [[MEDCON]] — sibling generation metrics.
- [[2025-bionlp-archehr-qa-neural]] — application: relevance reward component.
- [[2507.03152-medval]] — physician-correlation benchmark; BERTScore is weak ($r = 0.141$).
- [[MedVAL]] — the reference-free successor.

## From [[hands-on-llm-ch12-fine-tuning-generation-models|Hands-On LLMs Ch 12]]

Ch 12 of *Hands-On LLMs* names BERTScore (Zhang et al. 2019) as one of **four canonical word-level metrics** for evaluating generative LLMs — alongside [[Perplexity]] (Jelinek et al. 1977), [[ROUGE]] (Lin 2004), and [[bleu|BLEU]] (Papineni et al. 2002). The chapter's framing:

> *"They do not account for consistency, fluency, creativity, or even correctness of the generated text."* — Ch 12, on the limitations of word-level metrics

Ch 12 positions BERTScore alongside its overlap-based siblings as **classic token-level metrics comparing reference vs generated text** — useful but insufficient on their own, motivating the chapter's downstream sections on public benchmarks, [[LLMAsAJudge|LLM-as-a-judge]], and human evaluation via [[ChatbotArena|Chatbot Arena]].
