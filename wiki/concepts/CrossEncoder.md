---
title: "Cross-Encoder"
type: concept
tags: [llm-engineering]
sources: [leh-ch04-rag-feature-pipeline, leh-ch09-rag-inference-pipeline, hands-on-llm-ch08-semantic-search-and-rag, hands-on-llm-ch10-creating-text-embedding-models]
last_updated: 2026-05-23
---

## Definition
Transformer model that scores a (query, document) pair jointly.

## In LLM Engineer's Handbook
A cross-encoder takes a `(text_a, text_b)` pair jointly (concatenated with a separator) and outputs a single scalar relevance score — contrasting with a bi-encoder that embeds independently and compares via [[CosineSimilarity]]. Slower but more accurate. Per [[leh-ch04-rag-feature-pipeline]] and [[leh-ch09-rag-inference-pipeline]] the standard pattern is bi-encoder retrieval + cross-encoder [[ReRanking]]. Common checkpoints: `cross-encoder/ms-marco-MiniLM-L-6-v2`, `BAAI/bge-reranker-base`.

## From [[hands-on-llm-ch08-semantic-search-and-rag|*Hands-On LLMs* Ch 8]]

Ch 8 names the cross-encoder as **the structural mechanism of LLM rerankers**:

> *"One popular way of building LLM search rerankers is to present the query and each result to an LLM working as a cross-encoder. This means that a query and possible result are presented to the model at the same time allowing the model to view both these texts before it assigns a relevance score."* — Ch 8

The Ch 8 contribution beyond the LEH treatment is naming **[[MonoBERT|monoBERT]]** as the canonical reference cross-encoder architecture:

> *"This method is described in more detail in a paper titled 'Multi-stage document ranking with BERT' and is sometimes referred to as monoBERT."* — Ch 8

**The batch-but-independent inference pattern:** *"All of the documents are processed simultaneously as a batch yet each document is evaluated against the query independently. The scores then determine the new order of the results."* This is N forward passes per query (vs the bi-encoder's 1 query embed + N pre-computed document embeds + cosine sims) — the **structural reason cross-encoders are slow but accurate**, motivating the **two-stage pipeline** (bi-encoder retrieval + cross-encoder reranking) as the production default.

**The classification-problem framing:** *"This formulation of search as relevance scoring basically boils down to being a classification problem. Given those inputs, the model outputs a score from 0–1 where 0 is irrelevant and 1 is highly relevant."* Ch 8 explicitly back-references Ch 4's classification framing.

**The worked managed-API receipt** Ch 8 uses is [[CohereRerank|`co.rerank`]] — a black-box cross-encoder over Cohere's managed-model stack; no training/tuning required.

## Connections (consolidated)

- [[ReRanking]] — the technique family cross-encoders power.
- [[MonoBERT]] — the named reference cross-encoder architecture (Ch 8).
- [[BiEncoder]] — the speed-vs-quality complement (independent embeddings + cosine sim).
- [[CohereRerank]] — Cohere's managed cross-encoder API.
- [[SentenceTransformers]] — open-source library with cross-encoder checkpoints (`cross-encoder/ms-marco-*`).
- [[BAAI]] — produces the `bge-reranker-*` cross-encoder family.
- [[bert|BERT]] — the underlying encoder.
- [[hands-on-llm-ch08-semantic-search-and-rag]] — primary source.
- [[leh-ch04-rag-feature-pipeline]] / [[leh-ch09-rag-inference-pipeline]] — LEH coverage.
- [[hands-on-llm-ch10-creating-text-embedding-models]] — Ch 10's use of cross-encoders in Augmented SBERT (see section below).

## From [[hands-on-llm-ch10-creating-text-embedding-models|*Hands-On LLMs* Ch 10]]

Ch 10 codifies the **structural reason** cross-encoders cannot be the default at inference time but are useful at training time:

> *"A cross-encoder allows two sentences to be passed to the Transformer network simultaneously to predict the extent to which the two sentences are similar. It does so by adding a classification head to the original architecture that can output a similarity score. However, the number of computations rises quickly when you want to find the highest pair in a collection of 10,000 sentences. That would require $n \cdot (n-1)/2 = 49{,}995{,}000$ inference computations and therefore generates significant overhead. Moreover, a cross-encoder generally does not generate embeddings."* — Ch 10

**The bi-encoder / cross-encoder tradeoff restated**: *"Although a bi-encoder is quite fast and creates accurate sentence representations, cross-encoders generally achieve better performance than a bi-encoder but do not generate embeddings."*

**[[AugmentedSBERT]] — the chapter's worked use of cross-encoders at training time** (not inference):

1. Fine-tune a `CrossEncoder("bert-base-uncased", num_labels=2)` on a small **gold dataset** (10,000 labeled MNLI pairs).
2. Use the fine-tuned cross-encoder to label a much larger pool of unlabeled pairs (40,000) → **silver dataset**.
3. Train a [[BiEncoder|bi-encoder]] (SBERT) on the **gold + silver** union.

In code:

```python
from sentence_transformers.cross_encoder import CrossEncoder
cross_encoder = CrossEncoder("bert-base-uncased", num_labels=2)
cross_encoder.fit(train_dataloader=gold_dataloader, epochs=1, ...)

# Label silver pool
output = cross_encoder.predict(pairs, apply_softmax=True)
silver_labels = np.argmax(output, axis=1)
```

**MarginMSE loss** for training cross-encoders is mentioned: *"a loss like MarginMSE works great for training or fine-tuning a cross-encoder."*

This Ch 10 framing complements Ch 8's framing of cross-encoders as **reranking primitives** (run them on a short list of candidate documents, never on the full corpus). Same architectural object, two different production roles: **reranker at inference** (Ch 8) and **silver-dataset labeler at training** (Ch 10).
