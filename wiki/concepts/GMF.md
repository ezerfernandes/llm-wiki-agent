---
title: "GMF (Generalized Matrix Factorization)"
type: concept
tags: [recommender-systems, neural-collaborative-filtering]
sources: [d2l-recommender-systems]
last_updated: 2026-05-16
---

# GMF — Generalized Matrix Factorization

The **neural-network generalization of [[MatrixFactorization]]'s inner-product head**, introduced as one of the two parallel subnetworks of [[NeuMF]] ([[XiangnanHe|He]] et al. 2017).

$$\mathbf{x} = \mathbf{p}_u \odot \mathbf{q}_i, \quad \hat{y}_{ui} = \alpha(\mathbf{h}^\top\mathbf{x})$$

where $\odot$ is the Hadamard (element-wise) product, $\mathbf{h}\in\mathbb{R}^k$ is a learned output-layer weight vector, and $\alpha$ is an activation (identity / sigmoid).

## Why "generalized"

Standard MF predicts $\hat{y}_{ui} = \mathbf{p}_u^\top\mathbf{q}_i = \sum_l p_{u,l}q_{i,l}$. GMF replaces the uniform-weight sum with a *learned* weighted sum: setting $\mathbf{h}=\mathbf{1}$ and $\alpha=$ identity recovers MF exactly; any other $\mathbf{h}$ generalizes it. The output activation $\alpha$ further breaks the linear-in-latent-product assumption.

## Role in NeuMF

GMF is the "MF-flavored" branch; the MLP branch handles arbitrary user-item interaction. The two branches use **non-shared** embedding tables — the chapter notes this is what gives the joint model flexibility.

## Connections
- [[NeuMF]] — parent architecture.
- [[MatrixFactorization]] — special-case predecessor.
- [[NeuralCollaborativeFiltering]] — umbrella framework.
- [[XiangnanHe]] — author.
- [[d2l-recommender-systems]] — source §neumf.
