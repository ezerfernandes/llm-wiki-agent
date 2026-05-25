---
title: "UMAP (Uniform Manifold Approximation and Projection)"
type: concept
tags: [dimensionality-reduction, manifold-learning, unsupervised, visualization]
sources: [hands-on-llm-ch05-text-clustering-topic-modeling]
last_updated: 2026-05-23
---

# UMAP

**UMAP** — **Uniform Manifold Approximation and Projection** — is a nonlinear [[DimensionalityReduction|dimensionality-reduction]] algorithm ([[LelandMcInnes|McInnes]], Healy & Melville 2018, [arXiv:1802.03426](https://arxiv.org/abs/1802.03426)). It is the **default dimensionality reducer** in the modern text-clustering pipeline ([[TextClustering]] / [[BERTopic]]), preferred over [[PCA]] because *"it tends to handle nonlinear relationships and structures a bit better than PCA."*

## What UMAP does

Projects high-dimensional points to a lower-dimensional space while **preserving local and global manifold structure** — clusters in the high-dimensional space remain clusters in the projection, and topology (relative distances between clusters) is approximately preserved.

## Parameters (per [[hands-on-llm-ch05-text-clustering-topic-modeling|*Hands-On LLMs* Ch 5]])

```python
from umap import UMAP
umap_model = UMAP(
    n_components=5, min_dist=0.0, metric='cosine', random_state=42
)
reduced = umap_model.fit_transform(embeddings)
```

- **`n_components`** — output dimensionality. Ch 5 reduces 384 → 5 for clustering; 384 → 2 for visualization. *"Generally, values between 5 and 10 work well to capture high-dimensional global structures."*
- **`min_dist`** — minimum distance between embedded points. Set to `0.0` because *"that generally results in tighter clusters."*
- **`metric`** — distance metric in the input space. **`'cosine'`** is preferred for high-dimensional embeddings because *"Euclidean-based methods have issues dealing with high-dimensional data."*
- **`random_state`** — reproducibility tradeoff: *"setting a random_state in UMAP will make the results reproducible across sessions but will disable parallelism and therefore slow down training."*

## Lossy by design

*"Dimensionality reduction techniques, however, are not flawless. They do not perfectly capture high-dimensional data in a lower-dimensional representation. Information will always be lost with this procedure. There is a balance between reducing dimensionality and keeping as much information as possible."* Ch 5 explicitly warns against drawing conclusions from 2D UMAP visualizations alone — they can push clusters together or apart misleadingly.

## Why two UMAP projections in Ch 5

The chapter uses **two separate UMAP models** over the same embeddings:
- `n_components=5` — feeds [[HDBSCAN]] for clustering (5D balances information retention with HDBSCAN's distance-based logic).
- `n_components=2` — feeds [[matplotlib]] / [[Plotly]] for visualization (2D is required for plotting, but is **only an approximation** of cluster structure).

## Versus [[PCA]]

| | [[PCA]] | UMAP |
|---|---|---|
| Type | Linear projection | Nonlinear manifold |
| Preserves | Variance along orthogonal axes | Local + global topology |
| Output dim | Any | Any (typically 2–10 for clustering / viz) |
| Speed | Fast | Slow, especially with `random_state` set |
| Default in modern NLP pipelines | Rarely | Yes ([[BERTopic]] / Hugging Face `text-clustering`) |

## Connections

- [[hands-on-llm-ch05-text-clustering-topic-modeling]] — primary source.
- [[DimensionalityReduction]] — parent concept.
- [[PCA]] / [[PrincipalComponentAnalysis]] — the linear alternative.
- [[CurseOfDimensionality]] — the motivation for using UMAP.
- [[HDBSCAN]] / [[TextClustering]] / [[BERTopic]] — UMAP's standard downstream consumers.
- [[CosineSimilarity]] — UMAP's preferred metric on Transformer embeddings.
- [[UMAPLibrary|umap-learn]] — the Python package.
- [[LelandMcInnes]] — UMAP's lead author.
- [[Reproducibility]] — the `random_state` tradeoff.
