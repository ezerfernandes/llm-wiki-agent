---
title: "Classification Report"
type: concept
tags: [evaluation, metrics, sklearn, classification]
sources: [hands-on-llm-ch04-text-classification]
last_updated: 2026-05-23
---

# Classification Report

The **per-class precision / recall / F1-score / support table** produced by [[sklearn|scikit-learn]]'s `sklearn.metrics.classification_report` function — the chapter-default evaluation primitive in *Hands-On LLMs* Ch 4 and a near-universal practitioner shorthand for *"show me the per-class breakdown."*

## Output format

```
                precision    recall  f1-score   support

Negative Review     0.76      0.88      0.81       533
Positive Review     0.86      0.72      0.78       533

       accuracy                         0.80      1066
      macro avg     0.81      0.80      0.80      1066
   weighted avg     0.81      0.80      0.80      1066
```

Four kinds of rows:

- **Per-class** — precision / recall / F1 / support for each target class.
- **Accuracy** — overall accuracy across all predictions.
- **Macro avg** — unweighted mean of per-class metrics (each class counted equally).
- **Weighted avg** — class-frequency-weighted mean of per-class metrics.

## From [[hands-on-llm-ch04-text-classification|*Hands-On LLMs* Ch 4]]

Ch 4 wraps the function in a one-liner reused across all four model regimes:

```python
from sklearn.metrics import classification_report

def evaluate_performance(y_true, y_pred):
    performance = classification_report(
        y_true, y_pred,
        target_names=["Negative Review", "Positive Review"]
    )
    print(performance)
```

The chapter reports the **weighted-average F1 row** as its headline metric — *"we will consider the weighted average of the F1 score throughout the examples in this book to make sure each class is treated equally."*

On the balanced [[RottenTomatoes|Rotten Tomatoes]] test split (533 negative / 533 positive), weighted-average F1 ≡ macro-average F1, so the choice is benign for this dataset.

## Per-class F1 progression in Ch 4 (Rotten Tomatoes test)

| Regime | Neg F1 | Pos F1 | Weighted F1 |
|---|---|---|---|
| Twitter-RoBERTa | 0.81 | 0.78 | 0.80 |
| Embeddings + LogReg | 0.85 | 0.85 | 0.85 |
| Zero-shot embeddings | 0.78 | 0.78 | 0.78 |
| Flan-T5 small | 0.84 | 0.84 | 0.84 |
| ChatGPT GPT-3.5 | 0.92 | 0.91 | 0.91 |

## Connections

- [[F1Score]] — the headline metric the report computes.
- [[Precision]] / [[Recall]] / [[Accuracy]] / [[ConfusionMatrix]] — the other report metrics.
- [[sklearn]] — the library providing the function.
- [[hands-on-llm-ch04-text-classification]] — primary source.
