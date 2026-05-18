---
title: "Interaction Matrix"
type: concept
tags: [recommender-systems, data-structure]
sources: [d2l-recommender-systems]
last_updated: 2026-05-16
---

# Interaction Matrix

The central data structure of [[CollaborativeFiltering|collaborative-filtering]] recommenders. A matrix $\mathbf{R}\in\mathbb{R}^{m\times n}$ where row $u$ corresponds to a user and column $i$ to an item; the entry $R_{ui}$ is the (observed) interaction value — a rating, a click, a purchase, a watch.

## Sparsity

The defining empirical property. Most $R_{ui}$ are **unobserved** — most users have not interacted with most items. [[d2l-recommender-systems]] reports **93.695% sparsity** on the [[MovieLens]] 100K interaction matrix; production recommenders routinely face 99.99%+ sparsity.

Sparsity is the *long-standing challenge* of recommender-systems research; it motivates:

- **Latent-factor methods** ([[MatrixFactorization]]) — fill in unobserved entries by low-rank approximation.
- **Side information** ([[FactorizationMachines]], [[DeepFM]]) — incorporate user/item features when interactions alone are insufficient.
- **Negative sampling** — when treating implicit feedback as ranking, must sample from the vast unobserved region.

## Synonyms

When values are exact star ratings the chapter uses **rating matrix** interchangeably. *Interaction matrix* is the broader term covering implicit feedback (clicks / 1, no-click / 0) too.

## Connections
- [[CollaborativeFiltering]] — relies on this matrix.
- [[MatrixFactorization]] — factorizes it.
- [[AutoRec]] — reconstructs rows/columns of it.
- [[ImplicitFeedback]], [[ExplicitFeedback]] — value semantics.
- [[NegativeSampling]] — addresses the unobserved-entries problem.
- [[Sparsity]] — defining property.
- [[d2l-recommender-systems]] — source.
