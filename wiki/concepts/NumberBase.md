---
title: "Number Base"
type: concept
tags: [systems, math, number-systems, data-representation]
sources: [dis-4-1-bases]
last_updated: 2026-05-17
---

# Number Base

A **number base** (or **radix**) $B$ is the size of the digit alphabet used by a **positional number system**. An $N$-digit number $d_{N-1} d_{N-2} \cdots d_1 d_0$ in base $B$ denotes the integer

$$\sum_{i=0}^{N-1} d_i \cdot B^i$$

where each digit $d_i \in \{0, 1, \ldots, B-1\}$. [[dis-4-1-bases|DIS Ch 4.1]] codifies this as the unifying framework — *"the position of each digit in the number determines how important that digit is to the overall value"* — and notes that **decimal place-value arithmetic is just the $B=10$ instance**.

## Instances in *Dive into Systems* Ch 4.1

- **Decimal**: $B = 10$, digits $\{0\text{–}9\}$. The everyday human base.
- **[[BinaryNumber|Binary]]**: $B = 2$, digits $\{0, 1\}$. The native form of data inside [[ComputerHardware|hardware]].
- **[[OctalNumber|Octal]]**: $B = 8$, digits $\{0\text{–}7\}$. One octal digit = three bits.
- **[[HexadecimalNumber|Hexadecimal]]**: $B = 16$, digits $\{0\text{–}9, A\text{–}F\}$. One hex digit = four bits.

[[BinaryNumber|Binary]], [[OctalNumber|octal]], and [[HexadecimalNumber|hexadecimal]] are all **powers of two** ($2 = 2^1$, $8 = 2^3$, $16 = 2^4$), which is why their digits pack cleanly into bit groups and why hex dominates as the compact display form for [[BinaryRepresentation|binary data]].

## Conversion Algorithms

- **From base $B$ to decimal**: evaluate the place-value sum directly.
- **From decimal to base $B$**: divide repeatedly by $B$, collect remainders, read **bottom-up**. The general form of the divide-by-2 algorithm taught for binary.

## Connections

- [[BinaryNumber]] — the $B=2$ instance.
- [[OctalNumber]] — the $B=8$ instance.
- [[HexadecimalNumber]] — the $B=16$ instance.
- [[UnsignedInteger]] — the $[0, B^N - 1]$ range rule that follows from $N$ digits in base $B$.
- [[BasePrefix]] — the [[CLanguage|C]]-source-syntax prefixes (`0b` / `0` / `0o` / `0x`) that disambiguate a numeric literal's base.
- [[BinaryRepresentation]] — the umbrella concept; binary is the [[NumberBase|base]] hardware actually uses.
- [[dis-4-1-bases]] — source.
