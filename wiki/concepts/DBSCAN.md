---
title: "DBSCAN"
type: concept
tags: [clustering, density-based, unsupervised]
sources: [hands-on-llm-ch05-text-clustering-topic-modeling]
last_updated: 2026-05-23
---

# DBSCAN

**DBSCAN** — *Density-Based Spatial Clustering of Applications with Noise* — is the foundational [[DensityBasedClustering|density-based clustering]] algorithm ([[MartinEster|Ester]] et al., *"A density-based algorithm for discovering clusters in large spatial databases with noise."* KDD '96: 226–231). [[HDBSCAN]] is its hierarchical successor.

## Core idea

A cluster is a **maximal connected region of density-reachable points**. Points outside any such region are **noise**. Parameters:

- **`eps`** — radius around each point used to test density.
- **`minPts`** — minimum number of points within `eps` for a point to be a *core point*.

Three point types: **core** (dense), **border** (in a cluster but not dense), **noise** (outliers).

## Limitations vs [[HDBSCAN]]

- DBSCAN takes a single global `eps` — struggles when clusters have varying densities.
- HDBSCAN builds a **hierarchy of density-based clusterings** at multiple scales and condenses them, so a single dataset can contain clusters of different densities.

Per [[hands-on-llm-ch05-text-clustering-topic-modeling|*Hands-On LLMs* Ch 5]]: HDBSCAN *"is a hierarchical variation of a clustering algorithm called DBSCAN that allows for dense (micro)-clusters to be found without having to explicitly specify the number of clusters."*

## Connections

- [[HDBSCAN]] — the hierarchical successor.
- [[DensityBasedClustering]] — the algorithm family.
- [[MartinEster]] — DBSCAN's lead author.
- [[KMeansClustering]] — the centroid-based contrast.
- [[Outlier]] — explicit handling.
- [[hands-on-llm-ch05-text-clustering-topic-modeling]] — primary source.
