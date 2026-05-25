---
title: "Hierarchical Clustering"
type: concept
tags: [unsupervised, clustering]
sources: [islr-seventh-printing, hands-on-llm-ch05-text-clustering-topic-modeling]
last_updated: 2026-05-23
---

# Hierarchical Clustering

Bottom-up (*agglomerative*) clustering: start with each point its own cluster, then iteratively merge the closest pair until one cluster remains. *Linkage* (single, complete, average, centroid) defines inter-cluster distance. Result visualized as a [[Dendrogram]] — cut at any height for a clustering.

## Distinct from "hierarchical" in [[HDBSCAN]]

Note: [[HDBSCAN]] (introduced by [[hands-on-llm-ch05-text-clustering-topic-modeling|*Hands-On LLMs* Ch 5]]) also uses the word *"hierarchical"* — but it refers to a **hierarchy of density-based clusterings at varying scales**, condensed to a flat clustering, not to bottom-up agglomerative merging with linkage. The two senses share the name but use different mechanisms.

## From [[hands-on-llm-ch05-text-clustering-topic-modeling|*Hands-On LLMs* Ch 5]]

Ch 5 names **hierarchical topic modeling** ([[HierarchicalTopicModeling]]) as a [[BERTopic]] variant — but the hierarchy there operates on **topics produced by HDBSCAN**, not on raw points via ISLR-style agglomerative clustering. The variant builds a topic tree by recursively merging similar topics (via topic-embedding cosine similarity), enabling drill-down from coarse to fine topics.

## Connections
- [[islr-seventh-printing]] — Ch.10.3.2.
- [[hands-on-llm-ch05-text-clustering-topic-modeling]] — Ch 5 names a different sense of "hierarchical" via HDBSCAN.
- [[KMeansClustering]] — sibling clustering method.
- [[Dendrogram]] — output visualization.
- [[UnsupervisedLearning]] — parent paradigm.
- [[HDBSCAN]] — different sense of "hierarchical" clustering.
- [[HierarchicalTopicModeling]] — BERTopic variant.
