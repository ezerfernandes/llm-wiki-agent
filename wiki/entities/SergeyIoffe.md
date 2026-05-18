---
title: "Sergey Ioffe"
type: entity
tags: [person, researcher, deep-learning]
sources: [d2l-convolutional-modern]
last_updated: 2026-05-16
---

# Sergey Ioffe

Russian-American researcher at [[google|Google]]; first author with [[ChristianSzegedy|Christian Szegedy]] of the **batch normalization** paper (Ioffe & Szegedy 2015) — one of the most-cited deep-learning papers (tens of thousands of citations) and a technique applied "in nearly all deployed image classifiers" ([[d2l-convolutional-modern]] §batch-norm).

## Why he matters here

- **Batch normalization (2015).** Defined $\textrm{BN}(\mathbf{x})=\boldsymbol{\gamma}\odot\frac{\mathbf{x}-\hat{\boldsymbol{\mu}}_\mathcal{B}}{\hat{\boldsymbol{\sigma}}_\mathcal{B}}+\boldsymbol{\beta}$. The original motivation — that BN works by reducing "internal covariate shift" — has been disputed (Santurkar et al. 2018), but the empirical effectiveness is undisputed. Enables training of much deeper networks; allows aggressive learning rates; provides a regularization side-benefit through minibatch-statistic noise.
- **Inception-v3 / v4 co-author.** Szegedy, Vanhoucke, **Ioffe** et al. (2016) — the BN-augmented Inception variant.

## Connections

- [[d2l-convolutional-modern]] — canonical reference.
- [[BatchNormalization]] — first author of the introducing paper.
- [[ChristianSzegedy]] — co-author and long-time collaborator.
- [[google]] — institutional home.
- [[Inception]] — co-developed BN-augmented Inception variants.
