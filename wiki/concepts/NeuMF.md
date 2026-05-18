---
title: "NeuMF (Neural Matrix Factorization)"
type: concept
tags: [recommender-systems, neural-collaborative-filtering, deep-learning, ranking]
sources: [d2l-recommender-systems]
last_updated: 2026-05-16
---

# NeuMF — Neural Matrix Factorization

**Neural extension of [[MatrixFactorization]] for implicit-feedback personalized ranking** ([[XiangnanHe|He]], Liao, Zhang, Nie, Hu, Chua 2017, *WWW*) — the canonical paper of the **[[NeuralCollaborativeFiltering|Neural Collaborative Filtering]]** framework. Replaces MF's dot-product head with two parallel learned subnetworks.

## Architecture

Two branches sharing user/item IDs but **not embeddings**:

### GMF (Generalized Matrix Factorization)
$$\mathbf{x} = \mathbf{p}_u \odot \mathbf{q}_i, \quad \hat{y}_{ui}^{(\text{GMF})} = \alpha(\mathbf{h}^\top\mathbf{x})$$

Hadamard product of MF-style user/item latent factors, then a single output layer. Trivially generalizes MF (set $\mathbf{h}=\mathbf{1}$, $\alpha=$ identity to recover MF).

### MLP branch
Separate embedding tables $\mathbf{U}, \mathbf{V}$ (not shared with GMF). Concatenate $[\mathbf{u}_u, \mathbf{v}_i]$, feed through stacked dense layers with ReLU:

$$\hat{y}_{ui}^{(\text{MLP})} = \alpha(\mathbf{h}^\top\phi^L(\cdots))$$

### Fusion
Concatenate the GMF output vector and the MLP final hidden layer, project through one more dense + sigmoid:

$$\hat{y}_{ui} = \sigma(\mathbf{h}^\top[\mathbf{x}, \phi^L(\mathbf{z}^{(L-1)})])$$

## Training

- Implicit feedback only — ratings binarized (interacted → 1, not → 0).
- [[BPR]] loss with [[NegativeSampling]] (one negative per positive in D2L's `PRDataset`).
- `seq-aware` split: hold out each user's most-recent interaction as test.
- Evaluation: [[HitRate|Hit@k]] and [[AUC]] — not RMSE.

D2L config: $k=10$ latent dim, MLP hidden $=[10, 10, 10]$, $\eta=0.01$, 10 epochs, Adam.

## Connections
- [[XiangnanHe]] — first author.
- [[NeuralCollaborativeFiltering]] — broader framework.
- [[MatrixFactorization]] — linear predecessor NeuMF generalizes via GMF.
- [[GMF]] — the dedicated subnetwork.
- [[BPR]] — training loss.
- [[ImplicitFeedback]] — required feedback type.
- [[NegativeSampling]] — required training-time mechanic.
- [[HitRate]], [[AUC]] — evaluation metrics.
- [[MultilayerPerceptron]] — the MLP branch's primitive.
- [[d2l-recommender-systems]] — source §neumf.
