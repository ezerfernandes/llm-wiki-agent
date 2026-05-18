---
title: "Dive into Systems — Ch 4.1 Number Bases and Unsigned Integers"
type: source
tags: [systems, binary, data-representation, number-systems, unsigned-integers, hexadecimal, octal]
date: 2026-05-17
source_file: https://diveintosystems.org/book/C4-Binary/bases.html
---

## Summary

[[SuzanneJMatthews|Matthews]] / [[TiaNewhall|Newhall]] / [[KevinCWebb|Webb]]'s **Ch 4.1** of *[[DiveIntoSystems]]* — **opens Ch 4 *Binary and Data Representation***, the book's first descent below [[CLanguage|C]] into how data is encoded in [[ComputerHardware|hardware]]. Codifies positional [[NumberBase|number bases]] as the unifying framework (the place-value sum $\sum d_i \cdot B^i$) and instantiates it for **decimal (base 10)**, **binary (base 2)**, and **hexadecimal (base 16)** with [[OctalNumber|octal (base 8)]] as a historical sibling. Introduces the C-source [[BasePrefix|base prefixes]] **`0b`** ([[BinaryNumber|binary]]) / **`0`** or **`0o`** ([[OctalNumber|octal]]) / **`0x`** ([[HexadecimalNumber|hexadecimal]]) and the [[UnsignedInteger|unsigned-integer]] $[0,\,2^N-1]$ range rule for an $N$-bit storage cell.

## Key Claims

- **Positional principle**: in any base $B$, an $N$-digit number is $\sum_{i=0}^{N-1} d_i \cdot B^i$ — *"the position of each digit in the number determines how important that digit is to the overall value"*. The conversion machinery is identical across bases; only $B$ changes.
- **[[BinaryNumber|Binary (base 2)]]**: digits $\{0, 1\}$; each position is a power of $2$. Example: `0b10110100 = 128 + 32 + 16 + 4 = 180`. The native form of data inside [[ComputerHardware|hardware]] — every other base is a human-readable proxy.
- **[[HexadecimalNumber|Hexadecimal (base 16)]]**: digits $\{0\text{–}9, A\text{–}F\}$ (where `A=10`, ..., `F=15`); each position is a power of $16$. Example: `0x23C8 = 2·4096 + 3·256 + 12·16 + 8 = 9160`. Because $16 = 2^4$, **one hex digit packs exactly four bits** — the reason hex dominates as the compact display form for binary data.
- **[[OctalNumber|Octal (base 8)]]**: digits $\{0\text{–}7\}$; each position is a power of $8$. Because $8 = 2^3$, **one octal digit packs exactly three bits**. Historically dominant before hex took over.
- **[[BasePrefix|C-source base prefixes]]**: a numeric literal's leading characters disambiguate its base — `0b...` is binary, `0...` (or modern `0o...`) is octal, `0x...` is hexadecimal, no prefix is decimal. The prefix is **a source-syntax convenience only**: at run time every literal is the same bit pattern in memory.
- **[[UnsignedInteger|Unsigned-integer range]]**: an $N$-bit unsigned cell stores $2^N$ distinct values, namely the non-negative integers $[0,\,2^N-1]$. Canonical instance: an 8-bit `unsigned char` holds `0`–`255` (256 patterns). Signed encodings are deferred — Ch 4.1 covers only the unsigned half.
- **Decimal-↔-base-$B$ conversion**: from base-$B$ to decimal, evaluate the place-value sum directly. From decimal to base-$B$, **divide-by-$B$ with remainders read bottom-up** (the standard algorithm restated for general $B$).

## Key Quotes

> "The position of each digit in the number determines how important that digit is to the overall value." — the positional-system thesis that makes all base conversions instances of one algorithm.

> "0b1000 = (1 × 2³) + (0 × 2²) + (0 × 2¹) + (0 × 2⁰) = 8" — the canonical binary-to-decimal worked example, mirroring decimal place-value expansion.

> "0x23C8 = (2 × 16³) + (3 × 16²) + (12 × 16¹) + (8 × 16⁰) = 9160" — the canonical hex-to-decimal worked example with the `C=12` letter-digit substitution.

> An 8-bit unsigned variable stores `0`–`255` — i.e. $2^8 = 256$ unique values, $[0, 2^N - 1]$ for $N=8$.

## Connections

- [[DiveIntoSystems]] — Ch 4.1 **opens Ch 4 *Binary and Data Representation***, the book's first chapter to leave [[CLanguage|C]] source for the **bit-level** substrate. Follows the seven-section Ch 3 *C Debugging Tools* block ([[dis-3-1-gdb]] / [[dis-3-2-gdb-commands]] / [[dis-3-3-valgrind]] / [[dis-3-4-gdb-advanced]] / [[dis-3-5-gdb-assembly]] / [[dis-3-6-gdb-pthreads]] / [[dis-3-7-summary]]) and delivers on the [[dis-0-introduction|Ch 0]] preview that *"binary representation"* is a prerequisite for explaining C arithmetic, overflow, and signed/unsigned semantics.
- [[SuzanneJMatthews]] / [[TiaNewhall]] / [[KevinCWebb]] — co-authors.
- [[BinaryRepresentation]] — the umbrella concept Ch 4.1 starts populating with bit-level mechanics. Where [[dis-0-introduction|Ch 0]] previewed *"data as bits"* abstractly, Ch 4.1 begins giving it formal arithmetic.
- [[NumberBase]] — new concept page; the positional-system framework Ch 4.1 codifies.
- [[BinaryNumber]] / [[HexadecimalNumber]] / [[OctalNumber]] — new concept pages for the three base-$2^k$ representations.
- [[UnsignedInteger]] — new concept page for the non-negative-only $[0,\,2^N-1]$ encoding.
- [[BasePrefix]] — new concept page for the `0b` / `0` / `0o` / `0x` C-source-syntax prefixes.
- [[CLanguage]] — the host language whose numeric-literal syntax Ch 4.1 extends with the [[BasePrefix|base prefixes]]; bridges to [[CPrimitiveType|primitive types]] from [[dis-1-1-getting-started|Ch 1.1]] (the `unsigned` qualifier).
- [[ComputerHardware]] — Ch 4.1 frames binary as the **native form** of data inside hardware, with hex/octal as human-readable proxies.

## Contradictions

- None — purely additive. Ch 4.1 is the **first chapter to formally treat bit patterns**, so there is nothing for it to contradict in the existing [[DiveIntoSystems]] corpus. The [[BinaryRepresentation]] page (sourced from [[dis-0-introduction|Ch 0]]'s preview) is extended in spirit, not revised.
