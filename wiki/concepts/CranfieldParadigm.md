---
title: "Cranfield Paradigm"
type: concept
tags: [information-retrieval, evaluation, test-collection, methodology]
sources: [iir-ch08-ir-evaluation]
last_updated: 2026-05-23
---

The standard methodology for offline IR evaluation, originating with Cyril Cleverdon's Cranfield experiments (1966) at the College of Aeronautics, Cranfield. A **test collection** consists of three components:

1. A **document corpus** — a fixed set of documents.
2. A **query set** (also called the **topic set**) — a fixed set of information needs, typically with a topic-statement format (title + description + narrative).
3. **Relevance judgments** (**qrels**) — for each (query, document) pair in the judging pool, a human-assigned label indicating whether the document is relevant.

A retrieval system is then evaluated by running each query against the corpus and computing metrics ([[MeanAveragePrecision|MAP]], [[NDCG]], precision@K, recall, $F_\beta$) from the run + qrels. **Reproducible**, **comparable across systems**, **insensitive to user behavior on the day** — the methodology that turned IR from a craft into a science.

**Pooling**: relevance judgments cannot cover all (query, doc) pairs in a large corpus, so TREC-style evaluation pools the top-$K$ results from many participating systems and judges only that union. Documents outside the pool are presumed non-relevant. This biases against retrieval methods that find non-pooled relevant docs — a well-known limitation.

**Successor benchmarks** under the same paradigm: TREC (since 1992), CLEF (multilingual European), NTCIR (Japan/Korea/Chinese), FIRE (Indian languages), [[INEX]] (XML retrieval), MS MARCO (web-scale, weak labels). Full discussion of test collections and the kappa coefficient for inter-judge agreement in [[iir-ch08-ir-evaluation]].
