---
title: "MIRACL"
type: entity
tags: [benchmark, retrieval, multilingual, ir, ranking]
sources: [hands-on-llm-ch08-semantic-search-and-rag]
last_updated: 2026-05-23
---

# MIRACL

**MIRACL** (Multilingual Information Retrieval Across a Continuum of Languages) is a multilingual retrieval benchmark covering 18 typologically diverse languages over Wikipedia corpora; queries and relevance judgments are produced by native speakers. Standard scoring is **[[NDCG|nDCG@10]]**.

## From [[hands-on-llm-ch08-semantic-search-and-rag|*Hands-On LLMs* Ch 8]]

Ch 8 uses MIRACL as the source for **the chapter's headline reranker-efficacy claim**:

> *"On a multilingual benchmark like MIRACL, a reranker can boost performance from 36.5 to 62.8, measured as nDCG@10 (more on evaluation later in this chapter)."*

The 36.5 → 62.8 nDCG@10 jump is **almost a 2× lift** from adding a [[ReRanking|reranker]] on top of [[BM25]] — the wiki's first concrete reranker-lift number on a public benchmark. Cited in Ch 8's reranking section after the keyword-search + rerank worked pipeline on the *Interstellar* corpus.

## Why MIRACL matters

MIRACL is the **production-grade multilingual analogue** of mono-lingual benchmarks like [[MSMARCO|MS MARCO]] / [[BEIRBenchmark|BEIR]] — the harder benchmark because:
- 18 languages including under-resourced ones (Arabic, Bengali, Hindi, Swahili, Telugu, Thai, Yoruba, Indonesian).
- Native-speaker query construction (no machine-translated queries).
- Wikipedia-grounded ground-truth passages.

Strong retrievers must work cross-lingually, not just on English; this is why MIRACL is the benchmark Ch 8 cites to demonstrate reranking lift.

## Connections

- [[ReRanking]] — the system component whose lift MIRACL is used to demonstrate.
- [[CrossEncoder]] / [[MonoBERT]] — the reranker architecture being measured.
- [[NDCG]] — the reporting metric (nDCG@10).
- [[BM25]] — the first-stage baseline the reranker improves upon.
- [[HybridSearch]] — natural production target whose lift MIRACL can be used to measure.
- [[CohereRerank]] — the worked reranker in Ch 8.
- [[hands-on-llm-ch08-semantic-search-and-rag]] — primary source.
