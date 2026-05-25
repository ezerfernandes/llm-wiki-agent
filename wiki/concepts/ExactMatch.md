---
title: "Exact Match"
type: concept
tags: [evaluation, metric, similarity]
sources: [ai-engineering-ch03-evaluation-methodology]
last_updated: 2024-12-04
---

# Exact Match

The simplest reference-based similarity metric: a **binary** indicator of whether a generated response matches a reference exactly. Per [[ai-engineering-ch03-evaluation-methodology|*AI Engineering* Ch 3]]: *"Exact matching works for tasks that expect short, exact responses such as simple math problems, common knowledge queries, and trivia-style questions."*

## Variants

- **Strict match** — output must equal a reference verbatim.
- **Contains-the-reference match** — accepts any output containing the reference string. The relaxation lets *"The answer is 5"* count as matching *"5"* for *"What's 2 + 3?"*

## The "contains" trap

Ch 3's worked counterexample: *"Consider the question 'What year was Anne Frank born?' Anne Frank was born on June 12, 1929, so the correct response is 1929. If the model outputs 'September 12, 1929', the correct year is included in the output, but the output is factually wrong."* Contains-match accepts the factually wrong answer.

## Where exact match breaks

For open-ended generation, exact match collapses to noise. Ch 3 example: *"Comment ça va?"* has many valid English translations (*"How are you?"*, *"How is everything?"*, *"How are you doing?"*, *"How is it going?"*). Reference sets can never enumerate all of them — and **the longer and more complex the source, the more valid translations exist.**

> "It's impossible to create an exhaustive set of possible responses for an input. For complex tasks, lexical similarity and semantic similarity work better."

## Connections

- [[ai-engineering-ch03-evaluation-methodology]] — primary source.
- [[SimilarityMeasurement]] — parent concept.
- [[LexicalSimilarity]] / [[SemanticSimilarity]] — the alternatives when exact match is too brittle.
- [[ReferenceData]] / [[ReferenceBasedMetric]] — exact match consumes reference data.
