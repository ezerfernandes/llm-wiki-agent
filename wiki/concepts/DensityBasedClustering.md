---
title: "Density-Based Clustering"
type: concept
tags: [clustering, unsupervised, algorithm-family]
sources: [hands-on-llm-ch05-text-clustering-topic-modeling]
last_updated: 2026-05-23
---

# Density-Based Clustering

A clustering paradigm where a **cluster is a maximal region of high point density**, separated from other clusters by regions of low density. Points in low-density regions are explicitly marked as **noise / outliers**, not forced into any cluster.

## Defining property (per *Hands-On LLMs* Ch 5)

[[hands-on-llm-ch05-text-clustering-topic-modeling|Ch 5]]: *"a density-based algorithm freely calculates the number of clusters and does not force all data points to be part of a cluster."* This contrasts with [[CentroidBasedClustering|centroid-based clustering]] (e.g., [[KMeansClustering|k-means]]), which requires the number of clusters to be specified in advance and forces every point into one.

## Family members

- **[[DBSCAN]]** — Ester et al. KDD '96. Foundational; single density threshold `eps`.
- **[[HDBSCAN]]** — McInnes et al. 2017. Hierarchical variant; handles varying density.
- **OPTICS** — a related algorithm producing reachability orderings.

## When to use

- **Number of clusters unknown.**
- **Outliers should be flagged, not absorbed.**
- **Cluster shapes may be non-convex.**
- **The dataset may contain noise / niche items** (e.g., niche scientific papers in [[ArXivNLP|Ch 5's ArXiv NLP corpus]]).

When these conditions don't hold — e.g., you have a fixed number of customer segments to find — [[KMeansClustering|k-means]] / [[CentroidBasedClustering|centroid-based]] methods are usually preferred.

## Connections

- [[hands-on-llm-ch05-text-clustering-topic-modeling]] — primary source.
- [[DBSCAN]] / [[HDBSCAN]] — the canonical members.
- [[CentroidBasedClustering]] / [[KMeansClustering]] — the contrasted family.
- [[Outlier]] — what density-based methods explicitly handle.
- [[TextClustering]] / [[BERTopic]] — the modern NLP consumer.
