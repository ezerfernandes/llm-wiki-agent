---
title: "Exponent (Floating-Point)"
type: concept
tags: [floating-point, ieee-754, binary-representation]
sources: [dis-4-8-floating-point]
last_updated: 2026-05-17
---

# Exponent (Floating-Point)

The **exponent** is the scaling field of a [[FloatingPoint|floating-point]] number. It determines the **power of 2** by which the [[Mantissa|significand]] is multiplied — equivalently, the position of the implicit binary point relative to the leading 1.

## In [[IEEE754|IEEE 754]] `binary32`

- **8 bits** stored — values $E_{\text{stored}} \in [0, 255]$.
- **Bias 127** — the true exponent is $E_{\text{true}} = E_{\text{stored}} - 127$.
- Normal-number range: $E_{\text{stored}} \in [1, 254]$ → $E_{\text{true}} \in [-126, +127]$.
- Two reserved encodings: $E_{\text{stored}} = 0$ (subnormal / $\pm 0$) and $E_{\text{stored}} = 255$ ($\pm\infty$ / NaN).

[[dis-4-8-floating-point|Ch 4.8]] direct quote: *"the significand gets multiplied by $2^{\text{exponent} - 127}$, where the 127 is a bias."*

## Why a bias (not a sign bit)?

A floating-point format must represent both very large $(2^{+127})$ and very small $(2^{-126})$ scales. Two options:

1. **Signed exponent** with a dedicated sign bit — wastes a bit, complicates comparison.
2. **Biased unsigned exponent** — store $E + \text{bias}$ as plain unsigned; bias chosen so the representable range straddles zero.

[[IEEE754|IEEE 754]] picks option 2. The bias is **$2^{k-1} - 1$** for a $k$-bit exponent: 127 for `binary32` (8-bit exponent), 1023 for `binary64` (11-bit), 15 for `binary16` (5-bit).

## Bias-127 enables fast magnitude comparison

For positive [[FloatingPoint|floats]], **comparing the raw 32-bit pattern as an unsigned integer gives the correct numerical ordering**. This is a deliberate side-effect of the biased-exponent encoding sitting in the high bits next to the [[SignBit|sign]] — larger exponents produce larger bit patterns, which produce larger encoded values. Hardware float comparators exploit this directly.

## Dynamic range

`binary32` covers roughly $1.18 \times 10^{-38}$ to $3.40 \times 10^{38}$ — an enormous range that [[FixedPoint|fixed-point]] cannot match without absurd bit budgets. This range is the **payoff** of the moving binary point. The cost is **relative-not-absolute precision** — the [[Mantissa|mantissa]]'s 23 fractional bits buy ~7 decimal digits, but the absolute gap between adjacent floats scales with the magnitude.

## In `binary64` (wiki deepening)

11 exponent bits, bias 1023, normal $E_{\text{true}} \in [-1022, +1023]$. Dynamic range $\sim 10^{\pm 308}$.

## Connections

- [[FloatingPoint]] — the encoding family.
- [[IEEE754]] — the standard.
- [[Mantissa]] / [[SignBit]] — the other two fields.
- [[FloatingPointPrecision]] — what limited mantissa precision combined with exponent scaling means for arithmetic.
- [[dis-4-8-floating-point]] — DIS Ch 4.8 source.
