---
title: "FITS Dataset (Feedback for Interactive Talk & Search)"
type: concept
tags: [dataset, feedback, conversational-ai, evaluation]
sources: [ai-engineering-ch10-architecture-feedback]
last_updated: 2024-12-04
---

# FITS Dataset

**Feedback for Interactive Talk & Search** — a dataset of user complaint feedback against a conversational search/talk bot, released by **Xu et al. (2022)**. Cited in [[ai-engineering-ch10-architecture-feedback|*AI Engineering* Ch 10]] for its automatically-clustered eight-category taxonomy of [[NaturalLanguageFeedback|natural-language complaint feedback]].

## The eight clusters

From Ch 10's Table 10-1 (clustering result from **Yuan et al. 2023**):

| Group | Feedback type | Count | % |
|---|---|---|---|
| 1 | Clarify their demand again | 3,702 | 26.54% |
| 2 | Complain the bot (1) doesn't answer the question / (2) gives irrelevant information / (3) tells the user to find out the answer on their own | 2,260 | 16.20% |
| 3 | Point out specific search results that can answer the question | 2,255 | 16.17% |
| 4 | Suggest the bot should use the search results | 2,130 | 15.27% |
| 5 | State the answer is (1) factually incorrect / (2) not grounded in the search results | 1,572 | 11.27% |
| 6 | Point out the bot's answer is not specific / accurate / complete / detailed | 1,309 | 9.39% |
| 7 | Point out the bot lacks confidence — *"I am not sure"* / *"I don't know"* | 582 | 4.17% |
| 8 | Complain about repetition / rudeness in bot responses | 137 | 0.99% |

(Total: 13,947 feedback messages.)

## Why this taxonomy is load-bearing

The Ch 10 use is **engineering-actionable**: each cluster maps to a different fix path.

- **Verbose / lacks-detail (clusters 6, 8)** — prompt-engineering: make responses more concise or more specific.
- **Doesn't use search results (clusters 3, 4)** — retrieval / grounding fix.
- **Factually incorrect / not grounded (cluster 5)** — [[Hallucination|hallucination]] mitigation; retrieval quality.
- **Lacks confidence (cluster 7)** — calibration; prompt-tune away from over-hedging.
- **Repetition / rudeness (cluster 8)** — output-side filtering or post-training.

> *"Understanding how the bot fails the user is crucial in making it better. For example, if you know that the user doesn't like verbose answers, you can change the bot's prompt to make it more concise. If the user is unhappy because the answer lacks details, you can prompt the bot to be more specific."* — Ch 10

## Methodological role

FITS is a worked example of the more general claim in Ch 10 that **complaint feedback can be clustered into a small actionable taxonomy** — rather than treated as a single negative-feedback bucket. The clustering itself is automatic (per Yuan et al. 2023); the taxonomy isn't hand-designed.

## Citations

- **Xu, J., et al. (2022).** "Learning New Skills after Deployment: Improving open-domain internet-driven dialogue with human feedback." (The FITS dataset paper.)
- **Yuan, W., et al. (2023).** Clustering analysis cited for the eight-group breakdown.

## Connections

- [[ai-engineering-ch10-architecture-feedback]] — primary source.
- [[NaturalLanguageFeedback]] — the feedback class FITS exemplifies.
- [[ConversationalFeedback]] — broader category.
- [[Hallucination]] — failure mode flagged by cluster 5.
- [[FalseRefusalRate]] / [[RefusalRate]] — related to cluster 7.
- [[Evaluation]] — applied use of feedback-clustering for evaluation/improvement.
