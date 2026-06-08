---
title: "Kernel Trick"
type: concept
tags: [classification, kernel-methods, foundational]
sources: [mml-ch12-classification-svm, mml-book]
last_updated: 2026-06-05
---

# Kernel Trick

A technique for **implicit lifting** of inputs into a high-dimensional feature space, used to apply linear methods (SVM, ridge regression, PCA) to non-linearly-separable data ([[mml-book]] §12.4).

## The trick

Given a feature map $\boldsymbol\phi:\mathbb{R}^D\to\mathcal{H}$ to some inner-product space $\mathcal{H}$ (often infinite-dimensional), define the **kernel** as the inner product in feature space:

$$k(\mathbf{x},\mathbf{x}') := \langle\boldsymbol\phi(\mathbf{x}), \boldsymbol\phi(\mathbf{x}')\rangle_\mathcal{H}.$$

If an algorithm depends on inputs *only through inner products* — as the dual SVM does — then we can run the algorithm in feature space **without ever computing $\boldsymbol\phi$ explicitly**, evaluating only the kernel. This is the trick.

## Common kernels

| Kernel | Form | Implicit feature space |
|---|---|---|
| Linear | $\mathbf{x}^\top\mathbf{x}'$ | $\mathbb{R}^D$ (no lift) |
| Polynomial degree $d$ | $(\mathbf{x}^\top\mathbf{x}' + c)^d$ | All monomials up to degree $d$ |
| RBF / Gaussian | $\exp(-\|\mathbf{x}-\mathbf{x}'\|^2/(2\sigma^2))$ | Infinite-dimensional |
| Sigmoid | $\tanh(\alpha\mathbf{x}^\top\mathbf{x}' + c)$ | Approximates one-hidden-layer NN |

The RBF kernel's feature space contains a basis function localized at *every point* in $\mathbb{R}^D$ — which is why kernel SVMs can fit arbitrarily complex decision boundaries.

## Mercer's condition

Not every function $k(\mathbf{x},\mathbf{x}')$ is a kernel — it must correspond to an inner product in *some* feature space. The criterion: $k$ is a kernel iff the **Gram matrix** $\mathbf{K}_{ij} = k(\mathbf{x}_i, \mathbf{x}_j)$ is symmetric positive semi-definite for any finite set of inputs.

This is **Mercer's theorem**, and it's why the wiki's [[SymmetricPositiveDefiniteMatrix]] / [[InnerProduct]] machinery from [[mml-book]] Ch 3 is the load-bearing structure underneath kernel methods.

## Algorithms that "kernelize"

Any algorithm whose computations depend on inputs only through dot products $\mathbf{x}^\top\mathbf{x}'$ admits a kernelized variant:

- **Kernel SVM** ([[mml-book]] §12.4) — the canonical example.
- **Kernel ridge regression**: replace $\mathbf{x}_n^\top\mathbf{x}_m$ with $k(\mathbf{x}_n,\mathbf{x}_m)$ in the dual ridge solution.
- **Kernel PCA**: PCA on the centered Gram matrix.
- **Gaussian processes**: BLR with infinite features = GP with kernel $k$.

## From [[mml-ch12-classification-svm|MML Ch 12]]

§12.4 (book pp. 388–390) introduces the trick from the [[DualSVM|dual SVM]]: its objective contains inner products **only between examples** $\langle\mathbf{x}_i,\mathbf{x}_j\rangle$ — never between examples and parameters — "so the only change in the dual SVM will be to replace the inner product." A **[[KernelFunction|kernel]]** is *defined* as a function $k:\mathcal{X}\times\mathcal{X}\to\mathbb{R}$ for which there exists a Hilbert space $\mathcal{H}$ and feature map $\boldsymbol\phi$ with $k(\mathbf{x}_i,\mathbf{x}_j)=\langle\boldsymbol\phi(\mathbf{x}_i),\boldsymbol\phi(\mathbf{x}_j)\rangle_\mathcal{H}$ (Eq. 12.52). "The generalization from an inner product to a kernel function (12.52) is known as the kernel trick … as it hides away the explicit non-linear feature map" (p. 389). The validity condition is the [[GramMatrix|kernel/Gram matrix]] being symmetric PSD: $\forall\mathbf{z}:\mathbf{z}^\top\mathbf{K}\mathbf{z}\ge0$ (Eq. 12.53) — exactly the [[SymmetricPositiveDefiniteMatrix|SPD]] machinery of §3.2.3. The decoupling is the headline: "the choice of the classification method (the SVM) and the choice of the feature representation $\boldsymbol\phi(\mathbf{x})$ can be considered separately." The hypothesis class stays **linear** — "the non-linear surfaces are due to the kernel function" (Fig. 12.10, p. 390). Three names of "kernel" are disambiguated (RKHS / null space §2.7.3 / KDE smoothing §11.5); $\boldsymbol\phi(\mathbf{x})=k(\cdot,\mathbf{x})$ is the **canonical feature map** of the (unique, Aronszajn 1950) RKHS. Kernels can act on non-vector objects (strings, graphs, sets, distributions).

## Connections

- [[mml-ch12-classification-svm]] — §12.4 canonical per-chapter reference.
- [[mml-book]] — umbrella source.
- [[KernelFunction]] — the kernel function / PSD condition.
- [[DualSVM]] — the inner-product-only structure the trick exploits.
- [[SupportVectorMachine]] — primary application.
- [[InnerProduct]] — what kernels generalize.
- [[SymmetricPositiveDefiniteMatrix]] — Mercer's condition.
- [[FeatureMap]] — the implicit $\boldsymbol\phi$.
- [[BayesianLinearRegression]] — GP connection.
