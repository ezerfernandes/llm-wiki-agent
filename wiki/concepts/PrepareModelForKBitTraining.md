---
title: "prepare_model_for_kbit_training"
type: concept
tags: [peft, quantization, qlora, hugging-face, hands-on-llm]
sources: [hands-on-llm-ch12-fine-tuning-generation-models]
last_updated: 2026-05-23
---

# `prepare_model_for_kbit_training`

**`peft.prepare_model_for_kbit_training`** is the standard PEFT helper that **prepares a k-bit-quantized model** (4-bit or 8-bit) for training. Cast certain layers (e.g., layer-norms) to FP32 for stability, enable gradient checkpointing if requested, and disable caching so that the forward pass remains compatible with backprop.

## In Hands-On LLMs Ch 12

[[hands-on-llm-ch12-fine-tuning-generation-models|Ch 12]] calls it **immediately after loading the 4-bit model and before wrapping with `get_peft_model`**:

```python
from peft import LoraConfig, prepare_model_for_kbit_training, get_peft_model

# Prepare model for training (k-bit = 4-bit NF4)
model = prepare_model_for_kbit_training(model)
model = get_peft_model(model, peft_config)
```

The pattern is the same for the DPO stage. Without this call, training a 4-bit-quantized base with [[QLoRA]] would either fail outright or produce unstable gradients.

## What it does (in practice)

- **Casts layer norms and the LM head to FP32** to keep numerical stability through the loss.
- **Disables KV-cache** (sets `model.config.use_cache = False`) — needed because cached attention states break gradient computation.
- **Enables `requires_grad=True` on the input embeddings** so the LoRA gradient flows properly.

## Connections

- [[peft|PEFT]] — the library.
- [[QLoRA]] / [[lora|LoRA]] — the technique stack this prepares for.
- [[LoraConfig]] — the next call after this in the pipeline.
- [[BitsAndBytesConfig]] — the quantization this assumes was already applied at model-load time.
- [[GradientCheckpointing]] — the memory-saving trick this can enable.
- [[hands-on-llm-ch12-fine-tuning-generation-models]] — primary source.
