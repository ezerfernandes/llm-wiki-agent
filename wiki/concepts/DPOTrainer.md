---
title: "DPOTrainer"
type: concept
tags: [fine-tuning, preference-alignment, dpo, trl, hugging-face, training-loop, hands-on-llm]
sources: [hands-on-llm-ch12-fine-tuning-generation-models]
last_updated: 2026-05-23
---

# DPOTrainer

**`trl.DPOTrainer`** is [[HuggingFace|Hugging Face]] [[TRL]]'s **Direct Preference Optimization trainer**. Subclasses `transformers.Trainer` to implement the [[DPO]] objective directly: takes a `(prompt, chosen, rejected)` dataset, an explicit `beta` temperature, and (optionally) a frozen reference model — and optimizes the trainable model to assign higher relative log-probability to the chosen completion vs the rejected one *without* needing a separately trained reward model or a PPO loop.

## In Hands-On LLMs Ch 12

[[hands-on-llm-ch12-fine-tuning-generation-models|Ch 12]] uses `DPOTrainer` as Stage 2 of its two-stage pipeline, applied on top of the previously-trained QLoRA SFT adapter:

```python
from trl import DPOTrainer

dpo_trainer = DPOTrainer(
    model,
    args=training_arguments,           # DPOConfig
    train_dataset=dpo_dataset,         # prompt + chosen + rejected
    tokenizer=tokenizer,
    peft_config=peft_config,           # LoraConfig (same r=64, alpha=32 as SFT)
    beta=0.1,
    max_prompt_length=512,
    max_length=512,
)

dpo_trainer.train()
dpo_trainer.model.save_pretrained("TinyLlama-1.1B-dpo-qlora")
```

**Key hyperparameters in the worked recipe**:
- `beta=0.1` — DPO temperature. Lower β = stay closer to the reference model; higher β = more aggressive shift toward chosen-over-rejected.
- `max_prompt_length=512`, `max_length=512` — separate caps for the prompt vs the (prompt + completion) total.
- `learning_rate=1e-5` (in the [[DPOConfig]]) — **10× lower than the SFT 2e-4** — DPO operates on log-probability *shifts* between reference and trainable models, so smaller updates are necessary to avoid destabilizing the reference behavior.
- `warmup_ratio=0.1` — *"By maintaining a small learning rate at the start (i.e., warmup period), we allow the model to adjust to the data before applying larger learning rates, therefore avoiding harmful divergence."*
- `max_steps=200` instead of `num_train_epochs=1` for the chapter's illustrative run (vs the full-epoch SFT run).

The chapter notes the SFT-then-DPO **iterative adapter merge**: after DPO training, merge the SFT adapter into the base, then merge the DPO adapter into the SFT-merged model — two adapters stacked sequentially.

## How DPO removes the reward model

The reference model that `DPOTrainer` needs is **not a reward model** — it's a frozen copy of the LLM (typically the SFT checkpoint itself). The trainer computes log-probabilities of the chosen and rejected completions under both the reference and the trainable models, and the loss optimizes the relative log-probability gap. This collapses *"train reward model → run PPO with reward model + KL penalty"* into *"compute log-prob shifts, run gradient descent on a binary-cross-entropy-style loss"*.

## Connections

- [[trl|TRL]] — the parent library.
- [[DPO]] — the algorithm.
- [[DPOConfig]] — the hyperparameter container.
- [[SFTTrainer]] — the SFT counterpart in TRL.
- [[PPO]] / [[rlhf]] — the earlier algorithm class DPO sidesteps.
- [[lora|LoRA]] / [[QLoRA]] / [[PEFT]] — DPOTrainer integrates with these as readily as SFTTrainer does.
- [[ChatTemplate]] / [[DistilabelIntelOrcaDPOPairs]] — the data format and dataset used in Ch 12.
- [[hands-on-llm-ch12-fine-tuning-generation-models]] — primary source.
- [[leh-ch06-preference-alignment]] — DPOTrainer at 8B scale for the LLM Twin pipeline.
