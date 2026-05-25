---
title: "BitNet b1.58"
type: concept
tags: [quantization, 1-bit-llm, microsoft]
sources: [ai-engineering-ch07-finetuning]
last_updated: 2024-12-04
---

# BitNet b1.58

A 2024 transformer architecture from [[microsoft|Microsoft]] Research (Ma et al.) that uses **1.58 bits per parameter** by representing each weight as one of three values: {−1, 0, +1}. Per [[ai-engineering-ch07-finetuning|*AI Engineering* Ch 7]]:

> "In 2024, Microsoft researchers (Ma et al.) declared that we're entering the era of 1-bit LLMs by introducing BitNet b1.58, a transformer-based language model that requires only 1.58 bits per parameter and whose performance is comparable to 16-bit Llama 2 (Touvron et al., 2023) up to 3.9B parameters."

(The "1.58" is `log₂(3)` — the information content of a ternary symbol.)

## Performance (Ch 7's Table 7-4)

BitNet b1.58 vs 16-bit Llama 2 averaged across ARCe / ARCc / HellaSwag / BoolQ / OpenBookQA / PIQA / WinoGrande:

| Size | Llama 2 (FP16) | BitNet b1.58 |
|---|---|---|
| 700M | 45.5 | 44.3 |
| 1.3B | 46.2 | 45.4 |
| 3B | 49.7 | 50.2 |
| 3.9B | — | 51.2 |

At 3B and above, BitNet b1.58 is **on par with or better than** a 16-bit Llama-2 at the same parameter count — at roughly **1/10 the memory** (1.58 vs 16 bits/param).

## Why this is striking

For most of deep-learning history, sub-8-bit quantization caused dramatic quality loss. BitNet b1.58 (and the older 1-bit lineage — [[BinaryConnect]] (Courbariaux et al. 2015), [[XnorNet]] (Rastegari et al. 2016), original [[BitNet]] (Wang et al. 2023)) show that **the right architecture trained from scratch can match FP16 quality at ternary precision**.

## What's not yet known

- Whether BitNet scales to 70B+ parameters.
- Whether the approach extends to multimodal models.
- Whether it benefits inference latency as much as memory.

Ch 7 cites BitNet b1.58 as evidence we're entering "the era of 1-bit LLMs" — but the field is too young to declare victory.

## Connections

- [[Quantization]] — the parent family.
- [[NumericalRepresentation]] — umbrella concept.
- [[BinaryConnect]] / [[XnorNet]] / [[BitNet]] — the older 1-bit lineage.
- [[microsoft|Microsoft]] — the institution behind BitNet b1.58.
- [[ai-engineering-ch07-finetuning]] — primary source.
