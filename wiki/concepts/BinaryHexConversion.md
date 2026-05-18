---
title: "Binary ↔ Hexadecimal Conversion"
type: concept
tags: [systems, binary, data-representation, number-systems, hexadecimal]
sources: [dis-4-2-conversion]
last_updated: 2026-05-17
---

# Binary ↔ Hexadecimal Conversion

**Binary ↔ hex conversion** is the **arithmetic-free** [[BaseConversion|base-conversion]] shortcut between [[BinaryNumber|binary]] and [[HexadecimalNumber|hexadecimal]] that [[dis-4-2-conversion|DIS Ch 4.2]] derives from the identity $16 = 2^4$. Because each hex digit corresponds to **exactly four bits**, conversion in either direction is a **per-digit table lookup** — no addition, no multiplication, no division required.

## The Mapping Table

| Hex | Binary | Decimal | | Hex | Binary | Decimal |
|---|---|---|---|---|---|---|
| `0` | `0000` | 0 | | `8` | `1000` | 8 |
| `1` | `0001` | 1 | | `9` | `1001` | 9 |
| `2` | `0010` | 2 | | `A` | `1010` | 10 |
| `3` | `0011` | 3 | | `B` | `1011` | 11 |
| `4` | `0100` | 4 | | `C` | `1100` | 12 |
| `5` | `0101` | 5 | | `D` | `1101` | 13 |
| `6` | `0110` | 6 | | `E` | `1110` | 14 |
| `7` | `0111` | 7 | | `F` | `1111` | 15 |

## Hex → Binary

Substitute each hex digit with its 4-bit binary equivalent from the table. [[dis-4-2-conversion|Ch 4.2]]'s worked example:

```
0xB491 = 1011 0100 1001 0001
         B    4    9    1
```

## Binary → Hex

**Partition the bit string into groups of four from the right**, padding the leftmost group with leading zeros if needed, then table-lookup each 4-bit group:

```
1011 0100 1001 0001 → 0xB491
```

The right-to-left grouping matters: `10110100` partitions as `1011 0100` → `0xB4`, not `1 0110100` or `101 1010 0`. The least-significant bit is always the rightmost element of the rightmost group.

## Why It Works

The positional sums line up: $16^k = (2^4)^k = 2^{4k}$, so the $k$-th hex digit's place value is exactly the place value of bits $4k$ through $4k + 3$. The 4-bit group **is** the hex digit, by definition of the bases.

## Octal Analog

The same trick works for [[OctalNumber|octal]] with **groups of three** ($8 = 2^3$). Every base-$2^j$ ↔ base-$2^k$ conversion routes through binary as a per-group table lookup. Hex dominates over octal on modern hardware because byte / word widths (8, 16, 32, 64 bits) are all multiples of 4, aligning cleanly with hex's 4-bit grouping but misaligning octal's 3-bit grouping.

## Why Programmers Care

Most binary-data display in [[CLanguage|C]]-systems work is hex: pointer addresses, [[GdbExamineMemory|`x/nfu`]] memory dumps, [[Objdump|`objdump`]] disassembly, [[BasePrefix|`0x`-prefixed]] bitmask literals, struct alignment offsets. Fluency at binary-hex conversion lets you read bits directly from hex without decimal as an intermediate.

## Connections

- [[BaseConversion]] — the umbrella concept; this is route 4 (base-$2^k$ ↔ base-$2^j$).
- [[BinaryNumber]] — source/target for binary ↔ hex.
- [[HexadecimalNumber]] — source/target for binary ↔ hex.
- [[OctalNumber]] — analog via 3-bit grouping; less common on byte-aligned modern hardware.
- [[NumberBase]] — the positional-system framework.
- [[BasePrefix]] — `0x` / `0b` are the C-source handles for these literals.
- [[GdbExamineMemory]] — a canonical consumer of binary-hex fluency.
- [[BinaryRepresentation]] — the umbrella concept.
- [[dis-4-2-conversion]] — source.
