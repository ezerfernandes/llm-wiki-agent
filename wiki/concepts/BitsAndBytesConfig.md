---
title: "BitsAndBytesConfig"
type: concept
tags: [quantization, qlora, hugging-face, bitsandbytes, hands-on-llm]
sources: [hands-on-llm-ch12-fine-tuning-generation-models]
last_updated: 2026-05-23
---

# BitsAndBytesConfig

**`transformers.BitsAndBytesConfig`** is the Hugging Face Transformers config object that **declares the [[bitsandbytes]] quantization scheme** at model-load time. Passed via `quantization_config=` to `AutoModelForCausalLM.from_pretrained(...)` to load a model directly in 4-bit or 8-bit precision.

## In Hands-On LLMs Ch 12

[[hands-on-llm-ch12-fine-tuning-generation-models|Ch 12]] uses `BitsAndBytesConfig` to set up the **Q in QLoRA**:

```python
from transformers import BitsAndBytesConfig

bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,                 # 4-bit precision model loading
    bnb_4bit_quant_type="nf4",         # NormalFloat-4 quantization
    bnb_4bit_compute_dtype="float16",  # compute precision (forward/backward)
    bnb_4bit_use_double_quant=True,    # nested quantization on per-block scales
)

model = AutoModelForCausalLM.from_pretrained(
    model_name,
    device_map="auto",
    quantization_config=bnb_config,
)
```

### The four flags

| Flag | Ch 12 value | What it does |
|---|---|---|
| `load_in_4bit` | `True` | 4-bit base-model weights (alternative: `load_in_8bit`). |
| `bnb_4bit_quant_type` | `"nf4"` | Use [[NormalFloat4|NF4]] distribution-aware quantization (alternative: `"fp4"`). |
| `bnb_4bit_compute_dtype` | `"float16"` | Dequantize back to FP16 for the forward/backward computation. |
| `bnb_4bit_use_double_quant` | `True` | Enable [[DoubleQuantization|double quantization]] of the per-block scale factors. |

This single config object encodes **three of the four** QLoRA innovations (NF4 + double quant + dequant-to-FP16); the fourth ([[PagedOptimizer|paged optimizers]]) is set on the trainer via the `optim` argument.

### The parameterization-to-toggle-regimes property

Ch 12 emphasizes that **removing `quantization_config=bnb_config`** from the `AutoModelForCausalLM.from_pretrained` call flips the recipe from QLoRA (4-bit base + LoRA adapter) to ordinary full-precision LoRA. Combined with dropping the [[LoraConfig]], the same code path becomes full fine-tuning.

## VRAM impact (Ch 12)

> *"Loading the model now only uses ~1 GB VRAM compared to the ~4 GB of VRAM it would need without quantization."* — Ch 12 on loading [[TinyLlama|TinyLlama-1.1B]]

This is the ~4× memory reduction that lets a billion-parameter model fit alongside its gradients on a free Google Colab T4.

## Connections

- [[bitsandbytes]] — the library this config delegates to.
- [[QLoRA]] — the technique that combines this with `LoraConfig`.
- [[NormalFloat4|NF4]] / [[DoubleQuantization]] / [[PagedOptimizer]] — the QLoRA innovations stack.
- [[HuggingFace|Hugging Face]] / [[transformers]] — the library that exposes this config.
- [[LoraConfig]] — the PEFT config that pairs with this.
- [[hands-on-llm-ch12-fine-tuning-generation-models]] — primary source.
