---
title: "Online / Incremental Topic Modeling"
type: concept
tags: [topic-modeling, bertopic, streaming, incremental]
sources: [hands-on-llm-ch05-text-clustering-topic-modeling]
last_updated: 2026-05-23
---

# Online / Incremental Topic Modeling

A [[BERTopic]] variant for **streaming corpora** where new documents arrive continuously and the topic model must update without retraining from scratch. Replaces HDBSCAN (which is batch-only) with an incremental clusterer (e.g., MiniBatch k-means or River's online clusterers).

Named in [[hands-on-llm-ch05-text-clustering-topic-modeling|*Hands-On LLMs* Ch 5]] as one of BERTopic's algorithmic variants.

## Use cases

- **News feeds** — topics emerge / fade as headlines arrive.
- **Social-media monitoring** — real-time topic tracking.
- **Customer-support ticket streams** — keep topic taxonomy fresh as the product evolves.

## Tradeoff

Online clustering loses HDBSCAN's outlier-detection property; the streaming clusterer must accept every point into some cluster (or actively choose to flag novelty).

## Connections

- [[hands-on-llm-ch05-text-clustering-topic-modeling]] — primary source.
- [[BERTopic]] / [[TopicModeling]] — parent.
- [[DynamicTopicModeling]] — adjacent (post-hoc temporal analysis vs streaming updates).
- [[KMeansClustering]] — the typical replacement for HDBSCAN in online settings.
