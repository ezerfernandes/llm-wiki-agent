---
title: "Gensim"
type: entity
tags: [library, python, nlp, embeddings]
sources: [hands-on-llm-ch02-tokens-and-embeddings, hands-on-llm-ch05-text-clustering-topic-modeling]
last_updated: 2026-05-23
---

# Gensim

Open-source Python library by Radim Řehůřek (and contributors) for **topic modeling and vector-space NLP**. The canonical Python implementation of [[Word2Vec|word2vec]], [[GloVe]] loading, [[FastText]], LDA, LSA, and similar classical NLP / topic-modeling techniques.

## From [[hands-on-llm-ch02-tokens-and-embeddings|*Hands-On LLMs* Ch 2]]

Ch 2 uses Gensim for two demonstrations:

**Loading pretrained word embeddings:**
```python
import gensim.downloader as api
model = api.load("glove-wiki-gigaword-50")
model.most_similar([model['king']], topn=11)
# [('king', 1.0), ('prince', 0.82), ('queen', 0.78), ...]
```

**Training word2vec on song-playlist data** (the [[Word2VecRecommender]] worked example):
```python
from gensim.models import Word2Vec
model = Word2Vec(
    playlists, vector_size=32, window=20, negative=50, min_count=1, workers=4
)
model.wv.most_similar(positive=str(song_id))
```

The chapter recommends Gensim as the **lightest-weight tool** for any task involving word2vec, GloVe, or fastText — no need for a deep-learning framework.

## From [[hands-on-llm-ch05-text-clustering-topic-modeling|*Hands-On LLMs* Ch 5]]

Ch 5 engages Gensim **via contrast** — as the canonical Python implementation of classical [[LatentDirichletAllocation|LDA]], the topic-modeling baseline against which [[BERTopic]] is positioned. Gensim's LDA operates on raw bag-of-words (no context, no semantic similarity); BERTopic uses bag-of-words *only* at the topic-representation step and replaces topic discovery with embedding-based clustering. The two are complementary tools — Gensim is still the right answer for soft topic assignments and small-corpus generative-model use cases, while BERTopic owns the modern embedding-based pipeline.

## Connections

- [[Word2Vec]] / [[SkipGram]] / [[CBOW]] / [[NegativeSampling]] — the algorithms Gensim implements.
- [[GloVe]] / [[FastText]] — alternative embeddings Gensim can load.
- [[Word2VecRecommender]] — Ch 2's song-embedding worked use.
- [[LatentDirichletAllocation]] — Gensim's canonical topic-modeling algorithm (Ch 5's baseline).
- [[BERTopic]] — the modern alternative (Ch 5's flagship framework).
- [[TopicModeling]] — the field both inhabit.
- [[HandsOnLLM]] / [[hands-on-llm-ch02-tokens-and-embeddings]] — Ch 2 demos.
- [[hands-on-llm-ch05-text-clustering-topic-modeling]] — Ch 5 LDA contrast.
