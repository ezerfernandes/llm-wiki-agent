---
title: "Feature Map"
type: concept
tags: [linear-algebra, kernel-methods, foundational]
sources: [mml-book]
last_updated: 2026-05-16
---

# Feature Map

A function $\boldsymbol\phi:\mathbb{R}^D\to\mathbb{R}^K$ (or to an infinite-dim space) that re-represents inputs in a form where linear methods can capture non-linear relationships ([[mml-book]] §9.2, §12.4).

## Why feature maps make "linear" methods non-linear

[[mml-book]] §9.2 marginal (p. 295): "Linear regression refers to 'linear-in-the-parameters' regression models, but the inputs can undergo any nonlinear transformation."

Under a feature map, the regression model becomes

$$y = \boldsymbol\phi(\mathbf{x})^\top\boldsymbol\theta + \epsilon$$

which is *still* linear in $\boldsymbol\theta$ (so MLE has a closed form) but non-linear in $\mathbf{x}$. All the linear-regression machinery (Ch 9) carries over with the [[DesignMatrix]] $\boldsymbol\Phi$ in place of $\mathbf{X}$.

## Polynomial features

The most common explicit feature map ([[mml-book]] Example 9.3):

$$\boldsymbol\phi(x) = [1, x, x^2, x^3, \dots, x^{K-1}]^\top$$

lifts 1-D inputs into $\mathbb{R}^K$. Linear regression in this lifted space is **polynomial regression** of degree $K-1$ — but the optimization remains a single matrix inversion.

## Implicit feature maps via kernels

[[KernelTrick]]: if the algorithm only depends on inputs through inner products $\boldsymbol\phi(\mathbf{x})^\top\boldsymbol\phi(\mathbf{x}')$, the feature map need never be computed explicitly. The kernel $k(\mathbf{x},\mathbf{x}') := \boldsymbol\phi(\mathbf{x})^\top\boldsymbol\phi(\mathbf{x}')$ does it all. For the RBF kernel, $\boldsymbol\phi$ is *infinite-dimensional* — but $k$ is just one evaluation of a Gaussian.

## Modern context: learned feature maps

In deep learning, the feature map is *learned* rather than chosen: hidden layers are $\boldsymbol\phi(\mathbf{x})$, the final linear layer plays the role of $\boldsymbol\theta$. The "representation learning" view of deep networks is "an end-to-end-learnt feature map followed by a linear classifier."

This is the [[madewithml-foundations-embeddings|embedding]] insight: dense vectors *are* learned feature maps.

## Connections

- [[mml-book]] — §9.2 + §12.4 canonical references.
- [[DesignMatrix]] — matrix collecting $\boldsymbol\phi(\mathbf{x}_n)^\top$ as rows.
- [[KernelTrick]] — implicit feature maps.
- [[LinearRegression]] — primary consumer.
- [[ContextualEmbedding]] — modern learned-feature-map case.
