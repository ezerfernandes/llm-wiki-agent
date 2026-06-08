---
title: "Batch Size"
type: concept
tags: [training, hyperparameters, finetuning]
sources: [ai-engineering-ch07-finetuning, mlsysbook-ch05-neural-computation]
last_updated: 2026-06-05
---

# Batch Size

The number of training examples processed per [[Gradient|gradient]] update step. Per [[ai-engineering-ch07-finetuning|*AI Engineering* Ch 7]]:

> "The batch size determines how many examples a model learns from in each step to update its weights. A batch size that is too small, such as fewer than eight, can lead to unstable training. A larger batch size helps aggregate the signals from different examples, resulting in more stable and reliable updates."

## The trade-offs (Ch 7)

| Larger batch | Smaller batch |
|---|---|
| Stable updates | Unstable updates (b < ~8) |
| Faster epoch wall-clock | Slower epoch wall-clock |
| More memory | Less memory |
| Better hardware utilization | Wasted hardware |

## Rule of thumb (Ch 7)

- **b < 8** → likely unstable. Consider [[GradientAccumulation|gradient accumulation]] to fake a larger batch.
- **b ∈ [8, 64]** → typical for finetuning consumer-scale models.
- **b ∈ [64, 4096+]** → typical for full pre-training of foundation models.
- The upper limit is set by GPU memory (the [[MemoryBottleneck]]).

## The cost-vs-efficiency trade

> "More expensive compute allows faster finetuning." — Ch 7

A bigger GPU lets you use a bigger batch, which means more wall-clock training throughput. This is the hardware-cost side of the finetuning economics.

## Open theoretical question

Ch 7's footnote: *"While it's commonly acknowledged that small batch sizes lead to unstable training, I wasn't able to find good explanations for why that's the case. If you have references about this, please feel free to send them my way."* The phenomenon is empirically robust but theoretically under-explained.

## How to choose

- Start with the largest batch that fits in your memory after accounting for the model + optimizer + activations.
- If <8, use [[GradientAccumulation|gradient accumulation]] to fake a larger effective batch.
- When compute isn't the bottleneck, **experiment** — different batch sizes can produce noticeably different final model quality.

## Connections

- [[GradientAccumulation]] — the technique that simulates a larger batch.
- [[LearningRate]] — typically scales with batch size (linear-scaling rule).
- [[MemoryBottleneck]] — what bounds batch size.
- [[HyperparameterTuning]] — the broader hyperparameter discipline.
- [[NumberOfEpochs]] / [[LearningRate]] / [[PromptLossWeight]] — fellow finetuning hyperparameters.
- [[MiniBatchGradientDescent]] / [[mlsysbook-ch05-neural-computation]] — Ch 5 calls batch size a *systems lever*: GPUs process 32 inputs at ~the latency of 1 ([[MatrixMultiplication|matmul]] parallelizes across the batch dim), but each doubling roughly doubles activation memory; it couples to [[LearningRate|learning rate]] via the linear scaling rule, a common single→multi-GPU divergence trap.
- [[ai-engineering-ch07-finetuning]] — primary source.
