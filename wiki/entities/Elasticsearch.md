---
title: "Elasticsearch"
type: entity
tags: [tool, search, retrieval, lucene, term-based]
sources: [ai-engineering-ch06-rag-agents]
last_updated: 2024-12-04
---

# Elasticsearch

**Elasticsearch** (Shay Banon, 2010) is the canonical open-source **term-based search engine**, built on top of [[Lucene]]. Per [[ai-engineering-ch06-rag-agents|*AI Engineering* Ch 6]], it is one of the *"two common term-based retrieval solutions"* alongside [[BM25]]; it uses an [[InvertedIndex|inverted index]] to map terms to documents and stores per-term document counts and term frequencies for fast [[TFIDF|TF-IDF]] / [[BM25]] scoring.

## Position in RAG production

Elasticsearch is the **default term-based retriever** in modern hybrid-search RAG pipelines. The standard pattern:

1. **Index documents** in Elasticsearch for term-based recall (BM25).
2. **Embed documents** into a [[VectorDatabase]] for semantic recall.
3. **[[HybridSearch|Combine]]** the two via [[ReciprocalRankFusion|RRF]] at query time.

## Why it endures

Per Huyen: *"BM25 and its variances (BM25+, BM25F) are still widely used in the industry and serve as formidable baselines to compare against modern, more sophisticated retrieval algorithms, such as embedding-based retrieval."* Elasticsearch is the production realization of those baselines — battle-tested at scale, with mature tokenization, stop-word handling, and language-specific analyzers.

## Connections

- [[Lucene]] — the search library Elasticsearch is built on.
- [[BM25]] / [[TFIDF]] — the scoring functions Elasticsearch implements.
- [[InvertedIndex]] — the data structure under the hood.
- [[TermBasedRetrieval]] — the retrieval family Elasticsearch anchors.
- [[HybridSearch]] — the production pattern Elasticsearch usually participates in.
- [[ElasticStack]] — the broader ELK product family (the existing wiki entry).
- [[rag]] — the application surface.
- [[ai-engineering-ch06-rag-agents]] — primary source.
