---
title: "Angle"
type: concept
tags: [analytic-geometry, foundational]
sources: [mml-ch03-analytic-geometry, mml-book]
last_updated: 2026-06-04
---

# Angle

The **angle** $\omega$ between two non-zero vectors $\mathbf{x},\mathbf{y}$ in an inner-product space is defined via the [[InnerProduct]] ([[mml-ch03-analytic-geometry|MML Ch 3]] §3.4, Eq. 3.25):

$$\cos\omega = \frac{\langle\mathbf{x},\mathbf{y}\rangle}{\|\mathbf{x}\|\,\|\mathbf{y}\|}, \qquad \omega\in[0,\pi].$$

Intuitively, the angle tells you **how similar the orientations of the two vectors are**. A positive scaling does not change it: for $\mathbf{y}=4\mathbf{x}$ the angle is $0$ ([[mml-book]] p. 77).

## Why it is well-defined: Cauchy-Schwarz

The [[CauchySchwarzInequality]] $|\langle\mathbf{x},\mathbf{y}\rangle|\leq\|\mathbf{x}\|\,\|\mathbf{y}\|$ forces $-1\leq\frac{\langle\mathbf{x},\mathbf{y}\rangle}{\|\mathbf{x}\|\,\|\mathbf{y}\|}\leq 1$ (Eq. 3.24). Since $\cos$ restricted to $[0,\pi]$ is invertible (Fig. 3.4), there is a **unique** $\omega\in[0,\pi]$ — making the angle a real, well-defined quantity.

## Example (dot product, MML 3.6)

For $\mathbf{x}=[1,1]^\top$, $\mathbf{y}=[1,2]^\top$ under the dot product: $\cos\omega=\frac{\mathbf{x}^\top\mathbf{y}}{\sqrt{\mathbf{x}^\top\mathbf{x}}\sqrt{\mathbf{y}^\top\mathbf{y}}}=\frac{3}{\sqrt{10}}$, so $\omega=\arccos\frac{3}{\sqrt{10}}\approx 0.32$ rad $\approx 18°$.

## The angle is inner-product-relative

Like length and orthogonality, the angle is **not intrinsic** to the vectors — it depends on the chosen inner product. The same pair $[1,1]^\top$, $[-1,1]^\top$ is at $90°$ under the dot product but at $\approx 109.5°$ under $\langle\mathbf{x},\mathbf{y}\rangle=\mathbf{x}^\top\operatorname{diag}(2,1)\mathbf{y}$ ([[mml-book]] Example 3.7).

## ML uses

- **Cosine similarity** — $\cos\omega$ is the alignment score between embeddings (word / sentence / image / user vectors); the angle, not the magnitude, carries semantic similarity.
- **[[OrthogonalProjection]]** — the projected length onto a unit axis is $\|\pi_U(\mathbf{x})\|=|\cos\omega|\,\|\mathbf{x}\|$ ([[mml-book]] Eq. 3.44).
- **Attention** — [[ScaledDotProductAttention|scaled dot-product attention]] scores are (unnormalized) cosine-like alignments.

## Connections

- [[mml-ch03-analytic-geometry]] — §3.4 canonical reference (Eqs. 3.24–3.26).
- [[InnerProduct]] — defines the angle.
- [[CauchySchwarzInequality]] — makes the definition well-formed.
- [[Orthogonality]] — the special case $\omega=\pi/2$ (zero inner product).
- [[Norm]] — appears in the denominator (normalization to unit length).
- [[DotProduct]] — the default inner product used in cosine similarity.
