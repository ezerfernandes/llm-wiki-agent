---
title: "Semi-Supervised Topic Modeling"
type: concept
tags: [topic-modeling, bertopic, semi-supervised]
sources: [hands-on-llm-ch05-text-clustering-topic-modeling]
last_updated: 2026-05-23
---

# Semi-Supervised Topic Modeling

A [[BERTopic]] variant where **some documents have known labels** and the rest are unlabeled — clustering uses the labels as constraints, pulling labeled documents into the right clusters while letting unlabeled documents fall freely.

Named in [[hands-on-llm-ch05-text-clustering-topic-modeling|*Hands-On LLMs* Ch 5]] alongside [[GuidedTopicModeling]] (anchor words), [[ZeroShotTopicModeling]] (predefined topic names), [[DynamicTopicModeling|dynamic]], [[HierarchicalTopicModeling|hierarchical]], [[MultimodalTopicModeling|multimodal]], and [[OnlineTopicModeling|online/incremental]] topic modeling.

## Use case

You have a partially-labeled corpus (e.g., 10% of customer-support tickets tagged with category) and want to **discover topics consistent with the existing labels** plus any additional unlabeled themes.

## Connections

- [[hands-on-llm-ch05-text-clustering-topic-modeling]] — primary source.
- [[BERTopic]] / [[TopicModeling]] — parent.
- [[GuidedTopicModeling]] / [[ZeroShotTopicModeling]] — related variants.
- [[UnsupervisedLearning]] / [[FewShotLearning]] — adjacent paradigms.
