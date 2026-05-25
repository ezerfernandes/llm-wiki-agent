---
title: "bitsandbytes"
type: entity
tags: [tool, library, quantization, open-source]
sources: [leh-ch05-supervised-fine-tuning, leh-ch08-inference-optimization, leh-ch10-inference-pipeline-deployment, hands-on-llm-ch12-fine-tuning-generation-models]
last_updated: 2026-05-24
---

## What it is
`bitsandbytes` is an open-source CUDA library by Tim Dettmers and collaborators that implements 8-bit and 4-bit quantization (LLM.int8, NF4, double quantization, paged optimizers) for PyTorch models, integrated via `load_in_8bit=True` / `load_in_4bit=True` flags in `transformers`.

## In LLM Engineer's Handbook
Ch. 5 ([[leh-ch05-supervised-fine-tuning]]) uses bitsandbytes under [[QLoRA]] (NF4 + double quantization + paged optimizers) and for the `adamw_8bit` optimizer the SFTTrainer is configured with. Ch. 8 ([[leh-ch08-inference-optimization]]) is the canonical reference: bitsandbytes powers `load_in_8bit=True` (LLM.int8) and `load_in_4bit=True` (NF4), with code examples on `meta-llama/Meta-Llama-3-8B-Instruct`. Ch. 10 ([[leh-ch10-inference-pipeline-deployment]]) deploys the LLM Twin's TGI endpoint with `HF_MODEL_QUANTIZE=bitsandbytes`, applying runtime quantization to keep an 8B model on a single `ml.g5.xlarge` GPU.

## Connections
- [[HuggingFace]] — `transformers` integrates bitsandbytes via `load_in_*` flags.
- [[QLoRA]] / [[lora]] — fine-tuning techniques using bitsandbytes quantization.
- [[TextGenerationInference]] — TGI calls bitsandbytes for runtime quantization.
- [[NVIDIA]] — CUDA hardware bitsandbytes targets.
- [[Adam]] — `adamw_8bit` is a bitsandbytes optimizer.

## From [[hands-on-llm-ch12-fine-tuning-generation-models|Hands-On LLMs Ch 12]]

Ch 12 of *Hands-On LLMs* uses `bitsandbytes` as the **quantization library** of the chapter's four-package fine-tuning stack ([[transformers]] + [[peft|PEFT]] + `bitsandbytes` + [[trl|TRL]]). The chapter's [[BitsAndBytesConfig|`BitsAndBytesConfig`]]:

```python
bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype="float16",
    bnb_4bit_use_double_quant=True,
)
```

Loading [[TinyLlama|TinyLlama-1.1B]] under this config uses **~1 GB VRAM** (vs ~4 GB FP16) — the operational payoff that makes a free Google Colab Tesla T4 sufficient for the worked recipe. Ch 12 also uses `bitsandbytes`'s **`paged_adamw_32bit`** optimizer (the [[PagedOptimizer|paged-optimizer]] innovation from the QLoRA paper) via `optim="paged_adamw_32bit"` in `TrainingArguments`.

Ch 12 is the wiki's first runnable demonstration of all three QLoRA innovations together in a single recipe: [[BlockwiseQuantization|blockwise quantization]] + [[NormalFloat4|NF4]] + [[DoubleQuantization|double quantization]] + [[PagedOptimizer|paged optimizers]] — all delivered by `bitsandbytes`.
