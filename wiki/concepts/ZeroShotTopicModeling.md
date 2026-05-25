---
title: "Zero-Shot Topic Modeling"
type: concept
tags: [topic-modeling, bertopic, zero-shot]
sources: [hands-on-llm-ch05-text-clustering-topic-modeling]
last_updated: 2026-05-23
---

# Zero-Shot Topic Modeling

A [[BERTopic]] variant where you **pre-define a list of topics by name** (e.g., *"machine translation"*, *"sentiment analysis"*, *"speech recognition"*) and BERTopic **assigns documents to the closest predefined topic** by embedding similarity — with documents that don't match any predefined topic flagged as outliers (the *"open-vocabulary"* fraction).

Named in [[hands-on-llm-ch05-text-clustering-topic-modeling|*Hands-On LLMs* Ch 5]] as one of BERTopic's algorithmic variants.

## Mechanism

1. **Embed** the predefined topic names with the same embedding model used for documents.
2. For each document, compute cosine similarity to every topic embedding.
3. Assign to the topic with the highest similarity *if* it exceeds a threshold; otherwise label as outlier.
4. Optionally **discover new topics** among the outliers using the standard BERTopic pipeline.

This is the **topic-modeling analogue** of [[ZeroShotClassification|zero-shot classification via label embeddings]] from [[hands-on-llm-ch04-text-classification|Ch 4]] — same trick (embed the labels in the same space as the documents and compare by cosine), applied to topic discovery rather than category prediction.

## Use case

You **know** the topics you care about but want to:
- Identify which documents are about each topic.
- Discover what topics exist **outside** your predefined list.

## Connections

- [[hands-on-llm-ch05-text-clustering-topic-modeling]] — primary source.
- [[BERTopic]] / [[TopicModeling]] — parent.
- [[ZeroShotClassification]] / [[ZeroShotLearning]] — the broader zero-shot pattern.
- [[LabelEmbedding]] — the embedding-the-label trick.
- [[CosineSimilarity]] — the assignment metric.
- [[GuidedTopicModeling]] / [[SemiSupervisedTopicModeling]] — adjacent variants.
