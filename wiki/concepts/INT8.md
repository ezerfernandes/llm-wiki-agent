---
title: "INT8 — 8-Bit Integer"
type: concept
tags: [numerics, quantization, inference]
sources: [ai-engineering-ch07-finetuning]
last_updated: 2024-12-04
---

# INT8 — 8-Bit Integer

An 8-bit integer format used for **inference quantization** (and, increasingly, training). Per [[ai-engineering-ch07-finetuning|*AI Engineering* Ch 7]]:

> "Numbers can also be represented as integers. Even though not yet as common as floating formats, integer representations are becoming increasingly popular. Common integer formats are INT8 (8-bit integers) and INT4 (4-bit integers). ... Integer formats are also called fixed point formats."

## Range and step

- Signed INT8 range: −128 to +127 (256 values total).
- Quantization to INT8 typically uses a **scale factor** (and optionally a zero-point) per tensor or per channel: `q = round(x / scale)`. Inference dequantizes when needed: `x = q × scale`.
- Step size is uniform — INT8 has constant absolute precision across its range, unlike floats which have constant *relative* precision.

## Why INT8 became popular

- **2× smaller than [[FP16]], 4× smaller than [[FP32]]**.
- **Hardware support**: NVIDIA Ampere+ tensor cores, ARM Neon, x86 AVX-512 VNNI, mobile NPUs all have native INT8 dot-product instructions. Often **2× the throughput** of FP16.
- **[[Dettmers2022LLMint8|LLM.int8()]]** (Dettmers et al., 2022) made INT8 quantization viable for billion-scale transformers without significant quality loss.

## Training in INT8

Ch 7 cites [[CharacterAI]] (2024) as having **trained their models entirely in INT8** — eliminating the train/serve precision mismatch *and* significantly improving training efficiency. This is unusual; most teams use INT8 only for inference.

## Connections

- [[INT4]] — neighboring smaller-bit format.
- [[FP8]] — alternative 8-bit format (float rather than integer).
- [[Quantization]] — parent family.
- [[NumericalRepresentation]] — umbrella concept.
- [[Dettmers2022LLMint8]] — foundational LLM-quantization work.
- [[Bitsandbytes]] — library implementing INT8 quantization.
- [[CharacterAI]] — training-in-INT8 case study.
- [[ai-engineering-ch07-finetuning]] — primary source.
