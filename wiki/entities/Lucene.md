---
title: "Lucene"
type: entity
tags: [tool, search, retrieval, ir, library]
sources: [ai-engineering-ch06-rag-agents]
last_updated: 2024-12-04
---

# Lucene

**Apache Lucene** is the open-source **full-text search library** that underlies most production term-based retrieval systems, most notably [[Elasticsearch]] (Shay Banon 2010, built on top of Lucene). Lucene provides the [[InvertedIndex|inverted index]] data structures, [[BM25]] / [[TFIDF|TF-IDF]] scoring, query parsing, and tokenization analyzers that higher-level search systems package.

## Position in the IR ecosystem

| Layer | Component |
|---|---|
| **Library** | Lucene |
| **Search engine** | [[Elasticsearch]], Apache Solr, OpenSearch |
| **Application** | RAG retrievers, log analytics, e-commerce search |

Lucene is to search what FAISS is to vector ANN — the **library**, not the database. [[Elasticsearch]] adds the database layer (REST API, sharding, replication, cluster management) on top of Lucene's library primitives.

## Connections

- [[Elasticsearch]] — the most prominent system built on Lucene.
- [[InvertedIndex]] — Lucene's central data structure.
- [[BM25]] / [[TFIDF]] — Lucene's scoring functions.
- [[TermBasedRetrieval]] — the retrieval family Lucene serves.
- [[FAISS]] — the structural analog in the vector-search world.
- [[ai-engineering-ch06-rag-agents]] — primary source.
