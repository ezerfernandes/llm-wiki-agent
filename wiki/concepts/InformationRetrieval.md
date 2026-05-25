---
title: "Information Retrieval"
type: concept
tags: [field, ir, retrieval, search, foundations]
sources: [hands-on-llm-ch08-semantic-search-and-rag]
last_updated: 2026-05-23
---

# Information Retrieval

**Information Retrieval (IR)** is the **parent field** that [[rag|RAG]] and [[SemanticSearch|semantic search]] inherit their evaluation vocabulary, indexing primitives, and rank-sensitive metrics from. Ch 8 of *Hands-On LLMs* names IR explicitly:

> *"Semantic search is evaluated using metrics from the Information Retrieval (IR) field."* — Ch 8

## The IR vocabulary RAG inherits

- **Indexing**: [[InvertedIndex|inverted index]] (sparse), vector index (dense), [[FAISS]]-style ANN.
- **Scoring**: [[TFIDF|TF-IDF]], [[BM25|Okapi BM25]], dense similarity ([[CosineSimilarity|cosine]] / L2 / dot product).
- **Evaluation metrics**: [[PrecisionAtK|P@k]] / [[Recall|R@k]] / [[AveragePrecision|AP]] / [[MAP]] / [[MRR]] / [[NDCG]].
- **Benchmarks**: TREC, [[MSMARCO|MS MARCO]], [[BEIRBenchmark|BEIR]], [[MIRACL]].
- **Components**: archive + queries + [[RelevanceJudgment|relevance judgments]].

## The IR canon Ch 8 recommends

Ch 8's deeper-reading pointer:

> *"If you want to learn more about evaluation metrics, see the 'Evaluation in Information Retrieval' chapter of Introduction to Information Retrieval (Cambridge University Press) by Christopher D. Manning, Prabhakar Raghavan, and Hinrich Schütze."* — Ch 8

The Manning / Raghavan / Schütze textbook is the **canonical IR reference** — the academic counterpart to *Hands-On LLMs* for the pre-LLM IR fundamentals.

For the LLM-era extension:

> *"To learn more about the development of using LLMs for search, 'Pretrained transformers for text tanking: BERT and beyond' is a highly recommended look at the developments of these models until about 2021."* — Ch 8

The Lin / Nogueira / Yates 2021 monograph is the canonical reference for the transformer-era IR shift.

## What changed when LLMs entered IR

Pre-LLM IR (1960s–2010s):
- Sparse / lexical scoring ([[BM25]] dominant).
- Manual feature engineering (n-grams, named entities, structured fields).
- Learning to rank (RankNet, LambdaMART) on hand-crafted features.
- Evaluation: MAP / NDCG / MRR on TREC-style benchmarks.

LLM-era IR (2018–):
- Dense / semantic scoring (BERT-based [[DenseRetrieval|dense retrieval]]).
- Embeddings replace hand-crafted features.
- [[CrossEncoder|Cross-encoder]] / [[BiEncoder|bi-encoder]] split for the speed-quality tradeoff.
- [[ReRanking]] as a standard pipeline component.
- Same evaluation metrics + new ones for [[CitationRecall|citation-aware]] and [[Faithfulness|grounded-generation]] axes.

The **evaluation vocabulary stayed**; the **scoring mechanisms changed**.

## Connections

- [[rag]] / [[SemanticSearch]] / [[DenseRetrieval]] / [[SparseRetrieval]] / [[HybridSearch]] — the application families IR underpins.
- [[BM25]] / [[TFIDF]] — classical IR scorers.
- [[MAP]] / [[NDCG]] / [[MRR]] / [[PrecisionAtK]] / [[AveragePrecision]] — IR evaluation metrics.
- [[RelevanceJudgment]] — the ground-truth annotation requirement.
- [[InvertedIndex]] / [[VectorDatabase]] / [[FAISS]] — indexing primitives.
- [[MSMARCO]] / [[MIRACL]] / [[BEIRBenchmark]] — IR benchmarks.
- [[ReRanking]] / [[CrossEncoder]] / [[MonoBERT]] — the LLM-era IR pipeline.
- [[hands-on-llm-ch08-semantic-search-and-rag]] — primary source.
