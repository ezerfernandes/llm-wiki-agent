---
title: "Win Rate"
type: concept
tags: [evaluation, metric, ranking]
sources: [ai-engineering-ch03-evaluation-methodology]
last_updated: 2024-12-04
---

# Win Rate

The basic comparative signal: *"The probability that model A is preferred over model B is the win rate of A over B"* ([[ai-engineering-ch03-evaluation-methodology|*AI Engineering* Ch 3]]). Computed by looking at all matches between A and B and calculating the percentage A wins.

## In a ranking pipeline

[[RatingAlgorithm|Rating algorithms]] ([[EloRating|Elo]], [[BradleyTerry|Bradley-Terry]], [[TrueSkill]]) consume win rates between pairs as input and produce global rankings as output. The win rate is the **observed signal**; the rating is the **inferred latent strength**.

## The comparative-to-absolute gap

A win rate is **relative**, not absolute. Ch 3 example:

> "Imagine that we're using model A for customer support, and model A can resolve 70% of all the tickets. Consider model B, which wins against A 51% of the time. It's unclear how this 51% win rate will be converted to the number of requests model B can resolve. Several people have told me that in their experience, a 1% change in the win rate can induce a huge performance boost in some applications but just a minimal boost in other applications."

## Match outcomes feeding win rate

Many comparative-eval platforms allow **ties** (*"to avoid a winner being picked at random when drafts are equally good or bad"*) — meaning win rate is typically computed as `wins / (wins + losses)` excluding ties, or as `(wins + 0.5 × ties) / total` depending on the platform.

## Connections

- [[ai-engineering-ch03-evaluation-methodology]] — primary source.
- [[ComparativeEvaluation]] — parent paradigm.
- [[RatingAlgorithm]] — consumes win rates.
- [[EloRating]] / [[BradleyTerry]] / [[TrueSkill]] — specific consumers.
- [[ChatbotArena]] — where win rates are computed at scale.
- [[ComparisonData]] — the preference-data form whose aggregate is win rate.
