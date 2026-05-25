---
title: "Siamese Network"
type: concept
tags: [architecture, training-topology, sbert, contrastive-learning, similarity]
sources: [hands-on-llm-ch10-creating-text-embedding-models]
last_updated: 2026-05-23
---

# Siamese Network

A **siamese network** is a training topology in which **two (or more) copies of the same model with shared weights** are fed two (or more) inputs, and the loss is computed over the relationship between their outputs. The classic application is **similarity learning** — feed two inputs, get two embeddings, optimize their relationship to match a target similarity.

## In [[hands-on-llm-ch10-creating-text-embedding-models|*Hands-On LLMs* Ch 10]]

Ch 10 names the siamese network as **the training architecture of [[SBERT|Sentence-BERT]]** — *"the training for sentence-transformers uses a Siamese architecture. ... we have two identical BERT models that share the same weights and neural architecture. These models are fed the sentences from which embeddings are generated through the pooling of token embeddings. Then, models are optimized through the similarity of the sentence embeddings."*

The key implementation observation: **since the weights are tied, you don't actually need two models**. *"Since the weights are identical for both BERT models, we can use a single model and feed it the sentences one after the other."* The "siamese" is conceptual — two forward passes through the same model with their losses joined.

## Why the siamese topology

The siamese topology is the structural prerequisite for [[ContrastiveLearning|contrastive learning]]: you need two encodings of two inputs in the same vector space to compute a similarity score and a loss over it. Without weight tying, the two encoders could diverge and embed "similar" inputs into different parts of vector space — defeating the purpose.

## Bi-encoder = siamese at inference

After training, the siamese network is used as a **[[BiEncoder|bi-encoder]]**: each input goes through the (single, shared-weight) encoder once and produces an embedding; pair similarity is computed downstream. Ch 10's worked example: `model.encode(sentence_1)` and `model.encode(sentence_2)` each return a 384- or 768-dim vector; `util.cos_sim(...)` computes the similarity score.

## Triplet networks

Extending siamese networks to **three** inputs (anchor / positive / negative) yields the **triplet network** — the topology used for [[TripletLoss|triplet loss]] and [[MultipleNegativesRankingLoss|MNR loss]] with explicit triplets. Per Ch 10: *"to make these triplets we start with an anchor sentence (i.e., labeled as the 'premise'), which is used to compare other sentences. Then ... we only select sentence pairs that are positive (i.e., labeled as 'entailment'). To add negative sentences, we randomly sample sentences as the 'hypothesis.'"*

## Connections

- [[SBERTArchitecture]] / [[SBERT]] — the architecture this topology trains.
- [[BiEncoder]] — siamese at inference time.
- [[ContrastiveLearning]] — the paradigm siamese topology enables.
- [[MultipleNegativesRankingLoss]] / [[CosineSimilarityLoss]] / [[SoftmaxLoss]] — the loss functions Ch 10 walks on this topology.
- [[SentenceTransformers]] — the library.
- [[hands-on-llm-ch10-creating-text-embedding-models]] — primary source.
