---
title: "Preference Bias (User Feedback)"
type: concept
tags: [user-feedback, bias, evaluation, comparative-evaluation]
sources: [ai-engineering-ch10-architecture-feedback]
last_updated: 2024-12-04
---

# Preference Bias (User Feedback)

**An umbrella term for the many ways a user's preference signal is distorted by features unrelated to true quality — most prominently, length and [[RecencyBias|recency]].** Named in [[ai-engineering-ch10-architecture-feedback|*AI Engineering* Ch 10]] as one of four feedback biases to design around.

> *"Many other biases can affect a person's feedback, some of which have been discussed in this book. For example, people might prefer the longer response in a side-by-side comparison, even if the longer response is less accurate — length is easier to notice than inaccuracies. Another bias is recency bias, where people tend to favor the answer they see last when comparing two answers."* — Ch 10

## Length bias

The wiki already names [[VerbosityBias]] in the LLM-as-judge context (Ch 3). Ch 10 reports the *human* analog: in side-by-side comparison of model outputs, users favor longer responses even when length doesn't add quality — *because length is easier to notice than inaccuracies*. This means comparative feedback collected without length-controls systematically rewards verbosity.

## [[RecencyBias|Recency bias]]

Already in the wiki. Ch 10 names it explicitly as one of the preference-bias family: **users favor the answer seen last** in pairwise comparison. Mitigated by order randomization and double-evaluation (the [[FirstPositionBias|first-position-bias]] page's swap-and-check pattern, applied to humans).

## Why "preference bias" as a category

Where [[LeniencyBias]] is about absolute rating compression and [[PositionBias|position bias]] is about list-order effects, *preference bias* is about **what features users use to decide between options when they're not in fact judging the criterion you asked them to judge**. Length, formatting, familiarity, recency are all preference-bias channels.

## Implications for comparative evaluation

- Don't trust **single-pass** side-by-side comparison data — randomize order, swap-and-check (per Nemotron-4's synthetic-preference-data trick from [[FirstPositionBias]]).
- **Control for length** explicitly when collecting preference data — bucket by length, or filter pairs to similar lengths.
- **Cap the easy-to-notice channels** that users use as proxies for quality.

## Connections

- [[ai-engineering-ch10-architecture-feedback]] — primary source.
- [[LeniencyBias]] / [[PositionBias]] — sibling Ch 10 user-feedback biases.
- [[RecencyBias]] — most-named instance.
- [[VerbosityBias]] — AI-judge sibling for length bias.
- [[FirstPositionBias]] — swap-and-check mitigation is reusable here.
- [[ComparativeEvaluation]] — the methodology most affected.
- [[PreferenceData]] — what's distorted if biases aren't controlled.
