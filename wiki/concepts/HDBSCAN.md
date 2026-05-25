---
title: "HDBSCAN (Hierarchical Density-Based Spatial Clustering of Applications with Noise)"
type: concept
tags: [clustering, density-based, unsupervised, hdbscan, outlier-detection]
sources: [hands-on-llm-ch05-text-clustering-topic-modeling]
last_updated: 2026-05-23
---

# HDBSCAN

**HDBSCAN** — **Hierarchical Density-Based Spatial Clustering of Applications with Noise** — is a [[DensityBasedClustering|density-based]] clustering algorithm ([[LelandMcInnes|McInnes]], Healy & Astels, *J. Open Source Softw.* 2.11 (2017): 205). A **hierarchical variant** of [[DBSCAN]] (Ester et al., KDD '96), it finds dense micro-clusters at varying density scales without requiring the number of clusters to be specified in advance, and explicitly **detects outliers** (label `-1`).

## Why HDBSCAN over k-means (per *Hands-On LLMs* Ch 5)

[[hands-on-llm-ch05-text-clustering-topic-modeling|Ch 5]]: *"Although a common choice is a centroid-based algorithm like k-means, which requires a set of clusters to be generated, we do not know the number of clusters beforehand. Instead, a density-based algorithm freely calculates the number of clusters and does not force all data points to be part of a cluster."*

| | [[KMeansClustering|k-means]] | HDBSCAN |
|---|---|---|
| Requires `K` (# clusters) | Yes | No |
| Forces every point into a cluster | Yes | **No** — outliers labeled `-1` |
| Cluster shape | Convex / spherical | Arbitrary density-based |
| Handles noise | Poorly | **Designed for it** |

## Parameters (per Ch 5)

```python
from hdbscan import HDBSCAN
hdbscan_model = HDBSCAN(
    min_cluster_size=50, metric="euclidean", cluster_selection_method="eom"
).fit(reduced_embeddings)
clusters = hdbscan_model.labels_
```

- **`min_cluster_size`** — the minimum number of points required to form a cluster. **Lower** = more clusters. Ch 5 uses `50`.
- **`metric`** — distance metric. Ch 5 uses `'euclidean'` because the UMAP output is already low-dimensional (5D), where Euclidean works well.
- **`cluster_selection_method`** — `'eom'` (Excess of Mass; default; produces larger, more stable clusters) or `'leaf'` (more fine-grained micro-clusters).

## Outlier handling

HDBSCAN's signature feature: points in low-density regions are **not assigned to any cluster** and instead get label `-1`. In [[BERTopic]], these become **topic `-1`** — a useful catch-all for niche, off-topic, or noisy documents. On Ch 5's 44,949-abstract ArXiv NLP corpus, **14,520 abstracts** end up in topic `-1`.

To eliminate outliers in BERTopic:
- Swap HDBSCAN for [[KMeansClustering|k-means]] in the pipeline (k-means forces every point into a cluster), or
- Use BERTopic's `reduce_outliers()` function to reassign outliers post-hoc.

## Versus DBSCAN

DBSCAN ([[MartinEster|Ester]] et al. KDD '96) takes a single density threshold `eps`. HDBSCAN builds a **hierarchy of density-based clusterings at varying scales** and then **condenses the tree** to a flat clustering — robust to varying densities across the dataset.

Note: HDBSCAN's *"hierarchical"* is **not** the same as [[HierarchicalClustering|agglomerative hierarchical clustering]] (ISLR Ch 10.3.2), which is bottom-up with linkage. The two share the name but use different mechanisms.

## Output

`hdbscan_model.labels_` is a 1D array of cluster IDs in `{-1, 0, 1, ..., K-1}` where `K` is the number of clusters found and `-1` denotes outliers. Ch 5's dataset: `len(set(clusters)) == 156` (155 clusters + the outlier label).

## Connections

- [[hands-on-llm-ch05-text-clustering-topic-modeling]] — primary source.
- [[DBSCAN]] — the parent algorithm.
- [[DensityBasedClustering]] — the family.
- [[KMeansClustering]] — the centroid-based alternative.
- [[HierarchicalClustering]] — a *different* sense of "hierarchical clustering" (agglomerative); HDBSCAN's hierarchy is density-based.
- [[Outlier]] — what HDBSCAN explicitly detects.
- [[UMAP]] — the standard upstream dimensionality reducer.
- [[BERTopic]] / [[TextClustering]] / [[TopicModeling]] — standard consumers.
- [[HDBSCANLibrary|hdbscan]] — the Python package.
- [[LelandMcInnes]] — HDBSCAN's lead author.
