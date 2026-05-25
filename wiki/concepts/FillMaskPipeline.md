---
title: "Fill-Mask Pipeline"
type: concept
tags: [inference, huggingface, mlm, evaluation, qualitative]
sources: [hands-on-llm-ch11-fine-tuning-representation-models]
last_updated: 2026-05-23
---

# Fill-Mask Pipeline

Hugging Face's `pipeline("fill-mask")` wraps an `AutoModelForMaskedLM` checkpoint into a one-line inference tool that predicts the top-k tokens for a `[MASK]` position in an input sentence. The canonical **qualitative evaluation tool** for [[MaskedLanguageModel|MLM]] / [[ContinuedPretraining|continued-pretraining]] runs.

## Usage (Ch 11)

```python
from transformers import pipeline

# Base BERT
mask_filler = pipeline("fill-mask", model="bert-base-cased")
preds = mask_filler("What a horrible [MASK]!")
for pred in preds:
    print(f">>> {pred['sequence']}")
```

Output (base `bert-base-cased`):

```
>>> What a horrible idea!
>>> What a horrible dream!
>>> What a horrible thing!
>>> What a horrible day!
>>> What a horrible thought!
```

After [[ContinuedPretraining|continued-pretraining]] on Rotten Tomatoes:

```python
mask_filler = pipeline("fill-mask", model="mlm")  # saved checkpoint
preds = mask_filler("What a horrible [MASK]!")
```

Output:

```
>>> What a horrible movie!
>>> What a horrible film!
>>> What a horrible mess!
>>> What a horrible comedy!
>>> What a horrible story!
```

Per [[hands-on-llm-ch11-fine-tuning-representation-models|Ch 11]]: *"A horrible movie, film, mess, etc. clearly shows us that the model is more biased toward the data that we fed it compared to the pretrained model."*

## Why this matters

The fill-mask comparison is the **lowest-cost diagnostic** for whether continued pretraining actually shifted the model's distribution toward the target domain. Before running the expensive downstream fine-tune, you can verify that the MLM stage worked by comparing predictions on domain-relevant prompts.

## Connections

- [[hands-on-llm-ch11-fine-tuning-representation-models]] — primary source.
- [[MaskedLanguageModel]] — the training objective the pipeline exposes.
- [[ContinuedPretraining]] — the Ch 11 use case (qualitative diagnostic).
- [[Pipeline]] — Hugging Face's broader pipeline abstraction.
- [[HuggingFace]] — distributes `transformers`.
- [[bert]] — the canonical backbone.
