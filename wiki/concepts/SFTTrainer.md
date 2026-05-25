---
title: "SFTTrainer"
type: concept
tags: [fine-tuning, sft, trl, hugging-face, training-loop, hands-on-llm]
sources: [hands-on-llm-ch12-fine-tuning-generation-models]
last_updated: 2026-05-23
---

# SFTTrainer

**`trl.SFTTrainer`** is [[HuggingFace|Hugging Face]] [[TRL|TRL]]'s **supervised-fine-tuning trainer class** for generative LLMs. Subclasses `transformers.Trainer` with conveniences specific to instruction / chat-style next-token-prediction training: a `dataset_text_field` to point at the formatted prompt column, a `max_seq_length` cap, optional `peft_config` for [[lora|LoRA]] / [[QLoRA]] adapter training, and sensible defaults for `packing`, tokenizer padding, and chat-template handling.

## In Hands-On LLMs Ch 12

[[hands-on-llm-ch12-fine-tuning-generation-models|Ch 12]] uses `SFTTrainer` as the **canonical SFT entry point** for fine-tuning [[TinyLlama|TinyLlama-1.1B]] on a 3,000-example subset of [[UltraChat]] under [[QLoRA]]:

```python
from trl import SFTTrainer

trainer = SFTTrainer(
    model=model,                       # PEFT-wrapped, 4-bit quantized model
    train_dataset=dataset,             # ChatTemplate-formatted "text" column
    dataset_text_field="text",
    tokenizer=tokenizer,
    args=training_arguments,           # TrainingArguments
    max_seq_length=512,
    peft_config=peft_config,           # LoraConfig — omit for full FT
)

trainer.train()
trainer.model.save_pretrained("TinyLlama-1.1B-qlora")
```

The chapter notes the **parameterization-to-toggle-regimes** property: removing both `quantization_config` (on model loading) and `peft_config` (here) flips the same training script from *"Instruction tuning with QLoRA"* to *"full instruction tuning."*

The chapter's hyperparameters (full table in [[hands-on-llm-ch12-fine-tuning-generation-models|the source page]]):
- `per_device_train_batch_size=2`, `gradient_accumulation_steps=4`
- `optim="paged_adamw_32bit"` (the [[PagedOptimizer]] from QLoRA)
- `learning_rate=2e-4`, `lr_scheduler_type="cosine"`
- `num_train_epochs=1` — *"Higher values tend to degrade performance so we generally like to keep this low."*
- `fp16=True`, `gradient_checkpointing=True`

Single-epoch training takes ≈ 1 hour on a Colab Tesla T4.

## Why it's not just `Trainer`

`SFTTrainer` wraps `transformers.Trainer` with:
- **Automatic chat-template tokenization** when `dataset_text_field` is given.
- **Optional PEFT integration** — pass a `LoraConfig` directly; it handles `prepare_model_for_kbit_training` and `get_peft_model` under the hood when needed.
- **Sequence packing** support (multiple short sequences concatenated up to `max_seq_length` for efficiency).
- **Token loss masking** conveniences for instruction-only loss (don't compute loss on the user prompt).

## Connections

- [[trl|TRL]] — the parent library.
- [[Trainer]] — the underlying `transformers.Trainer` class.
- [[QLoRA]] / [[lora|LoRA]] / [[PEFT]] — the adapter techniques `SFTTrainer` integrates with.
- [[SupervisedFinetuning]] — the regime it implements.
- [[DPOTrainer]] — the preference-tuning sibling trainer in TRL.
- [[ChatTemplate]] — the formatting that feeds `dataset_text_field`.
- [[TrainingArguments]] — the hyperparameter container `args=` consumes.
- [[hands-on-llm-ch12-fine-tuning-generation-models]] — primary source.
- [[leh-ch05-supervised-fine-tuning]] — `SFTTrainer` at 8B scale for the LLM Twin pipeline.
