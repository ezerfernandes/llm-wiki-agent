---
title: "RAG-QA Arena (Tech)"
type: concept
tags: [dataset, rag, qa, benchmark, dspy]
sources: [dspy-rag-tutorial]
last_updated: 2026-05-22
---

# RAG-QA Arena (Tech)

The **"Tech"** split of the **RAG-QA Arena** benchmark (Han et al., 2024) — a long-form question-answering dataset over technical topics (programming, system administration, web development, networking) drawn from StackExchange-style sources. ~1,000 (question, gold-answer) pairs.

## Standard split used in [[dspy-rag-tutorial]]

| Split | Size | Role |
|---|---|---|
| Train | 200 | [[MIPROv2|MIPROv2]] training set + bootstrap-demo source |
| Dev | 300 | Metric tracking during optimization |
| Test | 500 | Held-out final evaluation |

Total ≈ **1,000** examples. The 200-train / 300-dev allocation is **~40/60** — closer to conventional ML splits than [[dspy-optimization-overview|the Optimization Overview's]] page-12-recommended **20/80** for prompt optimizers, but inside the same order of magnitude. Above the **30-example floor** for substantial-value optimization runs; below the **300-example target** for serious optimization.

## Companion retrieval corpus

The tutorial pairs the QA set with a **28,000-document downsampled technical corpus** — each document **truncated to 6,000 characters** for prompt-envelope discipline. Embeddings are pre-computed with [[openai|OpenAI]] `text-embedding-3-small`; top-`k=5` documents are retrieved per question.

## Performance envelope on this benchmark

| Program | [[SemanticF1]] |
|---|---|
| Baseline [[chainofthought|`dspy.ChainOfThought`]] (no retrieval) | ~42% |
| [[rag|RAG]] module (k=5 embedding retrieval + CoT) | ~55.5% |
| [[MIPROv2|MIPROv2]] `auto="medium"` over the RAG module | **~61.1%** |

The +13 / +6 split is the canonical wiki demonstration that **architecture (RAG)** buys more than **optimization** on a question-answering task that the bare LM cannot already do — but that optimization on top of architecture is additive.

## Position relative to other QA benchmarks in the wiki

| Benchmark | Domain | Size | Retrieval corpus | Wiki anchor |
|---|---|---|---|---|
| [[hotpotqa|HotPotQA]] | Wikipedia multi-hop | 113K | Wikipedia abstracts | [[hotpotqa]] |
| [[GSM8K]] | Math reasoning | 8.5K | — (no retrieval) | [[GSM8K]] |
| [[Banking77]] | Customer-service intent | 13K | — (classification) | [[dspy-optimizers]] |
| [[ArchEHRQA2025]] | Clinical EHR | ~150 cases | EHR notes | [[2025-bionlp-archehr-qa-neural]] |
| **RAG-QA Arena Tech** | **Technical / StackExchange-style** | **~1K** | **28K downsampled tech docs** | **this page** |
| [[AIME2025]] | Competition math | 30 problems | — | [[2507.19457-gepa]] |
| StackExchange (subset) | Q&A | (subset) | StackExchange | [[dspy-optimizers]] Receipt 2 |

RAG-QA Arena Tech is the wiki's **canonical small-scale long-form-QA benchmark** for DSPy RAG receipts — small enough to optimize end-to-end for ~$1.50 of LM cost, large enough to give a stable [[SemanticF1]] reading.

## Connections

- [[dspy-rag-tutorial]] — canonical worked source; the 42/55.5/61.1 progression that anchors the dataset in the wiki.
- [[rag|RAG]] — the application class this dataset is designed to evaluate.
- [[MIPROv2]] — the optimizer that lifts a single-hop CoT-based RAG on this dataset to ~61% [[SemanticF1]] in ~20–30 minutes for ~$1.50.
- [[SemanticF1]] — the metric used to score answers; reference-based [[llmasjudge|LLM-as-judge]] claim coverage.
- [[chainofthought|ChainOfThought]] — the baseline (no-retrieval) Module on this dataset; 42% [[SemanticF1]] floor.
- [[openai|OpenAI]] — provider for both the embedding model (`text-embedding-3-small`) and the generation model (`gpt-4o-mini`).
- [[DSPyData]] — the data discipline (plain `list[dspy.Example]`, train/dev/test as Python slices); RAG-QA Arena Tech is loaded the way every other DSPy dataset is.
- [[hotpotqa|HotPotQA]] — the **multi-hop Wikipedia** sibling benchmark; the [[dspy-optimizers|Optimizers page]]'s Receipt 1 dataset, paired with `dspy.ReAct` + `dspy.ColBERTv2` rather than embedding retrieval.
