---
title: "AutoRec"
type: concept
tags: [recommender-systems, autoencoder, collaborative-filtering]
sources: [d2l-recommender-systems]
last_updated: 2026-05-16
---

# AutoRec

**[[CollaborativeFiltering|Collaborative-filtering]] rating prediction reframed as autoencoder reconstruction** ([[SuvashSedhain|Sedhain]], Menon, Sanner & Xie 2015, *WWW*). Addresses the linearity limitation of [[MatrixFactorization]] by introducing **nonlinear transformations** into the latent-factor pipeline.

## Model

Single-hidden-layer [[Autoencoder]] over columns (item-based AutoRec) or rows (user-based) of the [[InteractionMatrix|rating matrix]] with unobserved entries set to zero:

$$h(\mathbf{R}_{*i}) = f(\mathbf{W}\cdot g(\mathbf{V}\mathbf{R}_{*i}+\mu)+b)$$

where $g$ is the encoder nonlinearity (sigmoid by default in D2L), $f$ is the decoder activation (identity), $\mathbf{V}$ and $\mathbf{W}$ are weight matrices. **Crucial subtlety**: the loss only backpropagates through observed-entry coordinates (gradient masked via `pred * np.sign(input)` during training) — *"only weights that are associated with observed inputs are updated during back-propagation."*

Loss: regularized squared error on observed entries.

$$\min_{\mathbf{W},\mathbf{V},\mu,b}\sum_{i=1}^M\|\mathbf{R}_{*i} - h(\mathbf{R}_{*i})\|_{\mathcal{O}}^2 + \lambda(\|\mathbf{W}\|_F^2 + \|\mathbf{V}\|_F^2)$$

## D2L implementation

Hidden dim $=500$, dropout $=0.05$ after encoder, sigmoid encoder + linear decoder. Trained 25 epochs with Adam, $\eta=0.002$, wd $=10^{-5}$. **Outperforms MF on MovieLens 100K** — first concrete demonstration in the chapter of "neural net > linear baseline" on explicit feedback.

## Limitations

- Still pointwise / rating-prediction; not suited to implicit-feedback ranking.
- Sensitive to gradient-masking implementation — naive autoencoders would propagate gradients through zeros (which encode "missing" not "rated as 0") and corrupt training.

## Connections
- [[Autoencoder]] — structural primitive.
- [[CollaborativeFiltering]], [[MatrixFactorization]] — predecessor.
- [[Dropout]] — regularizer used in D2L's implementation.
- [[ExplicitFeedback]] — only feedback type AutoRec handles.
- [[NeuMF]] — implicit-feedback neural successor.
- [[d2l-recommender-systems]] — source.
