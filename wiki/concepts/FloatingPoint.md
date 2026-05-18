---
title: "Floating Point"
type: concept
tags: [binary-representation, numerics, floating-point, real-numbers]
sources: [dis-4-8-floating-point]
last_updated: 2026-05-17
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
