---
title: "Dive into Systems — Ch 4.2 Converting Between Bases"
type: source
tags: [systems, binary, data-representation, number-systems, base-conversion, hexadecimal, octal]
date: 2026-05-17
source_file: https://diveintosystems.org/book/C4-Binary/conversion.html
---

## Summary

[[SuzanneJMatthews|Matthews]] / [[TiaNewhall|Newhall]] / [[KevinCWebb|Webb]]'s **Ch 4.2** of *[[DiveIntoSystems]]* — the **mechanics companion** to [[dis-4-1-bases|Ch 4.1]]: takes the positional-notation framework $\sum d_i \cdot B^i$ and operationalizes it as concrete algorithms for moving between bases. Codifies four conversion routes — **base-$B$ → decimal** via direct evaluation of the place-value sum, **decimal → base-$B$** via two interchangeable methods ([[BaseConversion|powers-of-the-target-base]] subtraction or [[RepeatedDivisionMethod|repeated division]] with bottom-up remainder collection), and the **[[BinaryHexConversion|binary ↔ hex]] shortcut** that exploits $16 = 2^4$ to make conversion a per-4-bit-digit table lookup with no arithmetic. Worked examples drive each algorithm: `0b110100110 = 422` (binary → decimal); `9742₁₀ = 0x260E` (powers-of-16 method); `422 → 0b110100110` (repeated division by 2 reading even/odd parity); `0xB491 ↔ 1011 0100 1001 0001` (per-nibble table lookup).

## Key Claims

- **Base-$B$ → decimal** is **always** the direct evaluation of the place-value sum $\sum_{i=0}^{N-1} d_i \cdot B^i$. The algorithm is base-independent — only $B$ changes. Example: `0b110100110 = 256 + 128 + 32 + 4 + 2 = 422`; `0x9F = 9·16 + 15 = 159`.
- **Decimal → base-$B$ via [[BaseConversion|powers-of-target-base]]** ("how-many-of-each-power" method): list the powers of $B$ that fit into the decimal value from largest to smallest; for each power, count how many fit (in $\{0, \ldots, B-1\}$), subtract, recurse on the remainder. Worked example: $9742_{10}$ → $4096$ fits twice (remainder $1550$), $256$ fits six times (remainder $14$), $16$ fits zero times, $1$ fits fourteen times — yielding `0x260E`. Trades arithmetic for memorized powers of $B$.
- **Decimal → base-2 via [[RepeatedDivisionMethod|repeated division]]** (the no-memorization alternative): repeatedly divide the decimal value by 2; at each step the **parity of the current quotient** is the next bit (*"if the decimal value is even, the next bit should be a zero; if it's odd, the next bit should be a one"*); collect bits **right-to-left** until the quotient reaches zero. Worked example: $422 \to 211 \to 105 \to 52 \to 26 \to 13 \to 6 \to 3 \to 1 \to 0$ produces bits `0 1 1 0 0 1 0 1 1` → `0b110100110`. Generalizes to any base $B$ as **divide by $B$, collect remainders bottom-up**.
- **The two decimal-to-base methods are interchangeable** — same answer, different cognitive load. Powers-of-$B$ is faster if you already know the powers (often the case for $B=16$ where every CS student memorizes $1, 16, 256, 4096, \ldots$); repeated division wins when the powers are unfamiliar (arbitrary $B$, or large $B^k$).
- **[[BinaryHexConversion|Binary ↔ hex conversion]]** exploits $16 = 2^4$: **every hex digit corresponds to exactly four bits**, so conversion in either direction is a **per-digit table lookup with no arithmetic**. To convert hex → binary, substitute each hex digit with its 4-bit binary equivalent. To convert binary → hex, **partition the bit string into groups of four from the right**, pad the leftmost group with leading zeros if needed, then look up each 4-bit group's hex digit. Worked example: `0xB491` → `1011 0100 1001 0001` (B=1011, 4=0100, 9=1001, 1=0001) and inversely.
- **Binary ↔ octal works the same way with groups of three** ($8 = 2^3$): each octal digit is exactly three bits, partition from the right, table-lookup per nibble. This is why hex and octal are the canonical compact display forms for binary data — both are base-$2^k$, so the conversion is information-preserving and arithmetic-free.
- **Hex is preferred over octal on modern machines** because contemporary [[ComputerHardware|hardware]] is 8/16/32/64-bit aligned, all multiples of 4 — so a byte is exactly 2 hex digits, a 32-bit word is exactly 8 hex digits, etc. Octal's 3-bit grouping creates misalignment with byte boundaries.

## Key Quotes

> "Because $16 = 2^4$, each hexadecimal digit corresponds to exactly four bits." — the structural identity that makes [[BinaryHexConversion|binary ↔ hex]] a table lookup.

> "If the decimal value is even, the next bit should be a zero; if it's odd, the next bit should be a one." — the [[RepeatedDivisionMethod|repeated-division]] core recurrence for decimal → binary.

> "When converting binary to hex, partition bits into groups of four from right to left, padding with leading zeros if needed." — the [[BinaryHexConversion|partition-from-the-right]] rule.

## Connections

- [[DiveIntoSystems]] — Ch 4.2 is the **second section of Ch 4 *Binary and Data Representation***, the mechanics companion to [[dis-4-1-bases|Ch 4.1]]'s base-definitions. Where Ch 4.1 codified the **positional-system framework** as an abstraction, Ch 4.2 turns it into **executable conversion routines** — the procedural knowledge a programmer needs to read memory dumps, write hex literals, and understand compiler-emitted bit patterns.
- [[SuzanneJMatthews]] / [[TiaNewhall]] / [[KevinCWebb]] — co-authors.
- [[dis-4-1-bases]] — direct predecessor; supplies the $\sum d_i \cdot B^i$ framework Ch 4.2 instantiates as algorithms. Ch 4.1's `0b1000 = 8`, `0b10110100 = 180`, `0x23C8 = 9160` worked examples are base-$B$-to-decimal instances of Ch 4.2's first route.
- [[NumberBase]] — the framework being converted between.
- [[BinaryNumber]] / [[HexadecimalNumber]] / [[OctalNumber]] — the three base-$2^k$ representations whose pairwise conversion is the chapter's headline shortcut.
- [[BaseConversion]] — new concept page; the umbrella concept covering all four routes.
- [[BinaryHexConversion]] — new concept page; the per-nibble table-lookup shortcut.
- [[RepeatedDivisionMethod]] — new concept page; the divide-by-$B$ remainder-collection algorithm.
- [[PositionalNotation]] — new concept page; the place-value formalism that powers base-$B$-to-decimal evaluation.
- [[BasePrefix]] — Ch 4.1's `0b` / `0` / `0o` / `0x` prefixes are the source-syntax handles for the bit patterns Ch 4.2 generates and parses.
- [[BinaryRepresentation]] — the umbrella concept Ch 4.2 continues populating.
- [[ComputerHardware]] — modern 8/16/32/64-bit alignment is why hex dominates over octal as the compact display form.

## Contradictions

- None — purely additive. Ch 4.2 is the **algorithmic mechanics** behind Ch 4.1's framework; it operationalizes prior claims rather than revising any.
