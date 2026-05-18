---
title: "Hyperplane"
type: concept
tags: [linear-algebra, geometry, foundational]
sources: [d2l-appendix-mathematics]
last_updated: 2026-05-16
---

# Hyperplane

The higher-dimensional generalization of a line (in 2D) and a plane (in 3D). In a $d$-dimensional vector space, a hyperplane has $d-1$ dimensions and divides the space into two **half-spaces** ([[d2l-appendix-mathematics]] §geometry-linear-algebraic-ops).

Defined by a normal vector $\mathbf{w}\in\mathbb{R}^d$ and an offset $c\in\mathbb{R}$:

$$\{\mathbf{v}\in\mathbb{R}^d : \mathbf{w}\cdot\mathbf{v} = c\}.$$

The two half-spaces are $\{\mathbf{v}:\mathbf{w}\cdot\mathbf{v}>c\}$ and $\{\mathbf{v}:\mathbf{w}\cdot\mathbf{v}<c\}$.

## Geometric interpretation

From the dot-product–angle identity $\mathbf{w}\cdot\mathbf{v}=\|\mathbf{w}\|\|\mathbf{v}\|\cos\theta$, the hyperplane equation $\mathbf{w}\cdot\mathbf{v}=c$ says: the **projection** of $\mathbf{v}$ onto the $\mathbf{w}$-direction has fixed length $c/\|\mathbf{w}\|$. The hyperplane is therefore the locus of points whose projection onto $\mathbf{w}$ is constant — geometrically *perpendicular to $\mathbf{w}$*.

## Why ML cares: decision boundaries

> "The majority of deep learned classification models end with a linear layer fed into a softmax, so one can interpret the role of the deep neural network to be to find a non-linear embedding such that the target classes can be separated cleanly by hyperplanes." — [[d2l-appendix-mathematics]] §geometry-linear-algebraic-ops

In this framing the *deep* network is a **representation learner** whose only job is to map raw inputs into a space where linear (hyperplane) decision rules suffice. Every modern classifier — [[CNN]] image classifiers, [[BERT]]/[[GPT]] sequence classifiers, [[VisionTransformer|ViT]] — uses this template.

## D2L hand-built example

[[d2l-appendix-mathematics]] demonstrates this with a hand-built [[FashionMNIST]] t-shirt vs trousers classifier: use the **difference of class means** $\mathbf{w} = \bar{\mathbf{x}}_1 - \bar{\mathbf{x}}_0$ as the normal vector, choose a threshold by eye, and get a working binary classifier on the 28×28 pixel space — no training required. The "model" is just one hyperplane.

## Classical ML uses

- **[[Perceptron]]** ([[FrankRosenblatt|Rosenblatt]] 1958): online algorithm that finds a separating hyperplane if one exists.
- **[[SVM|Support Vector Machine]]**: max-margin hyperplane separating two classes, defined entirely by the support vectors on the margin boundary.
- **[[LinearRegression|Linear regression]]**: the fitted regression surface is a hyperplane in the input-vs-target space.
- **[[LogisticRegression]] / [[Softmax|softmax regression]]**: decision boundary between class $c$ and class $c'$ is $(\mathbf{w}_c-\mathbf{w}_{c'})\cdot\mathbf{x} = b_{c'} - b_c$ — a hyperplane.

## Connections

- [[d2l-appendix-mathematics]] — §geometry-linear-algebraic-ops canonical reference.
- [[DotProduct]] / [[InnerProduct]] — defines the hyperplane equation.
- [[Norm]] — distance from origin to hyperplane is $|c|/\|\mathbf{w}\|$.
- [[Softmax]] — multi-class extension; pairwise decision boundaries remain hyperplanes.
- [[LinearRegression]] / [[LogisticRegression]] / [[Perceptron]] / [[SVM]] — classical models defined by a single hyperplane.
- [[DecisionBoundary]] — generalization to non-linear surfaces.
