---
title: "Double Quantization"
type: concept
tags: [quantization, qlora, memory-optimization, hands-on-llm]
sources: [hands-on-llm-ch12-fine-tuning-generation-models, ai-engineering-ch07-finetuning]
last_updated: 2026-05-23
---

# Double Quantization

**Double quantization** is one of the three innovations in the **[[QLoRA]]** paper ([[TimDettmers|Dettmers]] et al. 2023, arXiv:2305.14314), alongside [[NormalFloat4|NF4]] and [[PagedOptimizer|paged optimizers]]. The idea: **quantize even the per-block scale factors / quantization constants** that [[BlockwiseQuantization|blockwise quantization]] needs — recovering a small but meaningful additional slice of memory.

## In Hands-On LLMs Ch 12

[[hands-on-llm-ch12-fine-tuning-generation-models|Ch 12]] turns on double quantization via the `bnb_4bit_use_double_quant=True` flag on `BitsAndBytesConfig`:

```python
bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype="float16",
    bnb_4bit_use_double_quant=True,  # nested quantization
)
```

The chapter calls this *"nested quantization"* in the inline comment and refers readers to the QLoRA paper for the mathematical details.

## Why it helps

[[BlockwiseQuantization|Blockwise quantization]] requires storing a per-block quantization constant (typically a few floats per 64-element block). For a multi-billion-parameter model, those constants add up — sometimes hundreds of megabytes of FP32. Quantizing the constants themselves trims that back further.

## Connections

- [[QLoRA]] — the parent technique.
- [[NormalFloat4|NF4]] / [[PagedOptimizer]] — the two other QLoRA innovations.
- [[BlockwiseQuantization]] — what double quantization is layered on top of.
- [[BitsAndBytesConfig]] — where the flag is set.
- [[bitsandbytes]] — the library that implements it.
- [[hands-on-llm-ch12-fine-tuning-generation-models]] — primary source.
