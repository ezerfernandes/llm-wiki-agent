---
title: "DPOConfig"
type: concept
tags: [fine-tuning, preference-alignment, dpo, trl, hyperparameters, hands-on-llm]
sources: [hands-on-llm-ch12-fine-tuning-generation-models]
last_updated: 2026-05-23
---

# DPOConfig

**`trl.DPOConfig`** is [[TRL]]'s hyperparameter container for [[DPOTrainer]], analogous to [[TrainingArguments]] for `transformers.Trainer` and `SFTTrainer`. Bundles standard training arguments (batch size, optimizer, learning rate, scheduler, mixed precision, gradient checkpointing) along with DPO-specific knobs surfaced through the trainer itself (`beta`, `max_prompt_length`, `max_length`).

## In Hands-On LLMs Ch 12

The Ch 12 DPO recipe uses these settings:

```python
from trl import DPOConfig

training_arguments = DPOConfig(
    output_dir=output_dir,
    per_device_train_batch_size=2,
    gradient_accumulation_steps=4,
    optim="paged_adamw_32bit",
    learning_rate=1e-5,
    lr_scheduler_type="cosine",
    max_steps=200,
    logging_steps=10,
    fp16=True,
    gradient_checkpointing=True,
    warmup_ratio=0.1,
)
```

Key differences from the chapter's SFT `TrainingArguments`:

| Field | SFT recipe | DPO recipe |
|---|---|---|
| `learning_rate` | `2e-4` | `1e-5` (10× smaller) |
| Step budget | `num_train_epochs=1` (full epoch) | `max_steps=200` (illustration) |
| `warmup_ratio` | not set | `0.1` (10% of steps as linear warmup) |

The lower learning rate matters: DPO operates on the *shift* in log-probabilities between the reference and trainable models, and that shift is fragile — too-large updates destabilize the reference behavior the model was carefully built up to.

## Connections

- [[DPOTrainer]] — the trainer this configures.
- [[TrainingArguments]] — the `transformers.Trainer` analogue.
- [[trl|TRL]] — the library.
- [[Warmup]] — the warmup ramp the `warmup_ratio` invokes.
- [[CosineLRSchedule]] — the LR scheduler used.
- [[PagedAdamW32bit]] — the optimizer paired with QLoRA.
- [[hands-on-llm-ch12-fine-tuning-generation-models]] — primary source.
