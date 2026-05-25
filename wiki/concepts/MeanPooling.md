---
title: "Mean Pooling"
type: concept
tags: [pooling, embeddings, sbert, sentence-embeddings]
sources: [hands-on-llm-ch10-creating-text-embedding-models]
last_updated: 2026-05-23
---

# Mean Pooling

**Mean pooling** — for sentence-embedding models, the strategy of producing a single fixed-dim sentence vector by **averaging the token-level output embeddings** of the encoder's final layer. The default pooling strategy in [[SentenceTransformers|sentence-transformers]] and the [[SBERTArchitecture|SBERT architecture]].

## In [[hands-on-llm-ch10-creating-text-embedding-models|*Hands-On LLMs* Ch 10]]

Ch 10 names mean-pooling as **the structural device that lets SBERT solve the [[CrossEncoder|cross-encoder]] problem**: *"in sentence-transformers the classification head is dropped, and instead mean pooling is used on the final output layer to generate an embedding. This pooling layer averages the word embeddings and gives back a fixed dimensional output vector. This ensures a fixed-size embedding."*

The structural payoff: **the output dimension does not depend on input length**. Whatever the sentence length, mean-pooling produces the same fixed-size vector (e.g., 384 for `all-MiniLM-L6-v2`, 768 for `all-mpnet-base-v2`), which is what makes downstream cosine-similarity comparison and vector-database indexing possible.

## Mean vs other pooling strategies

Per Ch 10 (citing the Sentence-BERT paper):

> *"A solution to this overhead is to generate embeddings from a BERT model by averaging its output layer or using the [CLS] token. This, however, has shown to be worse than simply averaging word vectors, like GloVe."* — Ch 10 on naive (non-trained) BERT pooling.

The Reimers & Gurevych Sentence-BERT paper compared **mean pooling vs [CLS]-token pooling vs max pooling** and **mean pooling won** for the supervised-contrastive regime. Mean pooling is therefore the default in sentence-transformers.

## The TSDAE exception

The **only place** Ch 10 recommends switching to [[CLSPooling|[CLS]-token pooling]] is the [[TSDAE]] unsupervised regime: *"we run the training as before but with the [CLS] token as the pooling strategy instead of the mean pooling of the token embeddings. In the TSDAE paper, this was shown to be more effective since mean pooling loses the position information, which is not the case when using the [CLS] token."*

This is the **only place in the wiki** where [CLS]-pooling beats mean-pooling for a sentence-embedding regime — and it is regime-specific (denoising auto-encoder reconstruction), not a contradiction of the general mean-pooling-as-default discipline.

## Implementation

In sentence-transformers:

```python
from sentence_transformers import models, SentenceTransformer

word_embedding_model = models.Transformer("bert-base-uncased")
pooling_model = models.Pooling(
    word_embedding_model.get_word_embedding_dimension(),
    "mean",  # default; alternatives: "cls", "max"
)
embedding_model = SentenceTransformer(modules=[word_embedding_model, pooling_model])
```

## Connections

- [[CLSPooling]] — the alternative used in TSDAE.
- [[SBERTArchitecture]] / [[SBERT]] — where mean pooling sits in the architecture.
- [[Pooling]] — the parent concept.
- [[SentenceTransformers]] — the library that defaults to mean pooling.
- [[TSDAE]] — the exception that prefers [CLS]-pooling.
- [[NilsReimers]] / [[IrynaGurevych]] — Sentence-BERT authors.
- [[hands-on-llm-ch10-creating-text-embedding-models]] — primary source.
