---
title: "Text Clustering"
type: concept
tags: [unsupervised, clustering, nlp, llm, embeddings]
sources: [hands-on-llm-ch05-text-clustering-topic-modeling]
last_updated: 2026-05-23
---

# Text Clustering

**Text clustering** is the unsupervised grouping of documents by **semantic content** rather than surface tokens — *"Text clustering aims to group similar texts based on their semantic content, meaning, and relationships."* The recent surge in effectiveness comes from replacing classical bag-of-words / term-frequency features with **Transformer-based [[Embedding|embeddings]]** that capture context and meaning.

## The Modern Pipeline (per *Hands-On LLMs* Ch 5)

[[hands-on-llm-ch05-text-clustering-topic-modeling|Ch 5]] codifies a **three-step pipeline** that has become the dominant pattern:

1. **Embed documents** with an [[EmbeddingModel|embedding model]] (e.g., [[SentenceTransformers|sentence-transformers]]'s `thenlper/gte-small` → 384-dim). Choose models optimized for **semantic similarity** — *"Choosing embedding models optimized for semantic similarity tasks is especially important for clustering as we attempt to find groups of semantically similar documents."* Use the [[MTEB|MTEB]] leaderboard's **clustering column** to pick.
2. **Reduce dimensionality** with [[UMAP]] (or [[PCA]]) — 384 → 5 dimensions in the chapter's example. Combats the [[CurseOfDimensionality|curse of dimensionality]] that breaks distance-based clustering at high dimensions.
3. **Cluster** with [[HDBSCAN]] (or [[KMeansClustering|k-means]]) — Ch 5 prefers **density-based** HDBSCAN because (a) the number of clusters is unknown in advance and (b) outliers should be detected, not forced into a cluster.

## Why embedding-based clustering won

Classical text-clustering features (bag-of-words / [[TFIDF|TF-IDF]]) treat synonyms as orthogonal and have **no notion of context**. Transformer-based embeddings encode both — *"our text clustering example does take both [context and meaning] into account as it relies on Transformer-based embeddings that are optimized for semantic similarity and contextual meaning through attention."* For 44,949 ArXiv NLP abstracts, the pipeline produces **156 thematically coherent clusters** (e.g., automatic speech recognition, neural machine translation, sentiment analysis, medical NLP) via the gte-small + UMAP + HDBSCAN pipeline.

## Applications

- **Exploratory data analysis** — "what is in this corpus?"
- **Speedup labeling** — cluster first, then label whole clusters at once.
- **Outlier detection** — find documents that don't fit any cluster.
- **Finding incorrectly labeled data** — points whose embedding falls in the "wrong" cluster.
- **Topic modeling** — extending text clustering with **automatic cluster labeling** (see [[BERTopic]]).

## Visualization

Static 2D scatter via [[matplotlib]] over a separate UMAP `n_components=2` reduction; interactive 2D via [[Plotly]] (`topic_model.visualize_documents()`); labeled 2D landscape via [[Datamapplot]]. Ch 5 cautions: *"Using any dimensionality reduction technique for visualization purposes creates information loss. It is merely an approximation of what our original embeddings look like. ... Human evaluation, inspecting the clusters ourselves, is therefore a key component of cluster analysis!"*

## Connections

- [[hands-on-llm-ch05-text-clustering-topic-modeling]] — primary source.
- [[Embedding]] / [[SentenceTransformers]] / [[GTESmall]] / [[AllMPNetBaseV2]] — the embedding stack.
- [[UMAP]] / [[PCA]] / [[DimensionalityReduction]] — step 2.
- [[HDBSCAN]] / [[DBSCAN]] / [[KMeansClustering]] / [[DensityBasedClustering]] / [[CentroidBasedClustering]] — step 3.
- [[CurseOfDimensionality]] — the motivation for step 2.
- [[CosineSimilarity]] — the standard metric for UMAP on embeddings.
- [[BERTopic]] / [[TopicModeling]] / [[TopicClustering]] — the cluster-labeling extension.
- [[UnsupervisedLearning]] — the parent paradigm.
- [[MTEB]] — the embedding-selection rubric (clustering column).
- [[ArXivNLP]] — Ch 5's worked dataset.
