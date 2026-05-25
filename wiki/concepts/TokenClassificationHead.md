---
title: "Token Classification Head"
type: concept
tags: [architecture, ner, token-classification, fine-tuning, bert]
sources: [hands-on-llm-ch11-fine-tuning-representation-models]
last_updated: 2026-05-23
---

# Token Classification Head

The **token classification head** is the small task-specific neural network appended to a pretrained encoder to produce **one label per token** in the input sequence. In Hugging Face, materialized by `AutoModelForTokenClassification`.

Per [[hands-on-llm-ch11-fine-tuning-representation-models|*Hands-On LLMs* Ch 11]]:

> *"Rather than relying on the aggregation or pooling of token embeddings, the model now makes predictions for individual tokens in a sequence."*

## Architecture

```
input_ids → BERT encoder → per-position hidden states → Linear (num_labels) per token → logits per token
```

A dropout + linear projection from BERT's hidden size to `num_labels` (e.g., 9 for [[CoNLL2003|CoNLL-2003]]'s [[BIOTagging|BIO scheme]]), applied independently to **each position's** hidden state. Output shape: `(batch, seq_len, num_labels)`.

## How to load

```python
from transformers import AutoModelForTokenClassification

model = AutoModelForTokenClassification.from_pretrained(
    "bert-base-cased",
    num_labels=len(id2label),
    id2label=id2label,
    label2id=label2id
)
```

The `id2label` / `label2id` mappings let inference outputs surface as human-readable strings (`B-PER`, `I-LOC`, etc.) instead of integers — exposed by `pipeline("token-classification")`.

## Joint vs independent classification

The head treats each token's classification as **independent** given the encoder's representations. There's no per-pair transition modeling (as in a CRF layer). For BIO sequences, this means **the model can theoretically predict illegal sequences** like `O I-PER I-PER` (an inner-of-person without a preceding beginning). In practice, BERT-class encoders learn the valid transitions implicitly and rarely produce illegal sequences; for stricter guarantees, a CRF layer can be added on top.

## Inference pipeline

```python
from transformers import pipeline
token_classifier = pipeline("token-classification", model="ner_model")
token_classifier("My name is Maarten.")
```

Returns one dict per **predicted-entity subtoken** (positions where the model predicted a non-`O` label), with the predicted entity, confidence score, token text, and character offsets in the input.

## Connections

- [[hands-on-llm-ch11-fine-tuning-representation-models]] — primary source.
- [[SequenceClassificationHead]] — sibling head for document-level outputs.
- [[TokenClassification]] — the parent task family.
- [[NamedEntityRecognition]] — Ch 11's worked use case.
- [[BIOTagging]] — the standard label scheme.
- [[bert]] — the canonical backbone.
- [[FineTuningBert]] — broader template (Ch 11's *"token-level tagging"* row).
- [[HuggingFace]] — distributes `AutoModelForTokenClassification`.
