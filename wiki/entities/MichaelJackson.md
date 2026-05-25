---
title: "Michael Jackson"
type: entity
tags: [musician, pop]
sources: [hands-on-llm-ch02-tokens-and-embeddings]
last_updated: 2026-05-23
---

# Michael Jackson

American pop musician (1958–2009).

## From [[hands-on-llm-ch02-tokens-and-embeddings|*Hands-On LLMs* Ch 2]]

Ch 2 uses Michael Jackson's *"Billie Jean"* (ID 3822 in the Cornell radio-playlist dataset) as the **first query** to the [[Word2VecRecommender|song-embedding recommender]] worked example. Output:

| Title | Artist |
|---|---|
| Kiss | Prince & The Revolution |
| Wanna Be Startin' Somethin' | Michael Jackson |
| The Way You Make Me Feel | Michael Jackson |
| Holiday | Madonna |
| Don't Stop 'Til You Get Enough | Michael Jackson |

The chapter comments: *"That looks reasonable. Madonna, Prince, and other Michael Jackson songs are the nearest neighbors."* — evidence that the [[Word2Vec|word2vec]]-on-playlists pattern recovers same-era pop-genre similarity without supervised genre labels.

## Connections

- [[Word2VecRecommender]] — the recommendation pattern.
- [[Word2Vec]] — the underlying algorithm.
- [[hands-on-llm-ch02-tokens-and-embeddings]] — citation.
