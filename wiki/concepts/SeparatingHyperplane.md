---
title: "Separating Hyperplane"
type: concept
tags: [classification, geometry, foundational]
sources: [mml-book]
last_updated: 2026-05-16
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

## Connections

- [[mml-book]] — §12.1 canonical reference.
- [[SupportVectorMachine]] — the algorithm that chooses among separating hyperplanes.
- [[Margin]] — the criterion that picks a unique one.
- [[KernelTrick]] — how to handle non-linearly-separable data.
- [[OrthogonalProjection]] — distance computation.
