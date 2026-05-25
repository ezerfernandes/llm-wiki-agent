---
title: "Vector Space Model"
type: concept
tags: [information-retrieval, ranking, similarity]
sources: [iir-ch06-vector-space-model, iir-ch07-complete-search-system, iir-ch14-vector-space-classification, iir-ch18-lsi-matrix-decompositions]
last_updated: 2026-05-23
---

Represents documents and queries as vectors in a |V|-dimensional term space — each axis is a vocabulary term, each component is a [[TermFrequency]]-weighted (typically [[TfIdf]]-weighted) value. Relevance is approximated by **cosine similarity** between the query vector and each document vector:

$$\text{sim}(q,d) = \frac{\vec{q}\cdot\vec{d}}{\|\vec{q}\|\,\|\vec{d}\|}$$

The cosine is length-invariant, which neutralizes the bias toward long documents that a raw dot product would have. Computation is the **COSINESCORE** algorithm: accumulate per-document score contributions through the [[InvertedIndex]] postings, normalize at the end, return top-K.

VSM is the workhorse ranker behind the entire pre-neural retrieval stack — see [[iir-ch06-vector-space-model]] for tf-idf variants, the [[SmartNotation]] `ddd.qqq` encoding, and [[PivotedLengthNormalization]]. It is the conceptual ancestor of modern dense vector retrieval ([[DenseRetrieval]], [[EmbeddingBasedRetrieval]]), with the difference that classical VSM uses lexical / sparse vectors while modern systems use learned dense embeddings.
