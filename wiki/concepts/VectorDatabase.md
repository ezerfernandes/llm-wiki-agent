---
title: "Vector Database"
type: concept
tags: [rag, retrieval, vector-search, storage, llm-engineering]
sources: [leh-ch01-understanding-llm-twin-concept, leh-ch02-tooling-and-installation, leh-ch04-rag-feature-pipeline, leh-ch09-rag-inference-pipeline, leh-ch10-inference-pipeline-deployment, ai-engineering-ch06-rag-agents, hands-on-llm-ch08-semantic-search-and-rag]
last_updated: 2026-05-23
---

## Definition
A **vector database** is a database system optimized for storing high-dimensional embedding vectors and answering **approximate nearest neighbor (ANN)** queries against them, while also supporting standard CRUD, metadata filtering, scaling/sharding, replication, and access control. Vector DBs are the production-grade alternative to standalone vector indices like FAISS.

## In LLM Engineer's Handbook
[[leh-ch04-rag-feature-pipeline]] is the deepest treatment: it distinguishes vector DBs from vector *indices* (FAISS), explains how vector DBs support CRUD + metadata filtering + real-time updates + backups + access control, and surveys the four canonical ANN index algorithms — **HNSW**, **Random Projection**, **Product Quantization**, and **Locality-Sensitive Hashing**. The chapter explains the role of vector DBs in [[rag|RAG]] (embed + ANN-search + return top-K chunks) and the importance of using the **same embedding model** at ingest and at query time. [[leh-ch02-tooling-and-installation]] surveys the vendor landscape ([[Qdrant]], [[Milvus]], [[Weaviate]], [[Pinecone]], [[ChromaDB]], [[Pgvector]], Redis), citing the Superlinked Vector DB Comparison; the book picks [[Qdrant]] for the LLM Twin. [[leh-ch01-understanding-llm-twin-concept]] frames the vector DB as the online half of the [[LogicalFeatureStore]]; [[leh-ch09-rag-inference-pipeline]] uses it for [[FilteredVectorSearch|filtered vector search]] during retrieval; [[leh-ch10-inference-pipeline-deployment]] keeps it in the business microservice.

## Key details
- Workflow: index (HNSW/PQ/LSH/RP) → query by similarity (cosine / Euclidean / dot product) → post-process (refine, filter) → production ops (sharding, replication, monitoring, backup, access control).
- Embedding dimensions typically 64–2048; HNSW is the de-facto default index.
- Distinguished from a vector *index* like FAISS by full DBMS features (CRUD, metadata filtering, scalability, real-time updates, backups, ecosystem integration, security).
- Metadata indexes inside the vector DB enable [[FilteredVectorSearch]] (e.g., Qdrant `Filter(must=[FieldCondition(...)])`).
- Can double as a NoSQL store when used without a vector index — the book uses Qdrant's metadata index this way for the "cleaned only" snapshot in the [[LogicalFeatureStore]].

## Connections
- [[rag]] — vector DBs are the retrieval substrate.
- [[Qdrant]] / [[Milvus]] / [[Weaviate]] / [[Pinecone]] / [[ChromaDB]] / [[Pgvector]] / [[RedisVectorSearch]] — vendor implementations.
- [[CosineSimilarity]] — primary distance metric for ANN retrieval.
- [[Embedding]] — the data type a vector DB stores.
- [[FilteredVectorSearch]] — DB-side optimization combining vector + metadata.
- [[FeatureStore]] / [[LogicalFeatureStore]] — the broader architectural slot a vector DB fills in an LLM stack.
- [[Hadoop]] / [[NetflixPrize]] — the pre-LLM embedding lineage (collaborative filtering) the chapter cites.

## From [[ai-engineering-ch06-rag-agents|AI Engineering Ch 6]]

[[ChipHuyen|Huyen]] frames vector databases through the **storage-easy / search-hard** distinction:

> *"A vector database stores vectors. However, storing is the easy part of a vector database. The hard part is vector search."*

The chapter develops [[ApproximateNearestNeighbor|ANN]] as the structural enabler of vector search at scale — naive k-NN doesn't scale, so vector DBs index with [[LSH]] / [[HNSW]] / [[ProductQuantization]] / [[IVF]] / [[Annoy]] / etc.

**Two key non-vector-DB observations** Huyen makes that frame the category:

1. *"Vector search isn't unique to generative AI. Vector search is common in any application that uses embeddings: search, recommendation, data organization, information retrieval, clustering, fraud detection, and more."* This is the recommendation-systems lineage that predates RAG.

2. *"Any database that can store vectors can be called a vector database. Many traditional databases have extended or will extend to support vector storage and vector search."* The dedicated vector-DB category is converging with traditional DBs — [[Pgvector]] is the canonical example.

**Cost framing**: *"It's not uncommon to see a company's vector database spending be one-fifth or even half of their spending on model APIs."* Vector storage and query are *not* free — they are a structural cost line of any embedding-based RAG system.

**Evaluation rubric for vector DB selection** (Ch 6 checklist):

- What retrieval mechanisms supported? Hybrid search support?
- Which embedding models and ANN algorithms?
- Scalability — data storage and query traffic?
- Indexing time? Bulk operation throughput?
- Query latency per algorithm?
- Pricing structure (per-document/vector vs per-query)?
- Enterprise features — access control, compliance, data-plane/control-plane separation?

## From [[hands-on-llm-ch08-semantic-search-and-rag|*Hands-On LLMs* Ch 8]]

Ch 8 makes the **library-vs-database** distinction explicitly — consistent with both Huyen Ch 6 and LEH Ch 4:

> *"Another class of vector retrieval systems are vector databases like [[Weaviate]] or [[Pinecone]]. A vector database allows you to add or delete vectors without having to rebuild the index. They also provide ways to filter your search or customize it in ways beyond merely vector distances."* — Ch 8

The Ch 8 distinguishing-criterion is **the CRUD-and-no-rebuild axis**:

| Capability | ANN library ([[FAISS]] / [[Annoy]]) | Vector database (Weaviate / Pinecone) |
|---|---|---|
| Vector storage | ✓ | ✓ |
| ANN search | ✓ | ✓ |
| **Add/delete without rebuild** | ✗ | ✓ |
| Metadata filtering | Limited | ✓ |
| CRUD APIs | ✗ | ✓ |
| Customizable beyond vector distance | ✗ | ✓ |

The triple-source consistency (Ch 8 / Huyen Ch 6 / LEH Ch 4) makes this **the wiki's most-anchored distinction** in the vector-DB conceptual space.
