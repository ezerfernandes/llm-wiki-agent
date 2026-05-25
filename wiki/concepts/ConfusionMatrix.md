---
title: "Confusion Matrix"
type: concept
tags: [evaluation, metrics, classification]
sources: [hands-on-llm-ch04-text-classification]
last_updated: 2026-05-23
---

# Confusion Matrix

The 2×2 (binary) or K×K (multiclass) table tabulating **prediction vs ground-truth class counts** — the foundational data structure from which [[Precision|precision]], [[Recall|recall]], [[Accuracy|accuracy]], [[F1Score|F1]], and most other classification metrics are derived.

## Binary form

|  | Predicted Positive | Predicted Negative |
|---|---|---|
| **Actual Positive** | True Positive (TP) | False Negative (FN) |
| **Actual Negative** | False Positive (FP) | True Negative (TN) |

Metrics:
- **Accuracy** = (TP + TN) / (TP + FP + TN + FN)
- **Precision** = TP / (TP + FP) — *"how many of the items found are relevant"*
- **Recall** = TP / (TP + FN) — *"how many relevant classes were found"*
- **F1** = 2 · Precision · Recall / (Precision + Recall)

## From [[hands-on-llm-ch04-text-classification|*Hands-On LLMs* Ch 4]]

Ch 4 introduces the confusion matrix as the pedagogical anchor for the [[ClassificationReport|classification report]] metrics:

> "There are four combinations depending on whether we predict something correctly (True) versus incorrectly (False) and whether we predict the correct class (Positive) versus incorrect class (Negative). We can illustrate these combinations as a matrix, commonly referred to as a confusion matrix." — Ch 4

The chapter walks the four metric definitions explicitly:

> "**Precision** measures how many of the items found are relevant, which indicates the accuracy of the relevant results. **Recall** refers to how many relevant classes were found, which indicates its ability to find all relevant results. **Accuracy** refers to how many correct predictions the model makes out of all predictions, which indicates the overall correctness of the model. The **F1 score** balances both precision and recall to create a model's overall performance." — Ch 4

## Connections

- [[F1Score]] / [[Precision]] / [[Recall]] / [[Accuracy]] — the derived metrics.
- [[ClassificationReport]] — sklearn's tabular summary.
- [[Classification]] / [[TextClassification]] / [[SentimentAnalysis]] — the task settings where confusion matrices are reported.
- [[hands-on-llm-ch04-text-classification]] — primary source.
