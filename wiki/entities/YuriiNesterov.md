---
title: "Yurii Nesterov"
type: entity
tags: [person, researcher, optimization, mathematics]
sources: [d2l-optimization]
last_updated: 2026-05-16
---

# Yurii Nesterov

Russian-Belgian mathematician; foundational figure in convex optimization theory. Introduced **Nesterov accelerated gradient** ([[NesterovMomentum]], 1983) — a refinement of [[BorisPolyak|Polyak]]'s heavy-ball momentum with optimal $\mathcal{O}(1/T^2)$ convergence rate on smooth convex objectives. Author of *Introductory Lectures on Convex Optimization* (2004) and *Lectures on Convex Optimization* (2018), the canonical graduate references.

## Why he matters here

- **Nesterov accelerated gradient (1983).** $\mathbf{v}_t = \beta\mathbf{v}_{t-1}+\nabla f(\mathbf{x}_{t-1}-\eta\beta\mathbf{v}_{t-1})$ — evaluates the gradient at the *lookahead* point, achieving optimal $\mathcal{O}(1/T^2)$ rate vs Polyak's $\mathcal{O}(1/T)$ on convex problems.
- **Interior-point methods (1980s).** With Arkadi Nemirovski — polynomial-time interior-point algorithms for convex optimization.
- ***Lectures on Convex Optimization* (2018).** [[d2l-optimization]] §momentum cites this as the detailed theoretical treatment of momentum in the convex setting.

## Affiliations

- [[universitecatholiquedelouvain|Université catholique de Louvain]] (UCLouvain) — CORE (Center for Operations Research and Econometrics).
- [[higherschoolofeconomics|HSE University]] (Moscow).

## Connections

- [[d2l-optimization]] — momentum analysis cites Nesterov 2018.
- [[NesterovMomentum]] — the algorithm.
- [[BorisPolyak]] — Soviet-school colleague whose heavy-ball momentum Nesterov accelerated.
- [[ConvexOptimization]] — canonical reference.
