---
title: "Accuracy"
type: concept
tags: [evaluation, metrics, classification]
sources: [hands-on-llm-ch04-text-classification]
last_updated: 2026-05-23
---

# Accuracy

For a classification task: **the fraction of all predictions that were correct**.

$$\text{Accuracy} = \frac{\text{True Positives} + \text{True Negatives}}{\text{All Predictions}}$$

Per [[hands-on-llm-ch04-text-classification|*Hands-On LLMs* Ch 4]]: *"Accuracy refers to how many correct predictions the model makes out of all predictions, which indicates the overall correctness of the model."*

## When accuracy lies

Accuracy is **misleading on imbalanced datasets** — predicting always the majority class on a 99:1 split yields 99% accuracy with zero useful behavior. This is why [[F1Score|F1]] (or macro-F1) is the default headline metric in production NLP / LLM work, and accuracy is treated as a coarse sanity check.

On Ch 4's **balanced** [[RottenTomatoes|Rotten Tomatoes]] test split (533 / 533), accuracy and weighted-average F1 closely track each other across the four model regimes.

## Connections

- [[Precision]] / [[Recall]] / [[F1Score]] — the precision-recall metric trio.
- [[ConfusionMatrix]] — the source data structure.
- [[ClassificationReport]] — sklearn's per-class summary that includes accuracy.
- [[ClassImbalance]] — the pathology where accuracy fails.
- [[hands-on-llm-ch04-text-classification]] — primary source.
