---
title: "umap-learn"
type: entity
tags: [library, python, umap, dimensionality-reduction, unsupervised]
sources: [hands-on-llm-ch05-text-clustering-topic-modeling]
last_updated: 2026-05-23
---

# umap-learn

**`umap-learn`** is the canonical Python implementation of the [[UMAP]] (Uniform Manifold Approximation and Projection) algorithm, maintained by [[LelandMcInnes|Leland McInnes]] et al. Installable as `pip install umap-learn`; imported as `from umap import UMAP`.

## From [[hands-on-llm-ch05-text-clustering-topic-modeling|*Hands-On LLMs* Ch 5]]

Ch 5 uses `umap-learn` as the dimensionality-reduction step of the BERTopic pipeline:

```python
from umap import UMAP
umap_model = UMAP(n_components=5, min_dist=0.0, metric='cosine', random_state=42)
reduced_embeddings = umap_model.fit_transform(embeddings)
```

A second UMAP model with `n_components=2` is created over the same embeddings for the [[Plotly]] / [[matplotlib]] / [[Datamapplot]] visualizations.

## Connections

- [[hands-on-llm-ch05-text-clustering-topic-modeling]] — primary source.
- [[UMAP]] — the algorithm the package implements.
- [[LelandMcInnes]] — lead maintainer.
- [[HDBSCANLibrary|hdbscan]] — the standard downstream package in clustering pipelines.
- [[BERTopic]] — the framework that ships `umap-learn` as a default dependency.
