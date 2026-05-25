---
title: "Numerical Representation"
type: concept
tags: [numerics, hardware, training, inference, finetuning]
sources: [ai-engineering-ch07-finetuning]
last_updated: 2024-12-04
---

# Numerical Representation

The **bit-allocation pattern** by which a numerical value (typically a model weight or activation) is stored in memory. Per [[ai-engineering-ch07-finetuning|*AI Engineering* Ch 7]], the numerical representation is one of the three key contributors to a model's memory footprint:

> "The key contributors to a model's memory footprint during finetuning are its number of parameters, its number of trainable parameters, and its numerical representations."

## The bit-allocation triple

Every float format (per [[IEEE754]] and its AI-extensions) allocates bits to three roles:

- **Sign bit** (always 1 bit): positive or negative.
- **Range bits** (a.k.a. *exponents*, *significand*): how big or small a magnitude can be represented.
- **Precision bits** (a.k.a. *mantissa*): how accurately a value within that magnitude can be represented.

Ch 7's clearest summary: *"More bits means a wider range. ... Reducing the number of precision bits makes a number less precise."*

## The AI format spectrum

| Format | Total bits | Sign / Range / Precision | Designer | Use |
|---|---|---|---|---|
| [[FP64]] | 64 | 1 / 11 / 52 | IEEE | Scientific compute; default in NumPy / pandas; rare in NNs |
| [[FP32]] | 32 | 1 / 8 / 23 | IEEE | Historical NN default; "single precision" |
| [[FP16]] | 16 | 1 / 5 / 10 | IEEE | "Half precision"; less range than FP32 |
| [[BF16]] | 16 | 1 / 8 / 7 | [[google\|Google]] | Same range as FP32, less precision than FP16; TPU-optimized |
| [[TF32]] | **19** | 1 / 8 / 10 | [[NVIDIA]] | GPU-optimized; "32" is a misnomer |
| [[FP8]] | 8 | 1 / 4-5 / 2-3 | various | Hopper-supported; finetuning-viable |
| [[FP4]] | 4 | 1 / 2 / 1 | various | Blackwell-targeted; smallest IEEE-compliant float |
| [[INT8]] | 8 | sign + 7-bit integer | — | "Fixed point"; inference-standard |
| [[INT4]] | 4 | sign + 3-bit integer | — | Aggressive inference; QLoRA storage |
| [[NormalFloat4\|NF4]] | 4 | non-uniform quantile bins | [[TimDettmers\|Dettmers]] et al. | QLoRA's base-model format |

Less than 1 bit is impossible. **[[BitNetB158|BitNet b1.58]]** (1.58 bits/param, Microsoft 2024) and the older 1-bit lineage ([[BinaryConnect]], [[XnorNet]], [[BitNet]]) are pushing the lower bound.

## The Ch 7 cautionary tale

Llama 2 was released in BF16. Many teams loaded it in FP16 (same bit count!) and reported quality much worse than advertised. **BF16 and FP16 are NOT interchangeable** despite having the same bit count — they trade range for precision differently. `1234.56789` → `1235.0` in FP16 vs `1232.0` in BF16. The Llama 3.1 release saw the same confusion repeat.

**Rule: load a model in the format it was trained in.**

## Float vs integer

> "Strictly speaking, it's quantization only if the target format is integer. However, in practice, quantization is used to refer to all techniques that convert values to a lower-precision format." — Ch 7

The wiki follows the same loose convention.

## Connections

- [[FloatingPoint]] / [[FloatingPointPrecision]] — the IEEE-754 family.
- [[Quantization]] — the process of moving values to a lower-precision representation.
- [[BF16]] / [[FP16]] / [[FP32]] / [[FP8]] / [[FP4]] / [[INT8]] / [[INT4]] / [[NormalFloat4]] — specific formats.
- [[BitNetB158]] — the 1.58-bit frontier.
- [[MixedPrecisionTraining]] — the training-time application.
- [[MemoryBottleneck]] — the cost framework this representation drives.
- [[ai-engineering-ch07-finetuning]] — primary source.
