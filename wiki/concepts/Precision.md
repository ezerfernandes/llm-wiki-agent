---
title: "Precision"
type: concept
tags: [evaluation, metrics, classification]
sources: [hands-on-llm-ch04-text-classification]
last_updated: 2026-05-23
---

# Precision

For a classification task: **the fraction of positive predictions that were correct**.

$$\text{Precision} = \frac{\text{True Positives}}{\text{True Positives} + \text{False Positives}}$$

Per [[hands-on-llm-ch04-text-classification|*Hands-On LLMs* Ch 4]]: *"Precision measures how many of the items found are relevant, which indicates the accuracy of the relevant results."*

## Trade-off with Recall

Precision and [[Recall|recall]] are typically in tension: tightening the decision threshold (predict positive only when very confident) raises precision but lowers recall; loosening it does the reverse. The [[F1Score|F1 score]] is the harmonic mean of the two and is the most common single-number summary.

## Connections

- [[Recall]] — the complementary metric.
- [[F1Score]] — the harmonic mean.
- [[Accuracy]] — overall correctness (orthogonal to precision when classes are imbalanced).
- [[ConfusionMatrix]] — the data structure from which precision is computed.
- [[ClassificationReport]] — sklearn's tabular summary of all four metrics.
- [[hands-on-llm-ch04-text-classification]] — primary source.
