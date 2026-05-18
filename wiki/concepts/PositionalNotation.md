---
title: "Positional Notation"
type: concept
tags: [systems, math, number-systems, data-representation]
sources: [dis-4-2-conversion, dis-4-1-bases]
last_updated: 2026-05-17
---

# Positional Notation

**Positional notation** is the numerical-representation principle that **a digit's contribution to the overall value depends on its position** within the numeral. An $N$-digit number $d_{N-1} d_{N-2} \cdots d_1 d_0$ in [[NumberBase|base]] $B$ denotes

$$\sum_{i=0}^{N-1} d_i \cdot B^i$$

where digit $d_i$ at position $i$ contributes $d_i \cdot B^i$ to the total. [[dis-4-1-bases|DIS Ch 4.1]] codifies this as the unifying framework — *"the position of each digit in the number determines how important that digit is to the overall value"* — and [[dis-4-2-conversion|Ch 4.2]] operationalizes it as the **base-$B$ → decimal** conversion route.

## Read-out Convention

The rightmost digit is **position 0** (the **least significant**), and indices increase leftward. The leftmost digit is **position $N-1$** (the **most significant**). This convention is universal across [[BinaryNumber|binary]], [[OctalNumber|octal]], decimal, and [[HexadecimalNumber|hex]] — only the base $B$ changes.

## Worked Instances (Ch 4.1 / Ch 4.2)

- **Decimal** ($B = 10$): $3047 = 3 \cdot 10^3 + 0 \cdot 10^2 + 4 \cdot 10^1 + 7 \cdot 10^0$.
- **Binary** ($B = 2$): `0b1000` $= 1 \cdot 2^3 + 0 \cdot 2^2 + 0 \cdot 2^1 + 0 \cdot 2^0 = 8$.
- **Binary** ($B = 2$): `0b10110100` $= 2^7 + 2^5 + 2^4 + 2^2 = 128 + 32 + 16 + 4 = 180$.
- **Binary** ($B = 2$): `0b110100110` $= 2^8 + 2^7 + 2^5 + 2^2 + 2^1 = 422$.
- **Hex** ($B = 16$): `0x23C8` $= 2 \cdot 16^3 + 3 \cdot 16^2 + 12 \cdot 16^1 + 8 \cdot 16^0 = 9160$.

The substitution `C = 12` in the hex example exploits the digit-alphabet extension $\{0\text{–}9, A\text{–}F\}$ that hex needs because it has 16 digits but Arabic numerals supply only 10.

## Contrast: Sign-Value / Tally Systems

Positional notation contrasts with **sign-value systems** (Roman numerals: I, V, X, L, C, D, M — where `IV` means "5 minus 1" by symbol-order convention) and **tally systems** (where each mark stands for one unit). Positional notation's headline advantage is **compactness**: $N$ digits in base $B$ represent up to $B^N$ distinct values, growing exponentially with width — whereas tally and sign-value systems grow linearly or near-linearly.

## Why It Powers Base Conversion

Because every positional numeral is **literally** $\sum d_i \cdot B^i$, [[BaseConversion|base conversion]] from base-$B$ to decimal is **just evaluating the sum**. The algorithm is base-independent — only $B$ and the digit set change. [[dis-4-2-conversion|Ch 4.2]] makes this the first of its four conversion routes; the other three (powers-of-target-base, [[RepeatedDivisionMethod|repeated division]], [[BinaryHexConversion|per-group table lookup]]) all invert this fundamental relation in different ways.

## Connections

- [[NumberBase]] — positional notation is the formalism; a [[NumberBase|number base]] is its parameter $B$.
- [[BaseConversion]] — direct sum evaluation is route 1.
- [[BinaryNumber]] / [[OctalNumber]] / [[HexadecimalNumber]] — the three base-$2^k$ instances most relevant to systems.
- [[RepeatedDivisionMethod]] — the inverse algorithm (decimal → base-$B$ via remainders).
- [[BinaryHexConversion]] — the base-$2^k$ shortcut that exploits aligned digit groupings.
- [[UnsignedInteger]] — the $[0, B^N - 1]$ range rule follows from the positional sum's maximum.
- [[BinaryRepresentation]] — the umbrella concept.
- [[dis-4-1-bases]] — supplies the framework definition.
- [[dis-4-2-conversion]] — source for conversion algorithms.
