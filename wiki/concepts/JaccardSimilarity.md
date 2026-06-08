---
title: "Jaccard Similarity"
type: concept
tags: [ml-systems, data-selection, deduplication, metric, mlsysbook]
sources: [mlsysbook-ch09-data-selection]
last_updated: 2026-06-05
---

# Jaccard Similarity

A set-overlap metric $J(A,B)=|A\cap B|/|A\cup B|$, ranging from 0 (disjoint) to 1 (identical), used in [[DataDeduplication|near-duplicate detection]] for text ([[mlsysbook-ch09-data-selection|Reddi Ch 9]]). Its set-based formulation handles documents of different lengths without normalization. The **practical threshold matters**: a threshold above ~0.8 catches near-duplicates while preserving legitimately similar-but-distinct content, but lowering it below ~0.5 risks collapsing topically related documents and reducing dataset diversity. Estimated efficiently at scale via [[MinHash]]+[[LocalitySensitiveHashing|LSH]].

## Connections

- [[DataDeduplication]] — the application; [[MinHash]] / [[LocalitySensitiveHashing]] — efficient estimators.
- [[mlsysbook-ch09-data-selection]] — source.
