---
title: "Fixed Point"
type: concept
tags: [binary-representation, numerics, fixed-point, real-numbers]
sources: [dis-4-8-floating-point]
last_updated: 2026-05-17
---

# Fixed Point

**Fixed-point** is a binary encoding of real numbers that extends the [[UnsignedInteger|unsigned-integer]] place-value scheme by placing a **[[BinaryPoint|binary point]] at a predetermined, fixed bit position**. Bits to the **left** of the point use positive powers of two ($2^0, 2^1, 2^2, \ldots$ — the standard integer place values from [[dis-4-1-bases|Ch 4.1]]); bits to the **right** use **negative powers** ($2^{-1}, 2^{-2}, 2^{-3}, \ldots$).

## Worked example from [[dis-4-8-floating-point|Ch 4.8]]

For an 8-bit fixed-point format with the point between bits 2 and 1 (i.e., 6 integer bits + 2 fractional bits — written `xxxxxx.xx`):

$$\mathtt{0b000101.10} = 1 \cdot 2^2 + 0 \cdot 2^1 + 1 \cdot 2^0 + 1 \cdot 2^{-1} + 0 \cdot 2^{-2} = 4 + 1 + 0.5 = 5.5$$

The chapter's headline: fixed-point is *"unsigned-integer place value extended to negative exponents."* No new arithmetic hardware required — the same adder works, only the interpretation of the bit positions changes.

## Precision rule

With **$N$ fractional bits**, the smallest representable difference is $2^{-N}$. Any value falling between two grid points rounds. This is **uniform absolute precision** — the gap is the same everywhere on the number line, unlike [[FloatingPoint|floating-point]]'s relative precision.

## Rounding makes arithmetic non-associative

[[dis-4-8-floating-point|Ch 4.8]]'s headline demonstration uses a fixed-point scheme where dividing $0.75$ by $2$ rounds the exact $0.375$ down to $0.25$:

| Computation | Sequence | Intermediate | Final | Exact |
|---|---|---|---|---|
| $(0.75 / 2) \cdot 3$ | divide first | $0.25$ | $0.75$ | $1.125$ |
| $(0.75 \cdot 3) / 2$ | multiply first | $2.25$ → rounds to $2.00$ | $1.00$ | $1.125$ |

Same operands, same operations, different results. **Order matters** under rounding — a foundational property [[FloatingPoint|floating-point]] inherits.

## When fixed-point wins over floating-point

- **Embedded / DSP / FPGA** — no FPU available; integer ALUs run fixed-point arithmetic with no extra silicon.
- **Audio sample processing** — the input domain has bounded dynamic range; fixed-point's uniform absolute precision is a feature.
- **Financial calculations** — money in cents fits perfectly in 64-bit fixed-point; floating-point's relative precision is the wrong tool ($0.10 + 0.20 \ne 0.30$ in `binary64`).
- **Q-format conventions** — `Q15` (1 sign + 15 fractional), `Q31`, etc. dominate DSP code.

## Connections

- [[FloatingPoint]] — the alternative with a moving binary point.
- [[IEEE754]] — codifies the floating-point alternative.
- [[BinaryPoint]] — the conceptual divider.
- [[UnsignedInteger]] — the place-value scheme fixed-point extends.
- [[dis-4-1-bases]] — Ch 4.1, the place-value foundation.
- [[FloatingPointPrecision]] — the shared rounding-error phenomenon (despite differing precision regimes).
- [[dis-4-8-floating-point]] — DIS Ch 4.8 source.
