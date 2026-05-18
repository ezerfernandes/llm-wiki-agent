---
title: "Base Prefix (0b / 0 / 0o / 0x)"
type: concept
tags: [systems, c-language, syntax, binary, data-representation]
sources: [dis-4-1-bases]
last_updated: 2026-05-17
---

# Base Prefix (`0b` / `0` / `0o` / `0x`)

A **base prefix** is a leading-character convention on a numeric literal that tells the [[CLanguage|C]] [[CCompiler|compiler]] (or any reader) what [[NumberBase|base]] the digits should be interpreted in. Per [[dis-4-1-bases|DIS Ch 4.1]]:

| Prefix | [[NumberBase|Base]] | Digit alphabet | Example | Decimal value |
|---|---|---|---|---|
| *(none)* | 10 (decimal) | `0`–`9` | `255` | 255 |
| `0b` | 2 ([[BinaryNumber|binary]]) | `0`, `1` | `0b11111111` | 255 |
| `0` (leading zero) | 8 ([[OctalNumber|octal]]) | `0`–`7` | `0377` | 255 |
| `0o` | 8 ([[OctalNumber|octal]], modern) | `0`–`7` | `0o377` | 255 |
| `0x` | 16 ([[HexadecimalNumber|hexadecimal]]) | `0`–`9`, `A`–`F` | `0xFF` | 255 |

(Hex letters can be uppercase or lowercase: `0xFF`, `0xff`, `0xFf` all parse identically.)

## What the Prefix Is and Isn't

The prefix is a **source-syntax convenience only**. At run time, every numeric literal becomes the same bit pattern in memory — `0xFF`, `0b11111111`, `0377`, and `255` all compile to the identical 8-bit byte `1111 1111`. The prefix lets the **programmer** pick the most readable form for the value's meaning:

- `0b` for **bit-pattern intent**: bitmasks, flag combinations, hardware registers.
- `0x` for **byte-aligned values**: addresses, machine code, color codes, memory dumps.
- `0` / `0o` for **legacy octal**: Unix permission modes (`0755`), older system code.
- *no prefix* for **everyday counting**: loop bounds, array sizes, human-meaningful counts.

## The Leading-Zero Footgun

The bare `0`-prefix octal convention is a notorious [[CLanguage|C]] pitfall: `int x = 0755;` parses as octal `0755` (= decimal `493`), **not** decimal seven-hundred-fifty-five. The modern `0o` form (popularized by Python; available in some C extensions) makes the intent explicit.

## Connections

- [[NumberBase]] — what the prefix selects.
- [[BinaryNumber]] — selected by `0b`.
- [[OctalNumber]] — selected by leading `0` (or modern `0o`).
- [[HexadecimalNumber]] — selected by `0x`.
- [[UnsignedInteger]] — the value the literal denotes; same range rules regardless of prefix.
- [[CLanguage]] — the host language.
- [[CPrimitiveType]] — the integer types these literals can be stored in.
- [[dis-4-1-bases]] — source.
