---
title: "Latent Dirichlet Allocation (LDA)"
type: concept
tags: [topic-modeling, bag-of-words, probabilistic, classical-nlp]
sources: [hands-on-llm-ch05-text-clustering-topic-modeling]
last_updated: 2026-05-23
---

# Latent Dirichlet Allocation (LDA)

**Latent Dirichlet Allocation (LDA)** is the classical probabilistic [[TopicModeling|topic-modeling]] algorithm ([[DavidBlei|Blei]], [[AndrewNg|Ng]] & [[MichaelJordan|Jordan]], *Journal of Machine Learning Research* 3.Jan (2003): 993–1022). For two decades it was the dominant topic-modeling approach — until embedding-based methods like [[BERTopic]] reframed the problem.

## Core idea (per *Hands-On LLMs* Ch 5)

[[hands-on-llm-ch05-text-clustering-topic-modeling|Ch 5]]: LDA *"assume[s] that each topic is characterized by a probability distribution of words in a corpus's vocabulary. Each word in a vocabulary is scored against its relevance to each topic."*

Generatively: each document is a **mixture over topics**, and each topic is a **distribution over words**. Both are sampled from Dirichlet priors. Inference (typically variational Bayes or collapsed Gibbs sampling) recovers the topic-word and document-topic distributions.

## Bag-of-words limitation

LDA operates entirely on **[[BagOfWords|bag-of-words]] features** — *"these approaches generally use a bag-of-words technique for the main features of the textual data, which does not take the context nor the meaning of words and phrases into account."* Synonyms are treated as unrelated tokens; word order and context vanish.

## Contrast with [[BERTopic]]

| | LDA (2003) | BERTopic (2022) |
|---|---|---|
| **Topic discovery** | Probabilistic inference over bag-of-words | Embedding clustering ([[UMAP]] + [[HDBSCAN]]) |
| **Topic representation** | Word distribution per topic | [[ClassBasedTFIDF|c-TF-IDF]] keywords + optional rerank |
| **Captures context** | No | Yes (via Transformer attention) |
| **Number of topics** | Specified a priori | Found automatically (HDBSCAN density) |
| **Outliers** | None — every doc gets a mixture | Explicit topic `-1` |
| **Implementation** | [[Gensim]], Mallet, scikit-learn | [[BERTopic]] |

The chapter's pedagogical move: keep bag-of-words **only for the topic-representation step** (where its interpretability shines) and use **embeddings for topic discovery** (where semantic similarity matters). *"In contrast, our text clustering example does take both [context and meaning] into account as it relies on Transformer-based embeddings that are optimized for semantic similarity and contextual meaning through attention."*

## LDA is not obsolete

LDA remains useful when:
- You have very few documents and Transformer embeddings overfit.
- You want **soft assignments** (each document is a mixture, not a single topic) — BERTopic produces hard cluster assignments by default.
- You need a fully **generative probabilistic model** for downstream inference.

The wiki's [[Gensim]] entity page covers the canonical Python implementation of LDA.

## Connections

- [[hands-on-llm-ch05-text-clustering-topic-modeling]] — primary source (the contrasted baseline).
- [[TopicModeling]] — the parent concept.
- [[BERTopic]] — the modern alternative.
- [[BagOfWords]] — LDA's input representation.
- [[Gensim]] — the canonical Python LDA implementation.
- [[ClassBasedTFIDF]] — BERTopic's c-TF-IDF analogue for the representation step.
- [[DavidBlei]] / [[AndrewNg]] / [[MichaelJordan]] — original authors.
- [[MixtureModel]] — LDA is a mixture of categorical-over-vocabulary distributions.
- [[dirichletfunction]] — the underlying prior.
