---
title: "Unsigned Integer"
type: concept
tags: [systems, binary, data-representation, c-language, integer-types]
sources: [dis-4-1-bases]
last_updated: 2026-05-17
---

# Unsigned Integer

An **unsigned integer** is a non-negative integer stored as a plain [[BinaryNumber|binary]] place-value pattern, with no bit reserved for sign. Per [[dis-4-1-bases|DIS Ch 4.1]], an $N$-bit unsigned cell stores **$2^N$ distinct values** — the non-negative integers $[0,\,2^N - 1]$.

## The Range Formula

| Bit width $N$ | Distinct values $2^N$ | Range $[0, 2^N - 1]$ |
|---|---|---|
| 8 | 256 | `0`–`255` |
| 16 | 65 536 | `0`–`65 535` |
| 32 | 4 294 967 296 | `0`–`4 294 967 295` |
| 64 | $\sim 1.8 \cdot 10^{19}$ | `0`–`18 446 744 073 709 551 615` |

The 8-bit case is Ch 4.1's canonical worked example: an `unsigned char` holds exactly the 256 bit-patterns `0b00000000`–`0b11111111`, corresponding to decimal `0`–`255` and hex `0x00`–`0xFF`.

## Relation to C

In [[CLanguage|C]], the `unsigned` qualifier on any integer [[CPrimitiveType|primitive type]] (`unsigned char`, `unsigned short`, `unsigned int`, `unsigned long`) selects the unsigned encoding. Per [[dis-1-1-getting-started|DIS Ch 1.1]]'s byte-width table the bit count $N$ is implementation-defined but typically `unsigned char = 8`, `unsigned int = 32`, `unsigned long = 64`. Mixing signed and unsigned in the same expression triggers C's **usual arithmetic conversions** — a classic bug source covered in later Ch 4 sections.

## Why Unsigned First

Ch 4.1 covers **only the unsigned encoding** because positional [[BinaryNumber|binary]] directly represents non-negative integers without modification. Signed integers (two's complement and friends) require an extra layer of interpretation deferred to subsequent Ch 4 sections.

## Connections

- [[BinaryNumber]] — the encoding scheme; the bit pattern that lives in the unsigned cell.
- [[NumberBase]] — the $[0,\,B^N - 1]$ range generalizes to any base.
- [[HexadecimalNumber]] — the convenient display form (e.g. `0xFF == 255`, `0xFFFF_FFFF == 2^32 - 1`).
- [[BinaryRepresentation]] — the umbrella concept; unsigned is the first encoding Ch 4 formalizes.
- [[CPrimitiveType]] — where the `unsigned` qualifier on `char` / `short` / `int` / `long` was introduced.
- [[CLanguage]] — the host language.
- [[dis-4-1-bases]] — source.
