---
title: "hdbscan (Python package)"
type: entity
tags: [library, python, hdbscan, density-based-clustering, unsupervised]
sources: [hands-on-llm-ch05-text-clustering-topic-modeling]
last_updated: 2026-05-23
---

# hdbscan (Python package)

**`hdbscan`** is the canonical Python implementation of the [[HDBSCAN]] algorithm — *"Hierarchical Density-Based Spatial Clustering of Applications with Noise"* — maintained by [[LelandMcInnes|Leland McInnes]], John Healy, and Steve Astels (*J. Open Source Softw.* 2.11 (2017): 205). Installable as `pip install hdbscan`; imported as `from hdbscan import HDBSCAN`.

## From [[hands-on-llm-ch05-text-clustering-topic-modeling|*Hands-On LLMs* Ch 5]]

Ch 5 uses `hdbscan` as the clustering step of the BERTopic pipeline:

```python
from hdbscan import HDBSCAN
hdbscan_model = HDBSCAN(
    min_cluster_size=50, metric='euclidean', cluster_selection_method='eom'
).fit(reduced_embeddings)
clusters = hdbscan_model.labels_   # {-1, 0, 1, ..., 154}
```

The fitted model's `.labels_` attribute provides the cluster assignment for each input point; the special label `-1` marks outliers. On Ch 5's 44,949-abstract ArXiv NLP dataset, `len(set(clusters)) == 156` (155 clusters + outlier label).

## Connections

- [[hands-on-llm-ch05-text-clustering-topic-modeling]] — primary source.
- [[HDBSCAN]] — the algorithm the package implements.
- [[LelandMcInnes]] — lead maintainer.
- [[UMAPLibrary|umap-learn]] — the standard upstream dimensionality-reduction package.
- [[BERTopic]] — the framework that ships `hdbscan` as a default dependency.
- [[Outlier]] — the `-1` label `hdbscan` produces.
