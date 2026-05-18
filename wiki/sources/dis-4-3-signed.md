---
title: "Dive into Systems — Ch 4.3 Signed Binary Integers"
type: source
tags: [systems, binary, data-representation, signed-integers, twos-complement, c-language]
date: 2026-05-17
source_file: https://diveintosystems.org/book/C4-Binary/signed.html
---

## Summary

Ch 4.3 of *[[DiveIntoSystems]]* — the **signed-encoding** extension of [[dis-4-1-bases|Ch 4.1]]'s unsigned-only treatment. Codifies the two historical schemes for representing negative integers in fixed-width binary cells: [[SignMagnitude|sign-magnitude]] (presented as historical context only — *"no modern systems use signed magnitude"*) and [[TwosComplement|two's complement]] (the modern universal standard). Introduces the [[SignBit|sign bit]] / most-significant-bit convention, the **flip-all-bits-and-add-one** negation algorithm, the asymmetric range $[-2^{N-1},\,2^{N-1}-1]$, and the [[SignExtension|sign-extension]] rule for widening signed values across bit widths. **One's complement is not covered** — the chapter jumps directly from sign-magnitude to two's complement.

## Key Claims

- **Sign-magnitude** reserves the [[MostSignificantBit|high-order bit]] purely as a sign indicator (0 = non-negative, 1 = negative); the remaining $N-1$ bits hold the absolute magnitude. Negation is *"simply flip the most significant bit to change its sign."*
- **Sign-magnitude has two zeros** — e.g. in 4 bits, `0b0000 = +0` and `0b1000 = -0`. This duplicate-zero pathology *"complicates hardware design"* and is the reason *"no modern systems use signed magnitude."*
- **Two's complement** reinterprets the most-significant bit as contributing **negatively** to the value: for an $N$-bit pattern $d_{N-1}\cdots d_0$, the encoded integer is $-(d_{N-1} \cdot 2^{N-1}) + \sum_{i=0}^{N-2} d_i \cdot 2^i$.
- **Two's complement has a unique zero** — `0b0000…0` is the only zero pattern, eliminating the sign-magnitude pathology.
- **Two's complement range is asymmetric** — an $N$-bit cell holds $[-2^{N-1},\,2^{N-1}-1]$. 4-bit example: `-8` to `+7` — one more negative value than positive (no `+8` representation).
- **Negation algorithm**: *"flip all the bits and add one."* Example: negating 13 = `0b00001101` → flip to `0b11110010` → add 1 → `0b11110011` = −13.
- **Sign extension** widens a signed value to more bits by **replicating the high-order bit** — non-negative numbers prepend zeros, negative numbers prepend ones. This preserves both sign and magnitude across width changes.

## Key Quotes

> "no modern systems use signed magnitude" — Ch 4.3, on why sign-magnitude is historical curiosity only.

> "flip all the bits and add one" — Ch 4.3's practical [[TwosComplement|two's-complement]] negation recipe.

> "[the most significant bit] contributes negatively to the overall value" — Ch 4.3, the conceptual definition of two's complement as a place-value system where the top digit's weight is $-2^{N-1}$ instead of $+2^{N-1}$.

## Connections

- [[DiveIntoSystems]] — host textbook; Ch 4.3 is the **third section** of Ch 4 *Binary and Data Representation*, the signed-encoding companion to [[dis-4-1-bases|Ch 4.1]]'s unsigned-only treatment.
- [[SuzanneJMatthews]] / [[TiaNewhall]] / [[KevinCWebb]] — authors.
- [[dis-4-1-bases]] — direct predecessor (Ch 4.1); this chapter is **explicit follow-through** on Ch 4.1's deferral *"signed encodings deferred to subsequent Ch 4 sections."*
- [[dis-4-2-conversion]] — sibling (Ch 4.2); shares the place-value framework, extends to signed bit patterns.
- [[UnsignedInteger]] — the foil; Ch 4.3's signed encodings are the alternative interpretation of the same bit patterns.
- [[BinaryNumber]] — the underlying encoding; signed integers are an *interpretation layer* over plain binary.
- [[BinaryRepresentation]] — umbrella concept.
- [[SignedInteger]] — the umbrella for what this chapter covers.
- [[TwosComplement]] — the headline modern standard.
- [[SignMagnitude]] — the historical contrast.
- [[SignBit]] — the most-significant-bit convention shared by both schemes (with different semantics).
- [[SignExtension]] — the width-widening rule.
- [[CLanguage]] — host language; the `signed` qualifier on integer [[CPrimitiveType|primitive types]] selects two's complement.
- [[ComputerHardware]] — the consumer; the single-zero property of two's complement is why hardware adders work without a separate sign check.

## Contradictions

None — Ch 4.3 is purely additive over [[dis-4-1-bases|Ch 4.1]] and [[dis-4-2-conversion|Ch 4.2]]. The signed encodings layer on the same bit patterns Ch 4.1 introduced; the place-value framework $\sum d_i \cdot B^i$ generalizes via the negative-weight high-order bit.

## What's Deferred

- **One's complement** — explicitly **not covered** by this chapter; the text jumps from sign-magnitude directly to two's complement without the third historical scheme.
- **Signed overflow** — the wraparound behaviour at the `+2^{N-1}-1 → -2^{N-1}` boundary is named as a consequence but full overflow / arithmetic treatment deferred to later Ch 4 sections.
- **Mixed signed/unsigned C arithmetic** — the *"usual arithmetic conversions"* footgun named in [[UnsignedInteger]] is not yet treated here.
