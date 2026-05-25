---
title: "Qdrant"
type: entity
tags: [tool, vector-database, search, open-source]
sources: [leh-ch02-tooling-and-installation, leh-ch03-data-engineering, leh-ch04-rag-feature-pipeline, leh-ch09-rag-inference-pipeline, leh-ch10-inference-pipeline-deployment, leh-ch11-mlops-and-llmops]
last_updated: 2026-05-22
---

## What it is
Qdrant is an open-source, Rust-written vector database that supports ANN search (HNSW), payload metadata, filtered vector search, and a managed cloud tier. It is the LLM Twin's online retrieval store.

## In LLM Engineer's Handbook
Ch. 2 ([[leh-ch02-tooling-and-installation]]) selects Qdrant over [[Milvus]] / Redis / [[Weaviate]] / [[Pinecone]] / [[ChromaDB]] / [[Pgvector]] citing Superlinked's Vector DB Comparison for its RPS/latency/index-time trade-off, and spins it up as a Docker container alongside [[MongoDB]] and [[ZenML]]. Ch. 4 ([[leh-ch04-rag-feature-pipeline]]) writes both cleaned-only documents (NoSQL-style usage of Qdrant payloads) and embedded chunks (with HNSW vector index) into Qdrant via a custom Object-Vector Mapping (OVM) layer. Ch. 9 ([[leh-ch09-rag-inference-pipeline]]) issues filtered vector searches against Qdrant per data category using `Filter(must=[FieldCondition(...)])` constraints. Ch. 10 ([[leh-ch10-inference-pipeline-deployment]]) keeps Qdrant as the RAG store inside the FastAPI business microservice, and Ch. 11 ([[leh-ch11-mlops-and-llmops]]) migrates to **Qdrant Cloud (free tier on GCP)** for the production stack.

## Connections
- [[VectorDatabase]] — category Qdrant belongs to.
- [[Pinecone]] / [[Weaviate]] / [[Milvus]] / [[ChromaDB]] / [[Pgvector]] / [[RedisVectorSearch]] — competitors evaluated in Ch. 2.
- [[MongoDB]] — upstream raw-document store.
- [[ZenML]] — orchestrates ingest into Qdrant.
- [[Superlinked]] — published the comparison the authors cite.
- [[FeatureStore]] — Qdrant serves the online half of LLM Twin's logical feature store.
