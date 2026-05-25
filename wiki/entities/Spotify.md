---
title: "Spotify"
type: entity
tags: [company, music, recommender-system, vector-search]
sources: [ai-engineering-ch06-rag-agents]
last_updated: 2024-12-04
---

# Spotify

**Spotify** is the Swedish music-streaming company that **open-sourced [[Annoy]]** (Approximate Nearest Neighbors Oh Yeah; Bernhardsson 2013) — the tree-based [[ApproximateNearestNeighbor|ANN]] library named in [[ai-engineering-ch06-rag-agents|*AI Engineering* Ch 6]] as one of the canonical vector-search libraries.

## Position in the vector-search ecosystem

Spotify's contribution is structurally important: Annoy was the **first widely-adopted open-source ANN library** outside research, predating both [[FAISS]] (2017) and [[ScaNN]] (2020). It was built and battle-tested against Spotify's music-recommendation use case — billions of song embeddings, queried for *"users like you also liked..."* — and that recommendation-systems lineage seeded the broader vector-search field's awareness of ANN.

## Connections

- [[Annoy]] — the library Spotify open-sourced.
- [[ApproximateNearestNeighbor]] — the family Annoy belongs to.
- [[FAISS]] / [[ScaNN]] — the more recent peer libraries.
- [[EmbeddingBasedRetrieval]] — the application family.
- [[ai-engineering-ch06-rag-agents]] — primary source.
