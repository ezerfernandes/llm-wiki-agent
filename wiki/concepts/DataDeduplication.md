---
title: "Data Deduplication"
type: concept
tags: [llm-engineering]
sources: [leh-ch05-supervised-fine-tuning, ai-engineering-ch08-dataset-engineering]
last_updated: 2024-12-04
---

## Definition
Removing duplicate / near-duplicate samples from training data.

## In LLM Engineer's Handbook
Three flavors per [[leh-ch05-supervised-fine-tuning]]: exact deduplication (normalize -> hash MD5/SHA-256 -> drop dups); fuzzy via [[MinHashDeduplication]] (compact signature vectors -> Jaccard similarity); [[SemanticSimilarityDedup|semantic similarity]] (embed text, compute cosine/Euclidean distance, cluster). Prevents overfitting, biased performance, inefficient training, and inflated eval metrics.

## From [[ai-engineering-ch08-dataset-engineering|AI Engineering Ch 8]]

### The Anthropic finding

[[ChipHuyen|Huyen]] in Ch 8 cites Hernandez et al. (2022, [[anthropic|Anthropic]]):

> "Repeating 0.1% of the data 100 times can cause an 800M parameter model's performance to degrade to that of a 400M parameter model despite the other 90% of the training tokens remaining unique."

So even small amounts of duplication can have **size-equivalent** degradation effects — a powerful argument for why dedup pipelines need to run on every training corpus, not just web-scraped ones.

### Why dedup is non-trivial

Per Ch 8, several kinds of duplication exist:

- **Whole document duplications** — same document twice.
- **Intra-document duplications** — same paragraph twice within one doc.
- **Cross-document duplications** — same quote in many docs.

And the definition of "duplicate" varies: document / paragraph / sentence / token; exact match vs 80% overlap; ordered lists vs unordered lists with same items.

### Three Ch 8 deduplication methods

| Method | Description |
|---|---|
| **Pairwise comparison** | O(n²); compute similarity (exact / n-gram / fuzzy / semantic) for every pair |
| **Hashing** | Bucket via hash; only compare within bucket. [[MinHashDeduplication\|MinHash]] + [[BloomFilter\|Bloom filters]] |
| **Dimensionality reduction** | Embed, reduce dims, then pairwise compare — vector-search-style |

### Tools named in Ch 8

dupeGuru, Dedupe, datasketch, TextDistance, TheFuzz, deduplicate-text-datasets. [[ChipHuyen|Huyen]]'s own lazyNLP supports Bloom-filter overlap estimation (footnote).

### Dedup vs [[DataContamination|data contamination]]

Duplicates can cause **test-set contamination** when splitting data into train/test: one copy lands in train, another in test, inflating eval scores. Dedup is a structural defense against this leakage.
