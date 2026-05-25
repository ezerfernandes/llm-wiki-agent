---
title: "Semantic Similarity Deduplication"
type: concept
tags: [llm-engineering]
sources: [leh-ch05-supervised-fine-tuning]
last_updated: 2026-05-22
---

## Definition
Embedding-based near-duplicate detection.

## In LLM Engineer's Handbook
Semantic similarity deduplication embeds text with [[Word2Vec]] / [[GloVe]] / [[FastText]] (word-level) or [[bert|BERT]] / sentence-transformers / cross-encoders (sentence-level), computes cosine or Euclidean distance, and optionally clusters (K-means / DBSCAN / hierarchical) to keep one representative per cluster. Per [[leh-ch05-supervised-fine-tuning]] it complements exact and [[MinHashDeduplication|MinHash]] dedup for the long tail of near-duplicates that lexical methods miss.
