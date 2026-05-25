---
title: "Seeded Topic Modeling"
type: concept
tags: [topic-modeling, bertopic, seeded, guided, semi-supervised]
sources: [hands-on-llm-ch05-text-clustering-topic-modeling]
last_updated: 2026-05-23
---

# Seeded Topic Modeling

**Seeded topic modeling** — also called **guided topic modeling** — is a [[TopicModeling|topic-modeling]] variant in which the practitioner supplies **seed words** (or seed topics) that nudge the algorithm toward specific themes. The seeds bias either the term-weighting step (so seed-related terms surface in topic representations) or the clustering step (so documents containing seeds tend to cluster together).

## From [[hands-on-llm-ch05-text-clustering-topic-modeling|*Hands-On LLMs* Ch 5]]

Ch 5 names **guided / seeded topic modeling** as one of [[BERTopic]]'s many algorithmic variants (alongside [[HierarchicalTopicModeling|hierarchical]], [[DynamicTopicModeling|dynamic]], [[SemiSupervisedTopicModeling|semi-supervised]], [[MultimodalTopicModeling|multimodal]], [[OnlineTopicModeling|online]], and [[ZeroShotTopicModeling|zero-shot]] topic modeling). All variants share the same modular two-stage backbone — *"each part of the pipeline is completely replaceable with another, similar algorithm"* — and customize the topic-representation or clustering step.

In BERTopic, seeded topic modeling is exposed via `BERTopic(seed_topic_list=[["word1","word2"],["word3","word4"], ...])`, where each inner list is a seed topic that BERTopic tries to align discovered clusters with.

## Connections

- [[hands-on-llm-ch05-text-clustering-topic-modeling]] — primary source.
- [[GuidedTopicModeling]] — synonym (Ch 5 uses both labels interchangeably).
- [[BERTopic]] — the framework that exposes seeded modeling as a variant.
- [[TopicModeling]] — parent concept.
- [[SemiSupervisedTopicModeling]] / [[ZeroShotTopicModeling]] — sibling variants on the labels-vs-no-labels axis.
