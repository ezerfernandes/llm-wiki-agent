---
title: "Dimensionality Reduction"
type: concept
tags: [unsupervised, manifold-learning, preprocessing, embeddings]
sources: [hands-on-llm-ch05-text-clustering-topic-modeling]
last_updated: 2026-05-23
---

# Dimensionality Reduction

**Dimensionality reduction** is the process of mapping high-dimensional data to a lower-dimensional space *"that preserve[s] the global structure of high-dimensional data by finding low-dimensional representations."* It is the **second step** in the modern [[TextClustering|text-clustering pipeline]] — high-dimensional Transformer embeddings (384–1536+ dims) are reduced to 5–10 dimensions before clustering.

## Why reduce dimensionality before clustering (per *Hands-On LLMs* Ch 5)

The [[CurseOfDimensionality|curse of dimensionality]]: *"As the number of dimensions increases, there is an exponential growth in the number of possible values within each dimension. Finding all subspaces within each dimension becomes increasingly complex. As a result, high-dimensional data can be troublesome for many clustering techniques as it gets more difficult to identify meaningful clusters."*

Distance-based clustering methods ([[KMeansClustering|k-means]], [[DBSCAN]], [[HDBSCAN]]) all rely on distances becoming **less informative** in high dimensions — points concentrate near equidistant from each other, breaking density-based and centroid-based logic alike.

## Two canonical methods

- **[[PCA|PCA (Principal Component Analysis)]]** ([[HaroldHotelling|Hotelling]] 1933) — **linear** projection onto orthogonal directions of maximal variance. Fast, deterministic, well-understood. Loses nonlinear structure.
- **[[UMAP|UMAP (Uniform Manifold Approximation and Projection)]]** ([[LelandMcInnes|McInnes]], Healy & Melville 2018) — **nonlinear** manifold learning. *"It tends to handle nonlinear relationships and structures a bit better than PCA."* — Ch 5's preference.

Other named methods: **t-SNE** (popular for 2D visualization; less faithful to global structure than UMAP), **autoencoders** (neural-network nonlinear reducers).

## Information loss

*"Dimensionality reduction techniques, however, are not flawless. They do not perfectly capture high-dimensional data in a lower-dimensional representation. Information will always be lost with this procedure. There is a balance between reducing dimensionality and keeping as much information as possible."* — Ch 5

Ch 5 uses **two separate UMAP projections**: `n_components=5` for clustering, `n_components=2` for visualization — explicitly acknowledging that the 2D view is approximate and may distort cluster structure.

## Connections

- [[hands-on-llm-ch05-text-clustering-topic-modeling]] — primary source.
- [[UMAP]] / [[PCA]] / [[PrincipalComponentAnalysis]] — canonical methods.
- [[CurseOfDimensionality]] — the underlying problem.
- [[TextClustering]] / [[BERTopic]] — the modern NLP consumer.
- [[Embedding]] / [[SentenceEmbedding]] — typical input.
- [[CosineSimilarity]] — the metric typically used in the original high-dim space.
- [[HDBSCAN]] / [[KMeansClustering]] — typical downstream consumers.
