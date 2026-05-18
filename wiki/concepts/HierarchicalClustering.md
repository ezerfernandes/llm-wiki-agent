---
title: "Hierarchical Clustering"
type: concept
tags: [unsupervised, clustering]
sources: [islr-seventh-printing]
last_updated: 2026-05-16
---

# Hierarchical Clustering

Bottom-up (*agglomerative*) clustering: start with each point its own cluster, then iteratively merge the closest pair until one cluster remains. *Linkage* (single, complete, average, centroid) defines inter-cluster distance. Result visualized as a [[Dendrogram]] — cut at any height for a clustering.

## Connections
- [[islr-seventh-printing]] — Ch.10.3.2.
- [[KMeansClustering]] — sibling clustering method.
- [[Dendrogram]] — output visualization.
- [[UnsupervisedLearning]] — parent paradigm.
