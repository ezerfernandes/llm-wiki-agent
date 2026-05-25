---
title: "Pointwise Evaluation"
type: concept
tags: [evaluation, methodology, ranking]
sources: [ai-engineering-ch03-evaluation-methodology]
last_updated: 2024-12-04
---

# Pointwise Evaluation

The complement to [[ComparativeEvaluation|comparative evaluation]]: *"With pointwise evaluation, you evaluate each model independently, then rank them by their scores"* ([[ai-engineering-ch03-evaluation-methodology|*AI Engineering* Ch 3]]).

## Ch 3's dance-contest analogy

> "If you want to find out which dancer is the best, you evaluate each dancer individually, give them a score, then pick the dancer with the highest score."

Versus comparative: *"you ask all candidates to dance side-by-side and ask the judges which candidate's dancing they like the most, and pick the dancer preferred by most judges."*

## Where pointwise wins

- Tasks where scoring is **easier than comparing** — code generation with unit tests (functional correctness gives a clean score per model), benchmarks with reference answers, anything with a clear rubric.
- **New-model integration is cheap**: evaluate the new model in isolation, no need to re-run comparisons against all existing models.
- **Private-model evaluation is feasible**: no leaderboard or comparison partners required.

## Where comparative wins

For subjective tasks where giving an absolute score is hard but picking the better of two is easier. *"It's easier to tell which song of the two songs is better than to give each song a concrete score."*

## Trade-off table (Ch 3 framing)

| Property | Pointwise | Comparative |
|---|---|---|
| Adding a new model | Just evaluate it | Re-evaluate against existing |
| Private models | Easy | Hard |
| Subjective tasks | Harder | Easier |
| Score interpretation | Absolute | Relative |
| Scoring-system design | Heavy lift | Light lift |
| Ranking algorithm | Trivial (sort) | Non-trivial (Elo, Bradley-Terry, TrueSkill) |

## Connections

- [[ai-engineering-ch03-evaluation-methodology]] — primary source.
- [[ComparativeEvaluation]] — the orthogonal approach.
- [[Evaluation]] — parent.
- [[LikertScale]] — typical scoring system for pointwise subjective tasks.
