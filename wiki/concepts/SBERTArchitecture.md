---
title: "SBERT Architecture"
type: concept
tags: [architecture, embeddings, siamese, bi-encoder, contrastive-learning, sbert]
sources: [hands-on-llm-ch10-creating-text-embedding-models]
last_updated: 2026-05-23
---

# SBERT Architecture

The **Sentence-BERT (SBERT) architecture** — the design that became the de-facto default for [[TextEmbedding|text-embedding]] models. Introduced by [[NilsReimers|Reimers]] & [[IrynaGurevych|Gurevych]] (EMNLP 2019, arXiv:1908.10084 — *"Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks"*). It is the architecture the [[SentenceTransformers|sentence-transformers]] library implements.

## The three architectural moves

Per [[hands-on-llm-ch10-creating-text-embedding-models|*Hands-On LLMs* Ch 10]]:

1. **Drop the classification head** of the original cross-encoder BERT-for-similarity setup. *"In sentence-transformers the classification head is dropped."*
2. **Add a [[MeanPooling|mean-pooling]] layer** on top of the final BERT output layer. *"Mean pooling is used on the final output layer to generate an embedding. This pooling layer averages the word embeddings and gives back a fixed dimensional output vector. This ensures a fixed-size embedding."*
3. **Train siamese** — *"we have two identical BERT models that share the same weights and neural architecture. ... Since the weights are identical for both BERT models, we can use a single model and feed it the sentences one after the other."* See [[SiameseNetwork]].

## Why this design

Per Ch 10, the previous default — using a [[CrossEncoder|cross-encoder]] — *"generates significant overhead. ... finding the highest pair in a collection of 10,000 sentences ... would require $n \cdot (n-1)/2 = 49{,}995{,}000$ inference computations. Moreover, a cross-encoder generally does not generate embeddings."* And the naive fallback (mean-pool a generic BERT) was **worse than averaging GloVe vectors** — *"averaging its output layer or using the [CLS] token ... has shown to be worse than simply averaging word vectors, like GloVe."*

SBERT solves both problems: it produces **reusable embeddings** (one forward pass per sentence, then any-pair cosine-similarity is trivial) while training the encoder end-to-end with a **contrastive objective** so the geometry actually captures sentence similarity.

## The training objective

In the original SBERT formulation: *"During training, the embeddings for each sentence are concatenated together with the difference between the embeddings. Then, this resulting embedding is optimized through a softmax classifier."* This is the [[SoftmaxLoss|softmax loss]] (3-way classification over [[NLI]] labels: entailment / neutral / contradiction). Modern sentence-transformers training has moved to [[CosineSimilarityLoss|cosine similarity loss]] and [[MultipleNegativesRankingLoss|MNR loss]] which substantially outperform softmax (Ch 10's worked ladder: softmax 0.59 → cosine 0.72 → MNR 0.80 STS-B Pearson cosine).

## The bi-encoder framing

The output architecture is the **[[BiEncoder|bi-encoder]]** — query and document each encoded independently into the same vector space, compared via [[CosineSimilarity|cosine similarity]]. The structural complement of the [[CrossEncoder|cross-encoder]] (encodes the pair jointly). Per Ch 10: *"The resulting architecture is also referred to as a bi-encoder or SBERT for sentence-BERT. Although a bi-encoder is quite fast and creates accurate sentence representations, cross-encoders generally achieve better performance than a bi-encoder but do not generate embeddings."*

## All-layers trainable by default

Ch 10 notes: *"By default, all layers of an LLM in sentence-transformers are trainable. Although it is possible to freeze certain layers, it is generally not advised since the performance is often better when unfreezing all layers."*

## Connections

- [[SBERT]] — the model family this architecture produces.
- [[SentenceTransformers]] — the Python library implementing the architecture.
- [[SiameseNetwork]] — the training topology.
- [[MeanPooling]] — the default pooling layer.
- [[CLSPooling]] — the [TSDAE]-only alternative.
- [[BiEncoder]] / [[CrossEncoder]] — the structural pair.
- [[ContrastiveLearning]] — the training paradigm.
- [[SoftmaxLoss]] / [[CosineSimilarityLoss]] / [[MultipleNegativesRankingLoss]] — the loss-function ladder Ch 10 walks.
- [[NilsReimers]] / [[IrynaGurevych]] — Sentence-BERT authors.
- [[bert|BERT]] — the underlying encoder.
- [[hands-on-llm-ch10-creating-text-embedding-models]] — primary source.
