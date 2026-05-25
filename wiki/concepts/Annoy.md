---
title: "Annoy"
type: concept
tags: [vector-search, ann, retrieval, spotify]
sources: [ai-engineering-ch06-rag-agents, hands-on-llm-ch08-semantic-search-and-rag]
last_updated: 2026-05-23
---

# Annoy

**Annoy** (Approximate Nearest Neighbors Oh Yeah; Bernhardsson, [[Spotify]] 2013) is a **tree-based** [[ApproximateNearestNeighbor|ANN]] algorithm. It builds multiple binary trees, each of which splits the vectors into clusters using random criteria — *"such as randomly drawing a line and splitting the vectors into two branches using this line"* ([[ai-engineering-ch06-rag-agents|Huyen Ch 6]]). At query time, Annoy traverses these trees to gather candidate neighbors.

## Position in the ANN ecosystem

Spotify open-sourced Annoy as part of their music-recommendation infrastructure. It is the **canonical tree-based ANN library** — graph-based ([[HNSW]]), hash-based ([[LSH]]), quantization-based ([[ProductQuantization]]), and tree-based (Annoy) being the four main structural families. Annoy is competitive on **build time + memory** but generally trails HNSW on **recall × QPS** for large corpora.

## Connections

- [[ApproximateNearestNeighbor]] — the parent family.
- [[HNSW]] / [[LSH]] / [[ProductQuantization]] / [[IVF]] — sibling ANN techniques.
- [[FAISS]] — the dominant ANN library; Annoy is the lighter Spotify alternative.
- [[Spotify]] — open-sourcer.
- [[EmbeddingBasedRetrieval]] / [[VectorDatabase]] — the application surface.
- [[ai-engineering-ch06-rag-agents]] — primary source.
- [[hands-on-llm-ch08-semantic-search-and-rag]] — Ch 8 cites Annoy + [[FAISS]] together as the canonical ANN-library pair for scaling beyond NumPy-distance search.

## From [[hands-on-llm-ch08-semantic-search-and-rag|*Hands-On LLMs* Ch 8]]

Ch 8 names Annoy alongside [[FAISS]] as the **scale-out alternative to naive NumPy distance computation**:

> *"As you scale beyond to the millions of vectors, an optimized approach for retrieval is to rely on approximate nearest neighbor search libraries like Annoy or FAISS. These allow you to retrieve results from massive indexes in milliseconds and some of them can improve their performance by utilizing GPUs and scaling to clusters of machines to serve very large indices."* — Ch 8

The two libraries are positioned as **direct alternatives** at this point in the chapter; the more detailed library-vs-database distinction comes next, with [[Weaviate]] / [[Pinecone]] as the vector-database counterparts.
