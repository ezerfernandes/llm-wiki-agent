---
title: "Long-Context Finetuning"
type: concept
tags: [finetuning, context-length, positional-encoding]
sources: [ai-engineering-ch07-finetuning]
last_updated: 2024-12-04
---

# Long-Context Finetuning

Finetuning that **extends a model's maximum context length** beyond what it was pre-trained for, typically by modifying the model's positional embeddings to handle a wider range of positions. Per [[ai-engineering-ch07-finetuning|*AI Engineering* Ch 7]]:

> "It's possible to finetune a model to extend its context length. Long-context finetuning typically requires modifying the model's architecture, such as adjusting the positional embeddings. A long sequence means more possible positions for tokens, and positional embeddings should be able to handle them."

## Why it's hard

> "Compared to other finetuning techniques, long-context finetuning is harder to do. The resulting model might also degrade on shorter sequences." — Ch 7

Reasons:
- Positional encodings (RoPE / ALiBi / sinusoidal) were trained with specific position ranges; extrapolation breaks them.
- Attention's quadratic compute means long sequences are expensive even at inference, let alone training.
- Many short-context evaluations regress as the model is forced to generalize over longer ranges.

## Common techniques

- **RoPE scaling** (linear interpolation, dynamic scaling, YaRN) — adjust the rotary frequency to fit longer positions.
- **[[LongLoRA]]** (Chen et al. 2023) — shifted sparse attention + selectively unfrozen positional embeddings under a LoRA wrapper.
- **Position Interpolation** (Chen et al. 2023, Meta) — squeeze the positional encoding to fit more positions in the same range.

## Canonical case: [[CodeLlama]]

Per Ch 7: Code Llama was long-context-finetuned from Llama 2 to expand max context from **4,096 → 16,384 tokens** to fit longer code files. The same model family includes infilling-finetuned variants — multiple specialized FT phases stacked on the same base.

## Trade-offs vs simply choosing a long-context base model

- **Long-context FT cost** vs **long-context-native model cost**.
- If a strong long-context base model exists in your model family, it's usually cheaper to start there.
- If you have a specific base model you must use, long-context FT is the path.

## Connections

- [[FineTuning]] — parent operation.
- [[LongLoRA]] — a PEFT method for long-context FT.
- [[ContextLength]] — what long-context FT extends.
- [[positionalencoding|Positional Encoding]] — the architectural component being modified.
- [[CodeLlama]] — canonical example.
- [[ai-engineering-ch07-finetuning]] — primary source.
