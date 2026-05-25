---
title: "Trainer"
type: concept
tags: [training, framework]
sources: [madewithml-training, d2l-linear-regression, hands-on-llm-ch11-fine-tuning-representation-models]
last_updated: 2026-05-23
---

# Trainer

An abstraction (e.g., HuggingFace `Trainer`, [[PyTorchLightning|PyTorch Lightning]], [[d2l-preface|D2L]]'s own `d2l.Trainer`) that encapsulates training loops, evaluation hooks, [[ModelCheckpoint]] saving, and distributed concerns like [[PyTorchDDP]]. Reduces boilerplate around the core gradient step.

## D2L's Trainer

[[d2l-linear-regression]] §3.2 introduces `d2l.Trainer` as the third leg of the [[Module]] / [[DataModule]] / [[Trainer]] OO scaffold (inspired by [[PyTorchLightning|Lightning]]). The key method `fit(model, data)` iterates `max_epochs` times, calling `model.training_step(batch)` over each minibatch followed by `optim.step()` / `optim.zero_grad()`, then `model.validation_step(batch)` over the val loader. The chapter's `fit_epoch` is framework-specific (PyTorch uses `loss.backward()`; TF uses `tf.GradientTape()`; JAX uses `jax.value_and_grad`).

## Connections

- [[d2l-linear-regression]] — §3.2 canonical reference for the D2L Trainer scaffold.
- [[Module]] / [[DataModule]] — sibling classes in the D2L OO scaffold.
- [[PyTorchLightning]] — the named inspiration for D2L's design.
- [[Backpropagation]] / [[StochasticGradientDescent]] — what each `fit_epoch` step executes.

## Hugging Face `transformers.Trainer` (per [[hands-on-llm-ch11-fine-tuning-representation-models|*Hands-On LLMs* Ch 11]])

Ch 11 is the wiki's **canonical worked example** of Hugging Face's `Trainer` class — the same `Module / DataModule / Trainer` separation as D2L, with hyperparameters declared via [[TrainingArguments|`TrainingArguments`]] and a model + collator + metrics passed in:

```python
from transformers import TrainingArguments, Trainer

training_args = TrainingArguments(
    "model",
    learning_rate=2e-5,
    per_device_train_batch_size=16,
    per_device_eval_batch_size=16,
    num_train_epochs=1,
    weight_decay=0.01,
    save_strategy="epoch",
    report_to="none"
)

trainer = Trainer(
    model=model, args=training_args,
    train_dataset=tokenized_train,
    eval_dataset=tokenized_test,
    tokenizer=tokenizer,
    data_collator=data_collator,
    compute_metrics=compute_metrics,
)
trainer.train()
trainer.evaluate()
```

Ch 11 uses `Trainer` for **four distinct regimes** on the same `bert-base-cased` backbone — sequence classification (regime 1), layer-frozen sequence classification (regime 2), masked-LM continued pretraining (regime 4), and token classification (NER, regime 5). The only differences across regimes are:

- The model class (`AutoModelForSequenceClassification` / `AutoModelForMaskedLM` / `AutoModelForTokenClassification`).
- The data collator ([[DataCollatorWithPadding]] / [[DataCollatorForLanguageModeling]] / [[DataCollatorForTokenClassification]]).
- The `compute_metrics` function (per-document F1 via `evaluate.load("f1")` vs span-level F1 via [[seqeval|`seqeval`]]).
- The number of epochs (1 for classification, 10 for MLM).

This *"same `Trainer` + swap the model class + swap the collator"* pattern is what makes Hugging Face's interface so powerful for fine-tuning encoders. SetFit (regime 3) has its own `SetFitTrainer` mirroring this interface (`setfit.Trainer` / `setfit.TrainingArguments`).

The chapter also defines **`compute_metrics`** as a callable taking `(logits, labels)` and returning a dict — the standard hook for any in-training evaluation. *"With `compute_metrics` we can define any number of metrics that we are interested in and that can be printed out or logged during training. This is especially helpful during training as it allows for detecting overfitting behavior."*
