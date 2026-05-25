---
title: "Guided Topic Modeling"
type: concept
tags: [topic-modeling, bertopic, semi-supervised]
sources: [hands-on-llm-ch05-text-clustering-topic-modeling]
last_updated: 2026-05-23
---

# Guided Topic Modeling

**Guided topic modeling** (also called *seeded topic modeling*) is a [[BERTopic]] algorithmic variant where the user **provides anchor words per topic** to steer cluster discovery toward themes of interest. The base pipeline ([[TextClustering|embed → UMAP → HDBSCAN → c-TF-IDF]]) is unchanged; the anchor words bias either the embedding step (pre-seeding) or the topic-assignment step.

Named in *Hands-On LLMs* Ch 5 as one of the algorithmic variants BERTopic supports — alongside [[SemiSupervisedTopicModeling|semi-supervised]], [[HierarchicalTopicModeling|hierarchical]], [[DynamicTopicModeling|dynamic]], [[MultimodalTopicModeling|multimodal]], [[OnlineTopicModeling|online/incremental]], and [[ZeroShotTopicModeling|zero-shot]] topic modeling.

## Use case

When you have **domain knowledge** about expected themes (e.g., a customer-support corpus has known categories *"billing"*, *"shipping"*, *"product quality"*) but want BERTopic to also discover unknown themes, guided topic modeling seeds the known clusters while leaving the rest of the discovery space open.

## Connections

- [[hands-on-llm-ch05-text-clustering-topic-modeling]] — primary source.
- [[BERTopic]] — the parent framework.
- [[TopicModeling]] — parent concept.
- [[SemiSupervisedTopicModeling]] / [[ZeroShotTopicModeling]] — related variants.
