---
title: "monoBERT"
type: concept
tags: [reranking, cross-encoder, bert, ir, retrieval]
sources: [hands-on-llm-ch08-semantic-search-and-rag]
last_updated: 2026-05-23
---

# monoBERT

**monoBERT** is the canonical [[CrossEncoder|cross-encoder]] reranking architecture — a [[bert|BERT]]-based model that takes a **(query, document) pair** as joint input and outputs a single scalar relevance score in [0, 1]. Introduced and named in **Nogueira & Lin** *"Multi-stage document ranking with BERT"* (2019, arXiv:1910.14424); the name distinguishes the *single-document* scoring approach from **duoBERT** (pairwise — *which of these two documents is more relevant?*).

## From [[hands-on-llm-ch08-semantic-search-and-rag|*Hands-On LLMs* Ch 8]]

Ch 8 names monoBERT as the **reference architecture** for cross-encoder reranking:

> *"One popular way of building LLM search rerankers is to present the query and each result to an LLM working as a cross-encoder. This means that a query and possible result are presented to the model at the same time allowing the model to view both these texts before it assigns a relevance score ... This method is described in more detail in a paper titled 'Multi-stage document ranking with BERT' and is sometimes referred to as monoBERT."* — Ch 8

## How it works

The monoBERT input format is the standard BERT pair-classification scheme:

```
[CLS] query tokens [SEP] document tokens [SEP]
```

BERT processes the full sequence (with full self-attention across query + document tokens — this is what makes it a **cross-encoder**), and a classification head on top of the `[CLS]` token outputs a single relevance score.

Ch 8's structural insight: **this is a classification problem**.

> *"This formulation of search as relevance scoring basically boils down to being a classification problem. Given those inputs, the model outputs a score from 0–1 where 0 is irrelevant and 1 is highly relevant. This should be familiar from our classification discussions in Chapter 4."*

The Ch 4 → Ch 8 continuity is **structural** — the same supervised-classification-head pattern that powered [[TwitterRoBERTa|Twitter-RoBERTa]] for sentiment ([[TaskSpecificModel|task-specific model]] regime in Ch 4) powers monoBERT for relevance. The only thing that changes is the input pairing and the label semantics.

## The batch-but-independent inference pattern

Ch 8's load-bearing detail about how monoBERT is run at query time:

> *"All of the documents are processed simultaneously as a batch yet each document is evaluated against the query independently. The scores then determine the new order of the results."*

This is **N forward passes** for a batch of N candidate documents — one per (query, doc) pair. The batching is GPU-parallel efficiency; the **independence** is the structural property (no cross-document attention; each pair is scored in isolation).

This is also **the reason cross-encoders are slow** — N forward passes per query is much more expensive than the **bi-encoder** alternative (one query embed + N pre-computed document embeds + cosine similarity). Cross-encoders win on quality, bi-encoders win on speed; the **two-stage pipeline** (bi-encoder for first-stage retrieval, cross-encoder reranking on top-K) is the production-default that captures both.

## Why monoBERT is the reference

Modern rerankers (Cohere Rerank, cross-encoder/ms-marco-MiniLM-L-N-v2 from sentence-transformers, [[BAAI]] bge-reranker-base) follow the monoBERT architecture template:

- Cross-encoder (joint (query, doc) input).
- Classification head producing a scalar relevance score.
- Trained on MS MARCO-style query-document-relevance triples.

Ch 8 names monoBERT as the reference; subsequent improvements are mostly engineering — smaller distillations (MiniLM), larger backbones (BGE), multi-stage pipelines (duoBERT + monoBERT cascades).

## Connections

- [[ReRanking]] — the technique family monoBERT instantiates.
- [[CrossEncoder]] — the architectural mechanism.
- [[bert|BERT]] — the underlying encoder.
- [[CohereRerank]] — managed-API counterpart Ch 8 demonstrates.
- [[SentenceTransformers]] — open-source library with monoBERT-style rerankers (cross-encoder/ms-marco-MiniLM-L-*-v2).
- [[BiEncoder]] — the speed-vs-quality complement (one query embed + many cosine sims).
- [[TaskSpecificModel]] — the Ch 4 classification-regime ancestor.
- [[MSMARCO]] — the canonical training dataset for monoBERT-style rerankers.
- [[MIRACL]] — the multilingual benchmark Ch 8 cites for the 36.5 → 62.8 nDCG@10 reranking lift.
- [[hands-on-llm-ch08-semantic-search-and-rag]] — primary source.
