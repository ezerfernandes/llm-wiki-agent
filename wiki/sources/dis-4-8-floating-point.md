---
title: "Dive into Systems — Ch 4.8 Real Numbers in Binary"
type: source
tags: [book, textbook, dive-into-systems, ch-4, binary-representation, floating-point]
date: 2026-05-17
source_file: https://diveintosystems.org/book/C4-Binary/floating_point.html
---

## Summary

[[SuzanneJMatthews|Matthews]] / [[TiaNewhall|Newhall]] / [[KevinCWebb|Webb]]'s **Ch 4.8** of *[[DiveIntoSystems]]* — extends Ch 4's binary-representation arc from integers ([[dis-4-1-bases|Ch 4.1]]–[[dis-4-7-byte-order|Ch 4.7]]) to **real numbers**. Opens with the fundamental impossibility result: *"for any binary encoding of real numbers, there exist values that cannot be represented exactly"* — integers are countably infinite, reals are uncountable, so any fixed-bit encoding loses precision. Surveys two encodings: **[[FixedPoint|fixed-point]]** (extends unsigned-integer place-value to negative powers of 2 after a fixed binary point) and **[[FloatingPoint|floating-point]]** under the **[[IEEE754|IEEE 754]]** standard (sign / exponent / significand split with a movable point). Both schemes round, and the chapter's headline payoff is the **non-associativity** of rounded arithmetic ($(0.75 / 2) \cdot 3 \ne (0.75 \cdot 3) / 2$ under truncation) with two real-world catastrophes — the **1991 Patriot missile** failure and the **1996 Ariane 5** explosion. **45th ingested chapter; closes Ch 4 *Binary and Data Representation* fully.**

## Key Claims

- **Exact representation is impossible.** *"For any binary encoding of real numbers, there exist values that cannot be represented exactly."* Integers form a countably infinite set; reals are uncountable; finite-width binary encoding cannot bridge the gap.
- **[[FixedPoint|Fixed-point]] places a binary point at a predetermined bit position.** Bits left of the point use positive powers $2^k$; bits right of the point use negative powers $2^{-k}$. Example: `0b000101.10` = $1 \cdot 2^2 + 1 \cdot 2^0 + 1 \cdot 2^{-1} = 5.5$.
- **Fixed-point precision is bounded by $2^{-N}$** where $N$ is the count of fractional bits. Values finer than $2^{-N}$ round to the nearest representable grid point.
- **Rounding makes arithmetic non-associative.** Under an 8-bit fixed-point scheme, $(0.75 / 2) \cdot 3$ rounds to $0.75$ while $(0.75 \cdot 3) / 2$ rounds to $1.00$, though the exact answer is $1.125$ in both cases. **Operation order matters under rounding.**
- **[[IEEE754|IEEE 754]] 32-bit floating-point** partitions bits into three fields: **[[SignBit|sign]]** (1 bit, `0`=positive / `1`=negative), **[[Exponent|exponent]]** (8 bits, biased), **[[Mantissa|significand / mantissa]]** (23 bits, with an implicit leading `1`).
- **The exponent uses bias-127.** *"The significand gets multiplied by $2^{\text{exponent} - 127}$, where the 127 is a bias"* — this lets the same 8-bit field encode both very large positive exponents and very small (negative) ones, while keeping the stored field unsigned.
- **The significand's fractional bits work like fixed-point.** *"The fractional portion behaves like the fixed-point representation."* With the implicit leading 1, a stored fraction of `.10000…` denotes $1.5$, `.11000…` denotes $1.75$, etc.
- **Worked example:** `0b11000001101101000000000000000000` decodes to $-22.5$ — sign bit `1` (negative), exponent field decoded to factor $2^{16}$ (wiki note: the precise exponent walk-through in the textbook recovers the $\times 2^4$ scale; verify against the source), significand $1.40625$, product $-22.5$.
- **Floating-point inherits fixed-point's rounding pathologies.** *"Like fixed-point, rounding problems similarly affect floating-point encodings."* The same non-associativity that bites fixed-point bites floats — only with the scale factor moving with the value.
- **Two real-world rounding catastrophes:**
  - **1991 Patriot missile system** — accumulated time-tracking rounding error caused the system to *"fail to intercept an Iraqi missile,"* killing 28 U.S. soldiers in Dhahran.
  - **1996 Ariane 5 rocket** — *"exploded 39 seconds after taking off"* when a 64-bit floating-point value was converted to a 16-bit signed integer and overflowed, triggering the self-destruct sequence.

## Key Quotes

> "For any binary encoding of real numbers, there exist values that cannot be represented exactly." — opening impossibility claim

> "The significand gets multiplied by $2^{\text{exponent} - 127}$, where the 127 is a bias." — biased-exponent rule for IEEE 754 32-bit

> "The fractional portion behaves like the fixed-point representation." — significand interpretation

> "Like fixed-point, rounding problems similarly affect floating-point encodings." — connects the two schemes via shared failure mode

> "[The Ariane 5] exploded 39 seconds after taking off [when] converting a floating-point value to integer caused overflow." — real-world consequence

## Connections

- [[DiveIntoSystems]] — Ch 4.8 of the book; **45th ingested chapter**; closes Ch 4 *Binary and Data Representation* together with [[dis-4-7-byte-order|Ch 4.7]].
- [[SuzanneJMatthews]] / [[TiaNewhall]] / [[KevinCWebb]] — authors.
- [[dis-4-1-bases]] — Ch 4.1, the positional-notation $\sum d_i \cdot B^i$ framework Ch 4.8 extends to negative exponents.
- [[dis-4-3-signed]] — Ch 4.3, the sign-bit convention reused here for [[FloatingPoint|floats]] (top bit = sign).
- [[dis-4-5-overflow]] — Ch 4.5; the **Ariane 5** failure cited here is a [[IntegerOverflow|float-to-int overflow]] — same overflow mechanism Ch 4.5 codified for integers.
- [[FloatingPoint]] — the encoding scheme this chapter introduces.
- [[IEEE754]] — the dominant binary floating-point standard.
- [[FixedPoint]] — the simpler alternative encoding shown first.
- [[Mantissa]] / [[Exponent]] / [[SignBit]] — the three IEEE 754 fields.
- [[FloatingPointPrecision]] — the rounding-error phenomenon that produced the Patriot / Ariane catastrophes.
- [[BinaryRepresentation]] — the umbrella that this chapter completes for real numbers.
- [[Patriot]] / [[Ariane5]] — the two cited engineering disasters.

## Contradictions

None within the corpus. Complements [[dis-4-5-overflow|Ch 4.5]]'s integer-overflow examples with a **float-to-int conversion overflow** (Ariane 5) — same root mechanism, different operand type.

## Scope Notes

The textbook section deliberately **omits** several IEEE 754 details that a full treatment usually covers:
- **64-bit double precision** (`binary64`) is not discussed — only 32-bit `binary32`.
- **Denormalized / subnormal numbers** (exponent field = 0, no implicit leading 1) are not covered.
- **Special values** — `+0` / `-0`, $\pm\infty$, `NaN` (quiet / signaling) — are not discussed.
- **Normalization procedure** (shifting until the significand falls in $[1, 2)$) is implied by the implicit-leading-1 rule but not walked through.
- **Rounding modes** (round-to-nearest-even, round-toward-zero, round-toward-$\pm\infty$) are not enumerated.
- **Machine epsilon** $\epsilon \approx 1.19 \times 10^{-7}$ (binary32) is not named.

The wiki pages flag each of these as wiki-only deepenings beyond the chapter's scope.
