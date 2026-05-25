---
title: "Cosine Learning Rate Schedule"
type: concept
tags: [optimization, training, deep-learning]
sources: [d2l-optimization, hands-on-llm-ch12-fine-tuning-generation-models]
last_updated: 2026-05-24
---

# Cosine Learning Rate Schedule (Cosine Annealing)

Loshchilov & Hutter 2016 (SGDR) — a [[LearningRateScheduler|learning-rate schedule]] that decays $\eta$ along a half-cosine curve from initial $\eta_0$ to a small target $\eta_T$ over $t \in [0, T]$. Now ubiquitous in [[transformer|Transformer]] pretraining and computer-vision training.

## The schedule

$$\eta_t = \eta_T + \frac{\eta_0 - \eta_T}{2}\Big(1 + \cos\!\left(\frac{\pi t}{T}\right)\Big)$$

for $t \in [0, T]$, pinned to $\eta_T$ for $t > T$. At $t = 0$: $\eta_t = \eta_0$ (initial). At $t = T$: $\eta_t = \eta_T$ (target, often $0$ or a small floor like $0.01\,\eta_0$).

## Why it works

The cosine curve has two desirable properties ([[d2l-optimization]] §lr-scheduler-cosine):

- **Slow decay at the start**: the derivative $\eta'_t \to 0$ as $t \to 0$, so the learning rate stays near $\eta_0$ for the first few epochs — the model gets time to make real progress before the rate drops.
- **Slow decay at the end**: $\eta'_t \to 0$ as $t \to T$, so the final epochs use a small, slowly-changing rate — fine-tuning the solution without aggressive perturbation.

In between, the cosine drops monotonically — faster than polynomial decay around the midpoint, slower at the boundaries.

## Composition with [[Warmup|warmup]]

The most common production schedule is **linear warmup + cosine decay**:

1. Linearly ramp $\eta$ from $0$ (or $\eta_\textrm{init}$) to $\eta_0$ over $W$ warmup steps.
2. Apply cosine annealing from $\eta_0$ to $\eta_T$ over the remaining $T - W$ steps.

Used by essentially every modern LLM pretraining run (GPT-3, T5, LLaMA, etc.) and the default `CosineAnnealingLR` + `LinearLR` composition in PyTorch.

## Cyclical variant: cosine annealing with warm restarts (SGDR)

Loshchilov & Hutter's original paper proposes *restarting* the schedule periodically — at restart points $t = T_i$, the rate jumps back to $\eta_0$ and decays again over the next $T_{i+1}$ steps. Useful for stochastic weight averaging and for stepping out of suboptimal local minima.

## Connections

- [[d2l-optimization]] — canonical reference (§lr-scheduler-cosine).
- [[LearningRateScheduler]] — parent concept.
- [[Warmup]] — typically composed with cosine.
- [[LearningRate]] — what the schedule modifies.
- [[transformer|Transformer]] / [[BERT]] / [[T5]] / [[GPT]] — schedule is default in LLM pretraining.

## From [[hands-on-llm-ch12-fine-tuning-generation-models|Hands-On LLMs Ch 12]]

Ch 12 of *Hands-On LLMs* uses **`lr_scheduler_type="cosine"`** in both the SFT and DPO stages of its QLoRA recipe. The chapter's framing:

> *"A common method is to apply the cosine learning rate scheduler. This scheduler linearly increases the learning rate from 0 to the initial value of the learning rate ... Then, the learning rate gradually decreases following the cosine function."* — Ch 12

Ch 12 surfaces a Ch-12-specific data point from the QLoRA authors: *"higher learning rates work better for larger models (>33B parameters)."* The chapter pairs the cosine schedule with [[Warmup|`warmup_ratio=0.1`]] (DPO stage) for the standard linear-warmup → cosine-decay composition.
