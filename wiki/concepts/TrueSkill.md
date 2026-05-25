---
title: "TrueSkill"
type: concept
tags: [evaluation, ranking, rating-algorithm, bayesian]
sources: [ai-engineering-ch03-evaluation-methodology]
last_updated: 2024-12-04
---

# TrueSkill

**TrueSkill** ([[microsoft|Microsoft]] Research, Herbrich et al. 2007) is a Bayesian [[RatingAlgorithm|rating algorithm]] originally developed for **Xbox Live matchmaking**. Per [[ai-engineering-ch03-evaluation-methodology|*AI Engineering* Ch 3]], TrueSkill is one of the three named rating algorithms that *"can be adapted to evaluating AI models, such as Elo, Bradley–Terry, and TrueSkill."*

## How TrueSkill differs

| Property | [[EloRating\|Elo]] | [[BradleyTerry\|Bradley-Terry]] | TrueSkill |
|---|---|---|---|
| Multi-player | Pairwise only | Pairwise only | **Multi-player, multi-team** |
| Uncertainty estimate | No | No | **Yes (variance per player)** |
| Update rule | Incremental | Global ML fit | Bayesian update |
| Computational profile | Cheap | Medium | Medium-high |

The Bayesian framing gives each player a distribution (mean ± variance) rather than a single score — making it natural to express confidence and to **schedule matches that reduce uncertainty** about specific players' ratings.

## Why this matters for AI evaluation

Ch 3's comparative-evaluation section flags the **scalability bottleneck**: with 57 models and 1,596 pairs, you can't match every pair enough times. TrueSkill's per-player uncertainty enables **active matching strategies** — *"An efficient matching algorithm should sample matches that reduce the most uncertainty in the overall ranking"* — which Elo and Bradley-Terry don't naturally support.

## Position

[[ChatbotArena]] uses [[BradleyTerry|Bradley-Terry]], not TrueSkill, as of late 2024. TrueSkill is named in Ch 3 as a **candidate** algorithm that the AI-evaluation community could adopt for its uncertainty-aware matching, but is not yet the dominant choice.

## Connections

- [[ai-engineering-ch03-evaluation-methodology]] — primary source.
- [[RatingAlgorithm]] — parent concept.
- [[EloRating]] / [[BradleyTerry]] — sibling rating algorithms.
- [[ChatbotArena]] — currently uses Bradley-Terry, not TrueSkill.
- [[ComparativeEvaluation]] — parent paradigm.
- [[microsoft|Microsoft]] — authoring company.
