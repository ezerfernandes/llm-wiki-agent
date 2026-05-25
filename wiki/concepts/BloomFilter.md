---
title: "Bloom Filter"
type: concept
tags: [data-structures, deduplication, hashing]
sources: [ai-engineering-ch08-dataset-engineering]
last_updated: 2024-12-04
---

# Bloom Filter

**A probabilistic data structure for fast set-membership testing with one-sided error (no false negatives; controllable false positives).** Per [[ai-engineering-ch08-dataset-engineering|*AI Engineering* Ch 8]], Bloom filters are one of the two standard hashing-dedup methods used at large scale alongside [[MinHashDeduplication|MinHash]].

## Why it's used for deduplication

Pairwise comparison is **O(n²)** — infeasible at web scale. Hashing-based methods are **O(n)**:

1. Hash each example into one or more positions in a fixed-size bit array.
2. To check if an example is already seen: hash it; check if all positions are set.
3. If yes, **probably** seen before (small false-positive rate).
4. If no, **definitely** not seen before.

The one-sided error makes Bloom filters perfect for "have we seen this before?" — false positives waste compute but never lose data.

## Tradeoffs

- **No false negatives** — every duplicate is caught.
- **False positives possible** — some unique examples may be discarded, controllable by tuning array size + hash count.
- **No deletes** — can't remove items (a Bloom filter is a one-way accumulator).
- **Memory-efficient** — fixed-size regardless of how many items inserted (with degrading false-positive rate).

## Where it's used

Per Ch 8:

> "Hash-related deduplication methods include MinHash and Bloom filter."

Also cited in the chapter footnote — [[ChipHuyen|Huyen]]'s own open-source library `lazyNLP` supports overlap estimation and dedup via Bloom filter.

## When to choose Bloom over MinHash

| Bloom Filter | MinHash |
|---|---|
| Exact-match dedup at scale | Near-duplicate detection (fuzzy match) |
| One bit per hash function | Multiple hash signatures + Jaccard |
| Set-membership query | Similarity score |

## Connections

- [[DataDeduplication]] — parent operation.
- [[MinHashDeduplication]] — sibling hashing-dedup technique (handles fuzzy dups; Bloom only handles exact).
- [[FuzzyMatching]] — adjacent for partial-match scenarios.
- [[ai-engineering-ch08-dataset-engineering]] — primary source.
