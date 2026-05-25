---
title: "Floating Point"
type: concept
tags: [binary-representation, numerics, floating-point, real-numbers]
sources: [dis-4-8-floating-point, ai-engineering-ch07-finetuning]
last_updated: 2026-05-23
---

# Floating Point

**Floating-point** is a binary encoding of real numbers where the **binary point moves** with the value, in contrast to [[FixedPoint|fixed-point]]'s pinned point. A floating-point number is stored as three fields — a **[[SignBit|sign]]**, an **[[Exponent|exponent]]**, and a **[[Mantissa|significand / mantissa]]** — and decoded as

$$(-1)^{\text{sign}} \cdot 1.\text{mantissa} \cdot 2^{\text{exponent} - \text{bias}}$$

The moving point gives floating-point its **enormous dynamic range** — the same 32 bits can represent $\sim 10^{-38}$ and $\sim 10^{+38}$ — at the cost of **relative-not-absolute precision** (about 7 significant decimal digits in `binary32`).

## Why floating-point exists

[[dis-4-8-floating-point|Ch 4.8]]'s opening claim: *"for any binary encoding of real numbers, there exist values that cannot be represented exactly."* Real numbers are uncountable, so any finite-bit encoding must approximate. [[FixedPoint|Fixed-point]] gives **uniform absolute precision** ($2^{-N}$ everywhere) but wastes bits on values whose magnitude doesn't need them. Floating-point gives **uniform relative precision** ($\sim 2^{-23}$ of the value's magnitude) by letting the exponent scale the mantissa.

## The IEEE 754 32-bit format

The dominant standard. See [[IEEE754]] for the full spec.

| Field | Bits | Role |
|---|---|---|
| [[SignBit]] | 1 | `0` = positive, `1` = negative |
| [[Exponent]] | 8 | Biased: stored value − 127 = true exponent |
| [[Mantissa]] | 23 | Fractional part; implicit leading `1` |

[[dis-4-8-floating-point|Ch 4.8]] worked example: `0b11000001101101000000000000000000` = $-22.5$.

## Shared rounding pathology with fixed-point

[[dis-4-8-floating-point|Ch 4.8]] emphasizes: *"like fixed-point, rounding problems similarly affect floating-point encodings."* Floating-point arithmetic is **not associative** under rounding — $(a \cdot b) \cdot c$ and $a \cdot (b \cdot c)$ can produce different results. See [[FloatingPointPrecision]] for the rounding-error treatment and the **1991 Patriot** / **1996 Ariane 5** catastrophes.

## What [[dis-4-8-floating-point|Ch 4.8]] does not cover (wiki notes)

- **64-bit double-precision** (`binary64`): 1 sign / 11 exponent (bias 1023) / 52 mantissa bits; $\sim 15$–$17$ significant decimal digits.
- **Denormalized numbers**: exponent field = 0, no implicit leading 1 — fills the gap around zero.
- **Special values**: $\pm 0$, $\pm \infty$, `NaN` (quiet / signaling) — encoded via exponent field = all-ones.
- **Rounding modes**: round-to-nearest-even (default), round-toward-zero, round-toward-$+\infty$, round-toward-$-\infty$.

## Connections

- [[IEEE754]] — the standard that codifies the encoding.
- [[FixedPoint]] — the simpler alternative; uniform absolute (not relative) precision.
- [[Mantissa]] / [[Exponent]] / [[SignBit]] — the three fields.
- [[FloatingPointPrecision]] — rounding-error consequences.
- [[BinaryRepresentation]] — umbrella encoding family.
- [[dis-4-8-floating-point]] — DIS Ch 4.8 source.

## From [[ai-engineering-ch07-finetuning|AI Engineering Ch 7]]

[[ChipHuyen|Huyen]] surveys the **AI-specific extensions of the IEEE-754 float family** that have emerged since the 2010s — driven by neural-network workloads' tolerance for low precision and their need for high range:

| Format | Bits | Sign / Range / Precision | Designed by | Notes |
|---|---|---|---|---|
| [[FP64]] | 64 | 1 / 11 / 52 | IEEE | Default in [[NumPy]] / [[pandas]]; "double precision"; rarely used in neural networks |
| [[FP32]] | 32 | 1 / 8 / 23 | IEEE | "Single precision"; the historical NN default |
| [[FP16]] | 16 | 1 / 5 / 10 | IEEE | "Half precision"; smaller range than FP32, ~3.5 decimal digits precision |
| [[BF16]] | 16 | 1 / 8 / 7 | [[google\|Google]] | "Brain float"; *same range as FP32, less precision than FP16*; designed for TPUs; Llama 2's release format |
| [[TF32]] | **19** | 1 / 8 / 10 | [[NVIDIA]] | Actually 19 bits despite the "32" name (Huyen's footnote: "why it's called TF32 and not TF19 keeps me up at night"); compatible with FP32 inputs |
| [[FP8]] | 8 | 1 / variable | various | NVIDIA Hopper-supported |
| [[FP4]] | 4 | 1 / variable | various | The smallest IEEE-compliant float; NVIDIA Blackwell inference target |
| [[NormalFloat4\|NF4]] | 4 | non-uniform bins | [[TimDettmers\|Dettmers]] et al. | QLoRA's format; bins distributed by quantiles of $\mathcal{N}(0, \sigma^2)$, not uniformly |

### Range vs precision trade-off

Ch 7's clearest framing — every float format splits bits between **range** (exponent bits, called *exponents*) and **precision** (mantissa bits, called *significands*), beyond the always-needed sign bit. **More range bits → can represent larger / smaller magnitudes. More precision bits → can represent values more accurately.**

The BF16 vs FP16 confusion (Llama 2 was released in BF16, many teams loaded it in FP16 and got worse-than-advertised quality) is Ch 7's canonical example that **format ≠ bit count** — you must match the format the model was trained with.
