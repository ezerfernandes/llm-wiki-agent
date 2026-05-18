---
title: "Mantissa (Significand)"
type: concept
tags: [floating-point, ieee-754, binary-representation]
sources: [dis-4-8-floating-point]
last_updated: 2026-05-17
---

# Mantissa (Significand)

The **mantissa** — also called the **significand** — is the fractional-precision field of a [[FloatingPoint|floating-point]] number. It carries the **value's significant digits**; the [[Exponent|exponent]] carries the **scale**. The [[SignBit|sign]] gives orientation. [[dis-4-8-floating-point|Ch 4.8]]: *"the fractional portion behaves like the fixed-point representation."*

## In [[IEEE754|IEEE 754]] `binary32`

- **23 bits** stored, named $f_{22} f_{21} \ldots f_0$.
- **Implicit leading 1** (normalization rule): the actual significand is $1.f_{22} f_{21} \ldots f_0$ — the leading 1 is **not stored**, recovering one bit of precision.
- Value range of significand: $[1.0, 2.0)$ for normal numbers.
- Decoded numerically: $1 + \sum_{i=0}^{22} f_i \cdot 2^{i-23}$.

## Fractional bits work like [[FixedPoint|fixed-point]]

Each bit $f_i$ contributes $2^{i-23}$, exactly the negative-power-of-2 place-value scheme of fixed-point. So a mantissa field of `10000000000000000000000` means the significand is $1.5$ ($1 + 0.5$); `11000000…` means $1.75$; `10110100…0` means $1.40625$ (as in the [[dis-4-8-floating-point|Ch 4.8]] worked example for $-22.5$).

## Precision implications

23 stored mantissa bits + 1 implicit = 24 bits of precision = $\log_{10}(2^{24}) \approx 7.22$ significant decimal digits. The **relative precision** is $2^{-23} \approx 1.19 \times 10^{-7}$ — the **machine epsilon** for `binary32` (not named in [[dis-4-8-floating-point|Ch 4.8]] but standard terminology).

Because the exponent scales the value, the *absolute* precision is **proportional to the value's magnitude** — large numbers have large gaps between representable values, small numbers have small gaps. This is the key contrast with [[FixedPoint|fixed-point]]'s uniform absolute precision.

## In `binary64` (double precision — wiki deepening)

52 stored mantissa bits + 1 implicit = 53 bits → ~15–17 significant decimal digits. Machine epsilon $\approx 2.22 \times 10^{-16}$.

## Normalization

A floating-point number is **normalized** when its significand falls in $[1, 2)$ — equivalently, when the leading bit is 1 and can be left implicit. Subnormal / **denormalized** numbers (exponent field = 0) drop the implicit leading 1 to represent values smaller than $2^{-126}$ (binary32) at the cost of precision — not covered in [[dis-4-8-floating-point|Ch 4.8]].

## Connections

- [[FloatingPoint]] — the encoding family.
- [[IEEE754]] — the standard.
- [[Exponent]] / [[SignBit]] — the other two fields.
- [[FixedPoint]] — the place-value scheme the mantissa inherits.
- [[FloatingPointPrecision]] — the rounding consequence.
- [[dis-4-8-floating-point]] — DIS Ch 4.8 source.
