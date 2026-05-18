---
title: "Gram Matrix"
type: concept
tags: [computer-vision, linear-algebra, style-transfer]
sources: [d2l-computer-vision]
last_updated: 2026-05-16
---

# Gram Matrix

For a set of vectors $\{v_1, \ldots, v_C\} \subset \mathbb{R}^n$, the Gram matrix $G \in \mathbb{R}^{C \times C}$ has entries $G_{ij} = \langle v_i, v_j \rangle$. Captures all pairwise inner products — i.e. the *correlation structure* of the vectors — without preserving the vectors themselves.

## In [[StyleTransfer|neural style transfer]]

For a CNN feature map $\phi \in \mathbb{R}^{C \times H \times W}$, flatten each channel into a length-$HW$ vector and stack as the rows of $\phi_\text{flat} \in \mathbb{R}^{C \times HW}$. The Gram matrix is

$G = \phi_\text{flat} \phi_\text{flat}^\top \in \mathbb{R}^{C \times C}, \quad G_{ij} = \sum_{p=1}^{HW} \phi_{i, p} \phi_{j, p}.$

$G_{ij}$ measures how often channels $i$ and $j$ co-activate across spatial positions. **Style is captured by these inter-channel co-activation statistics**, which are by construction *invariant to spatial location* — perfect for "this image has the texture / brushwork of a Van Gogh" rather than "this object is at position $(x, y)$".

## Style loss formula

For style layers $l \in S$, summing across layers:

$L_\text{style} = \sum_{l \in S} \frac{1}{(2 C_l H_l W_l)^2} \| G_\text{synth}^{(l)} - G_\text{style}^{(l)} \|_F^2$

(Frobenius norm of the Gram-matrix difference.)

## Other ML uses

- **Kernel methods:** the *kernel Gram matrix* $K_{ij} = k(x_i, x_j)$ is the central object in SVMs / kernel ridge regression / Gaussian processes.
- **Spectral analysis:** eigendecomposition of a Gram matrix yields PCA-like principal directions.

## Connections

- [[StyleTransfer]] — primary application in [[d2l-computer-vision]].
- [[InnerProduct]] / [[LinearAlgebra]] / [[Norm]].
- [[CovarianceMatrix]] — closely related (mean-centered Gram matrix divided by $n-1$).
- Kernel methods broadly (SVMs, Gaussian processes).
