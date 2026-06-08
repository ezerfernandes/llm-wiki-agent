---
title: "Autoencoder"
type: concept
tags: [deep-learning, representation-learning]
sources: [mml-ch10-dimensionality-reduction-pca]
last_updated: 2026-06-05
---

# Autoencoder

A neural network trained to reconstruct its input through a low-dimensional bottleneck, learning compressed representations useful for denoising, anomaly detection, and pretraining. Conceptual ancestor of [[maskedlanguagemodel]] objectives in [[BERT]] and the encoder half of [[encoderdecoder]] architectures.

## PCA is the optimal *linear* auto-encoder ([[mml-ch10-dimensionality-reduction-pca|MML §10.8]])

[[mml-ch10-dimensionality-reduction-pca|MML Ch 10]] frames [[PrincipalComponentAnalysis|PCA]] as a linear auto-encoder (Fig. 10.16): the **encoder** $\mathbf z_n=\mathbf B^\top\mathbf x_n\in\mathbb R^M$ maps data to a code, the **decoder** $\tilde{\mathbf x}_n=\mathbf B\mathbf z_n$ maps it back, and the squared auto-encoding loss $\frac1N\sum_n\|\mathbf x_n-\mathbf B\mathbf B^\top\mathbf x_n\|^2$ (Eq. 10.76) is *identical* to PCA's [[ReconstructionError|reconstruction-error]] objective (Eq. 10.29) — so **PCA is the optimal linear auto-encoder**. Replacing the linear maps with nonlinear ones gives a nonlinear auto-encoder; replacing them with deep feedforward nets gives the **deep auto-encoder**, in which the encoder is also called the *recognition / inference network* and the decoder the *generator*. Setting the deep-AE activations to the identity recovers PCA exactly.

## Connections

- [[mml-ch10-dimensionality-reduction-pca|MML Ch 10]] — §10.8 (PCA as linear auto-encoder).
- [[PrincipalComponentAnalysis]] — the optimal linear auto-encoder.
- [[ReconstructionError]] — the shared training objective.
- [[ProbabilisticPCA]] — the generative / probabilistic relative.
- [[encoderdecoder]] / [[BERT]] / [[maskedlanguagemodel]] — the deep-learning descendants.
