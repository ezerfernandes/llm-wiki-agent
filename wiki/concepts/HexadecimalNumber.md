---
title: "Hexadecimal Number (Base 16)"
type: concept
tags: [systems, binary, data-representation, number-systems, hexadecimal]
sources: [dis-4-1-bases]
last_updated: 2026-05-17
---

# Hexadecimal Number (Base 16)

A **hexadecimal number** is a number expressed in base $B = 16$, using the sixteen digits $\{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F\}$, where the letters denote $A = 10, B = 11, C = 12, D = 13, E = 14, F = 15$. An $N$-digit hex number denotes

$$\sum_{i=0}^{N-1} d_i \cdot 16^i$$

per [[dis-4-1-bases|DIS Ch 4.1]]'s positional-system formula.

## Worked Example from Ch 4.1

`0x23C8 = (2 × 16³) + (3 × 16²) + (12 × 16¹) + (8 × 16⁰) = 8192 + 768 + 192 + 8 = 9160`

Note the letter-digit substitution `C = 12` — a routine step when evaluating hex literals by hand.

## Why Hex Dominates for Binary Display

Because $16 = 2^4$, **one hexadecimal digit packs exactly four bits** (one **nibble**). The mapping is fixed and table-lookup-fast:

| Hex | Binary | Hex | Binary |
|---|---|---|---|
| `0` | `0000` | `8` | `1000` |
| `1` | `0001` | `9` | `1001` |
| `2` | `0010` | `A` | `1010` |
| `3` | `0011` | `B` | `1011` |
| `4` | `0100` | `C` | `1100` |
| `5` | `0101` | `D` | `1101` |
| `6` | `0110` | `E` | `1110` |
| `7` | `0111` | `F` | `1111` |

This makes hex the compact display form of choice for [[BinaryRepresentation|binary data]] — memory dumps, machine code, pointer addresses, color codes, [[GdbExamineMemory|`x/nfu`]] output all use hex.

## Connections

- [[NumberBase]] — hex is the $B = 16$ instance.
- [[BinaryNumber]] — hex displays 4 bits per digit; the canonical compact form.
- [[OctalNumber]] — base-$2^3$ sibling; less common today.
- [[BasePrefix]] — `0x` is the [[CLanguage|C]]-source prefix (e.g. `0x23C8`).
- [[UnsignedInteger]] — `0xFF == 255` is the canonical 8-bit unsigned max example.
- [[BinaryRepresentation]] — hex is the human-readable proxy.
- [[dis-4-1-bases]] — source.
