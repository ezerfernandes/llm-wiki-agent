---
title: "Binary Number (Base 2)"
type: concept
tags: [systems, binary, data-representation, number-systems]
sources: [dis-4-1-bases]
last_updated: 2026-05-17
---

# Binary Number (Base 2)

A **binary number** is a number expressed in base $B = 2$, using only the digits $\{0, 1\}$ (each individual digit is a **bit**). An $N$-bit binary number $b_{N-1} \cdots b_1 b_0$ denotes the integer

$$\sum_{i=0}^{N-1} b_i \cdot 2^i$$

per [[dis-4-1-bases|DIS Ch 4.1]]'s positional-system formula. Binary is the **native form of data inside [[ComputerHardware|hardware]]** — every other [[NumberBase|base]] is a human-readable proxy that gets converted to and from bit patterns at the source-code / display boundary.

## Worked Examples from Ch 4.1

- `0b1000 = (1 × 2³) + (0 × 2²) + (0 × 2¹) + (0 × 2⁰) = 8`
- `0b10110100 = 128 + 32 + 16 + 4 = 180` — the place values that turn on are $2^7$, $2^5$, $2^4$, $2^2$.

The [[BasePrefix|`0b` prefix]] is the [[CLanguage|C]]-source convention for marking a numeric literal as binary; without it, `1000` means **one thousand** in decimal, not **eight** in binary.

## Why Base 2

Binary maps directly onto two-state physical phenomena (voltage high/low, current on/off, magnetic north/south) — every digital circuit is fundamentally a two-state device. The cost is verbosity: an 8-bit value needs 8 binary digits vs. 3 decimal vs. 2 hex, which is why [[HexadecimalNumber|hexadecimal]] is preferred for display of binary data.

## Connections

- [[NumberBase]] — binary is the $B = 2$ instance.
- [[HexadecimalNumber]] — base-$2^4$ proxy; one hex digit packs four bits.
- [[OctalNumber]] — base-$2^3$ proxy; one octal digit packs three bits.
- [[UnsignedInteger]] — an $N$-bit unsigned binary number ranges over $[0,\,2^N - 1]$.
- [[BasePrefix]] — `0b` is the C-source prefix.
- [[BinaryRepresentation]] — the broader concept that includes signed encodings, floating-point, characters, instructions.
- [[ComputerHardware]] — the substrate where binary is native.
- [[dis-4-1-bases]] — source.
