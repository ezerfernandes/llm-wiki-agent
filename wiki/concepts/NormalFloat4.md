---
title: "NormalFloat-4 (NF4)"
type: concept
tags: [numerics, quantization, qlora, finetuning]
sources: [ai-engineering-ch07-finetuning, hands-on-llm-ch12-fine-tuning-generation-models]
last_updated: 2026-05-24
---

# NormalFloat-4 (NF4)

A 4-bit numerical format introduced as part of **[[QLoRA]]** ([[TimDettmers|Dettmers]] et al., NeurIPS 2023), designed around the empirical insight that **pre-trained model weights approximately follow a normal distribution with mean zero**. Per [[ai-engineering-ch07-finetuning|*AI Engineering* Ch 7]]:

> "The 4-bit format that QLoRA uses is NF4 (NormalFloat-4), which quantizes values based on the insight that pre-trained weights usually follow a normal distribution with a median of zero."

## How NF4 differs from [[INT4]] / [[FP4]]

- **[[INT4]]**: 16 evenly-spaced integer levels. Step size uniform across the range.
- **[[FP4]]**: 16 floating-point levels with exponential spacing.
- **NF4**: 16 levels distributed by the **quantiles of N(0, σ²)** — dense bins near zero, sparse bins in the tails.

The result: NF4 minimizes quantization error for values drawn from a normal distribution — which is empirically what pre-trained LLM weights look like.

## Why this matters for [[QLoRA]]

[[QLoRA]] stores the base model's weights in NF4 (4× smaller than FP16) but **dequantizes back to BF16** during the forward and backward passes. The dequantization cost is the price you pay; the memory win is what lets you finetune a 65B model on a single 48 GB GPU.

NF4 is paired with:
- **Double quantization** — quantize even the per-block scale factors to save additional memory.
- **Paged optimizers** — swap optimizer states to CPU memory when GPU runs out.

## Limitations

> "The main limitation of QLoRA is that NF4 quantization is expensive. While QLoRA can reduce the memory footprint, it might increase training time due to the extra time required by quantization and dequantization steps." — Ch 7

So NF4 is a **memory-vs-time** trade. For practitioners on consumer-grade hardware, the memory wins; for practitioners with abundant memory, plain FP16 or BF16 LoRA is faster.

## Connections

- [[QLoRA]] — the technique NF4 was designed for.
- [[lora|LoRA]] — the underlying PEFT method.
- [[INT4]] / [[FP4]] — the uniform/exponential 4-bit alternatives.
- [[Quantization]] — parent family.
- [[NumericalRepresentation]] — umbrella concept.
- [[Bitsandbytes]] — implementation library.
- [[TimDettmers]] — first author.
- [[ai-engineering-ch07-finetuning]] — primary source.

## From [[hands-on-llm-ch12-fine-tuning-generation-models|Hands-On LLMs Ch 12]]

Ch 12 walks NF4 as the **second of three QLoRA innovations** ([[BlockwiseQuantization|blockwise quantization]] → NF4 → [[DoubleQuantization|double-quant]] + [[PagedOptimizer|paged optimizers]]). The chapter's pedagogical anchor is the **normality of pretrained weights**:

> *"It has been observed that pretrained values follow a centered normal distribution between –1 and 1. ... We can quantize the weights according to this normal distribution by establishing the bins by the normal distribution."* — Ch 12

NF4 places **more bins near zero and fewer in the tails** — preventing close-value collisions and reducing outlier impact. The result: *"we can go from a 16-bit float representation to a measly 4-bit normalized float representation."*

### Worked Ch 12 config

```python
bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype="float16",
    bnb_4bit_use_double_quant=True,
)
```

Loading [[TinyLlama|TinyLlama-1.1B]] under this config uses **~1 GB VRAM** (vs ~4 GB FP16) — the operational payoff that makes a free Google Colab T4 sufficient for the chapter's worked recipe.

### Inference dividend

> *"Note that the quantization of LLMs in general is also helpful for inference as quantized LLMs are smaller in size and therefore require less VRAM."* — Ch 12

NF4 is not just a training-memory hack; the resulting 4-bit base remains usable at inference time, decoupling fine-tuning memory cost from inference memory cost.
