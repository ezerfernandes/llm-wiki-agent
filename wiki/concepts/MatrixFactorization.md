---
title: "Matrix Factorization"
type: concept
tags: [recommender-systems, collaborative-filtering, latent-factor]
sources: [d2l-recommender-systems]
last_updated: 2026-05-16
---

# Matrix Factorization

The canonical **model-based [[CollaborativeFiltering|collaborative-filtering]]** algorithm and the historical baseline for every neural recommender. Proposed as a blog post by **Simon Funk** in 2006 ([[NetflixPrize]] context); formalized by **[[YehudaKoren|Koren]], Bell & Volinsky 2009** (IEEE Computer); played a load-bearing role in the **BellKor's Pragmatic Chaos** \$1M Netflix Prize win.

## Model

Factor the user-item [[InteractionMatrix|interaction matrix]] $\mathbf{R}\in\mathbb{R}^{m\times n}$ into the product of two low-rank matrices:

$$\hat{\mathbf{R}} = \mathbf{P}\mathbf{Q}^\top, \quad \mathbf{P}\in\mathbb{R}^{m\times k},\ \mathbf{Q}\in\mathbb{R}^{n\times k},\ k\ll m,n$$

with $\mathbf{p}_u$ = user latent factor and $\mathbf{q}_i$ = item latent factor. Adding **user/item bias terms** to capture per-user/per-item rating offsets gives the standard form:

$$\hat{R}_{ui} = \mathbf{p}_u\mathbf{q}_i^\top + b_u + b_i$$

trained by minimizing regularized [[MeanSquaredError|MSE]] over observed pairs:

$$\min_{\mathbf{P},\mathbf{Q},b}\sum_{(u,i)\in\mathcal{K}}(R_{ui}-\hat{R}_{ui})^2 + \lambda(\|\mathbf{P}\|_F^2 + \|\mathbf{Q}\|_F^2 + b_u^2 + b_i^2)$$

via [[StochasticGradientDescent|SGD]] or [[Adam]]. Evaluated by [[RMSE]].

## D2L implementation

D2L's MF is two `nn.Embedding` layers ($P$, $Q$) plus two scalar-output embedding tables for biases. Predict by lookup + dot product + bias add. Latent dimension $k=30$, $\eta=0.002$, weight decay $10^{-5}$, 20 epochs, Adam.

## Limitations

- Linear; can't model nonlinear user-item interactions ([[AutoRec]] addresses this).
- Pointwise MSE objective on observed entries only; treats unobserved pairs as missing rather than negative — bad fit for ranking on implicit feedback ([[NeuMF]] + [[BPR]] address this).
- No side information ([[FactorizationMachines]] / [[DeepFM]] address this).

## Connections
- [[CollaborativeFiltering]] — parent paradigm.
- [[YehudaKoren]] — co-canonical author.
- [[NetflixPrize]] — historical motivation.
- [[SimonFunk]] — original blog post.
- [[InteractionMatrix]] — input.
- [[RMSE]] — evaluation metric.
- [[AutoRec]] — nonlinear successor on explicit feedback.
- [[NeuMF]] — neural generalization on implicit feedback.
- [[FactorizationMachines]] — feature-rich generalization (FM's pairwise term is exactly the dot product between user and item embeddings when $i$=user-id, $j$=item-id features).
- [[MatrixDecomposition]] — broader linear-algebra umbrella.
- [[d2l-recommender-systems]] — primary source.
