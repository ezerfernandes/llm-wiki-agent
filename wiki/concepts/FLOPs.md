---
title: "FLOPs"
type: concept
tags: [compute, training, metrics]
sources: [ai-engineering-ch02-foundation-models]
last_updated: 2024-12-04
---

# FLOPs

**FLOP** = floating-point operation. **FLOPs** (plural) = the number of floating-point operations performed for a task. Per [[ai-engineering-ch02-foundation-models|*AI Engineering* Ch 2]], FLOPs are the **standardized unit for a model's compute requirement**, designed to be hardware-independent (different machines have different capacities and costs — an NVIDIA A10 vs H100 vs Intel Core Ultra are not comparable, but their FLOP counts are).

## FLOPs vs FLOP/s vs FLOP/s-day

Common source of confusion — Ch 2 spells out the three:

| Notation | Meaning |
|---|---|
| **FLOPs** | Total operations for a task (a count). |
| **FLOP/s** (also FLOPS) | Operations per second — a machine's *peak performance rate*. |
| **FLOP/s-day** | The work one FLOP/s does in 24 hours = **86,400 FLOPs**. Used by [[openai|OpenAI]] to dodge the FLOPs/FLOPS confusion. |

This book (and Ch 2 specifically) uses **FLOPs** for counts and **FLOP/s** for rates.

## Worked numbers from Ch 2

- **[[GPT3|GPT-3-175B]]** was trained with **3.14 × 10²³ FLOPs** (Brown et al., 2020).
- **PaLM-2** (largest variant) was trained with **10²² FLOPs** (Chowdhery et al., 2022).
- **NVIDIA H100 NVL** delivers up to **60 TeraFLOP/s** = 6 × 10¹³ FLOPs/sec ≈ **5.2 × 10¹⁸ FLOPs/day** (measured in FP32).

## Training cost calculation (Ch 2's worked example)

At 70% utilization and $2/h per H100, training GPT-3-175B on 256 H100s:

$$\$2 \times 256 \times 24 \times 256 / 0.7 = \$4{,}142{,}811$$

That's **≈$4.14M and ≈236 days** of wall-clock training — *if* you make no training mistakes.

## Three numbers that signal a model's scale

Per Ch 2's summary:

1. **Number of parameters** — proxy for *learning capacity*.
2. **Number of training tokens** — proxy for *how much the model learned*.
3. **Number of FLOPs** — proxy for *training cost*.

## Utilization

Ch 2's rule of thumb:
- **50% utilization** → okay
- **70% utilization** → great
- Above 70% → not the norm; achievable but unusual

## Connections
- [[ChinchillaScalingLaw]] — the compute-optimal allocation under a FLOP budget.
- [[scalinglaws]] — the broader power-law framework.
- [[ComputeOptimal]] — the goal under a fixed FLOP budget.
- [[pretraining]] — the workflow stage that consumes FLOPs.
- [[NVIDIA]] — the dominant FLOP/s provider.
- [[ai-engineering-ch02-foundation-models]] — primary source.
