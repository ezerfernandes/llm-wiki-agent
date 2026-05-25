---
title: "Bradley-Terry"
type: concept
tags: [evaluation, ranking, rating-algorithm, statistics]
sources: [ai-engineering-ch03-evaluation-methodology]
last_updated: 2024-12-04
---

# Bradley-Terry

The **Bradley-Terry model** (Bradley & Terry, 1952) is a probabilistic [[RatingAlgorithm|rating algorithm]] for pairwise comparisons. Per [[ai-engineering-ch03-evaluation-methodology|*AI Engineering* Ch 3]], Bradley-Terry is the algorithm [[ChatbotArena|LMSYS Chatbot Arena]] switched to after finding [[EloRating|Elo]] sensitive to evaluator/prompt order.

## How it differs from Elo

| Property | [[EloRating\|Elo]] | Bradley-Terry |
|---|---|---|
| Update rule | Incremental per-match | Global maximum-likelihood fit |
| Sensitivity to evaluation order | Yes | No |
| Computational cost | Cheap per match | Heavier (re-fit periodically) |
| Interpretability | Familiar "Elo points" | Probabilistic strengths |

Bradley-Terry models the probability that player A beats player B as `P(A beats B) = π_A / (π_A + π_B)` where `π_A`, `π_B` are latent strengths. Fitting maximizes the likelihood over all observed matches simultaneously — it doesn't depend on the order matches occurred.

## Why LMSYS switched

Ch 3: *"LMSYS's Chatbot Arena originally used Elo to compute models' ranking but later switched to the Bradley–Terry algorithm because they found Elo sensitive to the order of evaluators and prompts."*

When the evaluator population and prompt distribution shifts over time (as they do on a public leaderboard with model bursts), order-sensitive Elo produces artifacts. Bradley-Terry's global fit absorbs the entire history into a single coherent ranking.

## The nomenclature contradiction

Even after switching, LMSYS continued displaying scores as "Elo scores" for user familiarity — *"They scaled the resulting Bradley-Terry scores to make them look like Elo scores."* The displayed Chatbot Arena "Elo score" since the switch is actually a rescaled Bradley-Terry strength.

## Connections

- [[ai-engineering-ch03-evaluation-methodology]] — primary source.
- [[RatingAlgorithm]] — parent concept.
- [[EloRating]] — the algorithm Bradley-Terry replaced on LMSYS.
- [[TrueSkill]] — sibling Bayesian rating algorithm.
- [[ChatbotArena]] — current LMSYS implementation uses this.
- [[ComparativeEvaluation]] — parent paradigm.
- [[TransitivityAssumption]] — Bradley-Terry assumes it.
