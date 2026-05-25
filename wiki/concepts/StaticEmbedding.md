---
title: "Static Embedding"
type: concept
tags: [nlp, embeddings]
sources: [hands-on-llm-ch02-tokens-and-embeddings]
last_updated: 2026-05-23
---

# Static Embedding

A token / word representation that maps each token in the vocabulary to a **single fixed vector** — the same vector regardless of surrounding context. The canonical examples are [[Word2Vec|word2vec]], [[GloVe]], and [[FastText]]; in modern LLMs, the **input embedding matrix** is itself a static lookup table (each input token ID retrieves a fixed row), even though the model's deeper layers immediately produce [[ContextualEmbedding|contextualized]] per-position vectors.

## From [[hands-on-llm-ch02-tokens-and-embeddings|*Hands-On LLMs* Ch 2]]

Ch 2 frames the static / contextual split as the central pivot in the history of language embeddings:

> "Instead of representing each token or word with a static vector, language models create contextualized word embeddings that represent a word with a different token based on its context." — Ch 2

The chapter's running diagram (Figure 2-9): *"A language model operates on raw, static embeddings as its input and produces contextual text embeddings."* The static embeddings are the **input** to the model; contextualized embeddings are the **output**.

Static embeddings are still useful — in [[RecommendationSystem|recommendation]] settings (the chapter's song-embedding worked example), in [[WordSimilarity|word-similarity]] benchmarks, and as a lightweight baseline for downstream tasks. But for any task where word sense matters (`bank` of a river vs financial `bank`), contextualized embeddings dominate.

## Why "static"

The term emphasizes the **lookup-table** semantics: the embedding is a deterministic function of the token ID alone, not of context. In a Transformer, the input-embedding layer is a static lookup; the **attention layers** that follow inject context-dependence. The same word2vec model run twice on the same word produces identical embeddings.

## Connections

- [[ContextualEmbedding]] — the dual concept; the modern default.
- [[Word2Vec]] / [[GloVe]] / [[FastText]] — the three canonical static word-embedding families.
- [[TokenEmbedding]] — the LLM-input-layer special case.
- [[Embedding]] / [[WordEmbedding]] — the umbrella terms.
- [[hands-on-llm-ch02-tokens-and-embeddings]] — source page.
