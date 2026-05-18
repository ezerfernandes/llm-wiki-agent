---
title: "Base Conversion"
type: concept
tags: [systems, math, number-systems, data-representation, algorithm]
sources: [dis-4-2-conversion]
last_updated: 2026-05-17
---

# Base Conversion

**Base conversion** is the procedure for re-expressing the same integer value in a different [[NumberBase|positional number system]]. [[dis-4-2-conversion|DIS Ch 4.2]] codifies four conversion routes that together cover every pairwise transformation in the [[BinaryNumber|binary]] / decimal / [[OctalNumber|octal]] / [[HexadecimalNumber|hex]] cluster.

## The Four Routes

### 1. Base-$B$ → decimal — direct place-value sum

Evaluate $\sum_{i=0}^{N-1} d_i \cdot B^i$ directly. Works for any source base. Examples from Ch 4.2:

- `0b110100110 = 256 + 128 + 32 + 4 + 2 = 422`
- `0x9F = 9·16 + 15 = 159`

### 2. Decimal → base-$B$ — powers-of-target-base method

List the powers of $B$ ($1, B, B^2, B^3, \ldots$) that fit into the decimal value, working from largest to smallest. For each power, count how many fit (a digit in $\{0, \ldots, B-1\}$), subtract, recurse on the remainder. Worked example from Ch 4.2: $9742_{10}$ → $4096$ fits twice ($r = 1550$), $256$ fits six times ($r = 14$), $16$ fits zero times, $1$ fits fourteen times (`E`) → `0x260E`.

### 3. Decimal → base-$B$ — [[RepeatedDivisionMethod|repeated division]]

Divide the decimal value by $B$ repeatedly; at each step the **remainder** is the next digit. Read digits **bottom-up** (right-to-left in standard place-value order). For $B = 2$ this simplifies to: *"if the value is even, the next bit is 0; if odd, the next bit is 1."*

### 4. Base-$2^k$ ↔ base-$2^j$ — [[BinaryHexConversion|per-group table lookup]]

When source and target bases are both powers of 2, conversion is a **table lookup with no arithmetic**: route through binary if needed, then partition the bit string into groups of $\log_2(\text{base})$ bits and translate each group.

## Method Trade-offs

[[dis-4-2-conversion|Ch 4.2]] presents methods 2 and 3 as **interchangeable** — same answer, different cognitive load:

- **Powers-of-$B$** is faster *when you already know the powers* — typical for $B = 16$ (every CS student memorizes $1, 16, 256, 4096, 65536, \ldots$).
- **Repeated division** wins *when the powers are unfamiliar* — arbitrary $B$, or large $B^k$ that you'd otherwise need to recompute.

For base-$2^k$ ↔ base-$2^j$, route 4 dominates: it's arithmetic-free and information-preserving.

## Why It Matters

A systems programmer reads conversion outputs constantly — hex pointer addresses, binary bitmask literals, octal Unix permissions, memory-dump inspection in [[GdbExamineMemory|`x/nfu`]]. Ch 4.2 is the procedural knowledge that turns Ch 4.1's positional framework into executable mental arithmetic.

## Connections

- [[NumberBase]] — the framework being converted between.
- [[PositionalNotation]] — the place-value formalism powering route 1.
- [[RepeatedDivisionMethod]] — the divide-by-$B$ algorithm (route 3).
- [[BinaryHexConversion]] — the base-$2^k$ table-lookup shortcut (route 4).
- [[BinaryNumber]] / [[OctalNumber]] / [[HexadecimalNumber]] — the three base-$2^k$ instances most commonly converted.
- [[BasePrefix]] — `0b` / `0` / `0o` / `0x` are the source-syntax handles for the bit patterns conversion produces and consumes.
- [[BinaryRepresentation]] — the umbrella concept.
- [[dis-4-1-bases]] — supplies the positional-system framework.
- [[dis-4-2-conversion]] — source.
