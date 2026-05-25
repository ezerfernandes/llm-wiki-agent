---
title: "Product Quantization"
type: concept
tags: [vector-search, ann, quantization, retrieval]
sources: [ai-engineering-ch06-rag-agents]
last_updated: 2024-12-04
---

# Product Quantization

**Product Quantization (PQ)** (Jégou et al. 2011) reduces each vector to a **much simpler, lower-dimensional representation** by decomposing it into multiple subvectors and quantizing each subvector independently. Distances are then computed using the compressed representations — *"much faster to work with"* ([[ai-engineering-ch06-rag-agents|Huyen Ch 6]]) than the original dense vectors.

## Why it pairs with [[IVF]] in [[FAISS]]

Per Huyen: *"Product quantization is a key component of FAISS and is supported by almost all popular vector search libraries."* Together with [[IVF|inverted file index]] clustering, product quantization *"forms the backbone of FAISS."*

The standard recipe:

1. **[[IVF]]**: K-means cluster the database; at query time, restrict candidates to the nearest cluster's vectors.
2. **PQ**: store each candidate vector as a small set of subvector codes; compute distances on the compressed representation.

Combined, IVF + PQ enable billion-scale vector search at a fraction of the memory footprint of raw vectors.

## Connections

- [[ApproximateNearestNeighbor]] — the parent family.
- [[Quantization]] — the broader concept of reducing numerical precision.
- [[IVF]] — the clustering counterpart Product Quantization is usually paired with.
- [[HNSW]] / [[LSH]] / [[Annoy]] — sibling ANN techniques.
- [[FAISS]] — the canonical implementation.
- [[EmbeddingBasedRetrieval]] / [[VectorDatabase]] — the production stack.
- [[ai-engineering-ch06-rag-agents]] — primary source.
