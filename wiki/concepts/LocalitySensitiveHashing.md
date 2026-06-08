---
title: "Locality-Sensitive Hashing (LSH)"
type: concept
tags: [ml-systems, data-selection, deduplication, mlsysbook]
sources: [mlsysbook-ch09-data-selection]
last_updated: 2026-06-05
---

# Locality-Sensitive Hashing (LSH)

A probabilistic bucketing technique for fast approximate similarity search, used in [[DataDeduplication|near-duplicate detection]] ([[mlsysbook-ch09-data-selection|Reddi Ch 9]]). LSH hashes [[MinHash]] document fingerprints into buckets such that **similar fingerprints are highly likely to collide**, avoiding the quadratic cost of comparing every document pair. This shifts deduplication from an infeasible $\mathcal{O}(D^2)$ toward a manageable $\mathcal{O}(D)$. The core trade-off: tuning for higher recall (fewer missed duplicates) by using more hash functions raises compute cost.

## Connections

- [[DataDeduplication]] — the optimization LSH enables; [[MinHash]] — the fingerprints it buckets.
- [[JaccardSimilarity]] — the similarity LSH+MinHash approximates.
- [[FAISS]] — production ANN infrastructure for embedding-based selection.
- [[mlsysbook-ch09-data-selection]] — source.
