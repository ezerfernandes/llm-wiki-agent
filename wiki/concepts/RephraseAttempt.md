---
title: "Rephrase Attempt (Natural-Language Feedback)"
type: concept
tags: [user-feedback, natural-language-feedback, llm-app]
sources: [ai-engineering-ch10-architecture-feedback]
last_updated: 2024-12-04
---

# Rephrase Attempt (Natural-Language Feedback)

**A user re-asking the same question in different words — a [[NaturalLanguageFeedback|natural-language feedback]] signal that the model misunderstood.** Per [[ai-engineering-ch10-architecture-feedback|*AI Engineering* Ch 10]]:

> *"To correct errors, users might try to rephrase their requests. … Rephrase attempts can be detected using heuristics or ML models."* — Ch 10

Figure 10-12 in Ch 10 shows the canonical example: a user (1) terminates the model's generation early, then (2) rephrases the original question — combined, the two signals make the misunderstanding diagnosis robust.

## Detection

- **Heuristic** — embedding similarity between consecutive user messages above a threshold while the in-between model response is non-trivial.
- **ML-based** — a small classifier trained on labeled `(turn_n, turn_n+1)` pairs.

## Signal stacking

Rephrase alone is ambiguous (a user might add detail, not rephrase to correct). Combined with an [[ErrorCorrection|error-correction]] opener, early termination, or low [[ConfidenceRequest|"are you sure?"]] turn, the signal hardens.

## Where it's most useful

- **Quality monitoring** — rephrase-attempt rate per session as a top-line metric.
- **Failure mining** — pairs `(original, rephrased)` are a corpus of *what users had to say twice* — direct input for prompt engineering improvements or fine-tuning.

## Connections

- [[ai-engineering-ch10-architecture-feedback]] — primary source.
- [[NaturalLanguageFeedback]] — parent category.
- [[ErrorCorrection]] / [[ActionCorrectingFeedback]] — sibling signals; rephrase often co-occurs with these.
- [[SemanticSimilarity]] — the heuristic detector.
- [[ConversationalFeedback]] — grandparent category.
