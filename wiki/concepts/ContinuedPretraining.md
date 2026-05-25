---
title: "Continued Pre-Training"
type: concept
tags: [finetuning, pretraining, self-supervision]
sources: [ai-engineering-ch07-finetuning, hands-on-llm-ch11-fine-tuning-representation-models]
last_updated: 2026-05-23
---

# Continued Pre-Training

**Self-supervised finetuning** on cheap task-related raw text *before* doing expensive supervised finetuning. Per [[ai-engineering-ch07-finetuning|*AI Engineering* Ch 7]]:

> "Before finetuning this pre-trained model with expensive task-specific data, you can finetune it with self-supervision using cheap task-related data. For example, to finetune a model for legal question answering, before finetuning it on expensive annotated (question, answer) data, you can finetune it on raw legal documents. Similarly, to finetune a model to do book summarization in Vietnamese, you can first finetune it on a large collection of Vietnamese text. **Self-supervised finetuning is also called continued pre-training.**"

## The recipe

1. Start with a general-purpose pre-trained model.
2. Continue **next-token prediction** training on a domain-specific raw text corpus (no labels needed).
3. (Optional) Then do supervised finetuning ([[SupervisedFinetuning|SFT]]) on a small labeled dataset for the target task.
4. (Optional) Then do preference finetuning.

## Why it works

- **Data is cheap**: raw text in the target domain is much easier to find than (instruction, response) pairs.
- **Bridges the distribution gap**: pre-trained models may be trained mostly on web English; legal / medical / Vietnamese text may be under-represented. Continued pre-training closes that gap.
- **Sample-efficient SFT downstream**: with the domain learned, SFT needs fewer labeled examples.

## When to consider it

- Your domain or language is **substantially under-represented** in the pre-training mix.
- You have **plenty of raw text** but **little labeled data**.
- You're noticing the model "doesn't know the vocabulary" of your domain.

## When it's overkill

- Your task is just style/format adaptation — SFT alone suffices.
- The base model is already strong in your domain.

## Connections

- [[FineTuning]] — parent operation.
- [[SupervisedFinetuning]] — the downstream stage.
- [[SelfSupervisedLearning]] / [[SelfSupervision]] — the training paradigm.
- [[Pretraining]] — the prior phase that continued pre-training extends.
- [[TransferLearning]] — broader framework.
- [[ai-engineering-ch07-finetuning]] — primary source.

## From [[hands-on-llm-ch11-fine-tuning-representation-models|*Hands-On LLMs* Ch 11]]

Ch 11 provides the **encoder-side [[MaskedLanguageModel|MLM]] recipe** for continued pretraining — complementing the next-token-prediction recipe sketched in [[ai-engineering-ch07-finetuning|AI Engineering Ch 7]] for decoder-only models. The three-stage pipeline:

> *"Instead of adopting this two-step approach [pretrain + fine-tune], we can squeeze another step between them, namely continue pretraining an already pretrained BERT model. ... It is like going from a general BERT model to a BioBERT model specialized for the medical domain, to a fine-tuned BioBERT model to classify medication."*

The recipe (Ch 11):

```python
from transformers import AutoModelForMaskedLM, AutoTokenizer
from transformers import DataCollatorForLanguageModeling, Trainer, TrainingArguments

model = AutoModelForMaskedLM.from_pretrained("bert-base-cased")
tokenizer = AutoTokenizer.from_pretrained("bert-base-cased")

# MLM is self-supervised — remove labels
tokenized_train = train_data.map(preprocess_function, batched=True).remove_columns("label")
tokenized_test  = test_data.map(preprocess_function, batched=True).remove_columns("label")

data_collator = DataCollatorForLanguageModeling(
    tokenizer=tokenizer, mlm=True, mlm_probability=0.15
)

training_args = TrainingArguments(
    "model", learning_rate=2e-5,
    per_device_train_batch_size=16, num_train_epochs=10,
    weight_decay=0.01, save_strategy="epoch", report_to="none"
)

trainer = Trainer(
    model=model, args=training_args,
    train_dataset=tokenized_train, eval_dataset=tokenized_test,
    tokenizer=tokenizer, data_collator=data_collator
)
tokenizer.save_pretrained("mlm")
trainer.train()
model.save_pretrained("mlm")

# Then load the adapted model for the downstream classification fine-tune:
from transformers import AutoModelForSequenceClassification
model = AutoModelForSequenceClassification.from_pretrained("mlm", num_labels=2)
```

**Two masking modes**: [[TokenMasking|token masking]] (default, faster convergence) vs [[WholeWordMasking|whole-word masking]] (harder, more accurate representations, slower).

**Empirical demonstration via [[FillMaskPipeline|`fill-mask`]]**: on prompt *"What a horrible [MASK]!"*, base `bert-base-cased` predicts `idea / dream / thing / day / thought`; the MLM-continued-on-Rotten-Tomatoes model predicts `movie / film / mess / comedy / story` — *"clearly shows us that the model is more biased toward the data that we fed it compared to the pretrained model."*

**Reference**: Chi Sun et al. *"How to Fine-Tune BERT for Text Classification?"* (CCL 2019). *"Continuing pretraining on a pretrained BERT model has been shown to improve the performance of models in classification tasks and is a worthwhile addition to the fine-tuning pipeline."*

**Position in the wiki**: Ch 11 implements the **[[MaskedLanguageModel|MLM]] half** of [[hands-on-llm-ch10-creating-text-embedding-models|Ch 10]]'s [[DomainAdaptation|domain-adaptation]] / [[AdaptivePretraining|adaptive-pretraining]] recipe matrix; Ch 10 had walked the [[TSDAE|TSDAE]] half. Together, Ch 10 + Ch 11 give the wiki both unsupervised techniques for Stage 1 of adaptive pretraining (TSDAE for sentence-level, MLM for token-level), each with runnable code.
