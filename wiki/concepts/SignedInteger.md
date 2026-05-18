---
title: "Signed Integer"
type: concept
tags: [systems, binary, data-representation, signed-integers, c-language, integer-types]
sources: [dis-4-3-signed]
last_updated: 2026-05-17
---

# Signed Integer

A **signed integer** is a fixed-width binary encoding that represents both **non-negative and negative** integers — the foil to [[UnsignedInteger|unsigned integers]] which encode only the non-negative range. Per [[dis-4-3-signed|DIS Ch 4.3]], signed integers are an **interpretation layer** over plain [[BinaryNumber|binary]] bit patterns: the same $N$-bit cell that stores an unsigned $[0,\,2^N - 1]$ can be reinterpreted under a signed encoding to span roughly half the range below zero and half above.

## Encoding Schemes

Ch 4.3 covers two historical schemes; modern hardware uses only the second:

| Scheme | Status | High-order bit role | Negation | Zero |
|---|---|---|---|---|
| [[SignMagnitude\|Sign-magnitude]] | **historical only** (*"no modern systems use signed magnitude"*) | pure [[SignBit\|sign flag]] (0 = +, 1 = −) | flip the MSB | **two zeros** (`+0` and `−0`) |
| [[TwosComplement\|Two's complement]] | **universal modern standard** | place-value digit with **negative weight** $-2^{N-1}$ | flip all bits and add one | unique zero |

[[OnesComplement|One's complement]] — the third historical scheme — is **not covered by Ch 4.3**; the text jumps directly from sign-magnitude to two's complement.

## Range

Both schemes encode roughly $[-2^{N-1},\,2^{N-1}-1]$ in $N$ bits, but only two's complement makes this range exact:

| Bit width $N$ | [[TwosComplement\|Two's-complement]] range $[-2^{N-1},\,2^{N-1}-1]$ |
|---|---|
| 8 | `-128` to `+127` |
| 16 | `-32 768` to `+32 767` |
| 32 | `-2 147 483 648` to `+2 147 483 647` |
| 64 | `-9 223 372 036 854 775 808` to `+9 223 372 036 854 775 807` |

The range is **asymmetric** — one more negative value than positive (no `+2^{N-1}` representation). 4-bit example: $[-8, +7]$.

## Relation to C

In [[CLanguage|C]], every integer [[CPrimitiveType|primitive type]] is signed **by default** (`char` is implementation-defined; `short`, `int`, `long` are signed). The `signed` qualifier is rarely written explicitly because it's the default. The `unsigned` qualifier flips to the [[UnsignedInteger|unsigned encoding]]. Two's-complement representation has been *de facto* required since C99 and *de jure* required since C23.

## Why Signed Integers Need an Encoding at All

[[BinaryNumber|Binary]] place-value notation $\sum d_i \cdot B^i$ naturally represents only non-negative integers — there's no place-value position for a "minus sign." Signed encodings solve this by either reserving a bit as a sign flag ([[SignMagnitude|sign-magnitude]]) or reinterpreting the high-order bit's weight as negative ([[TwosComplement|two's complement]]). Both fit *N* bits worth of information into 2^N distinct patterns; they differ only in **which patterns mean which integers**.

## Connections

- [[UnsignedInteger]] — the non-signed dual; same bit patterns, different interpretation.
- [[TwosComplement]] — the modern universal scheme.
- [[SignMagnitude]] — the historical predecessor.
- [[SignBit]] — the most-significant-bit convention used by both schemes.
- [[SignExtension]] — the width-widening rule that preserves signed values across bit widths.
- [[BinaryNumber]] — the underlying encoding signed integers reinterpret.
- [[CPrimitiveType]] — where `signed` / `unsigned` qualifiers live.
- [[CLanguage]] — host language.
- [[dis-4-3-signed]] — source.
- [[dis-4-1-bases]] — the unsigned-only predecessor that deferred signed encodings to this chapter.
