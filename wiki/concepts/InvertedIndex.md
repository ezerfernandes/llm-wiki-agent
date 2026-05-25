---
title: "Inverted Index"
type: concept
tags: [retrieval, search, ir, data-structure]
sources: [ai-engineering-ch06-rag-agents]
last_updated: 2024-12-04
---

# Inverted Index

An **inverted index** is the data structure under [[TermBasedRetrieval|term-based retrieval]] systems — a dictionary that maps from **terms to documents that contain them**, instead of from documents to their terms (which would be the *forward* index). Per [[ai-engineering-ch06-rag-agents|*AI Engineering* Ch 6]], the inverted index is what makes [[Elasticsearch]] and [[Lucene]] capable of millisecond-latency keyword search over millions of documents.

## Example

| Term | Document count | (Document index, term frequency) for all documents containing the term |
|---|---|---|
| banana | 2 | (10, 3), (5, 2) |
| machine | 4 | (1, 5), (10, 1), (38, 9), (42, 5) |
| learning | 3 | (1, 5), (38, 7), (42, 5) |

For each term, the index typically stores: **document count** (used to compute the [[TFIDF|IDF]] denominator) and a list of `(document index, term frequency)` tuples (used to compute the [[TFIDF|TF]] component of the score). With these two fields, [[TFIDF|TF-IDF]] / [[BM25]] scoring across the whole corpus reduces to a single look-up per query term.

## Why it scales

A query *"machine learning"* on a billion-document corpus does not scan a billion documents; it looks up two postings lists and merges them. This is the structural reason term-based retrieval is *"much faster than embedding-based retrieval during both indexing and query"* (Ch 6).

## Connections

- [[TermBasedRetrieval]] — the retrieval family inverted indexes support.
- [[Elasticsearch]] / [[Lucene]] — production implementations.
- [[BM25]] / [[TFIDF]] — scoring functions evaluated against the index.
- [[rag]] — modern application.
- [[ai-engineering-ch06-rag-agents]] — primary source.
