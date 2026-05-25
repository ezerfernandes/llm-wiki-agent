---
title: "seqeval"
type: concept
tags: [evaluation, ner, token-classification, metrics, huggingface]
sources: [hands-on-llm-ch11-fine-tuning-representation-models]
last_updated: 2026-05-23
---

# seqeval

`seqeval` is a Python library for **span-aware** evaluation of sequence-labeling tasks ([[NamedEntityRecognition|NER]], chunking, POS tagging), exposed in Hugging Face's `evaluate` package. The canonical metric for [[CoNLL2003|CoNLL-2003]] and any other [[BIOTagging|BIO-tagged]] benchmark.

Per [[hands-on-llm-ch11-fine-tuning-representation-models|*Hands-On LLMs* Ch 11]]:

> *"We will make use of the evaluate package by Hugging Face to create a `compute_metrics` function that allows us to evaluate performance on a token level."*

## Span-aware F1

Unlike naive per-token F1, `seqeval` only counts an entity span as correct when **both its start and its end are predicted correctly**. Example: predicting `B-PER I-PER` for *"Dean Palmer"* is correct; predicting `B-PER B-PER` (one entity split into two) or `B-PER I-LOC` (wrong type on continuation) is wrong. This matches the CoNLL evaluation script's behavior.

## Usage (Ch 11)

```python
import evaluate
seqeval = evaluate.load("seqeval")

def compute_metrics(eval_pred):
    logits, labels = eval_pred
    predictions = np.argmax(logits, axis=2)

    true_predictions = []
    true_labels = []

    # Document-level iteration
    for prediction, label in zip(predictions, labels):
        # Token-level iteration
        for token_prediction, token_label in zip(prediction, label):
            # Ignore -100 special tokens
            if token_label != -100:
                true_predictions.append([id2label[token_prediction]])
                true_labels.append([id2label[token_label]])

    results = seqeval.compute(
        predictions=true_predictions, references=true_labels
    )
    return {"f1": results["overall_f1"]}
```

The `-100` filter removes special tokens (`[CLS]`, `[SEP]`, padding) from the metric calculation, matching the `CrossEntropyLoss(ignore_index=-100)` convention used during training.

## Output

`seqeval.compute(...)` returns a dict with `overall_f1`, `overall_precision`, `overall_recall`, `overall_accuracy`, plus per-class breakdowns (e.g., `PER`, `ORG`, `LOC`, `MISC`).

## Connections

- [[hands-on-llm-ch11-fine-tuning-representation-models]] — primary source.
- [[NamedEntityRecognition]] / [[TokenClassification]] — task families it evaluates.
- [[BIOTagging]] — the label scheme it understands.
- [[CoNLL2003]] — the dataset it's the canonical metric for.
- [[F1Score]] — the underlying metric (computed span-aware here).
- [[HuggingFace]] — distributes via the `evaluate` package.
