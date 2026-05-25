---
name: ContinuousColdStart
title: "Continuous Cold Start"
type: concept
tags: [recommender-systems, cold-start, continual-learning, personalization]
sources: [dmls-ch09-continual-learning]
last_updated: 2026-05-23
---

# Continuous Cold Start

Generalization of the classical **cold-start** problem (new user / new item lacks behavior history) to cover **existing** users whose history is stale or sparse. Per [[ChipHuyen|Huyen]]'s [[dmls-ch09-continual-learning|DMLS Ch 9]], [[Coveo]] reports that **~70% of online shoppers visit a given site fewer than 3 times per year** — meaning the majority of users are effectively continuously cold from the recommender's perspective even though they exist in the user table.

## Why the term matters
The classical cold-start framing implies a one-time onboarding problem: collect a few interactions and the user is "warm." Continuous cold start says the warm state is **never reached** for most users in low-frequency-engagement domains — every visit feels like a first visit. This shifts the modeling focus from per-user history accumulation toward:
- **Session-level personalization** ([[TikTok|TikTok]] within-session adaptation pattern).
- **Generalization across users via shared signals** — categorical features, item-side embeddings.
- **Continual-learning infrastructure** — the model has to update with the population, not the individual.

## Where it bites hardest
- E-commerce sites with infrequent purchase categories (cars, furniture, vacations).
- News/content recommenders where session-level interest dominates.
- Travel platforms where prior bookings poorly predict next ones.

## Mitigations per DMLS Ch 9
- Strong [[ContextualBandits|contextual bandits]] / [[ColdStart|cold-start]] strategies as first-class production patterns.
- [[ContinualLearning|Continual learning]] over the population so each new user sees a fresh, well-calibrated model.
- [[SessionBasedRecommendation|Session-based recommendation]] models (RNNs, [[transformer|Transformers]] over the in-session sequence).

## Connections
- [[ColdStart]] — the classical predecessor.
- [[ContinualLearning]] — the discipline-level response.
- [[ContextualBandits]] — handles partial-feedback exploration in cold settings.
- [[RecommenderSystems]] — the canonical application domain.
- [[Coveo]] — source of the 70%-infrequent-shopper statistic.
