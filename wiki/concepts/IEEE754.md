---
title: "IEEE 754"
type: concept
tags: [standards, floating-point, numerics, ieee, binary-representation]
sources: [dis-4-8-floating-point]
last_updated: 2026-05-17
---

# IEEE 754

**IEEE 754** is the **IEEE Standard for Floating-Point Arithmetic** — the dominant binary [[FloatingPoint|floating-point]] format implemented by virtually every modern [[CPU]], [[GPU]], and language runtime as of 2026. First published 1985, revised 2008 and 2019. *[[DiveIntoSystems]]* [[dis-4-8-floating-point|Ch 4.8]] treats only the **32-bit single-precision** subset (`binary32`).

## Single-precision (`binary32`) — the 32-bit format

| Field | Bits | Position (MSB → LSB) | Encoding |
|---|---|---|---|
| [[SignBit]] | 1 | bit 31 | `0` = positive, `1` = negative |
| [[Exponent]] | 8 | bits 30–23 | unsigned integer $E$; true exponent = $E - 127$ |
| [[Mantissa]] | 23 | bits 22–0 | fractional bits $f$; significand = $1.f$ (implicit leading 1) |

Decoded value (normal range):

$$(-1)^{\text{sign}} \cdot (1 + \text{mantissa}/2^{23}) \cdot 2^{E - 127}$$

[[dis-4-8-floating-point|Ch 4.8]] direct quote: *"the significand gets multiplied by $2^{\text{exponent} - 127}$, where the 127 is a bias."*

## Why bias 127?

The exponent must represent both very large and very small (negative) powers of 2. Storing it as a **biased unsigned integer** ($E_{\text{stored}} = E_{\text{true}} + 127$) keeps the field width-agnostic to sign — every `binary32` exponent fits in $[0, 255]$, with $E_{\text{stored}} = 127$ meaning $2^0$, $E_{\text{stored}} = 128$ meaning $2^1$, etc. The bias trick avoids stealing a bit for an exponent sign while also giving lexicographically-ordered bit patterns the same order as the numerical values they encode (useful for hardware comparators).

## Worked example from [[dis-4-8-floating-point|Ch 4.8]]

`0b11000001101101000000000000000000` decodes to $-22.5$:

- **Sign bit** = `1` → negative
- **Exponent field** = `10000011` = 131 → true exponent = $131 - 127 = 4$ → factor $2^4 = 16$
- **Mantissa fraction** = `10110100…0` → significand = $1 + 1/2 + 1/8 + 1/16 + 1/64 = 1.40625$
- **Product**: $-1 \cdot 1.40625 \cdot 16 = -22.5$ ✓

(Note: the [[dis-4-8-floating-point|Ch 4.8]] webfetch summary mentioned a $2^{16}$ factor; the correct decoding for $-22.5$ is $2^4$. Verify against the textbook prose if discrepancy persists.)

## Special values (not covered in [[dis-4-8-floating-point|Ch 4.8]] — wiki deepening)

| Exponent $E$ | Mantissa $f$ | Meaning |
|---|---|---|
| 0 | 0 | $\pm 0$ (sign-dependent) |
| 0 | $\ne 0$ | **denormalized** — value = $(-1)^s \cdot 0.f \cdot 2^{-126}$ |
| 1–254 | any | **normal** number |
| 255 | 0 | $\pm \infty$ |
| 255 | $\ne 0$ | **NaN** (Not-a-Number); MSB of $f$ distinguishes quiet vs signaling |

## Double-precision (`binary64`) — 64-bit (not in [[dis-4-8-floating-point|Ch 4.8]])

1 sign / 11 exponent (bias 1023) / 52 mantissa bits. ~15–17 significant decimal digits. The default `double` in C, the `f64` in Rust, the `Number` in JavaScript.

## Other precisions

- `binary16` (half) — 1 / 5 / 10. Standardized 2008. Heavy use in ML inference / [[GPU]] tensor cores.
- `binary128` (quadruple) — 1 / 15 / 112. Rare; some scientific computing.
- `bfloat16` — Google Brain's truncated 16-bit float (1 / 8 / 7) with `binary32`'s exponent range, traded for mantissa precision; dominant in ML training. **Not** IEEE 754 standard but widely deployed.

## Rounding modes (IEEE 754-2008)

- **roundTiesToEven** (default) — round to nearest representable; tie → even mantissa.
- **roundTiesToAway** — tie → larger magnitude.
- **roundTowardZero** (truncation)
- **roundTowardPositive** / **roundTowardNegative**

[[dis-4-8-floating-point|Ch 4.8]] does not enumerate modes; the demonstrated rounding is implicit truncation.

## Connections

- [[FloatingPoint]] — the encoding paradigm IEEE 754 standardizes.
- [[SignBit]] / [[Exponent]] / [[Mantissa]] — the three fields.
- [[FloatingPointPrecision]] — rounding-error properties.
- [[FixedPoint]] — the alternative encoding.
- [[CPU]] / [[GPU]] — where IEEE 754 hardware lives.
- [[dis-4-8-floating-point]] — DIS Ch 4.8 source.
