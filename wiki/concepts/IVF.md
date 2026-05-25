---
title: "IVF (Inverted File Index)"
type: concept
tags: [vector-search, ann, clustering, retrieval]
sources: [ai-engineering-ch06-rag-agents]
last_updated: 2024-12-04
---

# IVF

**IVF** (Inverted File Index; Sivic & Zisserman 2003) is the [[ApproximateNearestNeighbor|ANN]] algorithm that **organizes vectors into clusters using K-means**, then restricts query-time search to the cluster centroids closest to the query embedding.

## How it works

Per [[ai-engineering-ch06-rag-agents|*AI Engineering* Ch 6]]:

> *"IVF uses K-means clustering to organize similar vectors into the same cluster. Depending on the number of vectors in the database, it's typical to set the number of clusters so that, on average, there are 100 to 10,000 vectors in each cluster. During querying, IVF finds the cluster centroids closest to the query embedding, and the vectors in these clusters become candidate neighbors."*

Searching only the closest clusters dramatically reduces the candidate set — typically by a factor of 100×–1000× — at the cost of occasionally missing a true neighbor that fell into a sibling cluster.

## Why it pairs with [[ProductQuantization]]

Together with [[ProductQuantization]], IVF *"forms the backbone of FAISS."* IVF restricts the candidate set; PQ compresses each candidate. The combination delivers billion-scale vector search at fraction-of-raw-memory cost.

## Connections

- [[ApproximateNearestNeighbor]] — the parent family.
- [[ProductQuantization]] — the standard companion algorithm.
- [[HNSW]] / [[LSH]] / [[Annoy]] — sibling ANN techniques.
- [[FAISS]] — the canonical implementation pairing IVF + PQ.
- [[EmbeddingBasedRetrieval]] / [[VectorDatabase]] — the production stack.
- [[ai-engineering-ch06-rag-agents]] — primary source.
