---
title: "Kernel Trick"
type: concept
tags: [classification, kernel-methods, foundational]
sources: [mml-book]
last_updated: 2026-05-16
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

## Connections

- [[mml-book]] — §12.4 canonical reference.
- [[SupportVectorMachine]] — primary application.
- [[InnerProduct]] — what kernels generalize.
- [[SymmetricPositiveDefiniteMatrix]] — Mercer's condition.
- [[FeatureMap]] — the implicit $\boldsymbol\phi$.
- [[BayesianLinearRegression]] — GP connection.
