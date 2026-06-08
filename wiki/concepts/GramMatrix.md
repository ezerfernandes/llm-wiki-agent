---
title: "Gram Matrix"
type: concept
tags: [computer-vision, linear-algebra, style-transfer]
sources: [mml-ch03-analytic-geometry, mml-ch12-classification-svm, d2l-computer-vision]
last_updated: 2026-06-05
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

## From [[mml-ch03-analytic-geometry|MML Ch 3]]

The Gram matrix is the structural object underneath two Ch 3 results:

- **Inner products = SPD matrices** (§3.2.3): the matrix $A_{ij}=\langle\mathbf{b}_i,\mathbf{b}_j\rangle$ of pairwise [[InnerProduct|inner products]] of basis vectors *is* a Gram matrix, and it is exactly the [[SymmetricPositiveDefiniteMatrix|symmetric positive definite matrix]] that defines the inner product $\langle\mathbf{x},\mathbf{y}\rangle=\hat{\mathbf{x}}^\top\mathbf{A}\hat{\mathbf{y}}$ (Thm 3.5). A Gram matrix of *linearly independent* vectors is SPD (positive semidefinite in general).
- **[[OrthogonalProjection|Orthogonal projection]] / normal equation** (§3.8.2): the projection matrix $\mathbf{P}_\pi=\mathbf{B}(\mathbf{B}^\top\mathbf{B})^{-1}\mathbf{B}^\top$ inverts the Gram matrix $\mathbf{B}^\top\mathbf{B}$ of the basis columns. It is invertible iff $\mathbf{B}$ is full rank; a "jitter" $\epsilon\mathbf{I}$ (ridge) keeps it positive definite (p. 86). For an [[OrthonormalBasis|ONB]], $\mathbf{B}^\top\mathbf{B}=\mathbf{I}$ — the Gram matrix is the identity, so no inverse is needed.

## From [[mml-ch12-classification-svm|MML Ch 12]] — the kernel matrix and the PSD validity condition

[[mml-ch12-classification-svm|MML Ch 12]] §12.4 (Eq. 12.53, p. 389) makes the Gram matrix the gatekeeper of kernel validity. Applying a [[KernelFunction|kernel]] $k$ to a dataset produces the matrix $\mathbf{K}\in\mathbb{R}^{N\times N}$, $K_{ij}=k(\mathbf{x}_i,\mathbf{x}_j)$, "called the Gram matrix, and is often just referred to as the kernel matrix." A function $k$ is a *valid* kernel iff this matrix is **symmetric positive-semidefinite** for every finite dataset — $\forall\mathbf{z}\in\mathbb{R}^N:\mathbf{z}^\top\mathbf{K}\mathbf{z}\ge0$ — exactly the [[SymmetricPositiveDefiniteMatrix|SPD]] machinery of §3.2.3 that this page already anchors. This is the Mercer / positive-definite-kernel condition, and it is why the [[KernelTrick|kernel trick]] (and hence the [[DualSVM|dual SVM]]) is well-defined: $\mathbf{K}$ being PSD guarantees a feature space $\mathcal{H}$ in which $k$ is a genuine inner product.

## Connections

- [[mml-ch03-analytic-geometry]] — §3.2.3 (Thm 3.5) and §3.8.2 (normal equation).
- [[mml-ch12-classification-svm]] — §12.4 the kernel/Gram matrix + PSD validity condition.
- [[KernelTrick]] / [[KernelFunction]] / [[DualSVM]] — the kernel-machine consumers.
- [[StyleTransfer]] — primary application in [[d2l-computer-vision]].
- [[InnerProduct]] / [[SymmetricPositiveDefiniteMatrix]] — a Gram matrix of independent vectors is SPD and encodes an inner product.
- [[OrthogonalProjection]] / [[ProjectionMatrix]] — $\mathbf{B}^\top\mathbf{B}$ is the Gram matrix in the projection formula.
- [[LinearAlgebra]] / [[Norm]].
- [[DataCovarianceMatrix]] — closely related (mean-centered Gram matrix divided by $n-1$).
- Kernel methods broadly (SVMs, Gaussian processes).
