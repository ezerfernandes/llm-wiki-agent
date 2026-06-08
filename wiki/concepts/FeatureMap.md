---
title: "Feature Map"
type: concept
tags: [linear-algebra, kernel-methods, foundational]
sources: [mml-book, mml-ch09-linear-regression, mml-ch12-classification-svm]
last_updated: 2026-06-05
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

## From [[mml-ch09-linear-regression|MML Ch 9]]

[[mml-ch09-linear-regression|MML Ch 9]] §9.2 makes the feature map the engine of the chapter's defining claim — **"linear regression refers to models that are 'linear in the parameters'"** (p. 295). The featured model $y=\boldsymbol\phi^\top(\mathbf{x})\boldsymbol\theta+\epsilon=\sum_{k=0}^{K-1}\theta_k\phi_k(\mathbf{x})+\epsilon$ (Eq. 9.13) keeps $\boldsymbol\theta$ linear, so *all* the [[NormalEquations|normal-equations]] machinery carries over with the feature matrix $\boldsymbol\Phi$ replacing $\mathbf{X}$ (Eqs. 9.16, 9.19). The canonical explicit map is **polynomial** $\boldsymbol\phi(x)=[1,x,x^2,\dots,x^{K-1}]^\top$ (Example 9.3, Eq. 9.14), giving [[PolynomialRegression|polynomial regression]] of degree $K-1$ via one matrix inversion. Note $\phi_0(x)=1$ is precisely the **bias-augmentation** that recovers an intercept in MML's otherwise origin-passing model. §9.4 reads the feature functions as a basis spanning $\text{col}(\boldsymbol\Phi)$; orthonormal $\phi_k$ (wavelets/Fourier) decouple the [[OrthogonalProjection|projection]] into independent per-feature terms.

## From [[mml-ch12-classification-svm|MML Ch 12]] — the implicit (never-materialized) feature map

In [[mml-ch12-classification-svm|MML Ch 12]] §12.4 the feature map takes its most dramatic form: a [[KernelFunction|kernel]] is *defined* by the existence of a Hilbert space $\mathcal{H}$ and a map $\boldsymbol\phi:\mathcal{X}\to\mathcal{H}$ with $k(\mathbf{x}_i,\mathbf{x}_j)=\langle\boldsymbol\phi(\mathbf{x}_i),\boldsymbol\phi(\mathbf{x}_j)\rangle_\mathcal{H}$ (Eq. 12.52). The [[KernelTrick|kernel trick]] then runs the [[DualSVM|dual SVM]] entirely through $k$, so $\boldsymbol\phi$ is **never computed** — for the Gaussian [[RBFKernel|RBF]] kernel it is even infinite-dimensional and "cannot be explicitly represented." Each kernel has a *canonical feature map* $\boldsymbol\phi(\mathbf{x})=k(\cdot,\mathbf{x})$ into its (unique) RKHS. This is the same "linear-in-the-features" idea as Ch 9's polynomial map, but used implicitly: the explicit polynomial map of §9.2 is the *direct* version of what §12.4 hides behind the kernel.

## Connections

- [[mml-ch09-linear-regression]] — §9.2 (Eqs. 9.13–9.19), §9.4 (orthonormal-basis decoupling).
- [[mml-ch12-classification-svm]] — §12.4 the implicit feature map behind the kernel trick.
- [[mml-book]] — §9.2 + §12.4 canonical references.
- [[DesignMatrix]] — matrix collecting $\boldsymbol\phi(\mathbf{x}_n)^\top$ as rows.
- [[KernelTrick]] — implicit feature maps.
- [[LinearRegression]] — primary consumer.
- [[ContextualEmbedding]] — modern learned-feature-map case.
