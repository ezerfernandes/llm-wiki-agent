---
title: "MTEB (Massive Text Embedding Benchmark)"
type: concept
tags: [benchmark, evaluation, embeddings, nlp]
sources: [ai-engineering-ch03-evaluation-methodology, ai-engineering-ch06-rag-agents, hands-on-llm-ch04-text-classification, hands-on-llm-ch05-text-clustering-topic-modeling]
last_updated: 2026-05-23
---

# MTEB

**MTEB** — *Massive Text Embedding Benchmark* (Muennighoff et al. 2023) — is a benchmark that measures **embedding quality across multiple downstream tasks** rather than on a single similarity score. Per [[ai-engineering-ch03-evaluation-methodology|*AI Engineering* Ch 3]]:

> "You can also evaluate the quality of embeddings based on their utility for your task. Embeddings are used in many tasks, including classification, topic modeling, recommender systems, and RAG. An example of benchmarks that measure embedding quality on multiple tasks is MTEB, Massive Text Embedding Benchmark (Muennighoff et al., 2023)."

## What it evaluates

MTEB spans dozens of datasets across task families including:
- Classification
- Clustering
- Pair classification
- Reranking
- Retrieval
- [[SemanticTextualSimilarity|Semantic textual similarity (STS)]]
- Summarization

## Why utility-across-tasks matters

An embedding that excels on STS may still be poor at clustering or retrieval. MTEB is the **utility-spanning answer** to the question *"is this embedding good?"* — replacing single-task scoring (which can overfit to one downstream signal) with a portfolio score.

## The MTEB leaderboard

[[HuggingFace]] hosts the MTEB leaderboard; new commercial embedding models (OpenAI's `text-embedding-3-*`, Cohere's `embed-english-v3.0`, open-source [[SentenceTransformers]] models) all compete on it.

## Connections

- [[ai-engineering-ch03-evaluation-methodology]] — primary source.
- [[Embedding]] — what MTEB evaluates.
- [[SemanticTextualSimilarity]] — one of the task families.
- [[bert|BERT]] / [[SentenceTransformers]] / [[CLIP]] — embedding models MTEB scores.
- [[HuggingFace]] — host of the leaderboard.
- [[BERTScore]] / [[MoverScore]] — metrics whose underlying embedders MTEB grades.

## From [[ai-engineering-ch06-rag-agents|AI Engineering Ch 6]]

Ch 6 re-engages MTEB in the **retrieval evaluation** section as the canonical benchmark for evaluating the *embedding model* component of an [[EmbeddingBasedRetrieval|embedding-based RAG retriever]]:

> *"For semantic retrieval, you need to also evaluate the quality of your embeddings. ... The MTEB benchmark (Muennighoff et al., 2023) evaluates embeddings for a broad range of tasks including retrievals, classification, and clustering."*

Position in the Ch 6 evaluation rubric: MTEB scores **embeddings**; [[BEIRBenchmark|BEIR]] scores **retrieval systems**; [[ANNBenchmarks]] scores **ANN libraries**. All three are needed for a complete RAG retriever evaluation.

> *"To summarize, the quality of a RAG system should be evaluated both component by component and end to end. To do this, you should do the following things: (1) Evaluate the retrieval quality. (2) Evaluate the final RAG outputs. (3) Evaluate the embeddings (for embedding-based retrieval)."*

## From [[hands-on-llm-ch04-text-classification|*Hands-On LLMs* Ch 4]] / [[hands-on-llm-ch05-text-clustering-topic-modeling|Ch 5]]

Ch 4 names MTEB as the canonical leaderboard for picking an embedding model for **classification** workloads (selects [[AllMPNetBaseV2|`all-mpnet-base-v2`]]). Ch 5 deliberately switches the selection criterion to the **clustering column** of MTEB and picks [[GTESmall|`thenlper/gte-small`]] (384-dim, faster + higher clustering score than `all-mpnet-base-v2` at time of writing). The two chapters thus establish the wiki's framing of MTEB: *"don't pick on the average score; pick on the task-specific column."*
