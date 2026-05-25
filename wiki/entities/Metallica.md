---
title: "Metallica"
type: entity
tags: [musician, metal]
sources: [hands-on-llm-ch02-tokens-and-embeddings]
last_updated: 2026-05-23
---

# Metallica

American heavy-metal band (formed 1981, Los Angeles).

## From [[hands-on-llm-ch02-tokens-and-embeddings|*Hands-On LLMs* Ch 2]]

Ch 2 uses Metallica's *"Fade To Black"* (ID 2172 in the Cornell radio-playlist dataset) as the **third query** to the [[Word2VecRecommender|song-embedding recommender]] — chosen specifically to demonstrate that the embedding geometry generalizes to genres far from pop. Output:

| Title | Artist |
|---|---|
| Little Guitars | Van Halen |
| Unchained | Van Halen |
| The Last in Line | Dio |
| Mr. Brownstone | Guns N' Roses |
| Breaking the Law | Judas Priest |

> "This results in recommendations that are all in the same heavy metal and hard rock genre." — Ch 2

— evidence that the [[Word2Vec|word2vec]]-on-playlists pattern partitions playlist-co-occurrence into genre-coherent clusters without explicit genre supervision.

## Connections

- [[Word2VecRecommender]] — the recommendation pattern.
- [[Word2Vec]] — the underlying algorithm.
- [[hands-on-llm-ch02-tokens-and-embeddings]] — citation.
