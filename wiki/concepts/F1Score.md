---
title: "F1 Score"
type: concept
tags: [evaluation, metrics]
sources: [2507.03152-medval, hands-on-llm-ch04-text-classification, hands-on-llm-ch11-fine-tuning-representation-models]
last_updated: 2026-05-23
---

# F1 Score

The harmonic mean of precision and recall, robust to [[ClassImbalance]] in a way that raw accuracy is not. Standard reporting metric in classification and information retrieval; complementary to confusion-matrix-derived measures used in [[BehavioralTesting]].

In **ordinal multi-class evaluation** like [[2507.03152-medval|MedVAL]]'s 4-class [[RiskLevelTaxonomy|risk taxonomy]], reported as **macro-F1** (mean of per-class F1) — ensures equal weighting across risk levels regardless of class frequency. Headline MedVAL result: average baseline macro-F1 = 36.7% → MedVAL macro-F1 = 51.0% across 10 LMs. For binary safe/unsafe collapse, F1 = 66.2% → 82.8%. Used alongside Cohen's $\kappa$ for ordinal agreement and Krippendorff's $\alpha$ for inter-rater consistency.

## Connections
- [[2507.03152-medval]] — uses macro-F1 as the primary evaluation metric for 4-class risk grading.
- [[NonInferiorityTest]] — bootstraps over F1 to compare LM evaluator vs single human expert.
- [[McNemarTest]] — paired significance test on F1 differences across baseline-vs-MedVAL.
- [[CohensKappa]] / [[KrippendorffAlpha]] — sibling agreement statistics complementing F1.

## From [[hands-on-llm-ch04-text-classification|*Hands-On LLMs* Ch 4]]

Ch 4 uses **weighted-average F1** (via `sklearn.metrics.classification_report`) as its **single headline metric** across all four pretrained-LLM classification regimes on [[RottenTomatoes|Rotten Tomatoes]]:

> "We will consider the weighted average of the F1 score throughout the examples in this book to make sure each class is treated equally." — Ch 4

The chapter introduces F1 alongside [[Precision|precision]], [[Recall|recall]], and [[Accuracy|accuracy]] via the [[ConfusionMatrix|confusion-matrix]] walkthrough:

> "The F1 score balances both precision and recall to create a model's overall performance." — Ch 4

The headline F1 progression on Rotten Tomatoes test (1,066 examples):

| Regime | F1 |
|---|---|
| [[TwitterRoBERTa]] (task-specific) | 0.80 |
| [[AllMPNetBaseV2]] + [[LogisticRegression]] | 0.85 |
| [[ZeroShotClassification|Zero-shot embeddings]] | 0.78 |
| [[FLANT5]]-small (generative encoder-decoder) | 0.84 |
| [[ChatGPT]] gpt-3.5-turbo-0125 (generative decoder-only) | 0.91 |

On Ch 4's balanced 533/533 binary test split, weighted-average F1 ≈ macro F1 ≈ accuracy — the choice of averaging mode is benign. Macro F1 (the [[2507.03152-medval|MedVAL]] choice) is the right pick for **imbalanced** multi-class settings.

## From [[hands-on-llm-ch11-fine-tuning-representation-models|*Hands-On LLMs* Ch 11]]

Ch 11 reuses Ch 4's weighted-F1 reporting convention for sequence classification — computed via `evaluate.load("f1")` / `load_metric("f1")` inside a Hugging Face `compute_metrics` hook:

```python
import numpy as np
from datasets import load_metric

def compute_metrics(eval_pred):
    logits, labels = eval_pred
    predictions = np.argmax(logits, axis=-1)
    load_f1 = load_metric("f1")
    f1 = load_f1.compute(predictions=predictions, references=labels)["f1"]
    return {"f1": f1}
```

**F1 ladder Ch 11 produces on Rotten Tomatoes**:

| Regime | F1 |
|---|---|
| Full FT `bert-base-cased` (1 epoch) | **0.85** |
| [[LayerFreezing|Freeze blocks 0–9]] | 0.80 |
| Freeze backbone, train head only | 0.63 |
| [[SetFit]] on 32 labels | 0.85 |

**Span-level F1 for NER**: Ch 11 introduces **[[seqeval|`seqeval`]]** for span-level F1 on the [[NamedEntityRecognition|NER]] task — *"we now have multiple predictions per document, namely per token."* Span-level F1 only counts an entity span as correct when both its start and its end are predicted correctly — stricter than naive per-token F1 and matches the CoNLL-2003 official evaluation.
