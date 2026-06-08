---
title: "Convex Set"
type: concept
tags: [optimization, convex-optimization, mathematics, foundational]
sources: [mml-ch07-continuous-optimization, mml-book, d2l-optimization]
last_updated: 2026-06-05
---

# Convex Set

A set $\mathcal{C}$ is **convex** if the straight line connecting any two of its elements stays entirely inside it ([[mml-ch07-continuous-optimization|MML Ch 7]] §7.3, Def. 7.2, Eq. 7.29): for any $x,y\in\mathcal{C}$ and any scalar $\theta\in[0,1]$,

$$\theta x+(1-\theta)y\in\mathcal{C}.$$

Figure 7.5 shows a convex set; Figure 7.6 a nonconvex one (a "dented" blob where a chord pokes outside).

## Why it matters

A **[[ConvexOptimization|convex optimization problem]]** requires both a [[ConvexFunction|convex objective]] *and* a convex feasible set ([[mml-ch07-continuous-optimization|MML Ch 7]] Eq. 7.38). Convex sets are the feasible regions where local optima are global and [[Duality|strong duality]] holds. The constraints $g_i(\mathbf{x})\le0$ and $h_j(\mathbf{x})=0$ "truncate functions at a scalar value, resulting in sets" — those sets must be convex.

## Relation to convex functions (the epigraph)

A [[ConvexFunction|convex function]] is a "bowl-like object"; the set obtained by **"pouring water into it to fill it up"** — the **epigraph** — is a convex set ([[mml-ch07-continuous-optimization|MML Ch 7]] p. 236). This correspondence (a convex function ↔ its convex epigraph) is the bridge used by the [[ConvexConjugate|Legendre–Fenchel transform]]: because a convex set is fully described by its **supporting hyperplanes**, a convex function is fully described by a function of its gradient.

## Closure properties

- **Intersections** of convex sets are convex ([[d2l-optimization]] §convexity) — the line-segment property holds in each, so it holds in the intersection.
- **Unions** are *not* convex in general.
- $\mathbb{R}^d$, half-spaces, and $\ell_p$ balls ($p\ge1$) are convex.

(Exercise 7.3 of [[mml-ch07-continuous-optimization|MML Ch 7]] probes intersection/union/difference of convex sets.)

## Connections

- [[mml-ch07-continuous-optimization]] — §7.3 Def. 7.2 canonical reference.
- [[ConvexFunction]] — its epigraph is a convex set; the dual notion.
- [[ConvexOptimization]] — needs a convex feasible set.
- [[Convexity]] — the umbrella concept (sets + functions).
- [[ConvexConjugate]] — uses supporting hyperplanes of convex sets.
- [[d2l-optimization]] — alternative reference (intersection/union facts).
</content>
