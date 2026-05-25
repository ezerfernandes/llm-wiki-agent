---
title: "Full Finetuning"
type: concept
tags: [finetuning, training]
sources: [ai-engineering-ch07-finetuning, hands-on-llm-ch11-fine-tuning-representation-models]
last_updated: 2026-05-23
---

# Full Finetuning

The finetuning regime where **every parameter of the base model is trainable**. Per [[ai-engineering-ch07-finetuning|*AI Engineering* Ch 7]], full finetuning was the only finetuning regime in the early days of transfer learning, when models were small enough to fit in GPU memory along with their gradients and optimizer states. It became impractical for foundation-scale models around the 2020 inflection — motivating [[PEFT|parameter-efficient finetuning]].

## How it differs from training

> "Full finetuning can look similar to training. The main difference is that training starts with randomized model weights, whereas finetuning starts with model weights that have been previously trained." — Ch 7

So the *mechanics* are identical to training; only the initialization changes.

## Why it's expensive: the memory math

Per [[ai-engineering-ch07-finetuning|Ch 7]] for a **7B-parameter model in FP16 with [[Adam]]**:

| Component | Calculation | Memory |
|---|---|---|
| Weights | 7B × 2 bytes | 14 GB |
| Gradients + Adam states | 7B × 3 × 2 bytes | 42 GB |
| **Total (excluding activations)** | | **56 GB** |

That's already past most consumer GPUs (12–48 GB). And the activation memory (for caching values needed during the backward pass) can dwarf the weight memory at long sequence lengths.

## Data requirements

Full finetuning typically requires **at least thousands of (input, output) examples, often many more**. PEFT methods like [[lora|LoRA]] can match full finetuning's quality with hundreds — Ch 7 explicitly recommends LoRA over full finetuning for small datasets (< ~1,000 examples).

## When to choose full finetuning over PEFT

Per Ch 7:
- When PEFT can't reach the quality bar your task requires.
- When you have **lots** of data and **lots** of compute.
- When you're producing a base model others will further finetune (model-developer territory).

Otherwise: **start with [[lora|LoRA]], attempt full finetuning only if needed.**

## Connections

- [[FineTuning]] — the parent operation; full FT is the all-weights variant.
- [[PEFT]] — the memory-efficient alternative.
- [[PartialFinetuning]] — the in-between approach (freeze first-N layers).
- [[MemoryBottleneck]] / [[TrainingMemoryFormula]] / [[OptimizerState]] — the cost drivers.
- [[CPUOffloading]] / [[GradientCheckpointing]] / [[MixedPrecisionTraining]] — techniques to make full FT fit on smaller hardware.
- [[ai-engineering-ch07-finetuning]] — primary source.

## From [[hands-on-llm-ch11-fine-tuning-representation-models|*Hands-On LLMs* Ch 11]]

Ch 11 is the wiki's **runnable full-FT recipe for a representation model** — `bert-base-cased` (110M params) fully fine-tuned on Rotten Tomatoes via [[HuggingFace|Hugging Face]] [[Trainer]] + [[TrainingArguments]] (`lr=2e-5`, `batch_size=16`, `weight_decay=0.01`, 1 epoch). Result: **F1 = 0.85** in ~minutes on a Colab T4 — *"It only costs us a couple of minutes to train."*

For a 110M-param encoder this is **tractable on consumer hardware** in a way that 7B+ decoder-only LLMs are not — confirming Ch 7's point that full FT is feasible for *small enough* models. The chapter's [[LayerFreezing]] experiments quantify the trade-off vs full FT: freezing all but block 11 + head gets 0.80 (vs 0.85) with much less compute.

Ch 11 also walks full FT of `AutoModelForMaskedLM` (`bert-base-cased`) for [[ContinuedPretraining|continued pretraining]] — same memory profile, 10 epochs on Rotten Tomatoes raw text (labels stripped). Then loads the adapted model via `AutoModelForSequenceClassification.from_pretrained("mlm", num_labels=2)` for downstream classification fine-tune.
