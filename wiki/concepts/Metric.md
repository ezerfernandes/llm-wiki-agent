---
title: "Metric (Distance)"
type: concept
tags: [analytic-geometry, foundational]
sources: [mml-ch03-analytic-geometry, mml-book]
last_updated: 2026-06-04
---

# Metric (Distance)

A **metric** is a function $d:V\times V\to\mathbb{R}$, $(\mathbf{x},\mathbf{y})\mapsto d(\mathbf{x},\mathbf{y})$, that assigns each pair of points a *distance* ([[mml-ch03-analytic-geometry|MML Ch 3]] Def. 3.6, §3.3). In an inner-product space the canonical distance is

$$d(\mathbf{x},\mathbf{y}) := \|\mathbf{x}-\mathbf{y}\| = \sqrt{\langle\mathbf{x}-\mathbf{y},\,\mathbf{x}-\mathbf{y}\rangle}.$$

If the [[InnerProduct]] is the dot product, this is the **Euclidean distance**.

## The three axioms

A metric $d$ satisfies ([[mml-book]] §3.3, p. 76):

1. **Positive definite**: $d(\mathbf{x},\mathbf{y})\geq 0$ for all $\mathbf{x},\mathbf{y}$, and $d(\mathbf{x},\mathbf{y})=0\iff\mathbf{x}=\mathbf{y}$.
2. **Symmetric**: $d(\mathbf{x},\mathbf{y})=d(\mathbf{y},\mathbf{x})$.
3. **Triangle inequality**: $d(\mathbf{x},\mathbf{z})\leq d(\mathbf{x},\mathbf{y})+d(\mathbf{y},\mathbf{z})$.

## A metric needs only a norm

Unlike *length-via-inner-product*, distance does **not** require an inner product — a [[Norm]] is sufficient, via $d(\mathbf{x},\mathbf{y})=\|\mathbf{x}-\mathbf{y}\|$. But if the norm is induced by an inner product, the distance varies with the choice of inner product ([[mml-book]] Remark, p. 76).

## Metric and inner product behave in opposite directions

A key observation ([[mml-book]] Remark, p. 76): comparing the inner-product axioms (Def. 3.3) and the metric axioms (Def. 3.6), $\langle\mathbf{x},\mathbf{y}\rangle$ and $d(\mathbf{x},\mathbf{y})$ move *opposite* ways — **very similar $\mathbf{x},\mathbf{y}$ give a large inner product but a small distance.** This duality (similarity ↔ distance) is the conceptual substrate of the SVM (Ch 12) and of distance-based ML.

## ML uses

- **Nearest-neighbor methods** (k-NN) classify/regress by Euclidean (or other) distance.
- **Clustering** (k-means, GMM) minimizes within-cluster distances.
- **Mahalanobis distance** $d(\mathbf{x},\mathbf{y})=\sqrt{(\mathbf{x}-\mathbf{y})^\top\boldsymbol\Sigma^{-1}(\mathbf{x}-\mathbf{y})}$ is the metric induced by the inner product with SPD matrix $\boldsymbol\Sigma^{-1}$ — a recurring object (Murphy Ch 12.1 ↔ MML Ch 3).
- **Embedding similarity / retrieval** trades off cosine similarity (angle) against $\ell_2$ distance.

## Connections

- [[mml-ch03-analytic-geometry]] — §3.3 canonical reference (Def. 3.6).
- [[Norm]] — every norm induces a metric; metrics need only a norm.
- [[InnerProduct]] — inner-product-induced norms give the canonical metric.
- [[CauchySchwarzInequality]] — yields the triangle inequality the metric inherits.
- [[Angle]] — the "similarity" counterpart that moves opposite to distance.
- [[OrthogonalProjection]] — distance to a subspace = norm of the projection error.
