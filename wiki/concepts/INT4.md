---
title: "INT4 — 4-Bit Integer"
type: concept
tags: [numerics, quantization, inference]
sources: [ai-engineering-ch07-finetuning]
last_updated: 2024-12-04
---

# INT4 — 4-Bit Integer

A 4-bit integer format for **aggressive inference quantization**. Per [[ai-engineering-ch07-finetuning|*AI Engineering* Ch 7]]:

> "More commonly, however, parameter values are converted into an integer format, such as INT8 or INT4."

## Range and step

Signed INT4 range: −8 to +7 (16 values total). Combined with a scale factor (and optionally zero-point), INT4 spans the practical weight distribution at coarse uniform steps.

## Memory savings

- Llama-2-70B in [[FP16]]: 140 GB.
- Llama-2-70B in INT4: ~35 GB. **4× reduction.**
- Combined with PEFT adapter weights kept in BF16, this is the [[QLoRA]] formula.

## Quality cost

INT4 quantization can cause meaningful quality loss for naive PTQ. Mitigations:
- **GPTQ** (post-training quantization with weight error minimization).
- **AWQ** (activation-aware weight quantization).
- **SmoothQuant** (move quantization difficulty from activations to weights).
- **NF4** (non-uniform bins; see [[NormalFloat4]]).

## When INT4 is the right choice

- **Memory-constrained inference** — fitting a 70B model on a 48 GB GPU.
- **[[QLoRA]] finetuning** — base weights in NF4 (a non-uniform 4-bit format), LoRA adapter in BF16.
- **On-device inference** — making consumer-laptop LLM inference feasible.

## When INT4 is risky

- **First-time inference deployment** without quality regression testing.
- **Reasoning-heavy or precision-sensitive tasks** — INT4 quality loss can be larger than INT8 quality loss for these.

## Connections

- [[INT8]] — larger-bit integer sibling.
- [[FP4]] — float alternative at same bit count.
- [[NormalFloat4]] — non-uniform 4-bit format from QLoRA.
- [[Quantization]] — parent family.
- [[QLoRA]] — the canonical INT4-adjacent training method.
- [[NumericalRepresentation]] — umbrella concept.
- [[Bitsandbytes]] — implementation library.
- [[ai-engineering-ch07-finetuning]] — primary source.
