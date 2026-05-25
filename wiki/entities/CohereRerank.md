---
title: "Cohere Rerank"
type: entity
tags: [api, endpoint, cohere, reranking, cross-encoder, search]
sources: [hands-on-llm-ch08-semantic-search-and-rag]
last_updated: 2026-05-23
---

# Cohere Rerank

The `co.rerank` endpoint of the [[Cohere]] managed API — a **plug-and-play [[CrossEncoder|cross-encoder]] reranker** for search pipelines. Takes a query + list of documents + `top_n`; returns the documents reordered by relevance with per-document relevance scores in [0, 1].

## From [[hands-on-llm-ch08-semantic-search-and-rag|*Hands-On LLMs* Ch 8]]

Ch 8 uses `co.rerank` as the **worked reranking primitive** in the chapter's reranking section:

> *"Cohere's Rerank endpoint is a simple way to start using a first reranker. We simply pass it the query and texts and get the results back. We don't need to train or tune it."*

The minimal-API surface:

```python
results = co.rerank(query=query, documents=texts, top_n=3, return_documents=True)
for idx, result in enumerate(results.results):
    print(idx, result.relevance_score, result.document.text)
```

On the *Interstellar* corpus with the query *"how precise was the science"*, `co.rerank` assigns **0.1698** to the correct *"praise from astronomers for scientific accuracy"* sentence and ≤ **0.07** to all others — *"much more confident about the first result."*

## The two-stage search pipeline pattern

Ch 8's keyword-then-rerank pipeline uses `co.rerank` as the **second stage** after [[BM25]] retrieves a top-10 candidate set:

```python
def keyword_and_reranking_search(query, top_k=3, num_candidates=10):
    bm25_hits = bm25.get_scores(...)  # first stage
    docs = [texts[hit['corpus_id']] for hit in bm25_hits]
    results = co.rerank(query=query, documents=docs, top_n=top_k, return_documents=True)
```

On *"how precise was the science"*, this pipeline **elevates the correct sentence to position 1** even though BM25 had ranked it at position 2 — the canonical Ch 8 demonstration of rerank-on-top-of-keyword-search.

## Headline efficacy claim

Per Ch 8: *"On a multilingual benchmark like [[MIRACL]], a reranker can boost performance from 36.5 to 62.8, measured as [[NDCG|nDCG@10]]"* — almost a **2× lift** from adding a reranker on top of BM25. This is the wiki's anchor for *what reranking is worth*.

## Connections

- [[Cohere]] — the parent API provider.
- [[CohereChat]] / [[CohereEmbed]] — sibling endpoints in the same managed-RAG stack.
- [[CrossEncoder]] — the underlying mechanism (`co.rerank` is a managed cross-encoder).
- [[ReRanking]] — the technique family.
- [[MonoBERT]] — the reference cross-encoder architecture.
- [[MIRACL]] — the benchmark Ch 8 quotes for the efficacy claim.
- [[BM25]] — the canonical first-stage retriever paired with rerank.
- [[HybridSearch]] — the production-default first-stage pattern.
- [[SentenceTransformers]] — the open-source alternative (sentence-transformers' Retrieve & Re-Rank module).
- [[hands-on-llm-ch08-semantic-search-and-rag]] — primary source.
