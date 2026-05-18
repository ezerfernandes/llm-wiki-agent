---
title: "Factorization Machines"
type: concept
tags: [recommender-systems, ctr, feature-interactions]
sources: [d2l-recommender-systems]
last_updated: 2026-05-16
---

# Factorization Machines

General-purpose supervised model unifying [[LinearRegression|linear regression]], [[MatrixFactorization]], and polynomial-kernel SVMs in a single framework. Proposed by [[SteffenRendle|Rendle]] 2010 (*ICDM*); the dominant CTR-prediction model of the 2010s and structural ancestor of [[DeepFM]] / [[NFM]] / [[xDeepFM]].

## 2-way FM model

For input feature vector $\mathbf{x}\in\mathbb{R}^d$:

$$\hat{y}(\mathbf{x}) = w_0 + \sum_{i=1}^d w_i x_i + \sum_{i=1}^d\sum_{j=i+1}^d \langle\mathbf{v}_i, \mathbf{v}_j\rangle x_i x_j$$

with global bias $w_0$, per-feature linear weights $\mathbf{w}\in\mathbb{R}^d$, and learned feature embeddings $\mathbf{V}\in\mathbb{R}^{d\times k}$ where $\mathbf{v}_i$ is row $i$. The pairwise term *factorizes the polynomial-kernel weight matrix* through low-rank embeddings — *"if feature $i$ represents an item and feature $j$ represents a user, the third term is exactly the dot product between user and item embeddings."*

## The $\mathcal{O}(kd)$ trick

Naive evaluation of the pairwise sum is $\mathcal{O}(kd^2)$. Rendle's reformulation:

$$\sum_{i<j}\langle\mathbf{v}_i,\mathbf{v}_j\rangle x_i x_j = \frac{1}{2}\sum_{l=1}^k\left[\left(\sum_{i=1}^d v_{i,l}x_i\right)^2 - \sum_{i=1}^d v_{i,l}^2 x_i^2\right]$$

reduces complexity to **$\mathcal{O}(kd)$** — and for sparse $\mathbf{x}$ (the CTR / categorical-features case), only non-zero coordinates contribute, making FM *linear in the number of non-zero features*. This is what makes FM tractable on the high-cardinality categorical inputs of advertising / e-commerce systems.

## Training

- Embedding table indexed by *all* one-hot field-value pairs (via per-field offsets — D2L uses `np.cumsum(field_dims)` to shift each field's vocabulary into a single embedding space).
- Loss: MSE (regression), cross-entropy (classification — D2L wraps the FM output in sigmoid for CTR), or [[BPR]] (ranking).
- Optimizer: [[Adam]] or [[StochasticGradientDescent|SGD]].

D2L implementation: 20-d embeddings, $\eta=0.02$, 30 epochs on the chapter's 34-categorical-field CTR dataset.

## Higher-order generalizations

FM theoretically generalizes to higher orders ($\chi>2$) but numerical stability deteriorates; in practice 2-way is universal. [[DeepFM]], NFM, and xDeepFM augment with deep nonlinear layers to capture higher-order interactions instead.

## Connections
- [[SteffenRendle]] — author.
- [[CTRPrediction]] — primary application.
- [[MatrixFactorization]] — special case (FM reduces to MF when features are exactly one-hot user and item IDs).
- [[LinearRegression]] — special case (the first two terms).
- [[DeepFM]] — direct descendant fusing FM with an MLP.
- [[BPR]] — pairwise loss commonly used for FM-based ranking.
- [[Embedding]] — the per-feature latent factor primitive.
- [[CriteoDataset]], [[AvazuDataset]] — production CTR datasets FM is canonically benchmarked on.
- [[d2l-recommender-systems]] — source §fm.
