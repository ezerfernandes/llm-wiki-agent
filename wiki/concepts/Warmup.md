---
title: "Learning Rate Warmup"
type: concept
tags: [optimization, training, deep-learning]
sources: [d2l-optimization, hands-on-llm-ch12-fine-tuning-generation-models]
last_updated: 2026-05-24
---

# Learning Rate Warmup

Linear (or otherwise gradually-increasing) ramp of the [[LearningRate]] from a small value (often $0$) up to the target $\eta_0$ over the first $W$ training steps — before any decay schedule begins. Now standard in [[transformer|Transformer]] pretraining and most modern deep-network training pipelines.

## Why it works

Two reasons ([[d2l-optimization]] §lr-scheduler-warmup):

1. **Random initialization makes early gradients meaningless.** The first few hundred steps have parameter values that are essentially random; large updates in random directions can push the network into divergent regimes. A small initial $\eta$ keeps these early steps from doing damage.
2. **Adaptive optimizers ([[Adam]]) need time to accumulate stable second-moment estimates.** Adam's $\hat{\mathbf{s}}_t = \mathbf{s}_t/(1-\beta_2^t)$ bias correction is unstable when $t$ is small; warmup gives the second moment time to stabilize before the rate scales up.

Gotmare, Keskar, Xiong & Socher 2018 show that warmup particularly **limits divergence in very deep networks** — early in training, deep layers receive gradient signals that are essentially noise, and large initial $\eta$ amplifies that noise multiplicatively through the depth.

## The schedule

Standard linear warmup:

$$\eta_t = \frac{t}{W}\,\eta_0 \quad \textrm{for}\quad t \in [0, W].$$

After $t > W$, hand off to the main schedule (typically [[CosineLRSchedule|cosine annealing]] or polynomial decay).

Typical $W$ values:

- **[[transformer|Transformer]] pretraining**: 1k–10k steps (small fraction of total).
- **CNN fine-tuning**: 1–5 epochs.
- **LLaMA / GPT-3-style runs**: ~2000 warmup steps.

## Composition

Warmup composes with **any** decay schedule, not just cosine. The PyTorch idiom is `SequentialLR([LinearLR(warmup), CosineAnnealingLR(decay)])`.

## Connections

- [[d2l-optimization]] — canonical reference (§lr-scheduler-warmup).
- [[LearningRate]] / [[LearningRateScheduler]] — parent concepts.
- [[CosineLRSchedule]] — most common decay paired with warmup.
- [[Adam]] — particularly benefits from warmup (bias-correction stability).
- [[transformer|Transformer]] / [[BERT]] / [[T5]] / [[GPT]] — warmup is default in LLM pretraining.

## From [[hands-on-llm-ch12-fine-tuning-generation-models|Hands-On LLMs Ch 12]]

Ch 12 of *Hands-On LLMs* uses **`warmup_ratio=0.1`** in the DPO stage of its QLoRA recipe — a gentle ramp from 0 to the target LR (`1e-5`) over the first 10% of training steps. The chapter's pedagogical anchor: DPO updates are inherently **destabilizing if too large** (since they involve log-probability shifts relative to a frozen reference policy), and warmup gives the model a soft start before reaching the target rate.

The Ch 12 DPO recipe is the wiki's first runnable case where the **`warmup_ratio`** parameter (as opposed to `warmup_steps`) is used — `warmup_ratio=0.1` automatically computes the warmup-step count from total steps, decoupling the warmup spec from the exact training-step count.
