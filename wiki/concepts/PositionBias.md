---
title: "Position Bias (User Feedback)"
type: concept
tags: [user-feedback, bias, evaluation, ux]
sources: [ai-engineering-ch10-architecture-feedback]
last_updated: 2024-12-04
---

# Position Bias (User Feedback)

**The user-facing version of position bias: the position in which an option is presented influences whether users click / pick / endorse it — independent of quality.** Named in [[ai-engineering-ch10-architecture-feedback|*AI Engineering* Ch 10]] as one of four feedback biases to design around.

> *"The position in which an option is presented to users influences how this option is perceived. Users are generally more likely to click on the first suggestion than the second. If a user clicks on the first suggestion, this doesn't necessarily mean that it's a good suggestion."* — Ch 10

## Relationship to LLM-as-judge position bias

The wiki already documents [[FirstPositionBias|first-position bias]] in **AI judges** (Ch 3) — the AI tendency to favor option A in `(A, B)` pairs. This page documents the **user-side analog**: humans clicking the first option in a suggestion list.

A useful pairing: per the [[FirstPositionBias]] page, *"the position bias of AI is the opposite of that of humans. Humans tend to favor the answer they see last"* ([[RecencyBias|recency bias]]). The Ch 10 "users click the first suggestion more" claim describes a different setting (lists of suggestions, not pairwise A/B comparisons) where humans behave like AI judges — top-position-favoring. The directionality depends on the UI: in side-by-side, humans recency; in ranked lists, humans first-position.

## Mitigation

> *"When designing your feedback system, this bias can be mitigated by randomly varying the positions of your suggestions or by building a model to compute a suggestion's true success rate based on its position."* — Ch 10

Two patterns:

- **Randomize order** — the simplest defense; spreads the bias uniformly across options so it averages out.
- **Model the bias** — fit a position-dependent success-rate model; correct observed clicks for the position effect.

## Connections

- [[ai-engineering-ch10-architecture-feedback]] — primary source.
- [[FirstPositionBias]] — the LLM-as-judge sibling page.
- [[RecencyBias]] — the human counterpart in pairwise comparison settings.
- [[LeniencyBias]] / [[PreferenceBias]] — sibling Ch 10 user-feedback biases.
- [[ExplicitFeedback]] — the feedback class position bias most affects.
- [[DegenerateFeedbackLoop]] — uncorrected position bias compounds in recommender-system feedback loops.
