---
title: "TPOT (Time Per Output Token)"
type: concept
tags: [latency, metrics, inference, autoregressive]
sources: [ai-engineering-ch01-intro, ai-engineering-ch09-inference-optimization]
last_updated: 2024-12-04
---

# TPOT — Time Per Output Token

**The steady-state time per generated token during foundation-model inference.** One of three latency metrics named in [[ai-engineering-ch01-intro|*AI Engineering* Ch 1's]] [[UsefulnessThreshold|usefulness threshold]] discussion (the others being [[TTFT|TTFT]] and total latency).

## What TPOT measures

After [[TTFT]] elapses (prefill is done, the first token has emerged), the model enters steady-state autoregressive generation: each new token requires one forward pass over the model conditioned on all previous tokens. TPOT is the time per such forward pass.

Ch 1's concrete arithmetic: *"If it takes 10 ms for a model to generate a token, it'll take a second to generate an output of 100 tokens, and even more for longer outputs."*

## Position in the latency budget

> **Total latency = TTFT + (TPOT × output length)**

TPOT dominates for **long outputs** (analysis reports, code generation, document summaries). [[TTFT]] dominates for **short outputs** (one-line answers).

## Why TPOT is hard to improve

Each step requires a full forward pass — there's no obvious way to "skip" tokens (modulo speculative decoding, which is one of Chapter 9's deep-dive techniques). TPOT is therefore highly sensitive to:
- Model size (parameter count).
- KV-cache size and memory-bandwidth pressure.
- Batch size (sometimes increasing batch size improves throughput but worsens individual TPOT).
- Quantization precision.

## Connections

- [[InferenceOptimization]] — discipline targeting TPOT.
- [[TTFT]] — companion latency metric (startup cost).
- [[UsefulnessThreshold]] — planning framework.
- [[AutoregressiveLanguageModel]] — sequential generation is the structural reason TPOT exists as a metric.
- [[Quantization]] — common TPOT-reduction lever.
- [[ai-engineering-ch01-intro]] — primary source.

## From [[ai-engineering-ch09-inference-optimization|AI Engineering Ch 9]]

Ch 9 deepens TPOT into the canonical **steady-state autoregressive-generation metric** and introduces refinements:

### Concrete reading-speed reference

> *"A very fast reader can read 120 ms/token, so a TPOT of around 120 ms, or 6–8 tokens/second, is sufficient for most use cases."* — Ch 9

In streaming UIs, dropping below this threshold gives diminishing user-experience returns.

### TPOT, TBT, and ITL

[[TBT]] (Time Between Tokens, used by LinkedIn) and ITL (Inter-Token Latency, used by NVIDIA) are streaming-cadence variants:

> *"Both measure the time between output tokens."* — Ch 9

In practice TPOT and TBT are nearly the same number — TPOT emphasizes the average / steady-state view; TBT emphasizes the distribution / jitter view.

### Quantization is the dominant TPOT lever

Because [[Decode|decode]] is [[MemoryBandwidthBound|memory-bandwidth-bound]] and TPOT scales with bandwidth consumed per token:

```
TPOT ∝ (parameter count × bytes/param) / bandwidth
```

Halving bytes/param (FP16 → INT8) roughly halves TPOT (modulo format-conversion overhead).

### TPOT and goodput

A typical TPOT-side SLO ("TPOT ≤ 100 ms") is one of the constraints [[Goodput|goodput]] is measured against. Continuous batching tuning, prefill-decode disaggregation, and batch-size selection all optimize against TPOT-bounded goodput.
