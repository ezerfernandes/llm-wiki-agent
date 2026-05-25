---
title: "Explicit Feedback"
type: concept
tags: [recommender-systems, data, user-feedback, llm-app]
sources: [d2l-recommender-systems, d2l-introduction, ai-engineering-ch10-architecture-feedback]
last_updated: 2024-12-04
---

# Explicit Feedback

User preference signals **proactively provided by the user** — star ratings, thumbs up/down, written reviews. Canonical examples: IMDb 1–10 stars, Netflix 1–5 stars, YouTube thumbs.

## Defining traits

- **High-quality** — the user directly states a preference; little inference required.
- **Scarce** — collection requires user effort; *"many users may be reluctant to rate products"* ([[d2l-recommender-systems]]).
- **Censored / biased** — users preferentially rate items they feel strongly about, producing a bimodal one-star / five-star distribution (flagged on [[RecommenderSystems]] as a pathology from [[d2l-introduction]]).
- **Numeric / ordinal** — supports regression framings (predict the star rating) and the [[RMSE]] evaluation metric.

## Canonical datasets

- **[[MovieLens]]** — 1–5 stars; D2L's running benchmark.
- **Netflix Prize** dataset — 1–5 stars on ~480k users × 17k movies.
- **Yahoo! Music**, **Book-Crossing** — historical academic benchmarks.

## Modeling consequences

- **Rating prediction is the natural framing** — MSE / [[RMSE]] on observed entries. [[MatrixFactorization]] and [[AutoRec]] are designed for this regime.
- **Side information (timestamps, demographics) is helpful but not required** when explicit ratings carry strong signal.
- **Unobserved entries are treated as missing-at-random** by default — usually false in practice but tolerable for the rating-prediction task.

## Connections
- [[ImplicitFeedback]] — sibling category (more abundant, noisier).
- [[MatrixFactorization]], [[AutoRec]] — canonical explicit-feedback models.
- [[RMSE]] — explicit-feedback evaluation metric.
- [[MovieLens]] — canonical dataset.
- [[RecommenderSystems]] — parent application.
- [[d2l-recommender-systems]], [[d2l-introduction]] — sources.

## From [[ai-engineering-ch10-architecture-feedback|AI Engineering Ch 10]]

Ch 10 carries the recommender-systems definition into the **LLM application** setting and reports the same defining traits: high-quality but sparse, suffering from response biases, and standardized across applications (*"there are only so many ways you can ask a person if they like something"*).

### LLM-app forms of explicit feedback

- Thumbs up / down on a response.
- Upvote / downvote.
- Star rating.
- Yes/no answers to *"Did we solve your problem?"*

### Why explicit feedback is sparse

> *"Explicit feedback is easier to interpret, but it demands extra effort from users. Since many users may not be willing to put in this additional work, explicit feedback can be sparse, especially in applications with smaller user bases."* — Ch 10

### Response biases Ch 10 names

- **Self-selection** — *"unhappy users might be more likely to complain, causing the feedback to appear more negative than it is."*
- **[[LeniencyBias|Leniency bias]]** — overly-positive ratings to avoid conflict (the Uber 4.8-average example).
- **Randomness** — users click the easiest option to dispatch the prompt.
- **[[PositionBias|Position bias]]** — first option clicked more often regardless of quality.
- **[[PreferenceBias|Preference bias]]** — length, recency, familiarity proxies.

### Conversational interface implication

Ch 10 makes explicit that the conversational interface enables **a richer explicit-feedback vocabulary** — users can encode preferences directly in their natural-language follow-ups (*"shorter please"*, *"can you make it more formal"*). This blurs the explicit/implicit line that the recommender-systems framing kept sharp.
