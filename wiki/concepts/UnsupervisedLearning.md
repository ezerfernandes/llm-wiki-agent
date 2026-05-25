---
title: "Unsupervised Learning"
type: concept
tags: [paradigm, statistical-learning]
sources: [islr-seventh-printing, d2l-introduction, hands-on-llm-ch05-text-clustering-topic-modeling]
last_updated: 2026-05-23
---

# Unsupervised Learning

Learning structure from inputs $X$ without a labeled response — discovering low-dimensional representations or groupings. Canonical methods include [[PrincipalComponentAnalysis|PCA]], [[KMeansClustering|K-means]] and [[HierarchicalClustering]]. ISLR Chapter 10.

Per [[d2l-introduction]]: "the type and number of questions we can ask is limited only by our creativity." The chapter enumerates five archetypal unsupervised questions: (1) **clustering** (find a small number of prototypes), (2) **subspace estimation** (find a small number of parameters; [[PrincipalComponentAnalysis|PCA]] when linear), (3) **embedding** (Euclidean representations where symbolic relations hold — "Rome − Italy + France = Paris"), (4) **causality / [[ProbabilisticGraphicalModel|graphical-model]] discovery**, and (5) **deep generative modeling** ([[VariationalAutoencoder|VAEs]], [[generativeadversarialnetwork|GANs]], normalizing flows, [[DiffusionModel|diffusion models]]).

## From [[hands-on-llm-ch05-text-clustering-topic-modeling|*Hands-On LLMs* Ch 5]]

Ch 5 frames the entire [[TextClustering|text-clustering]] + [[TopicModeling|topic-modeling]] pipeline as **the unsupervised twin of [[hands-on-llm-ch04-text-classification|Ch 4]]'s supervised + zero-shot classification**. The chapter's closing line: *"despite supervised methods like classification being prevalent in recent years, unsupervised approaches such as text clustering hold immense potential due to their ability to group texts based on semantic content without prior labeling."* The embed → reduce → cluster pipeline operationalizes ISLR's classical unsupervised methods on top of Transformer embeddings — a generation more powerful than [[PrincipalComponentAnalysis|PCA]] / [[KMeansClustering|k-means]] on raw bag-of-words.

## Connections
- [[StatisticalLearning]] — parent (ISLR framing).
- [[MachineLearning]] — parent (D2L framing).
- [[SelfSupervisedLearning]] — modern recipe for label-free pretraining that the chapter frames as a development of unsupervised learning.
- [[PrincipalComponentAnalysis]], [[KMeansClustering]], [[HierarchicalClustering]] — Ch.10 methods.
- [[generativeadversarialnetwork]], [[DiffusionModel]], [[Autoencoder]] — deep generative-model lineage.
- [[islr-seventh-printing]], [[d2l-introduction]] — survey-textbook coverage.
- [[hands-on-llm-ch05-text-clustering-topic-modeling]] — modern LLM-embedding-based unsupervised pipeline.
- [[TextClustering]] / [[TopicModeling]] / [[BERTopic]] — Ch 5's worked unsupervised methods.
- [[UMAP]] / [[HDBSCAN]] / [[DBSCAN]] — modern unsupervised primitives.
