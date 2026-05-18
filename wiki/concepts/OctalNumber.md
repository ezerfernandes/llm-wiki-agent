---
title: "Octal Number (Base 8)"
type: concept
tags: [systems, binary, data-representation, number-systems]
sources: [dis-4-1-bases]
last_updated: 2026-05-17
---

# Octal Number (Base 8)

An **octal number** is a number expressed in base $B = 8$, using the eight digits $\{0, 1, 2, 3, 4, 5, 6, 7\}$. An $N$-digit octal number denotes

$$\sum_{i=0}^{N-1} d_i \cdot 8^i$$

per [[dis-4-1-bases|DIS Ch 4.1]]'s positional-system formula.

## Why $2^3$

Because $8 = 2^3$, **one octal digit packs exactly three bits**. The mapping:

| Octal | Binary |
|---|---|
| `0` | `000` |
| `1` | `001` |
| `2` | `010` |
| `3` | `011` |
| `4` | `100` |
| `5` | `101` |
| `6` | `110` |
| `7` | `111` |

This made octal the dominant compact form for displaying binary data on machines whose word width was a multiple of three bits (e.g. PDP-8, PDP-11). Modern 8 / 16 / 32 / 64-bit machines align cleanly on 4-bit boundaries, so [[HexadecimalNumber|hexadecimal]] (base 16) has largely displaced octal.

## Surviving Uses

- **Unix file permissions**: `chmod 755 file` packs three `rwx` triples into one octal digit each (`7 = 111 = rwx`, `5 = 101 = r-x`).
- **C numeric literals with a leading `0`**: `0755` parses as octal `755` (= decimal 493), a notorious footgun for programmers who think they wrote decimal seven-hundred-fifty-five.
- **Legacy file-format dumps** and ancient documentation.

## Connections

- [[NumberBase]] — octal is the $B = 8$ instance.
- [[BinaryNumber]] — octal displays 3 bits per digit.
- [[HexadecimalNumber]] — the $B = 2^4$ successor that mostly displaced octal.
- [[BasePrefix]] — leading `0` (or modern `0o`) is the [[CLanguage|C]]-source prefix (e.g. `0755` or `0o755`).
- [[BinaryRepresentation]] — octal is one of the human-readable proxies.
- [[dis-4-1-bases]] — source.
