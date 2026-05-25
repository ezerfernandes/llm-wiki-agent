---
title: "Recall"
type: concept
tags: [evaluation, metrics, classification]
sources: [hands-on-llm-ch04-text-classification]
last_updated: 2026-05-23
---

# Recall

For a classification task: **the fraction of actual positive examples the model correctly identified**.

$$\text{Recall} = \frac{\text{True Positives}}{\text{True Positives} + \text{False Negatives}}$$

Also called **sensitivity** or **true positive rate**.

Per [[hands-on-llm-ch04-text-classification|*Hands-On LLMs* Ch 4]]: *"Recall refers to how many relevant classes were found, which indicates its ability to find all relevant results."*

## Trade-off with Precision

Recall and [[Precision|precision]] are typically in tension; the [[F1Score|F1 score]] is the harmonic-mean compromise reported alongside both.

## Connections

- [[Precision]] — the complementary metric.
- [[F1Score]] — the harmonic mean of precision and recall.
- [[Accuracy]] — overall correctness.
- [[ConfusionMatrix]] — the data structure from which recall is computed.
- [[ClassificationReport]] — sklearn's tabular summary.
- [[hands-on-llm-ch04-text-classification]] — primary source.
