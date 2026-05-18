---
title: "Cauchy-Schwarz Inequality"
type: concept
tags: [analytic-geometry, foundational, inequality]
sources: [mml-book]
last_updated: 2026-05-16
---

# Cauchy-Schwarz Inequality

For any inner-product space $(V, \langle\cdot,\cdot\rangle)$ with induced norm $\|\mathbf{x}\|=\sqrt{\langle\mathbf{x},\mathbf{x}\rangle}$:

$$|\langle\mathbf{x},\mathbf{y}\rangle|\;\leq\;\|\mathbf{x}\|\,\|\mathbf{y}\|$$

with equality iff $\mathbf{x}$ and $\mathbf{y}$ are linearly dependent ([[mml-book]] §3.3, Eq. 3.17).

## Why it matters

The inequality is the precondition that makes the **angle definition** $\cos\omega = \frac{\langle\mathbf{x},\mathbf{y}\rangle}{\|\mathbf{x}\|\,\|\mathbf{y}\|}$ well-formed — Cauchy-Schwarz forces $\cos\omega\in[-1,+1]$ so $\omega$ is a real angle in $[0,\pi]$.

It is also the easiest route to the **triangle inequality** for the induced norm:

$$\|\mathbf{x}+\mathbf{y}\|^2 = \|\mathbf{x}\|^2 + 2\langle\mathbf{x},\mathbf{y}\rangle + \|\mathbf{y}\|^2 \leq (\|\mathbf{x}\|+\|\mathbf{y}\|)^2.$$

## Uses elsewhere

- **Probability**: $|\text{Cov}(X,Y)|\leq \sigma_X\sigma_Y$ (the correlation coefficient is in $[-1,+1]$) is Cauchy-Schwarz on the random-variable inner product $\langle X,Y\rangle = \mathbb{E}[XY]$.
- **Information theory**: bounds on mutual information.
- **Hölder inequality** generalizes Cauchy-Schwarz to $\ell_p$ norms.

## Connections

- [[mml-book]] — §3.3 canonical reference.
- [[InnerProduct]] — what the inequality lives on.
- [[Norm]] — induced norms inherit the triangle inequality from Cauchy-Schwarz.
- [[fundamental-inequalities-for-complex-numbers]] — algebrica.org's complex-number inequality page.
