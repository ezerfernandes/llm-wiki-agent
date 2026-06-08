---
title: "Separating Hyperplane"
type: concept
tags: [classification, geometry, foundational]
sources: [mml-ch12-classification-svm, mml-book]
last_updated: 2026-06-05
---

# Separating Hyperplane

A hyperplane $\{\mathbf{x}\in\mathbb{R}^D : \langle\mathbf{w},\mathbf{x}\rangle + b = 0\}$ that divides $\mathbb{R}^D$ into two half-spaces, one per class ([[mml-book]] §12.1).

For a [[SupportVectorMachine|binary SVM]] with labels $y_n\in\{+1,-1\}$, the hyperplane separates correctly when

$$y_n(\langle\mathbf{w},\mathbf{x}_n\rangle + b)\geq 0 \quad \text{for all } n.$$

## The non-uniqueness problem

If the data is linearly separable, there are **infinitely many** separating hyperplanes ([[mml-book]] Fig 12.3). The SVM's contribution is picking the *maximum-margin* one — the unique hyperplane equidistant from the two nearest training points of opposite class.

## Geometric facts

- $\mathbf{w}$ is **orthogonal** to the hyperplane: for any two points $\mathbf{x}_a, \mathbf{x}_b$ on the hyperplane, $\langle\mathbf{w}, \mathbf{x}_a - \mathbf{x}_b\rangle = 0$.
- The **signed distance** from any point $\mathbf{x}$ to the hyperplane is $\frac{\langle\mathbf{w},\mathbf{x}\rangle + b}{\|\mathbf{w}\|}$.
- A hyperplane is an **affine subspace** of dimension $D-1$ in $\mathbb{R}^D$.

## Beyond linear separation

When data isn't linearly separable in input space, two routes:

1. **Soft margin**: allow violations with slack variables ([[mml-book]] §12.2.4).
2. **[[KernelTrick]]** (§12.4): lift inputs into a higher-dimensional [[FeatureSpace]] via $\boldsymbol\phi$ where they *are* linearly separable. The hyperplane lives in feature space; the kernel evaluates inner products there without ever computing $\boldsymbol\phi$.

This is the move that lets SVMs handle non-linear decision boundaries — a hyperplane in feature space is a curved decision surface in input space.

## From [[mml-ch12-classification-svm|MML Ch 12]]

§12.1 (book pp. 372–373) sets up the separating hyperplane as the SVM's decision boundary. The function is $f(\mathbf{x})=\langle\mathbf{w},\mathbf{x}\rangle+b$ (Eq. 12.2b); the hyperplane is the zero set $\{\mathbf{x}:f(\mathbf{x})=0\}$ (Eq. 12.3); a test point is classified $+1$ iff $f(\mathbf{x}_\text{test})\ge0$. The normal-vector fact is derived directly: for $\mathbf{x}_a,\mathbf{x}_b$ on the hyperplane, $f(\mathbf{x}_a)-f(\mathbf{x}_b)=\langle\mathbf{w},\mathbf{x}_a-\mathbf{x}_b\rangle=0$ (Eqs. 12.4a–b), so $\mathbf{w}\perp$ every in-plane vector. The two label conditions $\langle\mathbf{w},\mathbf{x}_n\rangle+b\ge0$ (for $y_n=+1$, Eq. 12.5) and $<0$ (for $y_n=-1$, Eq. 12.6) **combine into one inequality** $y_n(\langle\mathbf{w},\mathbf{x}_n\rangle+b)\ge0$ (Eq. 12.7) — the $\pm1$-encoding payoff. A *Remark* (p. 373) flags the dual reading of vectors from [[mml-ch02-linear-algebra|Ch 2]]: here $\mathbf{w}$ is a *geometric* arrow (a direction) while $\mathbf{x}$ is a *coordinate* (a data point). With kernels (§12.4) the hyperplane lives in feature space, so it is a *nonlinear* surface in input space (Fig. 12.10) — "we are still solving for hyperplanes … the non-linear surfaces are due to the kernel function" (p. 390).

## Connections

- [[mml-ch12-classification-svm]] — §12.1 canonical per-chapter reference.
- [[mml-book]] — umbrella source.
- [[SupportVectorMachine]] — the algorithm that chooses among separating hyperplanes.
- [[Hyperplane]] — the general linear-algebra object.
- [[Margin]] — the criterion that picks a unique one.
- [[KernelTrick]] — how to handle non-linearly-separable data.
- [[OrthogonalProjection]] — distance computation.
