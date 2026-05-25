---
title: "IA3 — Infused Adapter by Inhibiting and Amplifying Inner Activations"
type: concept
tags: [peft, adapter, multi-task]
sources: [ai-engineering-ch07-finetuning]
last_updated: 2024-12-04
---

# IA3 — Infused Adapter by Inhibiting and Amplifying Inner Activations

A [[PEFT]] method from **Liu et al. (2022)** — *"Few-Shot Parameter-Efficient Fine-Tuning is Better and Cheaper than In-Context Learning"* (the "T-Few" paper). IA3 **rescales activations** at three points in each transformer block (key, value, and feedforward intermediate) using learned per-element vectors. The vectors are extremely small — far smaller than [[lora|LoRA]] adapters at typical ranks.

Per [[ai-engineering-ch07-finetuning|*AI Engineering* Ch 7]]:

> "Newer adapter methods include IA3 (Liu et al., 2022), whose efficient mixed-task batching strategy makes it particularly attractive for multi-task finetuning. It's been shown to outperform LoRA and even full finetuning in some cases."

## Why it's interesting

- **Smaller than LoRA**: IA3 trains only a single vector per layer per attention head, not a rank-r matrix.
- **Multi-task batching**: because IA3 is just multiplication by a vector, you can batch different tasks together at inference time more efficiently than LoRA (which requires different rank-r matrices per task).
- **Few-shot strength**: the original paper showed IA3 outperforming in-context learning on few-shot benchmarks.

## Trade-offs vs [[lora|LoRA]]

| Property | [[lora\|LoRA]] | IA3 |
|---|---|---|
| Trainable params | Higher (r · n + r · m per matrix) | Much lower (n or m per matrix) |
| Performance ceiling | Higher | Lower in absolute terms, but competitive |
| Inference batching across tasks | Hard (different matrix shapes) | Easy (different vectors) |
| Ecosystem support | Dominant | Limited |

## When to use

- Few-shot settings (the T-Few setting).
- Multi-task inference where you'd batch multiple tasks together.
- Memory-extremely-constrained finetuning.

Otherwise, [[lora|LoRA]] remains the default for most application engineers because of its much larger ecosystem.

## Connections

- [[PEFT]] — parent family.
- [[lora|LoRA]] — sibling adapter-based method.
- [[BitFit]] — minimal-parameter PEFT sibling.
- [[FineTuning]] — parent operation.
- [[ai-engineering-ch07-finetuning]] — primary source.
