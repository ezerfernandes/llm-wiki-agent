---
title: "DataCollatorForTokenClassification"
type: concept
tags: [training, huggingface, data-collator, ner, token-classification]
sources: [hands-on-llm-ch11-fine-tuning-representation-models]
last_updated: 2026-05-23
---

# DataCollatorForTokenClassification

`transformers.DataCollatorForTokenClassification` is the Hugging Face data-collator for [[TokenClassification|token-classification]] tasks (NER, POS tagging, chunking). Pads both **inputs** AND **labels** dynamically to the longest sequence in a batch, padding the label sequence with `-100` (the default `ignore_index` of PyTorch `CrossEntropyLoss`) so loss isn't computed on padded positions.

Per [[hands-on-llm-ch11-fine-tuning-representation-models|*Hands-On LLMs* Ch 11]]:

> *"Instead of `DataCollatorWithPadding`, we need a collator that works with classification on a token level, namely `DataCollatorForTokenClassification`."*

## The idiom

```python
from transformers import DataCollatorForTokenClassification

data_collator = DataCollatorForTokenClassification(tokenizer=tokenizer)

trainer = Trainer(
    model=model, args=training_args,
    train_dataset=tokenized["train"], eval_dataset=tokenized["test"],
    tokenizer=tokenizer,
    data_collator=data_collator,
    compute_metrics=compute_metrics,
)
trainer.train()
```

## Why a special collator

In sequence classification, labels are scalar (one per document) — padding doesn't apply to them. In token classification, labels are sequences (one per token) — they must be padded to match the input. The collator pads label sequences with `-100`; the loss function (`CrossEntropyLoss(ignore_index=-100)`) skips those positions.

The same `-100` convention also handles special tokens (`[CLS]`, `[SEP]`) and any continuation tokens the user wants to exclude from the loss — see [[LabelAlignment]].

## Connections

- [[hands-on-llm-ch11-fine-tuning-representation-models]] — primary source.
- [[TokenClassification]] — the parent task family.
- [[NamedEntityRecognition]] — Ch 11's worked use case.
- [[LabelAlignment]] — the upstream preprocessing step that produces the per-token labels (including `-100` for special tokens).
- [[DataCollatorWithPadding]] / [[DataCollatorForLanguageModeling]] — sibling collators for other Ch 11 regimes.
- [[Trainer]] — the training-loop class.
- [[seqeval]] — the span-aware F1 evaluator.
- [[HuggingFace]] — distributes `transformers`.
