---
title: "Recency Bias"
type: concept
tags: [evaluation, bias, human-evaluator, user-feedback]
sources: [ai-engineering-ch03-evaluation-methodology, ai-engineering-ch10-architecture-feedback]
last_updated: 2024-12-04
---

# Recency Bias

The **human-evaluator counterpart** of [[FirstPositionBias|AI first-position bias]]. Per [[ai-engineering-ch03-evaluation-methodology|*AI Engineering* Ch 3]]:

> "Humans tend to favor the answer they see last, which is called recency bias."

This is the inverse of AI judges, which anchor on the *first* option in a comparison.

## Why it matters

In a pairwise evaluation pipeline:
- **AI judges** systematically prefer the first-shown option.
- **Human judges** systematically prefer the last-shown option.

If you use a mixed pipeline (some AI judges, some human judges) without randomizing order, you build **two opposite biases into the same dataset** — making aggregate results harder to interpret than either alone.

## Mitigation

Same as [[FirstPositionBias]]: randomize the presentation order, or evaluate every pair in both orderings and require agreement.

## Beyond evaluation

Recency bias is well-documented in the broader cognitive-science literature (serial-position effect, last-impression effects in interviews and lists). Ch 3's contribution is specifically pointing out that **AI and humans have opposite position biases**, which has direct methodological consequences for hybrid evaluation pipelines.

## Connections

- [[ai-engineering-ch03-evaluation-methodology]] — primary source.
- [[FirstPositionBias]] — the AI counterpart (inverse direction).
- [[LLMAsAJudge]] — the methodology where this matters.
- [[ComparativeEvaluation]] — parent paradigm.
- [[SelfBiasJudge]] / [[VerbosityBias]] — sibling AI-judge biases (not human-side).

## From [[ai-engineering-ch10-architecture-feedback|AI Engineering Ch 10]]

Ch 10 names recency bias as one of the **[[PreferenceBias|user-feedback preference biases]]** to design around — not just an evaluation-pipeline concern:

> *"Another bias is recency bias, where people tend to favor the answer they see last when comparing two answers."* — Ch 10

In product UX, recency bias affects:

- **Side-by-side comparative feedback** (e.g., ChatGPT's two-response comparison UI; [[gemini|Gemini]]'s partial-response side-by-side in Figure 10-16) — users may favor whichever response they read last.
- **Regeneration comparisons** — Figure 10-13 in Ch 10 shows ChatGPT asking users to compare a new response with the previous one; recency bias points toward the new response.

Standard mitigation (order randomization + swap-and-check) applies. The contribution Ch 10 adds is the **product-design** scope: recency bias isn't only a problem in offline evaluation pipelines — it shapes the live preference data your application is collecting from users right now.
