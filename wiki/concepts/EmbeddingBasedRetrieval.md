---
title: "Embedding-Based Retrieval"
type: concept
tags: [retrieval, search, rag, embeddings, vector-search]
sources: [ai-engineering-ch06-rag-agents, hands-on-llm-ch08-semantic-search-and-rag]
last_updated: 2026-05-23
---

# Embedding-Based Retrieval

**Embedding-based retrieval** (a.k.a. *semantic retrieval*, *dense retrieval*) is the [[rag|RAG]] retrieval family that ranks documents by **how closely their meanings align with the query**, rather than by lexical term match. Per [[ChipHuyen|Huyen]] in [[ai-engineering-ch06-rag-agents|*AI Engineering* Ch 6]], it solves the term-ambiguity failure mode of [[TermBasedRetrieval|term-based retrieval]] (querying *"transformer architecture"* returning movie/electric-device results) by operating in a learned vector space where semantic neighbors are geometric neighbors.

## The two-step workflow

1. **Embedding model**: convert the query into an embedding using the *same* model used for indexing — see [[TrainingServingSkew]] for what happens if you don't.
2. **Retriever**: fetch `k` data chunks whose embeddings are closest to the query embedding in the [[VectorDatabase]], as determined by an [[ApproximateNearestNeighbor|ANN]] algorithm.

Real-world implementations add **rerankers** (a cheap-fetch-then-expensive-rerank sequencing) and **caches** to keep the embedding-generation latency manageable.

## Why it costs more than [[TermBasedRetrieval|term-based]]

- **Embedding generation**: every chunk needs an embedding at index time, every query needs one at query time.
- **Vector storage** is denser than inverted indexes for a comparable corpus.
- **Vector search** is computationally heavier than inverted-index lookup, especially without ANN.
- *"It's not uncommon to see a company's vector database spending be one-fifth or even half of their spending on model APIs."*

## The keyword-obscuration trade-off

Embedding-based retrieval can **obscure specific keywords** like error codes (`EADDRNOTAVAIL (99)`) or product names — they are absorbed into a continuous space where exact-match signal is lost. The standard fix is [[HybridSearch|hybrid search]]: combine embedding-based with term-based so the term-based path catches exact-keyword queries.

## Why use it anyway

- **Improvement headroom**: unlike [[TermBasedRetrieval|term-based]], embedding-based can be finetuned — embedding model, retriever, and (jointly) generator can all be improved over time.
- **Natural-language queries**: focuses on semantics, so users can phrase queries colloquially.
- **Multimodality**: a shared [[CLIP]]-style embedding space enables [[MultimodalRAG|cross-modal retrieval]] (text query → image results) at all.

## Connections

- [[rag]] — the application family.
- [[Embedding]] — the substrate.
- [[VectorDatabase]] — the storage layer.
- [[ApproximateNearestNeighbor]] — the speed mechanism.
- [[CLIP]] — the canonical multimodal embedding model for [[MultimodalRAG]].
- [[MTEB]] — the embedding-quality benchmark Huyen names for evaluation.
- [[TermBasedRetrieval]] — the complementary family.
- [[HybridSearch]] — the production-standard combination.
- [[ReRanking]] — the standard post-step.
- [[ai-engineering-ch06-rag-agents]] — primary source.
- [[hands-on-llm-ch08-semantic-search-and-rag]] — Ch 8's name for the same architectural family is *"dense retrieval"* — see [[DenseRetrieval]].
- [[DenseRetrieval]] — the wiki's Ch 8-aliased page for this concept.
- [[SemanticSearch]] — the user-facing name.

## Vocabulary note

The same architectural family has **three concept pages** in the wiki — each named for a different framing tradition:

| Page | Framing | Source |
|---|---|---|
| **[[EmbeddingBasedRetrieval]]** (this page) | Embedding-model substrate | [[ai-engineering-ch06-rag-agents|Huyen Ch 6]] |
| **[[DenseRetrieval]]** | Vector-space geometry | [[hands-on-llm-ch08-semantic-search-and-rag|Ch 8]] |
| **[[SemanticSearch]]** | User-facing capability | Both sources |

All three refer to the same family — embed query + documents, find nearest neighbors. The wiki keeps all three pages because each name resolves cleanly to the originating source's framing.
