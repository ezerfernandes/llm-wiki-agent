---
title: "BAAI/bge-small-en-v1.5"
type: entity
tags: [model, embedding, retrieval, sentence-transformers, baai, open-weights]
sources: [hands-on-llm-ch08-semantic-search-and-rag]
last_updated: 2026-05-23
---

# BAAI/bge-small-en-v1.5

The **small English variant of the BGE (BAAI General Embedding) family v1.5**, published by the [[BAAI|Beijing Academy of Artificial Intelligence]]. A compact 384-dim text-embedding model designed to balance **[[MTEB]] performance** with **inference cost** — explicitly positioned as a strong default for dense retrieval / [[rag|RAG]] when compute is constrained.

## From [[hands-on-llm-ch08-semantic-search-and-rag|*Hands-On LLMs* Ch 8]]

Ch 8 names `BAAI/bge-small-en-v1.5` as the **embedding model for the chapter's local-RAG worked example**:

> *"Let's now load an embedding language model. In this example, we will choose the BAAI/bge-small-en-v1.5 model. At the time of writing, it is high on the MTEB leaderboard for embedding models and relatively small."*

The selection criterion — **high MTEB position + small size** — embodies the *Hands-On LLMs* GPU-poor design discipline carried through the entire book; the same logic that selects [[Phi3Mini|Phi-3-mini]] for generation and [[GTESmall|gte-small]] for clustering selects bge-small-en-v1.5 for retrieval.

**Transcription inconsistency note**: the surrounding text discusses `BAAI/bge-small-en-v1.5`, but the actual code snippet loads `thenlper/gte-small` ([[GTESmall]]). The wiki records both as named candidates — bge-small-en-v1.5 is the **intended** local-RAG embedding model per the chapter prose; gte-small is the **actually-loaded** model per the code. This is a documentation bug in Ch 8, not a wiki contradiction.

## Position in the BGE family

`bge-small-en-v1.5` is the smallest of the BGE v1.5 English-only models. The full v1.5 family at the time of *Hands-On LLMs* publication:

| Model | Dimensions | Approximate parameters |
|---|---|---|
| `bge-large-en-v1.5` | 1024 | ≈335M |
| `bge-base-en-v1.5` | 768 | ≈110M |
| **`bge-small-en-v1.5`** | **384** | **≈33M** |

The BGE family is consistently a top-performing open-weights embedding family on [[MTEB]] — and the smallest model is the natural default for laptop / Colab inference.

## Connections

- [[BAAI]] — the producer (Beijing Academy of Artificial Intelligence).
- [[MTEB]] — the benchmark Ch 8 selects this model against.
- [[SentenceTransformers]] — the canonical Python interface for loading BGE models.
- [[HuggingFace]] — model-hub home.
- [[GTESmall]] — the actually-loaded model in Ch 8's code snippet (a parallel small embedding model from a different lab).
- [[Phi3Mini]] — the generation model the local-RAG example pairs this with.
- [[FAISS]] — the index the embeddings are stored in.
- [[LangChain]] — the `HuggingFaceEmbeddings` wrapper used in the worked example.
- [[rag]] / [[DenseRetrieval]] / [[EmbeddingBasedRetrieval]] — the application family.
- [[hands-on-llm-ch08-semantic-search-and-rag]] — primary source.
