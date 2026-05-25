---
title: "Relevance Judgment"
type: concept
tags: [evaluation, retrieval, ir, annotation, ground-truth]
sources: [hands-on-llm-ch08-semantic-search-and-rag]
last_updated: 2026-05-23
---

# Relevance Judgment

**Relevance judgments** are the human-annotated ground-truth labels that tell a retrieval evaluation system **which documents are relevant for which queries**. The third component (alongside a text archive and a set of queries) that Ch 8 of *Hands-On LLMs* names as required for IR evaluation:

> *"Evaluating search systems needs three major components: a text archive, a set of queries, and relevance judgments indicating which documents are relevant for each query."* — Ch 8

## The annotation bottleneck

Relevance judgments are **expensive** because they require human annotators to read both the query and each candidate document and label the relevance. For a benchmark with 1,000 queries × 1,000 candidates each = **1 million labeling decisions**. Two mitigations the IR field has converged on:

1. **Pooling** — only label the top-k documents returned by a set of *participating systems*. Any document not in the pool is assumed irrelevant (with caveats — *"hole in the pool"* unjudged-document bias).

2. **Graded relevance** — instead of binary relevant/not, use a 3-5-level scale (e.g., *perfectly relevant / highly relevant / fairly relevant / marginally relevant / not relevant*). Graded judgments power [[NDCG|nDCG]].

## Position relative to dataset construction

Relevance judgments are the **labeled-data** component of an IR benchmark, parallel to:

- **Train/test queries** — the questions to be answered.
- **Document corpus** — the searchable archive.
- **Relevance judgments** — the (query, doc, label) triples.

[[MSMARCO|MS MARCO]], [[MIRACL]], [[BEIRBenchmark|BEIR]], TREC tracks — all production-grade IR benchmarks are organized around these three components.

## Why this matters for [[rag|RAG]] evaluation

[[rag|RAG]] systems inherit IR's relevance-judgment requirement for **retrieval-side evaluation** ([[MAP]] / [[NDCG]] / [[MRR]] / [[PrecisionAtK|P@k]]). The generation-side axes ([[Fluency]] / [[PerceivedUtility]] / [[CitationRecall]] / [[CitationPrecision]]) require **different annotations** — generated-answer judgments rather than retrieved-document judgments. This is part of the structural reason [[RAGEvaluation|RAG evaluation]] needs multiple axes; no single annotation effort covers everything.

## Connections

- [[InformationRetrieval]] — the parent field.
- [[MAP]] / [[NDCG]] / [[MRR]] / [[PrecisionAtK]] — the metrics relevance judgments enable.
- [[MSMARCO]] / [[MIRACL]] / [[BEIRBenchmark]] — benchmarks built on relevance judgments.
- [[AnnotationGuidelines]] — the discipline of writing instructions for human annotators producing relevance judgments.
- [[RAGEvaluation]] — the broader evaluation surface relevance judgments contribute to.
- [[hands-on-llm-ch08-semantic-search-and-rag]] — primary source.
