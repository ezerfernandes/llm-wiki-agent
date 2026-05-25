---
title: "Hierarchical Topic Modeling"
type: concept
tags: [topic-modeling, bertopic, hierarchical]
sources: [hands-on-llm-ch05-text-clustering-topic-modeling]
last_updated: 2026-05-23
---

# Hierarchical Topic Modeling

**Hierarchical topic modeling** organizes topics into a **tree** where leaf-topics are fine-grained themes and parent-nodes merge related leaf-topics into broader themes. In [[BERTopic]] (per *Hands-On LLMs* Ch 5), it is implemented by computing **pairwise similarity between topic embeddings** and merging the closest topics iteratively, producing a `visualize_hierarchy()` dendrogram of the topic landscape.

This **is not** the same as [[HierarchicalClustering|agglomerative hierarchical clustering]] of *documents* — it is hierarchical clustering of **already-discovered topics** for navigation / aggregation.

## Use cases

- **Drill-down topic browsing** — start at coarse parent topics, navigate down to specific subtopics.
- **Topic-count tuning** — pick how many topics to expose downstream by cutting the dendrogram at a chosen depth.
- **Topic merging** — manually merge over-fragmented topics into coherent themes.

## Visualization

```python
topic_model.visualize_hierarchy()  # interactive Plotly dendrogram
```

## Connections

- [[hands-on-llm-ch05-text-clustering-topic-modeling]] — primary source.
- [[BERTopic]] / [[TopicModeling]] — parent.
- [[HierarchicalClustering]] — a different sense (agglomerative bottom-up of documents).
- [[Dendrogram]] — the standard visualization.
