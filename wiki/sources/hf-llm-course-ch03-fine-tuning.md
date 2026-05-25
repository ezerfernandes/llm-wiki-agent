---
title: "HuggingFace LLM Course — Ch 3: Fine-tuning a pretrained model"
type: source
tags: [hf-llm-course, course, fine-tuning, training, transformers]
date: 2026-05-23
source_file: raw/hf-llm-course/ch03-fine-tuning.md
---

## Summary
Chapter 3 of the [[HuggingFace]] LLM Course teaches end-to-end [[FineTuning]] of a pretrained transformer ([[bert]]-base-uncased) on the [[MRPC]] paraphrase task from the [[GLUE]] benchmark. It walks through dataset loading and preprocessing with the Datasets library, dynamic padding via [[DataCollatorWithPadding]], the high-level [[Trainer]] API with [[TrainingArguments]] and `compute_metrics`, then re-implements the same pipeline as a native [[PyTorch]] training loop with [[Adam]]/AdamW, a linear [[LearningRateScheduler]], and an evaluation loop using the Evaluate library. The chapter closes by showing how 🤗 Accelerate ports the loop to multi-GPU/TPU distributed training and how to read [[LearningCurves]] to diagnose [[Overfitting]], [[Underfitting]], and erratic training.

## Key Claims
- [[FineTuning]] adapts a pretrained model to a specific task by re-using pretrained weights and adding/replacing a task-specific head (e.g., `AutoModelForSequenceClassification` discards the pretraining head and randomly initializes a new classification head).
- The chapter is **PyTorch-only**, reflecting [[PyTorch]]'s dominance over TensorFlow/JAX in current Hugging Face workflows.
- [[MRPC]] (Microsoft Research Paraphrase Corpus, 5,801 sentence pairs) is one of 10 tasks in the [[GLUE]] benchmark; loaded via `load_dataset("glue", "mrpc")` returning a `DatasetDict` with train/validation/test splits (3,668 / 408 / 1,725).
- The [[bert]] tokenizer emits three tensors for sentence pairs: `input_ids`, `attention_mask`, and `token_type_ids` — the latter distinguishing `[CLS] s1 [SEP] s2 [SEP]` segments because BERT was pretrained with the [[nextsentenceprediction]] objective on top of [[maskedlanguagemodel]] (MLM).
- `Dataset.map(fn, batched=True)` is the canonical preprocessing primitive; backed by Apache Arrow on disk, it streams without loading the whole dataset into RAM.
- **Dynamic padding** — padding to the max length *within each batch* rather than the dataset max — is more efficient and is implemented by [[DataCollatorWithPadding]], passed as `collate_fn` to a PyTorch `DataLoader`. Caveat: TPUs prefer fixed shapes.
- The [[Trainer]] API requires only model, [[TrainingArguments]], train/eval datasets, a data collator, and a `processing_class` (newer parameter naming the tokenizer); calling `trainer.train()` runs a full epoch-based loop.
- Without `eval_strategy="epoch"` (or `"steps"`) and a `compute_metrics` function, `Trainer` reports only training loss; metrics like accuracy/F1 require the Evaluate library: `evaluate.load("glue", "mrpc")`.
- Reported result on MRPC validation: ~85.78% accuracy, F1 ~89.97 — close to the BERT paper's 88.9 F1 for the base model.
- The Trainer's default optimizer is **AdamW** (decoupled weight decay, Loshchilov & Hutter 2017), the default LR schedule is **linear decay** from 5e-5 to 0 over 3 epochs, computed as `num_epochs * len(train_dataloader)` (1,377 steps for MRPC).
- A from-scratch PyTorch loop requires: removing string columns, renaming `label`→`labels`, `set_format("torch")`, building `DataLoader`s, moving model+batch to `device`, calling `loss.backward()` then `optimizer.step()`, `lr_scheduler.step()`, `optimizer.zero_grad()` per step.
- Evaluation requires `model.eval()` + `torch.no_grad()`; metrics accumulate per batch via `metric.add_batch(...)` then a final `metric.compute()`.
- 🤗 [[Accelerate]] converts a single-device loop into a distributed one with three changes: instantiate `Accelerator()`, wrap objects in `accelerator.prepare(...)`, swap `loss.backward()` for `accelerator.backward(loss)`; launched via `accelerate config` + `accelerate launch train.py` or `notebook_launcher`.
- Advanced features exposed via `TrainingArguments`: [[MixedPrecisionTraining]] (`fp16=True`), [[GradientAccumulation]] (`gradient_accumulation_steps`), LR schedulers (`lr_scheduler_type="cosine"`), and `EarlyStoppingCallback`.
- **Learning curve diagnostics** ([[LearningCurves]]): accuracy curves appear "steppy" because predictions are discrete; loss is continuous. [[Overfitting]] shows divergent train/val loss; [[Underfitting]] shows both loss curves plateauing high; erratic curves indicate LR too high or batch too small, fixed by lower LR, larger batch, [[GradientClipping]].
- Production recommendations: hyperparameter tuning with Optuna/Ray Tune, parameter-efficient methods like LoRA/AdaLoRA, gradient checkpointing, quantization, and tracking with [[WeightsAndBiases]].

## Key Quotes
> "Padding all the samples to the maximum length is not efficient: it's better to pad the samples when we're building a batch, as then we only need to pad to the maximum length in that batch, and not the maximum length in the entire dataset." — rationale for dynamic padding

> "BERT is pretrained with token type IDs, and on top of the masked language modeling objective we talked about in Chapter 1, it has an additional objective called next sentence prediction." — why `token_type_ids` exist

> "The optimizer used by the Trainer is AdamW, which is the same as Adam, but with a twist for weight decay regularization." — default optimizer choice

> "🤗 Accelerate handles the device placement for you... the main bulk of the work is done in the line that sends the dataloaders, the model, and the optimizer to `accelerator.prepare()`." — Accelerate philosophy

> "The loss can improve if the model's output gets closer to the target, even if the final prediction is still incorrect. Accuracy, however, only improves when the prediction crosses the threshold to be correct." — why accuracy curves plateau while loss decreases

## Code & Patterns
- **Tokenize sentence pairs** with `tokenizer(s1, s2, truncation=True)` → `input_ids`, `attention_mask`, `token_type_ids`.
- **Dataset preprocessing pipeline**: `load_dataset` → `map(tokenize_fn, batched=True)` → `DataCollatorWithPadding(tokenizer=tokenizer)`.
- **Trainer setup**:
  ```py
  training_args = TrainingArguments("test-trainer", eval_strategy="epoch")
  model = AutoModelForSequenceClassification.from_pretrained(checkpoint, num_labels=2)
  trainer = Trainer(model, training_args, train_dataset=..., eval_dataset=...,
                    data_collator=data_collator, processing_class=tokenizer,
                    compute_metrics=compute_metrics)
  trainer.train()
  ```
- **compute_metrics pattern**: load metric via `evaluate.load("glue", "mrpc")`, argmax logits on last axis, call `metric.compute(predictions=..., references=...)`.
- **Native PyTorch loop**: `remove_columns([...])` → `rename_column("label","labels")` → `set_format("torch")` → `DataLoader(collate_fn=data_collator)` → AdamW(lr=5e-5) → `get_scheduler("linear", num_warmup_steps=0, num_training_steps=num_epochs*len(loader))` → forward/backward/step/zero_grad.
- **Evaluation loop**: `model.eval()`, wrap in `torch.no_grad()`, `metric.add_batch(...)`, final `metric.compute()`.
- **Accelerate diff**: `Accelerator()`, `accelerator.prepare(train_dl, eval_dl, model, optimizer)`, `accelerator.backward(loss)` — no manual `.to(device)`.
- **Advanced TrainingArguments**: `fp16=True`, `gradient_accumulation_steps=4`, `lr_scheduler_type="cosine"`, `load_best_model_at_end=True`, `metric_for_best_model="eval_loss"`.
- **Early stopping**: `callbacks=[EarlyStoppingCallback(early_stopping_patience=3)]`.
- **Experiment tracking**: `wandb.init(...)`, `TrainingArguments(report_to="wandb", logging_steps=10, eval_steps=50)`.

## Connections
- [[FineTuning]] — overarching workflow this chapter teaches.
- [[FineTuningBert]] — concrete worked example (BERT on MRPC).
- [[bert]] — the pretrained backbone used; explains `[CLS]/[SEP]` and `token_type_ids`.
- [[HuggingFace]] — ecosystem provider (Transformers, Datasets, Tokenizers, Accelerate, Evaluate).
- [[Trainer]] — high-level training API at the chapter's center.
- [[TrainingArguments]] — hyperparameter container for Trainer.
- [[DataCollatorWithPadding]] — implements dynamic padding.
- [[Padding]] — concept of fixed vs. dynamic padding strategies.
- [[Tokenizer]] / [[Tokenization]] — preprocessing primitive consumed by the model.
- [[MRPC]] — the example dataset.
- [[GLUE]] — the benchmark MRPC belongs to.
- [[maskedlanguagemodel]] / [[nextsentenceprediction]] — BERT pretraining objectives explaining tokenizer output.
- [[Adam]] / AdamW — default optimizer; weight-decay variant.
- [[LearningRate]] / [[LearningRateScheduler]] / [[CosineLRSchedule]] — scheduling defaults and alternatives.
- [[MixedPrecisionTraining]] / [[AutomaticMixedPrecision]] — `fp16=True` shortcut.
- [[GradientAccumulation]] / [[GradientClipping]] / [[GradientCheckpointing]] — memory/stability optimizations referenced.
- [[BatchSize]] / [[NumberOfEpochs]] — knobs adjusted in the curve-diagnosis examples.
- [[LearningCurves]] / [[Overfitting]] / [[Underfitting]] / [[EarlyStopping]] — diagnostics section.
- [[DistributedTraining]] / [[PyTorch]] / [[GoogleColab]] — runtime context.
- [[WeightsAndBiases]] — experiment tracker used in the W&B example.
- [[Evaluation]] / [[ModelEvaluation]] — accuracy / F1 metric computation via the Evaluate library.

## Contradictions
- None observed. Chapter is internally consistent and complements earlier course chapters (Ch 1: pretraining objectives; Ch 2: tokenizers/models).
