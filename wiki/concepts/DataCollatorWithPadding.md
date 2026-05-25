---
title: "DataCollatorWithPadding"
type: concept
tags: [training, huggingface, data-collator, fine-tuning, batching]
sources: [hands-on-llm-ch11-fine-tuning-representation-models]
last_updated: 2026-05-23
---

# DataCollatorWithPadding

`transformers.DataCollatorWithPadding` is the Hugging Face data-collator that **pads each batch to the longest sequence in that batch** — the default collator for sequence-classification fine-tuning. Per [[hands-on-llm-ch11-fine-tuning-representation-models|*Hands-On LLMs* Ch 11]]:

> *"A DataCollator is a class that helps us build batches of data but also allows us to apply data augmentation. ... we will add padding to the input text to create equally sized representations. We use DataCollatorWithPadding for that."*

## The idiom

```python
from transformers import DataCollatorWithPadding

data_collator = DataCollatorWithPadding(tokenizer=tokenizer)

# Passed into the Trainer
trainer = Trainer(..., data_collator=data_collator)
```

Tokenize first **without** padding (`tokenizer(examples["text"], truncation=True)`), then let the collator pad **dynamically** at batch-build time. This is more memory-efficient than padding all examples to a global max length — batches with shorter sequences use less memory and run faster.

## Variants for other tasks

| Collator | Use case | Behavior |
|---|---|---|
| `DataCollatorWithPadding` | Sequence classification (Ch 11 regime 1) | Pad to longest in batch |
| [[DataCollatorForLanguageModeling]] | Masked-LM continued pretraining (Ch 11 regime 4) | Pad + apply random token masking |
| `DataCollatorForWholeWordMask` | MLM with whole-word masking | Pad + apply whole-word masking |
| [[DataCollatorForTokenClassification]] | NER / token classification | Pad inputs AND label sequences (with `-100`) |
| `DataCollatorForSeq2Seq` | Encoder-decoder fine-tuning | Pad source + target separately |

## Connections

- [[hands-on-llm-ch11-fine-tuning-representation-models]] — primary source.
- [[Trainer]] — the training-loop class that consumes the collator.
- [[TrainingArguments]] — Hugging Face's hyperparameter container.
- [[DataCollatorForLanguageModeling]] / [[DataCollatorForTokenClassification]] — sibling collators for other Ch 11 regimes.
- [[HuggingFace]] — distributes `transformers`.
- [[Tokenizer]] — the upstream component.
