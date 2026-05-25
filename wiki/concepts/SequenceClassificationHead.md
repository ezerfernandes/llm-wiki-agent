---
title: "Sequence Classification Head"
type: concept
tags: [architecture, classification, fine-tuning, bert]
sources: [hands-on-llm-ch11-fine-tuning-representation-models]
last_updated: 2026-05-23
---

# Sequence Classification Head

The **sequence classification head** is the small task-specific neural network appended to a pretrained encoder (e.g., [[bert|BERT]]) to produce a **single label per document**. In Hugging Face, materialized by `AutoModelForSequenceClassification` and the `classifier` attribute that sits on top of the pooled `[CLS]` token's hidden state.

Per [[hands-on-llm-ch11-fine-tuning-representation-models|*Hands-On LLMs* Ch 11]]:

> *"We will use a pretrained BERT model and add a neural network as a classification head, both of which will be fine-tuned for classification. ... In practice, this means that the pretrained BERT model and the classification head are updated jointly. Instead of independent processes, they learn from one another and allow for more accurate representations."*

## Architecture

```
input_ids → BERT encoder → pooled [CLS] hidden state → Dense + activation → Linear (num_labels) → logits
```

The Hugging Face `BertForSequenceClassification` head is a dropout + linear projection from BERT's hidden size (`768` for `bert-base-cased`) to `num_labels`. Looking at the parameter names:

```
bert.embeddings...           # embeddings layers
bert.encoder.layer.0...      # encoder block 0
...
bert.encoder.layer.11...     # encoder block 11
bert.pooler.dense.weight     # CLS pooler
bert.pooler.dense.bias
classifier.weight            # the head — randomly initialized
classifier.bias
```

## How to load

```python
from transformers import AutoModelForSequenceClassification

model = AutoModelForSequenceClassification.from_pretrained(
    "bert-base-cased",
    num_labels=2  # binary sentiment classification
)
```

`num_labels` determines the head's output dimension; the head's weights are **randomly initialized** and learned from scratch during fine-tuning.

## Joint update vs frozen head

Ch 11's main demonstration trains backbone + head **jointly** (F1 = 0.85). The frozen-backbone-only-head variant freezes the encoder and trains only `classifier.*` (F1 = 0.63 — much worse). See [[LayerFreezing]].

## Architecturally vs token classification

| Aspect | Sequence head | [[TokenClassificationHead|Token classification head]] |
|---|---|---|
| Operates on | Pooled `[CLS]` representation | Per-token final hidden states |
| Output shape | `(batch, num_classes)` | `(batch, seq_len, num_classes)` |
| Use case | Document classification, [[NLI]], sentiment, paraphrase | NER, POS tagging |

## Connections

- [[hands-on-llm-ch11-fine-tuning-representation-models]] — primary source.
- [[TokenClassificationHead]] — sibling head for per-token outputs.
- [[FineTuningBert]] — D2L's broader fine-tuning template; the `[CLS]` + MLP pattern.
- [[ClsToken]] — the pooled hidden state the head consumes.
- [[bert]] — the canonical backbone.
- [[FineTuning]] — the parent operation.
- [[HuggingFace]] — the framework that ships `AutoModelForSequenceClassification`.
