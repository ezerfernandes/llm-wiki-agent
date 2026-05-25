---
title: "Word2Vec Recommender"
type: concept
tags: [embeddings, recommendation-system, word2vec]
sources: [hands-on-llm-ch02-tokens-and-embeddings]
last_updated: 2026-05-23
---

# Word2Vec Recommender

A [[RecommendationSystem|recommendation-system]] pattern that **trains [[Word2Vec|word2vec]] over sequences of objects** — treating each object as a "word" and each user-generated sequence as a "sentence" — to learn dense embeddings whose nearest neighbors are good recommendation candidates.

## From [[hands-on-llm-ch02-tokens-and-embeddings|*Hands-On LLMs* Ch 2]]

The chapter's headline non-NLP application:

> "Imagine if we treated each song as we would a word or token, and we treated each playlist like a sentence. These embeddings can then be used to recommend similar songs that often appear together in playlists." — Ch 2

**Dataset.** A collection of US-radio-station playlists collected by [[ShuoChen|Shuo Chen]] at [[CornellUniversity|Cornell University]] — each playlist is a sequence of song IDs.

**Training.** Standard [[Gensim|gensim]] `Word2Vec`:

```python
from gensim.models import Word2Vec
model = Word2Vec(
    playlists, vector_size=32, window=20, negative=50, min_count=1, workers=4
)
```

**Hyperparameters worth noting:**
- `vector_size=32` — small embedding dimension; songs need fewer dimensions than natural-language words.
- `window=20` — wide context window; songs within the same playlist are co-occurrence candidates regardless of position.
- `negative=50` — aggressive [[NegativeSampling|negative sampling]]; 50 random non-co-occurring songs per positive pair.
- `min_count=1` — keep all songs, even rare ones.

**Recommendation queries** from the chapter:
- *Billie Jean* (Michael Jackson, ID 3822) → *Kiss* (Prince), *Wanna Be Startin' Somethin'*, *The Way You Make Me Feel*, *Holiday* (Madonna), *Don't Stop 'Til You Get Enough*.
- *California Love* (2Pac, ID 842) → *If I Ruled the World* (Nas), *I'll Be Missing You* (Puff Daddy), *Hate It or Love It* (The Game), *Hypnotize* (Notorious B.I.G.), *Drop It Like It's Hot* (Snoop Dogg).
- *Fade To Black* (Metallica, ID 2172) → *Little Guitars* + *Unchained* (Van Halen), *The Last in Line* (Dio), *Mr. Brownstone* (Guns N' Roses), *Breaking the Law* (Judas Priest).

The chapter emphasizes: **all three queries return same-genre / artist-adjacent neighbors** without any explicit genre or artist supervision — the geometry emerges purely from co-occurrence in human-curated playlists.

## Why the pattern generalizes

Any domain where users produce **sequences of discrete objects** is a candidate:
- Songs in playlists → song-similarity.
- Products in shopping baskets / browsing sessions → product-similarity (item2vec-style approaches).
- Pages visited in a web session → page-similarity.
- Movies watched in order → movie-similarity.
- API calls in traces, words in commit messages, etc.

The conceptual move is identical: **co-occurrence in a user-generated sequence is a proxy for semantic similarity**, and word2vec's [[SkipGram|skip-gram]] + [[NegativeSampling|negative-sampling]] objective is computationally cheap, well-understood, and produces vectors that nearest-neighbor queries can use directly.

## Connections

- [[Word2Vec]] / [[SkipGram]] / [[NegativeSampling]] — the underlying algorithm.
- [[RecommenderSystems]] — the broader application domain.
- [[Gensim]] — the canonical Python implementation.
- [[Embedding]] / [[StaticEmbedding]] — the type of vectors produced.
- [[CosineSimilarity]] — the typical nearest-neighbor metric.
- [[ContrastiveLearning]] — the broader family of training procedures.
- [[ShuoChen]] / [[CornellUniversity]] — author and source of the playlist dataset.
- [[hands-on-llm-ch02-tokens-and-embeddings]] — source page.
