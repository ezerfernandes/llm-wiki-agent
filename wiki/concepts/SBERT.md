---
title: "SBERT (Sentence-BERT)"
type: concept
tags: [model-family, embeddings, sbert, bi-encoder, siamese]
sources: [hands-on-llm-ch10-creating-text-embedding-models]
last_updated: 2026-05-23
---

# SBERT (Sentence-BERT)

**Sentence-BERT** — the model family that pioneered modern [[TextEmbedding|text-embedding]] models. Introduced by [[NilsReimers|Reimers]] & [[IrynaGurevych|Gurevych]] (EMNLP 2019, arXiv:1908.10084 — *"Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks"*).

Per [[hands-on-llm-ch10-creating-text-embedding-models|*Hands-On LLMs* Ch 10]]: *"The resulting architecture is also referred to as a bi-encoder or SBERT for sentence-BERT."* The model = a [[bert|BERT]]-derived encoder + a [[MeanPooling|mean-pooling]] layer over the final layer's token embeddings, trained siamese-style with a contrastive objective.

## What SBERT is vs is not

- **What SBERT IS**: a way to use BERT to produce **reusable, fixed-size sentence embeddings** that are semantically meaningful under cosine similarity.
- **What SBERT IS NOT**: a [[CrossEncoder|cross-encoder]]. SBERT does not output a single similarity score for a pair of sentences; it outputs an embedding per sentence. Pair similarity is computed downstream as cosine similarity of the two embeddings.

## Family of models

The [[SentenceTransformers|sentence-transformers]] library hosts hundreds of SBERT-family checkpoints. The most-cited:

- `all-MiniLM-L6-v2` — 384-dim, the most popular small/fast default ([[AllMiniLML6V2]]).
- `all-mpnet-base-v2` — 768-dim, the higher-quality default ([[AllMPNetBaseV2]]).
- `bge-small-en-v1.5` / `gte-small` / `e5-small-v2` — newer SBERT-family models that compete on the [[MTEB]] leaderboard.

## See also

- [[SBERTArchitecture]] — the architectural recipe.
- [[BiEncoder]] / [[SiameseNetwork]] — the structural framings.
- [[MeanPooling]] — the default pooling.
- [[ContrastiveLearning]] — the training paradigm.
- [[SentenceTransformers]] — the library.
- [[NilsReimers]] / [[IrynaGurevych]] — the authors.
- [[hands-on-llm-ch10-creating-text-embedding-models]] — primary source.
