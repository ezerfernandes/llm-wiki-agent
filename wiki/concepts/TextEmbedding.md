---
title: "Text Embedding"
type: concept
tags: [nlp, embeddings, rag, semantic-search]
sources: [hands-on-llm-ch02-tokens-and-embeddings, hands-on-llm-ch10-creating-text-embedding-models]
last_updated: 2026-05-23
---

# Text Embedding

A **single dense vector** that represents a piece of text longer than one token — a sentence, paragraph, or document — capturing its meaning in a form amenable to similarity search. The substrate of [[SemanticSearch|semantic search]], [[rag|RAG]], topic modeling, and clustering.

## From [[hands-on-llm-ch02-tokens-and-embeddings|*Hands-On LLMs* Ch 2]]

> "While token embeddings are key to how LLMs operate, a number of LLM applications require operating on entire sentences, paragraphs, or even text documents. This has led to special language models that produce text embeddings — a single vector that represents a piece of text longer than just one token." — Ch 2

Two production approaches:

1. **Pooled token embeddings.** *"One of the most common ways is to average the values of all the token embeddings produced by the model."* Quick and free if you already have a language model — but quality is bounded by how well the underlying model's contextualized token embeddings happen to align in a pool-able geometry.
2. **Dedicated text-embedding models.** *"high-quality text embedding models tend to be trained specifically for text embedding tasks."* The chapter introduces [[SentenceTransformers|sentence-transformers]] (Reimers & Gurevych 2019, *"Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks"*) as the canonical Python package, with `all-mpnet-base-v2` as the worked example — 768-dim output for `"Best movie ever!"`.

The chapter forward-references **Ch 4** (choosing an embedding model for your task) and **Part II** for the downstream uses (categorization, semantic search, RAG).

## Worked code from Ch 2

```python
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("sentence-transformers/all-mpnet-base-v2")
vector = model.encode("Best movie ever!")
vector.shape  # (768,)
```

## Connections

- [[SentenceEmbedding]] — the sentence-only special case.
- [[Embedding]] — the parent.
- [[TokenEmbedding]] / [[ContextualEmbedding]] — the per-position counterpart.
- [[SentenceTransformers]] — the canonical Python library.
- [[AllMPNetBaseV2]] — the chapter's worked text-embedding model.
- [[rag]] / semantic search — downstream consumers.
- [[hands-on-llm-ch02-tokens-and-embeddings]] — source page (introduces text embeddings).
- [[hands-on-llm-ch10-creating-text-embedding-models]] — Ch 10 walks **how to create** text embedding models (training a [[SBERTArchitecture|SBERT]]-family model from scratch with [[ContrastiveLearning|contrastive learning]] / [[MultipleNegativesRankingLoss|MNR loss]] / [[CosineSimilarityLoss|cosine loss]]; fine-tuning [[AllMiniLML6V2|all-MiniLM-L6-v2]] on domain data; [[AugmentedSBERT]] for few-labels; [[TSDAE]] for no-labels). The end-to-end resolution of Ch 2's *"high-quality text embedding models tend to be trained specifically for text embedding tasks"* statement.
