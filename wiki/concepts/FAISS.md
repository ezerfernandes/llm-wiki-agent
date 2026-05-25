---
title: "FAISS"
type: concept
tags: [vector-search, ann, library, retrieval, meta]
sources: [ai-engineering-ch06-rag-agents, hands-on-llm-ch08-semantic-search-and-rag]
last_updated: 2026-05-23
---

# FAISS

**FAISS** (Facebook AI Similarity Search; Johnson et al. 2017) is **[[meta|Meta]]'s open-source [[ApproximateNearestNeighbor|vector search library]]** and the most-implemented-against reference in the ANN ecosystem. FAISS bundles implementations of [[LSH]], [[HNSW]], [[ProductQuantization]], and [[IVF]] in a single C++ library with Python bindings.

## Position

Per [[ai-engineering-ch06-rag-agents|*AI Engineering* Ch 6]]:

> *"Product quantization is a key component of FAISS and is supported by almost all popular vector search libraries. ... Together with product quantization, IVF forms the backbone of FAISS."*

FAISS is the **library**, not a database — it provides indexing and search primitives, not CRUD / metadata filtering / replication. Production [[VectorDatabase|vector databases]] like [[Milvus]] / [[Pinecone]] / [[Qdrant]] / [[Weaviate]] build the database layer *on top of* FAISS-style ANN primitives.

## Why it dominates

- **Algorithm breadth**: ships LSH + HNSW + PQ + IVF + their combinations.
- **GPU support**: FAISS is one of the few ANN libraries with first-class GPU implementations.
- **Production hardening**: used inside [[meta|Meta]] at internet scale before open-sourcing.

## Connections

- [[meta|Meta]] (Facebook AI Research) — developer and open-sourcer.
- [[ApproximateNearestNeighbor]] — the algorithm family FAISS implements.
- [[HNSW]] / [[LSH]] / [[ProductQuantization]] / [[IVF]] / [[Annoy]] — the algorithms FAISS bundles or competes with.
- [[ScaNN]] — Google's competing ANN library.
- [[VectorDatabase]] — the production-DB layer built on top of FAISS-style primitives.
- [[EmbeddingBasedRetrieval]] — the retrieval family.
- [[ai-engineering-ch06-rag-agents]] — primary source.
- [[hands-on-llm-ch08-semantic-search-and-rag]] — Ch 8's worked dense-retrieval index.

## From [[hands-on-llm-ch08-semantic-search-and-rag|*Hands-On LLMs* Ch 8]]

Ch 8 uses FAISS as the **worked in-memory search index** for the dense-retrieval pipeline. The minimal-API receipt:

```python
import faiss
dim = embeds.shape[1]  # 4096 for Cohere embeddings, 384 for gte-small / bge-small
index = faiss.IndexFlatL2(dim)
index.add(np.float32(embeds))
# Search
distances, similar_item_ids = index.search(np.float32([query_embed]), number_of_results)
```

The chapter uses `IndexFlatL2` — **flat / exhaustive index with L2 distance** — appropriate for the 15-sentence *Interstellar* corpus where exact nearest neighbors are tractable. Ch 8 names the scaling story explicitly: *"As you scale beyond to the millions of vectors, an optimized approach for retrieval is to rely on approximate nearest neighbor search libraries like [[Annoy]] or FAISS."* — at scale, the same library exposes [[HNSW]] / [[IVF]] / [[ProductQuantization|PQ]] indexes for sub-linear retrieval.

FAISS also serves as the **vector store backend** in Ch 8's local-RAG path via `langchain.vectorstores.FAISS.from_texts(texts, embedding_model)` — a LangChain wrapper around the same library that adds metadata-management on top.
