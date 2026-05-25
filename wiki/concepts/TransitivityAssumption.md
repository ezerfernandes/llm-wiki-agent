---
title: "Transitivity Assumption"
type: concept
tags: [evaluation, ranking, methodology]
sources: [ai-engineering-ch03-evaluation-methodology]
last_updated: 2024-12-04
---

# Transitivity Assumption

The assumption that **A>B ∧ B>C ⇒ A>C** — used by every [[RatingAlgorithm|rating algorithm]] ([[EloRating|Elo]], [[BradleyTerry|Bradley-Terry]], [[TrueSkill]]) to avoid needing every pairwise comparison. Per [[ai-engineering-ch03-evaluation-methodology|*AI Engineering* Ch 3]]:

> "Ranking algorithms typically assume transitivity. If model A ranks higher than B, and B ranks higher than C, then with transitivity, you can infer that A ranks higher than C. This means that if the algorithm is certain that A is better than B and B is better than C, it doesn't need to compare A against C to know that A is better."

## Why it matters

[[ComparativeEvaluation|Comparative evaluation]]'s pair count grows quadratically (57 models → 1,596 pairs). Without transitivity, you'd need direct comparisons for every pair — infeasible at scale. With transitivity, you can infer most rankings from a sparse subset of pairwise outcomes.

## Why it's contested for AI

Ch 3 explicitly flags this as **an open question** for AI evaluation:

> "However, it's unclear if this transitivity assumption holds for AI models. Many papers that analyze Elo for AI evaluation cite transitivity assumption as a limitation (Boubdir et al.; Balduzzi et al.; and Munos et al.). They argued that human preference is not necessarily transitive. In addition, non-transitivity can happen because different model pairs are evaluated by different evaluators and on different prompts."

## Two sources of non-transitivity

1. **Genuinely non-transitive preferences** — humans might prefer A to B, B to C, and C to A on a rock-paper-scissors basis when models excel at different things.
2. **Evaluator/prompt heterogeneity** — different model pairs get evaluated by different people on different prompts, so the comparisons are *not over the same task distribution*. This is a methodological artifact rather than a fundamental preference structure.

## Mitigation

- Explicit modeling of non-transitivity in rating algorithms (active research).
- Larger and more uniform evaluator/prompt distributions (LMSYS's hard-prompt filtering is a step toward this).
- Stratified comparison by task category to reduce heterogeneity.

## Connections

- [[ai-engineering-ch03-evaluation-methodology]] — primary source.
- [[RatingAlgorithm]] / [[EloRating]] / [[BradleyTerry]] / [[TrueSkill]] — algorithms that depend on transitivity.
- [[ComparativeEvaluation]] — the paradigm whose scalability depends on this.
- [[ChatbotArena]] — where the assumption gets stress-tested in practice.
- [[ComparisonData]] — the preference-data form that feeds into all of this.
