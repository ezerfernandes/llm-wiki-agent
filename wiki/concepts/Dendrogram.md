---
title: "Dendrogram"
type: concept
tags: [visualization, clustering]
sources: [islr-seventh-printing, hands-on-llm-ch05-text-clustering-topic-modeling]
last_updated: 2026-05-23
---

# Dendrogram

Tree diagram representing nested merges produced by [[HierarchicalClustering]]. Leaves are observations; the height of each merge encodes inter-cluster distance. Horizontal cuts at chosen heights yield flat clusterings.

## Connections
- [[islr-seventh-printing]] — Ch.10.3.2.
- [[hands-on-llm-ch05-text-clustering-topic-modeling]] — dendrograms also produced by [[HDBSCAN]]'s condensed-tree visualization and by [[BERTopic]]'s `visualize_hierarchy()` (hierarchical topic relationships).
- [[HierarchicalClustering]] — produces it.
- [[HDBSCAN]] — produces a different style of dendrogram (density-based condensed tree).
- [[HierarchicalTopicModeling]] / [[BERTopic]] — topic-level dendrograms.
