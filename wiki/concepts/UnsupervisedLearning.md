---
title: "Unsupervised Learning"
type: concept
tags: [paradigm, statistical-learning]
sources: [islr-seventh-printing, d2l-introduction]
last_updated: 2026-05-16
---

# Unsupervised Learning

Learning structure from inputs $X$ without a labeled response — discovering low-dimensional representations or groupings. Canonical methods include [[PrincipalComponentAnalysis|PCA]], [[KMeansClustering|K-means]] and [[HierarchicalClustering]]. ISLR Chapter 10.

Per [[d2l-introduction]]: "the type and number of questions we can ask is limited only by our creativity." The chapter enumerates five archetypal unsupervised questions: (1) **clustering** (find a small number of prototypes), (2) **subspace estimation** (find a small number of parameters; [[PrincipalComponentAnalysis|PCA]] when linear), (3) **embedding** (Euclidean representations where symbolic relations hold — "Rome − Italy + France = Paris"), (4) **causality / [[ProbabilisticGraphicalModel|graphical-model]] discovery**, and (5) **deep generative modeling** ([[VariationalAutoencoder|VAEs]], [[generativeadversarialnetwork|GANs]], normalizing flows, [[DiffusionModel|diffusion models]]).

## Connections
- [[StatisticalLearning]] — parent (ISLR framing).
- [[MachineLearning]] — parent (D2L framing).
- [[SelfSupervisedLearning]] — modern recipe for label-free pretraining that the chapter frames as a development of unsupervised learning.
- [[PrincipalComponentAnalysis]], [[KMeansClustering]], [[HierarchicalClustering]] — Ch.10 methods.
- [[generativeadversarialnetwork]], [[DiffusionModel]], [[Autoencoder]] — deep generative-model lineage.
- [[islr-seventh-printing]], [[d2l-introduction]] — survey-textbook coverage.
