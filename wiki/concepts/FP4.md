---
title: "FP4 — 4-Bit Float"
type: concept
tags: [numerics, floating-point, quantization]
sources: [ai-engineering-ch07-finetuning]
last_updated: 2024-12-04
---

# FP4 — 4-Bit Float

A 4-bit floating-point format — **the smallest IEEE-compliant float**, per [[ai-engineering-ch07-finetuning|*AI Engineering* Ch 7]]:

> "The smallest possible float size that follows all IEEE principles is 4-bit."

## Bit allocation

Typical FP4: 1 sign + 2 exponent + 1 mantissa (E2M1), though variants exist.

## Where FP4 lives

- **NVIDIA Blackwell** announced 4-bit float inference as a first-class feature in 2024.
- **Inference-only** in practice — FP4 doesn't have enough range or precision for stable training in most setups.
- **Compared to [[INT4]]** — FP4 has wider dynamic range but discrete quantization steps; INT4 has uniform absolute steps. The choice depends on the value distribution.

## How aggressive is 4-bit?

A 70B-parameter model in FP4 = 70B × 0.5 bytes = **35 GB**. The same model in FP16 = 140 GB. **4× memory reduction.** Combined with hardware speedups, FP4 inference makes 70B+ models viable on consumer-tier hardware.

## Quality trade-off

Aggressive quantization (≤4 bits) causes meaningful quality loss without careful design. [[NormalFloat4|NF4]] (used by [[QLoRA]]) is one solution: non-uniform bins distributed by the quantile of the empirical weight distribution, designed specifically for the **N(0, σ²) shape of pre-trained weights**.

## Connections

- [[FP8]] — neighboring float format, 2× the bits.
- [[INT4]] — integer alternative at the same bit count.
- [[NormalFloat4]] — non-uniform 4-bit format from QLoRA.
- [[Quantization]] — the parent family.
- [[NumericalRepresentation]] — umbrella concept.
- [[NVIDIA]] — Blackwell native support.
- [[ai-engineering-ch07-finetuning]] — primary source.
