---
title: "Hybrid Search"
type: concept
tags: [llm-engineering]
sources: [leh-ch04-rag-feature-pipeline, leh-ch09-rag-inference-pipeline, ai-engineering-ch06-rag-agents, hands-on-llm-ch08-semantic-search-and-rag]
last_updated: 2026-05-23
---

## Definition
Retrieval strategy fusing dense vector (semantic) search with sparse keyword (BM25) search.

## In LLM Engineer's Handbook
Hybrid search runs vector and keyword retrievers in parallel and blends normalized scores via a weighted sum (or reciprocal rank fusion). Per [[leh-ch04-rag-feature-pipeline]] and [[leh-ch09-rag-inference-pipeline]], it combines semantic recall on paraphrases with exact-match precision on technical terms; the `alpha` weight is the tuning knob.

## From [[ai-engineering-ch06-rag-agents|AI Engineering Ch 6]]

[[ChipHuyen|Huyen]] develops hybrid search as **two distinct combination patterns**:

1. **Sequential combination** (cheap-then-expensive): a cheap, less-precise retriever (typically [[TermBasedRetrieval|term-based]] / [[BM25]]) fetches a candidate set; a more-precise but more-expensive mechanism ([[EmbeddingBasedRetrieval|embedding-based]] with k-NN) reranks the candidates. *"This second step is also called reranking."* Concrete example: query *"transformer"* → BM25 fetches all transformer documents → embedding search finds the ones about neural architectures (not movies or electric devices).

2. **Parallel combination** (ensemble): multiple retrievers fetch candidates **at the same time**, then [[ReciprocalRankFusion|reciprocal rank fusion (RRF)]] (Cormack et al. 2009) combines the rankings. The RRF formula gives a document its final score as the sum, over retrievers, of `1 / (k + rank_i)` with `k=60` typical.

The hybrid pattern is Huyen's structural answer to the embedding-vs-term trade-off: term-based retrievers obscure exact-keyword signals (error codes, product names) that embedding retrievers lose, while embedding retrievers handle semantic paraphrasing that term-based misses. Running both — sequentially or in parallel — captures both signals.

## From [[hands-on-llm-ch08-semantic-search-and-rag|*Hands-On LLMs* Ch 8]]

Ch 8 names hybrid search as **the structural answer to dense retrieval's exact-phrase weakness**:

> *"Another caveat of dense retrieval is when a user wants to find an exact match for a specific phrase. That's a case that's perfect for keyword matching. That's one reason why **hybrid search**, which includes both semantic search and keyword search, is advised instead of relying solely on dense retrieval."* — Ch 8

This is **consistent with Huyen Ch 6's two-pattern decomposition** (sequential cheap-then-expensive + parallel ensemble). The Ch 8 framing is shorter — *hybrid search is the production default* — without the full RRF mechanism walk. The reader should read this page's Huyen Ch 6 section for the sequential-vs-parallel patterns and [[ReciprocalRankFusion|RRF]] for the parallel-combination algorithm.

Ch 8's worked example demonstrates **the sequential pattern** in its keyword-search + rerank pipeline ([[BM25]] first-stage → [[CohereRerank|`co.rerank`]] second-stage) — see [[ReRanking]] for the worked code.
