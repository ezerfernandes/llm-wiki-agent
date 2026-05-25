---
title: "Centroid-Based Clustering"
type: concept
tags: [clustering, unsupervised, algorithm-family]
sources: [hands-on-llm-ch05-text-clustering-topic-modeling]
last_updated: 2026-05-23
---

# Centroid-Based Clustering

A clustering paradigm where each cluster is represented by a **centroid** (a representative point — typically the mean of cluster members) and points are assigned to their nearest centroid. The canonical member is [[KMeansClustering|k-means]].

## Defining property

The number of clusters `K` must be **specified in advance**, and **every point is assigned to exactly one cluster** — there is no native notion of outliers.

Per [[hands-on-llm-ch05-text-clustering-topic-modeling|*Hands-On LLMs* Ch 5]]: *"a centroid-based algorithm like k-means ... requires a set of clusters to be generated, [and] we do not know the number of clusters beforehand."* This motivates Ch 5's preference for [[DensityBasedClustering|density-based clustering]] ([[HDBSCAN]]) on the ArXiv NLP dataset.

## When centroid-based wins

- **`K` is known or fixed** (e.g., segmentation into a known number of categories).
- **Every point should be assigned to a cluster** — no outliers tolerated.
- **Clusters are convex / roughly spherical** — k-means assumes this implicitly.

[[BERTopic]] explicitly supports swapping HDBSCAN for k-means when outliers are unwanted.

## Family members

- **[[KMeansClustering|k-means]]** — the canonical algorithm.
- **k-medoids** — uses actual data points as centroids (more robust to outliers than k-means).
- **Mini-batch k-means** — scalable variant.
- **Bisecting k-means** — hierarchical variant.

## Connections

- [[KMeansClustering]] — the canonical member.
- [[DensityBasedClustering]] / [[DBSCAN]] / [[HDBSCAN]] — the contrasted family.
- [[HierarchicalClustering]] — a third clustering paradigm (linkage-based).
- [[BERTopic]] / [[TextClustering]] — modern NLP consumer.
- [[hands-on-llm-ch05-text-clustering-topic-modeling]] — primary source.
