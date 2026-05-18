---
title: "Two's Complement"
type: concept
tags: [systems, binary, data-representation, signed-integers, twos-complement]
sources: [dis-4-3-signed]
last_updated: 2026-05-17
---

# Two's Complement

**Two's complement** is the universal modern encoding for [[SignedInteger|signed integers]] in fixed-width binary cells. Per [[dis-4-3-signed|DIS Ch 4.3]], it reinterprets the [[MostSignificantBit|most-significant bit]] (MSB) of an $N$-bit pattern as a place-value digit with **negative weight** $-2^{N-1}$, while the remaining $N-1$ bits keep their standard positive weights.

## The Formula

For an $N$-bit pattern $d_{N-1} d_{N-2} \cdots d_1 d_0$:

$$\text{value} \;=\; -(d_{N-1} \cdot 2^{N-1}) \;+\; \sum_{i=0}^{N-2} d_i \cdot 2^i$$

The MSB $d_{N-1}$ thus doubles as the [[SignBit|sign bit]]: when $d_{N-1} = 0$ the term vanishes and the remaining sum is non-negative; when $d_{N-1} = 1$ it contributes the large negative number $-2^{N-1}$ which dominates the positive remainder.

## Range

An $N$-bit two's-complement cell holds the **asymmetric** range:

$$[-2^{N-1},\;2^{N-1} - 1]$$

| $N$ | Min | Max | Note |
|---|---|---|---|
| 4 | `-8` | `+7` | Ch 4.3's worked example |
| 8 | `-128` | `+127` | C `signed char` |
| 16 | `-32 768` | `+32 767` | C `short` |
| 32 | `-2 147 483 648` | `+2 147 483 647` | C `int` |
| 64 | $-2^{63}$ | $2^{63} - 1$ | C `long` (on LP64) |

**One more negative than positive** — no `+2^{N-1}` representation exists, but $-2^{N-1}$ does (the pattern `1000…0`).

## Negation: Flip All Bits and Add One

The practical negation recipe: **flip every bit, then add 1**.

> Ch 4.3 worked example: negating `13` (8-bit).
>
> | Step | Bits | Decimal |
> |---|---|---|
> | Start: 13 | `00001101` | +13 |
> | Flip all bits | `11110010` | (intermediate) |
> | Add 1 | `11110011` | **−13** |

This works because *flipping all bits* computes the [[OnesComplement|one's complement]] (which equals $2^N - 1 - x$), and *adding 1* gives $2^N - x$ — exactly the bit pattern that, interpreted as two's complement, evaluates to $-x$.

## Unique Zero

Unlike [[SignMagnitude|sign-magnitude]], two's complement has **exactly one** zero representation — the all-zeros pattern `0b00…0`. The pattern `0b10…0` (MSB=1, rest=0) is **not** `−0`; it's the unique most-negative value $-2^{N-1}$. This single-zero property is what makes two's complement *the* hardware choice — adders and comparators don't need special-case logic for negative zero, and ordinary unsigned binary addition produces the correct signed-result bit pattern.

## Sign Extension

When widening a two's-complement value from $N$ bits to $M > N$ bits, **replicate the MSB** $M - N$ times into the new high-order positions. See [[SignExtension]] for the full treatment.

## Why It Works

The arithmetic insight: in modulo-$2^N$ arithmetic, $-x \equiv 2^N - x \pmod{2^N}$. So the bit pattern for $-x$ is the same as for $2^N - x$. Computing $2^N - x$ via "flip and add 1" exploits the identity $2^N - x = (2^N - 1) - x + 1 = \overline{x} + 1$ where $\overline{x}$ is the bitwise complement.

## Connections

- [[SignedInteger]] — the umbrella; two's complement is one of the two encoding schemes Ch 4.3 covers.
- [[SignMagnitude]] — the historical alternative that two's complement displaced.
- [[OnesComplement]] — the intermediate step in the flip-and-add-one negation algorithm; **not covered as a standalone scheme** by Ch 4.3.
- [[SignBit]] — the dual-role MSB.
- [[SignExtension]] — the width-widening rule.
- [[BinaryNumber]] — the underlying encoding.
- [[UnsignedInteger]] — the unsigned dual; same bit patterns under a different interpretation.
- [[CLanguage]] — every signed integer type in C uses two's complement (de facto since C99, de jure since C23).
- [[ComputerHardware]] — adopts two's complement universally because adder hardware doesn't need sign-special-casing.
- [[dis-4-3-signed]] — source.
