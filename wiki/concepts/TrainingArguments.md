---
title: "TrainingArguments"
type: concept
tags: [training, huggingface, hyperparameters, fine-tuning]
sources: [hands-on-llm-ch11-fine-tuning-representation-models, hands-on-llm-ch12-fine-tuning-generation-models]
last_updated: 2026-05-24
---

# TrainingArguments

`transformers.TrainingArguments` is the Hugging Face dataclass that **declares hyperparameters for a `Trainer` run** — learning rate, batch size, number of epochs, weight decay, save strategy, logging, etc. Pairs with [[Trainer|`Trainer`]] as the standard fine-tuning interface.

Per [[hands-on-llm-ch11-fine-tuning-representation-models|*Hands-On LLMs* Ch 11]]:

> *"The `TrainingArguments` class defines hyperparameters we want to tune, such as the learning rate and how many epochs (rounds) we want to train. The `Trainer` is used to execute the training process."*

## Ch 11 canonical config (sequence classification)

```python
from transformers import TrainingArguments

training_args = TrainingArguments(
    "model",                          # output directory
    learning_rate=2e-5,
    per_device_train_batch_size=16,
    per_device_eval_batch_size=16,
    num_train_epochs=1,
    weight_decay=0.01,
    save_strategy="epoch",
    report_to="none"
)
```

| Argument | Ch 11 value | Purpose |
|---|---|---|
| `learning_rate` | `2e-5` | Standard BERT fine-tuning LR |
| `per_device_train_batch_size` | `16` | Fits on Colab T4 with `bert-base-cased` |
| `per_device_eval_batch_size` | `16` | Same for eval |
| `num_train_epochs` | `1` (classification) / `10` (MLM) | More epochs for MLM since only 15% of positions contribute gradient per batch |
| `weight_decay` | `0.01` | Standard regularization |
| `save_strategy` | `"epoch"` | Checkpoint after each epoch |
| `report_to` | `"none"` | Disable W&B / TensorBoard logging |

## Other useful fields

- `evaluation_strategy` — `"epoch"` or `"steps"`; triggers `compute_metrics` calls.
- `logging_dir`, `logging_steps` — for stdout / TB logging.
- `warmup_steps` / `warmup_ratio` — for linear LR [[Warmup|warmup]].
- `gradient_accumulation_steps` — virtual-batch-size trick when memory-constrained.
- `fp16` / `bf16` — automatic mixed-precision training.

## Connections

- [[hands-on-llm-ch11-fine-tuning-representation-models]] — primary source.
- [[Trainer]] — consumes the `TrainingArguments` and executes the loop.
- [[FineTuning]] / [[FineTuningBert]] — the broader context.
- [[Warmup]] — controllable via `warmup_steps` / `warmup_ratio`.
- [[LearningRate]] / [[BatchSize]] / [[NumberOfEpochs]] — the main knobs.
- [[HuggingFace]] — distributes `transformers`.

## From [[hands-on-llm-ch12-fine-tuning-generation-models|Hands-On LLMs Ch 12]]

Ch 12 of *Hands-On LLMs* uses `TrainingArguments` as the **config substrate for both stages** of its two-stage post-training pipeline ([[QLoRA]]-SFT and [[QLoRA]]-DPO). The chapter's QLoRA-tuned hyperparameter set introduces several Ch-12-specific knobs:

### Ch 12 SFT config

```python
training_arguments = TrainingArguments(
    output_dir="./results",
    per_device_train_batch_size=2,
    gradient_accumulation_steps=4,
    optim="paged_adamw_32bit",
    learning_rate=2e-4,
    lr_scheduler_type="cosine",
    num_train_epochs=1,
    logging_steps=10,
    fp16=True,
    gradient_checkpointing=True,
)
```

| Argument | Ch 12 value | Purpose |
|---|---|---|
| `per_device_train_batch_size` | `2` | Small per-device batch for VRAM-constrained Colab T4 |
| `gradient_accumulation_steps` | `4` | [[GradientAccumulation]] for effective batch size 8 |
| `optim` | `"paged_adamw_32bit"` | [[PagedAdamW32bit]] — QLoRA's [[PagedOptimizer|paged optimizer]] |
| `learning_rate` | `2e-4` (SFT) / `1e-5` (DPO) | Higher for SFT, 10× lower for DPO stability |
| `lr_scheduler_type` | `"cosine"` | [[CosineLRSchedule]] decay |
| `num_train_epochs` | `1` | *"Higher values tend to degrade performance"* — Ch 12 |
| `fp16` | `True` | Mixed-precision training |
| `gradient_checkpointing` | `True` | [[GradientCheckpointing]] — recompute activations to save memory |

### Ch 12 DPO config additions

The DPO stage swaps to `trl.DPOConfig` (a `TrainingArguments` subclass) and adds:

- `max_steps=200` (illustration) instead of `num_train_epochs`.
- `warmup_ratio=0.1` — [[Warmup]] ramp.
- DPO-specific `beta=0.1`, `max_prompt_length=512`, `max_length=512` parameters.

### The structural point

Ch 12's `TrainingArguments` config is parameterized to **toggle between QLoRA and full FT** — *"By removing those, we would go from 'Instruction tuning with QLoRA' to 'full instruction tuning.'"* — making `TrainingArguments` the **stable interface** across regime changes.
