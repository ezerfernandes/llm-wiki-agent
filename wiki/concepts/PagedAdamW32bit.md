---
title: "paged_adamw_32bit"
type: concept
tags: [optimizer, quantization, qlora, memory-optimization, hands-on-llm]
sources: [hands-on-llm-ch12-fine-tuning-generation-models]
last_updated: 2026-05-23
---

# `paged_adamw_32bit`

The **paged AdamW optimizer** shipped by [[bitsandbytes]] — keeps Adam's first- and second-moment optimizer states in FP32 (32-bit) and **pages them between CPU and GPU memory on demand** to avoid OOM spikes during long-sequence training. The 32-bit precision keeps the optimizer numerically stable (vs aggressive 8-bit Adam variants), while paging unlocks the memory headroom needed for 4-bit-quantized base models.

## In Hands-On LLMs Ch 12

The Ch 12 worked QLoRA recipe sets `optim="paged_adamw_32bit"` for **both the SFT and DPO** training runs:

```python
training_arguments = TrainingArguments(
    ...
    optim="paged_adamw_32bit",
    ...
)
```

This is the [[PagedOptimizer|paged-optimizer]] variant used in the original QLoRA paper.

## Why "32bit"

`bitsandbytes` also ships **8-bit** Adam variants (`adamw_8bit`) for additional memory savings — see [[leh-ch05-supervised-fine-tuning|LEH Ch 5]] for the 8-bit-AdamW use case. The 32-bit version trades that ~3× memory win on optimizer states for numerical stability that helps the QLoRA training stay on-rails despite the 4-bit base.

## Connections

- [[PagedOptimizer]] — the parent concept.
- [[Adam]] — the underlying optimizer.
- [[bitsandbytes]] — the library that ships the implementation.
- [[QLoRA]] — the technique stack it pairs with.
- [[TrainingArguments]] / [[DPOConfig]] — where the `optim=` string is set.
- [[hands-on-llm-ch12-fine-tuning-generation-models]] — primary source.
