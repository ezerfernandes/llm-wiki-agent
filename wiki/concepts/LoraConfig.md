---
title: "LoraConfig"
type: concept
tags: [lora, peft, hyperparameters, hugging-face, hands-on-llm]
sources: [hands-on-llm-ch12-fine-tuning-generation-models]
last_updated: 2026-05-23
---

# LoraConfig

**`peft.LoraConfig`** — the Hugging Face [[peft|PEFT]] library's hyperparameter container for a [[lora|LoRA]] adapter. Bundles the rank `r`, the scaling `lora_alpha`, dropout, the target-module list, the task type, and bias handling into a single object that gets passed to `get_peft_model(model, lora_config)` or directly to [[SFTTrainer]] / [[DPOTrainer]].

## In Hands-On LLMs Ch 12

[[hands-on-llm-ch12-fine-tuning-generation-models|Ch 12]] uses the **same `LoraConfig`** for both the SFT stage and the DPO stage:

```python
from peft import LoraConfig

peft_config = LoraConfig(
    lora_alpha=32,           # LoRA scaling
    lora_dropout=0.1,        # dropout on LoRA layers
    r=64,                    # rank
    bias="none",
    task_type="CAUSAL_LM",
    target_modules=[
        "k_proj", "gate_proj", "v_proj", "up_proj",
        "q_proj", "o_proj", "down_proj",
    ],
)
```

### The fields the chapter calls out

- **`r=64`** — *"the rank of the compressed matrices ... Values typically range between 4 and 64."* Higher rank = less compression, more representative power, more memory.
- **`lora_alpha=32`** — *"Controls the amount of change that is added to the original weights. In essence, it balances the knowledge of the original model with that of the new task."* The chapter's stated rule of thumb: *"choose a value twice the size of r"* — but the worked recipe uses `alpha=32 / r=64 = 0.5×`, **inconsistent with the inline rule**. (See [[hands-on-llm-ch12-fine-tuning-generation-models|the source page]]'s soft-consistency notes.)
- **`target_modules`** — the seven LLaMA-family projection layers (`q_proj`, `k_proj`, `v_proj`, `o_proj`, `up_proj`, `down_proj`, `gate_proj`). Together these cover all of attention's QKVO matrices *and* the FFN's gate-up-down trio (LLaMA's SwiGLU MLP block).
- **`bias="none"`** — biases are frozen; only the low-rank A·B factors train.
- **`task_type="CAUSAL_LM"`** — flags the model as causal language modeling so PEFT plumbs the right output head.

## The chapter's parameterization-to-toggle-regimes property

Ch 12 emphasizes that this `LoraConfig` is the **toggle that turns the recipe from QLoRA into full fine-tuning** — drop the `peft_config` (and the `BitsAndBytesConfig` quantization on the model loader) and the same training script runs full FT.

## Connections

- [[lora|LoRA]] — the technique this configures.
- [[peft|PEFT]] — the library.
- [[QLoRA]] — the technique stack that pairs `LoraConfig` with `BitsAndBytesConfig`.
- [[SFTTrainer]] / [[DPOTrainer]] — the trainers that consume it.
- [[PrepareModelForKBitTraining]] — the function called before `get_peft_model` to make a 4-bit-quantized model trainable.
- [[hands-on-llm-ch12-fine-tuning-generation-models]] — primary source.
