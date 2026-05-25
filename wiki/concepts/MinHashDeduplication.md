---
title: "MinHash Deduplication"
type: concept
tags: [llm-engineering]
sources: [leh-ch05-supervised-fine-tuning, ai-engineering-ch08-dataset-engineering]
last_updated: 2024-12-04
---

## Definition
Fuzzy deduplication algorithm using min-hash signatures + Jaccard similarity.

## In LLM Engineer's Handbook
MinHash compresses text into a set of shingles, applies multiple hash functions, keeps the minimum hash per function as a signature vector, and compares signatures with Jaccard similarity. Per [[leh-ch05-supervised-fine-tuning]] it is the standard fuzzy dedup tool — the default at web-corpus scale (CCNet, FineWeb, RedPajama).

## From [[ai-engineering-ch08-dataset-engineering|AI Engineering Ch 8]]

Ch 8 places MinHash alongside [[BloomFilter|Bloom filters]] as one of the two standard hashing-based dedup techniques — both scale to web-corpus size where pairwise comparison (O(n²)) is infeasible:

> "Hash examples into different buckets and check only among examples that fall into the same bucket. Hash-related deduplication methods include MinHash and Bloom filter."

### When to choose MinHash over Bloom

| MinHash | Bloom Filter |
|---|---|
| **Near-duplicate** detection (fuzzy match) | **Exact-match** dedup |
| Multiple hash signatures + Jaccard score | Single bit per hash position |
| Continuous similarity score | Boolean membership |
| O(n) with fixed-rate accuracy | O(n) with one-sided error |

The choice depends on whether you need fuzzy matching (use MinHash) or just exact-duplicate filtering (Bloom is cheaper).
