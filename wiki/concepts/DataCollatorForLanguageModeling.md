---
title: "DataCollatorForLanguageModeling"
type: concept
tags: [training, huggingface, data-collator, mlm, masked-language-modeling, pretraining]
sources: [hands-on-llm-ch11-fine-tuning-representation-models]
last_updated: 2026-05-23
---

# DataCollatorForLanguageModeling

`transformers.DataCollatorForLanguageModeling` is the Hugging Face data-collator that **randomly masks tokens at batch-build time** for [[MaskedLanguageModel|masked-language-modeling]] (MLM) training. Used in [[hands-on-llm-ch11-fine-tuning-representation-models|*Hands-On LLMs* Ch 11]] for the [[ContinuedPretraining|continued-pretraining]] regime on `bert-base-cased`.

## The idiom

```python
from transformers import DataCollatorForLanguageModeling

data_collator = DataCollatorForLanguageModeling(
    tokenizer=tokenizer,
    mlm=True,
    mlm_probability=0.15
)
```

The `mlm_probability=0.15` matches BERT's original 15% masking rate. The collator applies BERT's standard 80/10/10 split internally: of the 15% masked positions, 80% are replaced with `[MASK]`, 10% with a random token, 10% left unchanged.

## Continued-pretraining setup (Ch 11)

```python
model = AutoModelForMaskedLM.from_pretrained("bert-base-cased")
tokenizer = AutoTokenizer.from_pretrained("bert-base-cased")

# Tokenize and remove labels (MLM is self-supervised)
def preprocess_function(examples):
    return tokenizer(examples["text"], truncation=True)

tokenized_train = train_data.map(preprocess_function, batched=True)
tokenized_train = tokenized_train.remove_columns("label")

data_collator = DataCollatorForLanguageModeling(
    tokenizer=tokenizer, mlm=True, mlm_probability=0.15
)

training_args = TrainingArguments(
    "model",
    learning_rate=2e-5,
    per_device_train_batch_size=16,
    num_train_epochs=10,
    weight_decay=0.01,
    save_strategy="epoch", report_to="none"
)

trainer = Trainer(
    model=model, args=training_args,
    train_dataset=tokenized_train, eval_dataset=tokenized_test,
    tokenizer=tokenizer, data_collator=data_collator
)
trainer.train()
model.save_pretrained("mlm")
```

## Token masking vs whole-word masking

Per Ch 11: *"There are two methods that are generally used for this: token and whole-word masking. With token masking, we randomly mask 15% of the tokens in a sentence. It might happen that part of a word will be masked. To enable masking of the entire word, we could apply whole-word masking."* For whole-word masking, swap in `DataCollatorForWholeWordMask`:

> *"Generally, predicting whole words tends to be more complicated than tokens, which makes the model perform better as it needs to learn more accurate and precise representations during training. However, it tends to take a bit more time to converge."* — Ch 11

See [[TokenMasking]] / [[WholeWordMasking]].

## Connections

- [[hands-on-llm-ch11-fine-tuning-representation-models]] — primary source.
- [[MaskedLanguageModel]] — the training objective.
- [[ContinuedPretraining]] — the Ch 11 use case.
- [[TokenMasking]] / [[WholeWordMasking]] — the two masking modes.
- [[DataCollatorWithPadding]] / [[DataCollatorForTokenClassification]] — sibling collators for other Ch 11 regimes.
- [[Trainer]] — the training-loop class.
- [[bert]] — the canonical target model.
- [[HuggingFace]] — distributes `transformers`.
