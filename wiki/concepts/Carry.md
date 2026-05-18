---
title: "Carry"
type: concept
tags: [binary, arithmetic, addition, computer-systems, digital-logic]
sources: [dis-4-4-1-addition]
last_updated: 2026-05-17
---

# Carry

A **carry** is the bit (or digit, in non-binary bases) that propagates from one column-addition position to the next when the column sum exceeds the base. In [[BinaryAddition|binary addition]] (base $2$), the carry is always **$0$ or $1$** — the only multi-bit elementary sum is $1 + 1 = \mathtt{0b10}$, so no column can produce more than a single bit of carry into the next position.

Per [[dis-4-4-1-addition|Dive into Systems Ch 4.4.1]], every bit-position adder has two carry signals:

- **`CarryIn`** — the carry bit arriving from the next-lower position (or $0$ at the least-significant bit during standard addition).
- **`CarryOut`** — the carry bit produced for the next-higher position.

The two are wired in a chain: bit $i$'s `CarryOut` becomes bit $i+1$'s `CarryIn`. This **ripple-carry** structure is the canonical introductory adder layout (every CS architecture course builds it once before moving to faster carry-lookahead designs).

## Carry-in is implicit zero — but the wire exists

For ordinary $N$-bit addition, the rightmost bit's `CarryIn` is hard-wired to $0$. The reason the input *exists architecturally* at all — rather than being absent — is [[BinarySubtraction|subtraction]]: [[TwosComplement|two's-complement]] negation is *"flip the bits and add one"*, and the *add one* is delivered for free by setting `CarryIn = 1` on the same adder. *"This feature becomes critical for subtraction implementations"* ([[dis-4-4-1-addition|Ch 4.4.1]]).

## Carry-out from the MSB = silent overflow

When the most-significant-bit (MSB) adder produces `CarryOut = 1`, that bit has **nowhere to go** — there is no bit position $N$ in an $N$-bit register to receive it. Per [[dis-4-4-1-addition|Ch 4.4.1]], *"the hardware simply drops or truncates"* this bit. The visible result is the lower $N$ bits only — which is silently wrong when the true mathematical result didn't fit in $N$ bits.

This is the root mechanism of [[IntegerOverflow|integer overflow]] (for [[UnsignedInteger|unsigned]] arithmetic, MSB-carry-out *is* overflow; for [[TwosComplement|two's-complement]] arithmetic, overflow is detected by a different rule — XOR of the MSB carry-in and carry-out — formalized in subsequent Ch 4 sections).

## Decimal vs binary carry

In **decimal** addition, the carry can be any digit $0$–$9$ because the column sum is in $[0, 19]$. In **binary**, the column sum is in $[0, 3]$, so the carry is exactly $\{0, 1\}$. This is what makes binary addition operationally simpler than decimal — the per-column logic fits in an 8-row truth table.

## Carry as a CPU flag

Most [[CPU|CPU]] [[ISA|ISAs]] expose the MSB `CarryOut` as a status-register flag — x86's **CF** (carry flag) and ARM's **C** (carry flag). High-level languages don't expose this directly, but assembly programmers use it for multi-word arithmetic (`adc` *add-with-carry*) and unsigned-overflow detection.

## See also

- [[BinaryAddition]] — the algorithm carries propagate through.
- [[FullAdder]] — the per-bit primitive that takes a `CarryIn` and produces a `Sum` and a `CarryOut`.
- [[IntegerOverflow]] — the named consequence of MSB carry-out truncation.
- [[BinarySubtraction]] — why `CarryIn` exists as a wire at all.
- [[TwosComplement]] — the encoding whose *flip-and-add-one* negation recipe is delivered by `CarryIn = 1`.
- [[dis-4-4-1-addition|Dive into Systems Ch 4.4.1]] — primary source.
