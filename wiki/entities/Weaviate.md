---
title: "Weaviate"
type: entity
tags: [product, vector-database, search, open-source, hybrid-search]
sources: [leh-ch02-tooling-and-installation, leh-ch04-rag-feature-pipeline, hands-on-llm-ch08-semantic-search-and-rag, agentic-design-patterns-ch14-rag]
last_updated: 2026-06-07
---

## What it is
Weaviate is an open-source vector database with strong hybrid-search (BM25 + vector) support, schema-based collections, and a GraphQL query interface. Offered both self-hosted and as a managed cloud service.

## In LLM Engineer's Handbook
Ch. 2 ([[leh-ch02-tooling-and-installation]]) lists Weaviate among the vector-DB alternatives evaluated against [[Qdrant]] via the Superlinked Vector DB Comparison; the book picks Qdrant. Ch. 4 ([[leh-ch04-rag-feature-pipeline]]) re-mentions Weaviate in the vector-DB landscape.

## From [[hands-on-llm-ch08-semantic-search-and-rag|*Hands-On LLMs* Ch 8]]

Ch 8 names Weaviate alongside [[Pinecone]] as the **canonical vector-database example pair** (vs the [[Annoy]] / [[FAISS]] [[ApproximateNearestNeighbor|ANN-library]] pair):

> *"Another class of vector retrieval systems are vector databases like Weaviate or Pinecone. A vector database allows you to add or delete vectors without having to rebuild the index. They also provide ways to filter your search or customize it in ways beyond merely vector distances."* — Ch 8

Same framing as the LEH treatment — Weaviate is positioned as a category exemplar, with the distinguishing CRUD-and-no-rebuild + metadata-filtering capabilities.

## From [[agentic-design-patterns-ch14-rag|Agentic Design Patterns (Gulli) Ch 14]]

Ch 14 of [[AntonioGulli|Gulli's]] [[AgenticDesignPatterns|*Agentic Design Patterns*]] uses Weaviate as the **vector store in its full [[LangChain]]/[[langgraph|LangGraph]] [[rag|RAG]] hands-on example** — the wiki's first runnable Weaviate-as-RAG-backend receipt. The pipeline runs `client = weaviate.Client(embedded_options=EmbeddedOptions())` (Weaviate's embedded mode) then `vectorstore = Weaviate.from_documents(client=client, documents=chunks, embedding=OpenAIEmbeddings(), by_text=False)`, exposing retrieval via `vectorstore.as_retriever()`. The chapter also names Weaviate (alongside [[Pinecone]]) as a **managed** vector-database example in its prose survey of the [[VectorDatabase|vector DB]] landscape (vs open-source [[ChromaDB|Chroma]] / [[Milvus]] / [[Qdrant]] and vector-augmented [[RedisVectorSearch|Redis]] / [[Elasticsearch]] / [[PostgreSQL|Postgres]]). Consistent with the LEH and *Hands-On LLMs* framing.

## Connections
- [[rag]] / [[agentic-design-patterns-ch14-rag]] — Weaviate as the `Weaviate.from_documents(...)` vector store in Gulli Ch 14's LangChain/LangGraph RAG pipeline.
- [[Qdrant]] — chosen vector DB.
- [[Pinecone]] / [[Milvus]] / [[ChromaDB]] / [[Pgvector]] / [[RedisVectorSearch]] — peer vector DBs.
- [[VectorDatabase]] — category.
- [[BM25]] — Weaviate ships built-in hybrid search.
- [[hands-on-llm-ch08-semantic-search-and-rag]] — Ch 8 cites Weaviate as a vector-database exemplar.
