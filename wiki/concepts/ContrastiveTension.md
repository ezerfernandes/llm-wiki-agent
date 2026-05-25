---
title: "Contrastive Tension (CT)"
type: concept
tags: [unsupervised, embeddings, contrastive-learning, sentence-transformers]
sources: [hands-on-llm-ch10-creating-text-embedding-models]
last_updated: 2026-05-23
---

# Contrastive Tension (CT)

**Contrastive Tension** — an unsupervised technique for sentence embeddings introduced by Carlsson, Mossberg, Heimann, Sahlgren et al. (*"Semantic Re-tuning with Contrastive Tension,"* International Conference on Learning Representations, 2021).

Per [[hands-on-llm-ch10-creating-text-embedding-models|*Hands-On LLMs* Ch 10]]: Contrastive Tension is one of four named unsupervised techniques (alongside [[SimCSE]], [[TSDAE]], [[GPL]]) for creating sentence embeddings without labels. Ch 10 names it but does not walk a code example, focusing instead on TSDAE for its *"great performance on unsupervised tasks as well as domain adaptation."*

## The CT trick

Train **two copies** of the same encoder with different weights, then **align them** via a contrastive objective: the two copies should produce similar embeddings for the same sentence and dissimilar embeddings for different sentences. Over time, the two encoders converge on a representation that is robust under the disagreement they started with.

## Connections

- [[ContrastiveLearning]] — the paradigm.
- [[TSDAE]] / [[SimCSE]] / [[GPL]] — the other unsupervised techniques Ch 10 names.
- [[SentenceTransformers]] — supports CT via specific loss configurations.
- [[hands-on-llm-ch10-creating-text-embedding-models]] — primary source for the named-but-not-walked mention.
