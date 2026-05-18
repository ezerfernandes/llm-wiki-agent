---
title: "Neural Collaborative Filtering"
type: concept
tags: [recommender-systems, deep-learning, collaborative-filtering]
sources: [d2l-recommender-systems]
last_updated: 2026-05-16
---

# Neural Collaborative Filtering

Umbrella framework for **replacing the dot-product head of [[MatrixFactorization]] with learnable neural-network heads** to model nonlinear user-item interactions. Coined and popularized by [[XiangnanHe|He]], Liao, Zhang, Nie, Hu, Chua 2017 (*WWW*) — the same paper that introduces [[NeuMF]] as the canonical instance.

## Defining moves

- Replace $\hat{y}_{ui} = \mathbf{p}_u^\top\mathbf{q}_i$ with $\hat{y}_{ui} = f_\theta(\mathbf{p}_u, \mathbf{q}_i)$ for some learnable $f_\theta$.
- Trained on [[ImplicitFeedback|implicit feedback]] with [[BPR]] or [[BinaryCrossEntropy]] (treat positives as $1$, sampled negatives as $0$).
- Evaluated by ranking metrics: [[HitRate|Hit@k]], [[AUC]], [[NDCG]].

## Instances

- **[[GMF|Generalized MF]]** — element-wise product $\mathbf{p}_u\odot\mathbf{q}_i$ followed by a single dense layer.
- **MLP-only** — concatenation $[\mathbf{p}_u, \mathbf{q}_i]$ followed by stacked dense+ReLU.
- **[[NeuMF]]** — parallel fusion of both.
- **[[AutoRec]]** — autoencoder-style, but trained on explicit feedback rather than ranking (chronological predecessor).
- Subsequent: NGCF, LightGCN ([[XiangnanHe|He]] et al. 2020), graph-neural-network extensions over the user-item bipartite graph.

## Connections
- [[CollaborativeFiltering]] — parent paradigm.
- [[MatrixFactorization]] — linear predecessor NCF generalizes.
- [[NeuMF]], [[GMF]] — concrete architectures.
- [[XiangnanHe]] — framework's most prominent author.
- [[BPR]], [[ImplicitFeedback]] — training-loss / data-type defaults.
- [[d2l-recommender-systems]] — source.
