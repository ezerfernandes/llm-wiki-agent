---
title: "Sentence Embedding"
type: concept
tags: [nlp, embeddings, semantic-search]
sources: [hands-on-llm-ch02-tokens-and-embeddings, hands-on-llm-ch05-text-clustering-topic-modeling, hands-on-llm-ch10-creating-text-embedding-models]
last_updated: 2026-05-23
---

# Sentence Embedding

A [[TextEmbedding|text embedding]] whose unit is a **single sentence** — one fixed-dim dense vector representing the entire sentence's meaning. The canonical training recipe is [[SentenceTransformers|Sentence-BERT]] (Reimers & Gurevych, 2019).

## From [[hands-on-llm-ch02-tokens-and-embeddings|*Hands-On LLMs* Ch 2]]

The chapter does not separate "sentence" from "text" embeddings sharply — both fall under the [[TextEmbedding|text-embedding]] umbrella. The worked example, `model.encode("Best movie ever!")` producing a 768-dim vector via `sentence-transformers/all-mpnet-base-v2`, is a sentence embedding by convention (a single short sentence in, one vector out).

The two production routes per Ch 2:
1. Mean-pool [[ContextualEmbedding|contextualized token embeddings]] from a generic encoder.
2. Use a model trained specifically for sentence-embedding tasks — typically with a **siamese-network contrastive objective** (the [[SkipGram|skip-gram-style]] contrastive training Ch 2 names as the prototype of "any model that takes two vectors and predicts a relation").

## From [[hands-on-llm-ch05-text-clustering-topic-modeling|*Hands-On LLMs* Ch 5]]

Ch 5's [[BERTopic]] pipeline starts with sentence embeddings of each ArXiv abstract — produced by [[GTESmall|`thenlper/gte-small`]] (384-dim). The chapter establishes the embedding-as-substrate thesis at scale: 44,949 abstracts × 384 dims is the input matrix for [[UMAP]] → [[HDBSCAN]] → [[ClassBasedTFIDF|c-TF-IDF]]. The chapter explicitly notes that **embedding model choice matters more than any other pipeline component** for clustering quality, and recommends consulting the [[MTEB]] leaderboard's *clustering column* (not the average score) when selecting one.

## Connections

- [[TextEmbedding]] — the broader parent.
- [[Embedding]] — the umbrella concept.
- [[ContextualEmbedding]] / [[TokenEmbedding]] — the per-token counterparts pool-able into sentence embeddings.
- [[SentenceTransformers]] — the canonical library.
- [[AllMPNetBaseV2]] — Ch 2's worked example.
- [[GTESmall]] — Ch 5's clustering-optimized choice.
- [[rag]] / semantic search / [[ColBERTv2]] — downstream consumers.
- [[BERTopic]] / [[TextClustering]] — Ch 5's downstream consumer pipeline.
- [[hands-on-llm-ch02-tokens-and-embeddings]] — Ch 2 source page.
- [[hands-on-llm-ch05-text-clustering-topic-modeling]] — Ch 5 source page.
- [[hands-on-llm-ch10-creating-text-embedding-models]] — Ch 10's full **training** recipe for sentence embeddings: [[SBERTArchitecture|SBERT architecture]] ([[SiameseNetwork|siamese]] [[bert|BERT]] + [[MeanPooling|mean-pooling]]) + [[MultipleNegativesRankingLoss|MNR loss]] / [[CosineSimilarityLoss|cosine loss]] on [[MNLI|NLI]] data; [[AugmentedSBERT]] for few-labels; [[TSDAE]] for no-labels. Resolves Ch 2's forward reference to *"a model trained specifically for sentence-embedding tasks — typically with a siamese-network contrastive objective."*
