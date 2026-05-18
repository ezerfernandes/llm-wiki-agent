---
title: "Sign-Magnitude Representation"
type: concept
tags: [systems, binary, data-representation, signed-integers, historical]
sources: [dis-4-3-signed]
last_updated: 2026-05-17
---

# Sign-Magnitude Representation

**Sign-magnitude** is a historical [[SignedInteger|signed-integer]] encoding in which the [[MostSignificantBit|most-significant bit]] is reserved as a pure [[SignBit|sign flag]] (0 = non-negative, 1 = negative) and the remaining $N-1$ bits hold the **absolute magnitude** of the value as a plain unsigned binary number. Per [[dis-4-3-signed|DIS Ch 4.3]], it is presented for historical context only — *"no modern systems use signed magnitude."*

## The Scheme

For an $N$-bit pattern $s\,d_{N-2}\,d_{N-3}\cdots d_0$:

$$\text{value} \;=\; (-1)^s \cdot \sum_{i=0}^{N-2} d_i \cdot 2^i$$

The sign bit $s$ stands apart from the place-value sum — it multiplies the magnitude by $\pm 1$ rather than contributing as a weighted digit. This makes **negation trivial**: *"simply flip the most significant bit to change its sign."*

## 4-Bit Example Table

| Bit pattern | Sign-magnitude value |
|---|---|
| `0000` | +0 |
| `0001` | +1 |
| `0010` | +2 |
| `0111` | +7 |
| `1000` | **−0** |
| `1001` | −1 |
| `1010` | −2 |
| `1111` | −7 |

Range: $[-7, +7]$ — symmetric around zero, **but with a duplicate zero**.

## The Two-Zeros Pathology

Sign-magnitude's fatal flaw: **`0b0000` and `0b1000` both represent zero** — one as `+0`, the other as `−0`. This breaks equality testing (`+0 == −0`?), wastes a bit pattern, and forces hardware to add a special-case check before every comparison or arithmetic operation. *"No modern systems use signed magnitude"* (Ch 4.3) — it was displaced by [[TwosComplement|two's complement]], which has a unique zero and admits standard adder hardware.

## Where It Survives

Despite obsolescence as an *integer* encoding, sign-magnitude survives as the **mantissa sign** convention in [[FloatingPointNumber|IEEE 754 floating-point]] (a dedicated 1-bit sign field separate from the exponent and mantissa) — preserving the `+0` / `−0` distinction that has *defined* semantics for floats (e.g., `1.0 / +0.0 = +∞`, `1.0 / −0.0 = −∞`). This is exactly the dual-zero pathology that disqualifies it for integers, repurposed as a feature.

## Why Ch 4.3 Covers It

The pedagogy: contrasting sign-magnitude's intuitive simplicity (sign flag + magnitude — what a beginner would invent) against [[TwosComplement|two's complement]]'s counter-intuitive negative-weight MSB makes the latter's headline advantage (unique zero + adder-friendly arithmetic) memorable. Ch 4.3 spends one paragraph on sign-magnitude before pivoting to two's complement for the rest of the section.

## Connections

- [[SignedInteger]] — the umbrella.
- [[TwosComplement]] — the successor that displaced it; contrast on the unique-zero property.
- [[SignBit]] — the pure sign-flag role here; two's complement extends it to a dual role.
- [[BinaryNumber]] — the underlying encoding of the magnitude field.
- [[FloatingPointNumber]] — IEEE 754's sign-magnitude survivor (for mantissa sign, not exponent).
- [[ComputerHardware]] — rejected sign-magnitude for adder complexity.
- [[dis-4-3-signed]] — source.
