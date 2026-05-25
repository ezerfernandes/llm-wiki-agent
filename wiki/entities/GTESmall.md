---
title: "gte-small (thenlper/gte-small)"
type: entity
tags: [embedding-model, sentence-transformer, alibaba, gte, huggingface]
sources: [hands-on-llm-ch05-text-clustering-topic-modeling]
last_updated: 2026-05-23
---

# gte-small (`thenlper/gte-small`)

**`thenlper/gte-small`** is a **384-dimensional** sentence-embedding model from [[AlibabaDAMOAcademy|Alibaba DAMO Academy]]'s **General Text Embeddings (GTE)** family (Li et al., 2023). It targets the same use cases as [[SentenceTransformers|sentence-transformers]]' `all-mpnet-base-v2` (768-dim) but with a **smaller dimensionality, smaller parameter count, and higher [[MTEB|MTEB]] clustering score** at time of writing.

## From [[hands-on-llm-ch05-text-clustering-topic-modeling|*Hands-On LLMs* Ch 5]]

Ch 5 chooses `gte-small` over Ch 4's `all-mpnet-base-v2` *"because at the time of writing, it outperforms the previous model on clustering tasks and is significantly smaller, making inference much faster."* The model is loaded via `SentenceTransformer("thenlper/gte-small")` and feeds the embed step of the BERTopic pipeline (44,949 abstracts × 384 dims).

The chapter explicitly recommends checking the **clustering column** of the MTEB leaderboard when picking an embedding model for clustering — a different metric to optimize than retrieval or general-purpose embedding.

## Family

The **GTE (General Text Embeddings)** family is a line of sentence-embedding models from Alibaba DAMO Academy that consistently rank near the top of the MTEB leaderboard across multiple sizes (`gte-small`, `gte-base`, `gte-large`).

## Connections

- [[hands-on-llm-ch05-text-clustering-topic-modeling]] — primary source.
- [[AlibabaDAMOAcademy]] — research lab behind GTE.
- [[SentenceTransformers]] — the loading interface.
- [[MTEB]] — the benchmark used to select it.
- [[AllMPNetBaseV2]] — the predecessor model Ch 5 replaces it with.
- [[Embedding]] / [[SentenceEmbedding]] — what it produces.
- [[BERTopic]] / [[TextClustering]] — the downstream pipeline.
