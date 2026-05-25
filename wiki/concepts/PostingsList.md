---
title: "Postings List"
type: concept
tags: [information-retrieval, inverted-index, data-structure]
sources: [iir-ch01-boolean-retrieval, iir-ch02-term-vocabulary-postings, iir-ch04-index-construction, iir-ch05-index-compression]
last_updated: 2026-05-23
---

For each term in the dictionary, the sorted list of document IDs (and optionally positions, frequencies, or zone tags) in which that term occurs. Postings lists are the per-term arrays that make up the [[InvertedIndex]] — together with the dictionary, they enable efficient term-keyed lookup over the entire collection.

**Layout variants**:
- **Document-only**: $\langle \text{term}, \text{df}_t; \text{docID}_1, \text{docID}_2, \ldots \rangle$ — minimal, supports Boolean and tf-idf scoring.
- **Frequency-augmented**: $\langle \text{term}, \text{df}_t; (\text{docID}_1, \text{tf}_1), (\text{docID}_2, \text{tf}_2), \ldots \rangle$ — needed for ranked retrieval.
- **[[PositionalIndex]]**: $\langle \text{term}, \text{df}_t; (\text{docID}_1, \text{tf}_1, [p_{1,1}, p_{1,2}, \ldots]), \ldots \rangle$ — required for phrase / proximity queries.

**Key operations**:
- **Intersection** of two postings lists (Boolean AND): two-pointer merge in $O(x+y)$, accelerated with [[SkipPointer|skip pointers]] placed at $\sqrt{P}$ intervals.
- **Union** (Boolean OR): also two-pointer merge.
- **Score accumulation**: traverse postings, accumulate per-doc tf-idf contributions for [[VectorSpaceModel]] / [[BM25]] scoring.

**Compression**: postings are stored as **gap-encoded** docID deltas, then encoded with [[VariableByteCode]] (byte-aligned, fast decode) or [[GammaCode]] (bit-aligned, smaller) — see [[iir-ch05-index-compression]] for ~2.5× reduction on Reuters-RCV1.

**Ordering**:
- **docID-sorted**: standard, enables intersection.
- **Impact-ordered**: sorted by weight descending — supports [[ImpactOrdering|impact-ordered]] early termination.
- **Tier-partitioned**: split into tiers by static quality score (see [[TieredIndex]]).
