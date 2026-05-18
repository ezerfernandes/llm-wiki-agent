---
title: "Collaborative Filtering"
type: concept
tags: [recommender-systems, machine-learning]
sources: [d2l-recommender-systems]
last_updated: 2026-05-16
---

# Collaborative Filtering

The central abstraction of [[RecommenderSystems|recommender-systems]] research. Term coined by the **Tapestry system** (Goldberg, Nichols, Oki & Terry 1992, *CACM*) — *"people collaborate to help one another perform the filtering process"*. In its broad sense, [[d2l-recommender-systems]] defines CF as *"the process of filtering for information or patterns using techniques involving collaboration among multiple users, agents, and data sources"*.

## Taxonomy (Su & Khoshgoftaar 2009)

- **[[MemoryBasedCF|Memory-based CF]]** — nearest-neighbor methods. *User-based* (find similar users by rating-vector overlap, predict by similarity-weighted average) or *item-based* (Sarwar, Karypis, Konstan & Riedl 2001). Limitation: scales poorly and breaks on sparse data because similarity is computed only over commonly-rated items.
- **[[ModelBasedCF|Model-based CF]]** — latent-factor models. Canonical example: [[MatrixFactorization]] (Funk 2006, Koren 2009). Handles sparsity and scales because the factorization is learned end-to-end.
- **Hybrid** — combines both.

[[d2l-recommender-systems]]'s editorial position: *model-based methods dominate* and are the path forward; neural extensions of model-based CF ([[AutoRec]], [[NeuMF]], [[CaserModel]]) make up the bulk of the chapter.

## Scope of "CF" vs side information

CF in the narrow sense uses **only the user-item interaction matrix** — no item content, no user profile, no context. Recommenders that *do* use such side information are called **content-based** (item-content-driven) or **context-based** (timestamp/location-aware). [[FactorizationMachines]] and [[DeepFM]] are the chapter's framework for incorporating arbitrary categorical features beyond pure interaction signal — strictly speaking, the *feature-rich* recommender family rather than CF proper.

## Connections
- [[RecommenderSystems]] — parent paradigm.
- [[MatrixFactorization]], [[AutoRec]], [[NeuMF]], [[NeuralCollaborativeFiltering]] — model-based CF instances.
- [[ImplicitFeedback]], [[ExplicitFeedback]] — the feedback types CF operates on.
- [[InteractionMatrix]] — CF's only input.
- [[YehudaKoren]] — most prominent CF / MF researcher.
- [[d2l-recommender-systems]] — primary source.
