---
title: "Optimizer State"
type: concept
tags: [optimization, training, memory]
sources: [ai-engineering-ch07-finetuning]
last_updated: 2024-12-04
---

# Optimizer State

The **per-parameter auxiliary values that an optimizer maintains across training steps** — typically momentum and variance estimates that smooth the gradient signal. Per [[ai-engineering-ch07-finetuning|*AI Engineering* Ch 7]], optimizer states are one of the **four contributors to training memory** alongside weights, activations, and gradients.

## Per-optimizer cost

| Optimizer | Values per [[TrainableParameters\|trainable parameter]] | Description |
|---|---|---|
| Vanilla [[StochasticGradientDescent\|SGD]] | **0** | Just use the current gradient; no state. |
| [[Momentum]] SGD | **1** | Running average of past gradients. |
| **[[Adam]]** | **2** | First moment (momentum) + second moment (variance estimate). |
| AdamW | 2 | Same as Adam structurally; weight-decay handled differently. |
| Adafactor | <2 | Factorizes the second moment to save memory; used in [[T5]]. |
| Lion | 1 | EvoLved Sign Momentum (Chen et al. 2023); single state per param. |

## The Adam dominance and its memory cost

> "For transformer-based models, Adam is, by far, the most widely used optimizer." — Ch 7

Adam's two-state-per-parameter cost is the reason a 13B-param model in FP16 with Adam needs **78 GB** for gradients + optimizer states (13B × 3 × 2 bytes). Halving this — Lion, Adafactor, momentum-only — has been an active research area; Adam's empirical advantages have so far made the memory cost worth it for most teams.

## Where this matters most

- **[[FullFinetuning|Full finetuning]]** — optimizer states are the largest memory cost beyond activations.
- **[[PEFT|PEFT]]** — optimizer states are tiny (only over trainable params); not the bottleneck.
- **[[QLoRA]]** — uses *paged optimizers* to swap optimizer states to CPU when GPU memory is exhausted.

## Connections

- [[Adam]] / [[Momentum]] / [[StochasticGradientDescent]] — concrete optimizers.
- [[Gradient]] — what optimizer states smooth.
- [[TrainingMemoryFormula]] — formula in which optimizer states appear.
- [[TrainableParameters]] — what optimizer states are stored per.
- [[CPUOffloading]] — strategy for swapping out optimizer states.
- [[QLoRA]] — paged optimizers.
- [[ai-engineering-ch07-finetuning]] — primary source.
