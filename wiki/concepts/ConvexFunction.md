---
title: "Convex Function"
type: concept
tags: [optimization, convex-optimization, mathematics, foundational]
sources: [mml-ch07-continuous-optimization, mml-book, d2l-optimization]
last_updated: 2026-06-05
---

# Convex Function

A function $f:\mathbb{R}^D\to\mathbb{R}$ whose domain is a [[ConvexSet|convex set]] is **convex** if for all $\mathbf{x},\mathbf{y}$ in the domain and any $\theta\in[0,1]$ ([[mml-ch07-continuous-optimization|MML Ch 7]] §7.3, Def. 7.3, Eq. 7.30):

$$f(\theta\mathbf{x}+(1-\theta)\mathbf{y})\;\leq\;\theta f(\mathbf{x})+(1-\theta)f(\mathbf{y}).$$

Geometrically, **the chord (straight line) between any two points of the graph lies above the function**. A **concave function** is the negative of a convex function. The "filled-in" region above the graph — the **epigraph** — is a [[ConvexSet|convex set]] (pour water into the bowl).

## Tests for convexity ([[mml-ch07-continuous-optimization|MML Ch 7]] Eq. 7.31, p. 237)

- **First-order** (differentiable $f$): convex iff the tangent lies below the graph everywhere, $f(\mathbf{y})\geq f(\mathbf{x})+\nabla_{\mathbf{x}}f(\mathbf{x})^\top(\mathbf{y}-\mathbf{x})$.
- **Second-order** (twice differentiable $f$): convex iff the [[Hessian]] is positive semidefinite, $\nabla_{\mathbf{x}}^2 f(\mathbf{x})\succeq0$, everywhere.
- **One-dimensional**: $f''\ge0$.

**Worked example** ([[mml-ch07-continuous-optimization|MML Ch 7]] Example 7.3): the **negative entropy** $f(x)=x\log_2 x$ is convex for $x>0$, verified against both Def. 7.3 (at $x=2,4$, midpoint $\theta=0.5$: LHS $3\log_2 3\approx4.75\le$ RHS $5$) and the first-order test.

## Operations that preserve convexity (closure)

- A **nonnegative weighted sum** of convex functions is convex ([[mml-ch07-continuous-optimization|MML Ch 7]] Example 7.4): $\alpha f$ for $\alpha\ge0$; $f_1+f_2$ (sum the two inequalities); hence $\alpha f_1+\beta f_2$ for $\alpha,\beta\ge0$.
- Affine compositions $f(\mathbf{A}\mathbf{x}+\mathbf{b})$ and pointwise maxima preserve convexity. "This is again the idea of closure that we introduced in Chapter 2 for vector spaces."

Standard convex examples: $\frac12 x^2$, $\exp(x)$, $\log\sum_i\exp(x_i)$ (log-sum-exp), $\|\mathbf{x}\|_p$ for $p\ge1$. Nonconvex: $\cos(\pi x)$.

## Why it matters

A convex objective over a [[ConvexSet|convex feasible set]] makes a [[ConvexOptimization|convex optimization problem]], where **every local minimum is global** and the first-order condition $\nabla f=\mathbf{0}$ is both necessary and sufficient. The inequality in Def. 7.3 is also called **[[JensensInequality|Jensen's inequality]]**.

## Connections

- [[mml-ch07-continuous-optimization]] — §7.3 Def. 7.3 canonical reference.
- [[ConvexSet]] — domain and epigraph; the dual notion.
- [[JensensInequality]] — the named form of the defining inequality.
- [[Hessian]] — the second-order PSD convexity test.
- [[ConvexOptimization]] — needs a convex objective.
- [[Convexity]] — the umbrella concept.
- [[ConvexConjugate]] — describes a convex function by its tangent slopes.
- [[d2l-optimization]] — alternative reference.
</content>
