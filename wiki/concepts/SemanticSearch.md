---
title: "Semantic Search"
type: concept
tags: [search, retrieval, embeddings, dense-retrieval, llm, rag]
sources: [hands-on-llm-ch08-semantic-search-and-rag, ai-engineering-ch06-rag-agents]
last_updated: 2026-05-23
---

# Semantic Search

**Semantic search** is the **user-facing name** for search systems that rank documents **by meaning rather than by keyword overlap**. Ch 8 of *Hands-On LLMs* introduces the term as the capability that LLMs add to traditional search:

> *"The ability they add is called semantic search, which enables searching by meaning, and not simply keyword matching."* — Ch 8

The architectural family that powers semantic search is **[[DenseRetrieval|dense retrieval]]** (a.k.a. [[EmbeddingBasedRetrieval|embedding-based retrieval]]) — embed the query and the documents in a shared vector space; return the nearest documents.

## The historical anchor

Ch 8 opens with the **2018-BERT-Google-Search adoption story** as the historical pivot point:

> *"Search was one of the first language model applications to see broad industry adoption. Months after the release of the seminal 'BERT: Pre-training of deep bidirectional transformers for language understanding' (2018) paper, Google announced it was using it to power Google Search and that it represented 'one of the biggest leaps forward in the history of Search.' Not to be outdone, Microsoft Bing also stated that 'Starting from April of this year, we used large transformer models to deliver the largest quality improvements to our Bing customers in the past year.'"* — Ch 8

The **first industrial-scale LLM adoption was search**, not chat. Generative-search products like [[Perplexity]] / Microsoft Bing AI / [[gemini|Gemini]] came years later.

## The keyword-search contrast

Ch 8's canonical demonstration is on the **15-sentence Wikipedia *Interstellar* corpus**: the query *"how precise was the science"* returns the **correct** *"praise from many astronomers for its scientific accuracy and portrayal of theoretical astrophysics"* via semantic search but the **wrong** *"Interstellar is a 2014 epic science fiction film..."* via [[BM25|BM25 keyword search]] (which over-weights the literal word *"science"*).

> *"Notice that this wouldn't have been possible if we were only doing keyword search because the top result did not include the same keywords in the query."* — Ch 8

This is the **canonical motivating contrast** for why semantic search exists alongside keyword search.

## When keyword search still wins

Per Ch 8: *"another caveat of dense retrieval is when a user wants to find an exact match for a specific phrase. That's a case that's perfect for keyword matching. That's one reason why hybrid search, which includes both semantic search and keyword search, is advised instead of relying solely on dense retrieval."*

Three structural cases where keyword search wins:

1. **Exact-phrase queries** — error codes (`EADDRNOTAVAIL`), product SKUs, named entities.
2. **Out-of-distribution queries** — semantic search returns nearest-but-irrelevant (cf. [[SimilarityThreshold]]).
3. **Low-resource domains** — semantic-search embedding models trained on Wikipedia perform poorly on legal / medical / code corpora.

[[HybridSearch|Hybrid search]] is the production-default that captures both signals.

## Position in the wiki

Three concept pages overlap on the same architectural family:

- **[[SemanticSearch]]** (this page) — the **user-facing name**: *"searching by meaning."*
- **[[DenseRetrieval]]** — Ch 8's name; emphasizes the vector-space geometry.
- **[[EmbeddingBasedRetrieval]]** — Huyen Ch 6's name; emphasizes the embedding-model substrate.

All three point at the same architectural family; the differences are framing and lineage.

## Connections

- [[DenseRetrieval]] / [[EmbeddingBasedRetrieval]] — the wiki's other names for the architectural family.
- [[rag]] — the application that pairs semantic search with grounded generation.
- [[BM25]] / [[SparseRetrieval]] / [[TermBasedRetrieval]] — the complementary keyword-search family.
- [[HybridSearch]] — the production-default combination.
- [[ReRanking]] — the standard post-step.
- [[Embedding]] / [[SentenceTransformers]] — the substrate.
- [[FAISS]] / [[VectorDatabase]] / [[ApproximateNearestNeighbor]] — the storage / speed layer.
- [[SemanticSimilarity]] — the underlying scoring mechanism.
- [[google|Google]] / [[microsoft|Microsoft]] — the 2018-2019 adopters Ch 8 names.
- [[bert|BERT]] — the 2018 model that enabled the first wave of semantic search.
- [[hands-on-llm-ch08-semantic-search-and-rag]] — primary source.
- [[ai-engineering-ch06-rag-agents]] — secondary source.
