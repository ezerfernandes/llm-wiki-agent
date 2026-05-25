---
title: "Ossification"
type: concept
tags: [finetuning, pretraining, llm-training]
sources: [ai-engineering-ch08-dataset-engineering]
last_updated: 2024-12-04
---

# Ossification

**The phenomenon in which pre-training freezes (ossifies) a model's weights so that they don't adapt as well to a large finetuning dataset as they would if trained from scratch.** Per [[ai-engineering-ch08-dataset-engineering|*AI Engineering* Ch 8]], the effect was named by Hernandez et al. (2021).

## When ossification matters

For most data scales (1K–100K examples), the chapter's standard advice holds: **finetuning a pre-trained model beats training from scratch**. Ossification flips this at the unusual *millions-of-examples* scale.

> "Finetuning on top of a pre-trained model is typically more efficient than training from scratch, [but] there are situations when finetuning can be worse, especially when you have a lot of training data."

## Susceptibility scales inversely with model size

> "Smaller models are more susceptible to ossification than larger models."

So a small pre-trained model + millions of finetuning examples is the worst-case ossification scenario; a large pre-trained model is more robust.

## Decision implication

If you have **millions of examples** and **a smaller base model**, evaluate:

1. PEFT-on-large-base-model performance.
2. Full-finetune-on-medium-base-model performance.
3. **Train-from-scratch-small-model** performance.

Ossification can make (3) competitive with (2), even though the conventional wisdom favors (2).

## Connections

- [[FineTuning]] / [[FullFinetuning]] — the operation ossification degrades.
- [[Pretraining]] — the operation that causes ossification.
- [[DataQuantity]] — ossification is a data-quantity-regime-specific effect.
- [[PEFT]] — alternative path that sidesteps full-FT ossification by training fewer parameters.
- [[ai-engineering-ch08-dataset-engineering]] — primary source.
