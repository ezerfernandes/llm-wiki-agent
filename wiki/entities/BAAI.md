---
title: "BAAI (Beijing Academy of Artificial Intelligence)"
type: entity
tags: [organization, ai-lab, china, embedding-models, open-source]
sources: [hands-on-llm-ch08-semantic-search-and-rag]
last_updated: 2026-05-23
---

# BAAI — Beijing Academy of Artificial Intelligence

A non-profit research organization headquartered in Beijing, founded in 2018, focused on foundational AI research. BAAI is one of the most active publishers of **open-weights embedding models** for retrieval / [[rag|RAG]] — most notably the **BGE (BAAI General Embedding) family** (`bge-small`, `bge-base`, `bge-large` across English, Chinese, multilingual, and reranker variants).

## From [[hands-on-llm-ch08-semantic-search-and-rag|*Hands-On LLMs* Ch 8]]

Ch 8 names BAAI through its **`BAAI/bge-small-en-v1.5`** model — Ch 8's selected local-RAG embedding model. The selection criterion is *"at the time of writing, it is high on the [[MTEB]] leaderboard for embedding models and relatively small"* — BAAI's BGE family is consistently in the top tier of MTEB rankings and routinely tops open-weights leaderboards.

## Position in the embedding-model ecosystem

BAAI's BGE family is one of three dominant **open-weights embedding-model families** Chinese labs have produced as alternatives to proprietary API embeddings:

- **BAAI BGE** — English, Chinese, multilingual, reranker variants.
- **[[GTESmall|GTE]] family** ([[AlibabaDAMOAcademy|Alibaba DAMO Academy]]) — general text embeddings.
- **E5 family** ([[microsoft|Microsoft Research]]) — multilingual + multiple sizes.

Together with Western labs ([[SentenceTransformers|sentence-transformers]] / [[Cohere]] / [[openai|OpenAI]] / [[NomicAtlas|Nomic]]), these constitute the open-weights embedding landscape that **MTEB** rates.

## Connections

- [[BGESmallEnV15]] — the BGE small English v1.5 model — Ch 8's named local-RAG embedding model.
- [[MTEB]] — the benchmark BAAI's BGE models routinely top.
- [[AlibabaDAMOAcademy]] — peer Chinese AI lab producing the GTE embedding family.
- [[HuggingFace]] — model-hub home.
- [[Cohere]] / [[openai|OpenAI]] — managed-API embedding alternatives.
- [[SentenceTransformers]] — the library interface.
- [[hands-on-llm-ch08-semantic-search-and-rag]] — primary source.
