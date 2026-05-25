---
title: "MS MARCO"
type: concept
tags: [benchmark, retrieval, ir, microsoft, dataset]
sources: [hands-on-llm-ch08-semantic-search-and-rag]
last_updated: 2026-05-23
---

# MS MARCO

**MS MARCO** (Microsoft MAchine Reading COmprehension) is a **large-scale information-retrieval benchmark** released by [[microsoft|Microsoft]] (Bajaj et al. 2016, *"MS MARCO: A Human Generated MAchine Reading COmprehension Dataset"*). The dataset's **passage-ranking task** has become the canonical training and evaluation corpus for modern dense retrievers and cross-encoder rerankers.

## Why it matters for RAG

Modern reranker model checkpoints are typically distributed under names like `cross-encoder/ms-marco-MiniLM-L-6-v2`, `cross-encoder/ms-marco-TinyBERT-L-2-v2`, `cross-encoder/ms-marco-MiniLM-L-4-v2` — the **`ms-marco-` prefix** indicates training data lineage. These are the **bi-encoder + cross-encoder** open-source models the [[SentenceTransformers]] library ships and that [[hands-on-llm-ch08-semantic-search-and-rag|*Hands-On LLMs* Ch 8]] names as the local-RAG reranking path.

[[leh-ch04-rag-feature-pipeline|LEH Ch 4]] and [[leh-ch09-rag-inference-pipeline|LEH Ch 9]] both use `cross-encoder/ms-marco-MiniLM-L-4-v2` as the reranker; the [[CrossEncoder]] page lists `cross-encoder/ms-marco-MiniLM-L-6-v2` as one of two common checkpoints. The MS MARCO training corpus is **the unifying lineage** across these implementations.

## Position in the IR-benchmark ecosystem

| Benchmark | Scale | Language |
|---|---|---|
| **MS MARCO** | **8.8M passages, 530K queries** | **English** |
| [[BEIRBenchmark|BEIR]] | Heterogeneous (18 datasets) | English |
| [[MIRACL]] | Wikipedia (per-language subsets) | **18 languages multilingual** |
| TREC tracks | Domain-specific | Various |

MS MARCO is **the English mono-lingual training default**; [[MIRACL]] is the multilingual evaluation default.

## Connections

- [[microsoft|Microsoft]] — releaser.
- [[InformationRetrieval]] — the parent field.
- [[CrossEncoder]] / [[MonoBERT]] — the architectures typically trained on MS MARCO.
- [[BiEncoder]] / [[SentenceTransformers]] — the bi-encoder model family trained on MS MARCO.
- [[MIRACL]] — the multilingual evaluation counterpart.
- [[BEIRBenchmark]] — the heterogeneous evaluation counterpart.
- [[RelevanceJudgment]] — what MS MARCO provides for queries and passages.
- [[hands-on-llm-ch08-semantic-search-and-rag]] — primary source (cited indirectly via reranker model names).
