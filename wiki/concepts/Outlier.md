---
title: "Outlier"
type: concept
tags: [statistics, clustering, anomaly-detection]
sources: [hands-on-llm-ch05-text-clustering-topic-modeling]
last_updated: 2026-05-23
---

# Outlier

A **data point that does not belong to any cluster** — sufficiently distant from dense regions that forcing it into a cluster would hurt cluster purity. **Density-based clustering** ([[DBSCAN]] / [[HDBSCAN]]) treats outliers as a first-class output category (label `-1`).

## In modern text clustering (per *Hands-On LLMs* Ch 5)

[[hands-on-llm-ch05-text-clustering-topic-modeling|Ch 5]]: *"As a density-based method, HDBSCAN can also detect outliers in the data, which are data points that do not belong to any cluster. These outliers will not be assigned or forced to belong to any cluster. In other words, they are ignored. Since ArXiv articles might contain some niche papers, using a model that detects outliers could be helpful."*

For the chapter's 44,949 ArXiv NLP abstract corpus, **14,520 abstracts (32%) are flagged as outliers** with `min_cluster_size=50` and the default UMAP settings. These end up in **BERTopic's topic `-1`** — *"the very first topic is labeled -1. That topic contains all documents that could not be fitted within a topic and are considered outliers."*

## Handling outliers in [[BERTopic]]

Two options if you want every document assigned to a topic:
- **Swap [[HDBSCAN]] for [[KMeansClustering|k-means]]** — k-means forces every point into a cluster, no outliers exist.
- **Use `topic_model.reduce_outliers()`** — post-hoc reassignment of `-1`-labeled documents to their nearest existing topic.

## Outlier as signal vs noise

In [[TextClustering]] / [[TopicModeling]], outliers can be:
- **Genuinely off-topic** — niche papers that don't fit the dominant themes.
- **Hard cases** — papers spanning multiple topics or written in an unusual style.
- **Embedding-model failure modes** — domain-specific vocabulary the embedding model can't represent.

Reviewing the outlier set is a common quality-check loop.

## Connections

- [[hands-on-llm-ch05-text-clustering-topic-modeling]] — primary source.
- [[HDBSCAN]] / [[DBSCAN]] / [[DensityBasedClustering]] — the algorithms that label outliers.
- [[BERTopic]] — uses outlier label `-1` for topic `-1`.
- [[KMeansClustering]] — the no-outliers alternative.
- [[CurseOfDimensionality]] — high dimensions can synthesize outliers artificially.
