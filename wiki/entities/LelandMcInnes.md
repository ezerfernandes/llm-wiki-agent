---
title: "Leland McInnes"
type: entity
tags: [person, researcher, umap, hdbscan, dimensionality-reduction, clustering]
sources: [hands-on-llm-ch05-text-clustering-topic-modeling]
last_updated: 2026-05-23
---

# Leland McInnes

Research mathematician at the **Tutte Institute for Mathematics and Computing** in Ottawa, Canada. Lead author of two of the most widely deployed unsupervised-learning algorithms in the modern LLM stack:

- **[[UMAP]]** — *"UMAP: Uniform Manifold Approximation and Projection for Dimension Reduction"* ([[LelandMcInnes|McInnes]], John Healy & James Melville, [arXiv:1802.03426](https://arxiv.org/abs/1802.03426), 2018) — the default nonlinear dimensionality reducer in modern text-clustering pipelines.
- **[[HDBSCAN]]** — *"hdbscan: Hierarchical density based clustering"* (McInnes, Healy & Steve Astels, *J. Open Source Softw.* 2.11 (2017): 205) — the default density-based clustering algorithm in [[BERTopic]] and the Hugging Face `text-clustering` package.

Maintainer of the [[UMAPLibrary|umap-learn]] and [[HDBSCANLibrary|hdbscan]] Python packages.

## From [[hands-on-llm-ch05-text-clustering-topic-modeling|*Hands-On LLMs* Ch 5]]

Ch 5 cites both papers when introducing the chapter's embed → reduce → cluster pipeline; the two-paragraph parameter discussions for [[UMAP]] (`min_dist`, `metric`, `n_components`, `random_state`) and [[HDBSCAN]] (`min_cluster_size`, `metric`, `cluster_selection_method`) are direct reflections of the API choices made by McInnes and his collaborators.

## Connections

- [[hands-on-llm-ch05-text-clustering-topic-modeling]] — Ch 5 source.
- [[UMAP]] / [[UMAPLibrary]] — algorithm and package.
- [[HDBSCAN]] / [[HDBSCANLibrary]] — algorithm and package.
- [[DBSCAN]] — HDBSCAN's parent algorithm ([[MartinEster|Ester]] et al., 1996).
- [[DimensionalityReduction]] / [[DensityBasedClustering]] — the two algorithmic families he co-defined for modern use.
