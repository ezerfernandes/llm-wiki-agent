---
title: "Dive into Systems — Ch 4.4.2 Subtraction"
type: source
tags: [dive-into-systems, binary, arithmetic, subtraction, twos-complement, computer-systems]
date: 2026-05-17
source_file: https://diveintosystems.org/book/C4-Binary/arithmetic_subtraction.html
sources: [dis-4-4-2-subtraction]
last_updated: 2026-05-17
---

## Summary

**Ch 4.4.2 *Subtraction*** is the second subsection of [[dis-4-4-arithmetic|Ch 4.4 *Binary Integer Arithmetic*]] of *[[DiveIntoSystems]]* by [[SuzanneJMatthews|Matthews]] / [[TiaNewhall|Newhall]] / [[KevinCWebb|Webb]]. The chapter delivers the headline **hardware-reuse insight**: subtraction is implemented as **addition of the [[TwosComplement|two's-complement]] negation** — *"subtracting $7 - 3$ is equivalent to expressing the operation as $7 + (-3)$"* — so the existing [[dis-4-4-1-addition|Ch 4.4.1]] [[BinaryAddition|adder]] circuit serves subtraction with **no new arithmetic hardware**. The *flip all the bits and add one* [[TwosComplement|two's-complement]] negation recipe ([[dis-4-3-signed|Ch 4.3]]) splits cleanly across the adder's existing inputs: the **bit-flip** is a row of [[XOR|XOR]] gates on operand B; the **add one** is delivered for free by setting [[CarryIn|`CarryIn`]] of the least-significant-bit adder to `1` — finally cashing in the architectural hook [[dis-4-4-1-addition|Ch 4.4.1]] flagged with *"this feature becomes critical for subtraction implementations."* Two worked examples — $7 - 3$ (positive minus positive) and $7 - (-3)$ (positive minus negative) — show the same mechanism handles **all four sign combinations** without special-casing.

## Key Claims

- **Subtraction = addition of negation**: *"subtracting $7 - 3$ is equivalent to expressing the operation as $7 + (-3)$"*. The two-step procedure is (1) negate the subtrahend by [[TwosComplement|two's-complement]] (*flip all the bits and add one*), (2) add. No dedicated subtractor hardware is required.
- **Hardware reuse via [[CarryIn|`CarryIn = 1`]]**: rather than spending a separate full-bit increment circuit on the *add one* step, hardware sets the least-significant adder's [[CarryIn|`CarryIn`]] input to `1`, **folding the +1 into the existing ripple-carry addition for free**. This cashes in the [[dis-4-4-1-addition|Ch 4.4.1]] observation that `CarryIn` exists as an input *because* of subtraction (it's hard-wired to `0` for ordinary addition).
- **Bit-flip via [[XOR|XOR]] gates**: the *flip all the bits* step is implemented as a row of [[XOR|XOR]] gates on the second operand controlled by a `Subtract` mode signal — `XOR(b, 0) = b` (passthrough for addition), `XOR(b, 1) = ¬b` (flip for subtraction). The same `Subtract` signal feeds [[CarryIn|`CarryIn`]] of the LSB adder, unifying mode-switching to **one wire**.
- **[[SignedInteger|Signed-operand]] insensitivity**: the mechanism handles **all four sign combinations** (+−+, +−−, −−+, −−−) identically because [[TwosComplement|two's complement]] is the universal signed encoding and the bit-level steps don't depend on the operand interpretation — the [[dis-4-4-arithmetic|Ch 4.4]] **interpretation-invariance** principle reapplied.
- **Worked example 1 — $7 - 3$**: $7 = \mathtt{0b0111}$, $3 = \mathtt{0b0011}$. Flip $3$ to $\mathtt{0b1100}$, set `CarryIn = 1`, add to $7$: $\mathtt{0b0111} + \mathtt{0b1100} + 1 = \mathtt{0b10100}$. Truncate MSB carry-out → $\mathtt{0b0100} = 4$. **Correct.**
- **Worked example 2 — $7 - (-3)$**: $7 = \mathtt{0b0111}$, $-3 = \mathtt{0b1101}$. Flip $-3$ to $\mathtt{0b0010}$, set `CarryIn = 1`, add to $7$: $\mathtt{0b0111} + \mathtt{0b0010} + 1 = \mathtt{0b1010} = 10$. **Correct** — and yields a negative-looking MSB whose interpretation is in fact the positive value $10$ when the unsigned reading is intended (or the overflow/range question is deferred to a subsequent section).
- **MSB carry-out is *not* automatic overflow**: in subtraction contexts the carry-out from the high-order bit *"doesn't necessarily indicate overflow"* — its meaning differs from the addition case because of the implicit *add one* via [[CarryIn|`CarryIn`]]. The full [[IntegerOverflow|overflow]] story is deferred to a later Ch 4 section.

## Key Quotes

> "Subtracting $7 - 3$ is equivalent to expressing the operation as $7 + (-3)$." — the chapter's headline framing.

> The carry-out from the high-order bit "doesn't necessarily indicate overflow" in subtraction contexts.

## Worked Example 1: `0b0111 - 0b0011` (7 − 3)

```
   Step 1: negate 0b0011 = 3 via two's complement
     flip bits:  0b1100
     add one:    delivered by CarryIn = 1 of the LSB adder (no separate step)

   Step 2: add operand A and flipped operand B with CarryIn = 1

   carries:  1 1 1 1   (the rightmost is the injected CarryIn=1)
             0 1 1 1   (operand A = 7)
           + 1 1 0 0   (flipped operand B)
           ---------
           1 0 1 0 0   (result before MSB truncation)
             0 1 0 0   (result after MSB truncation = 4)
```

- **MSB carry-out** of `1` is truncated; the residual lower 4 bits are `0b0100 = 4`.
- The MSB carry-out **does not signal overflow here** — the correct result `4` fits in 4 bits.
- The same operation reads as $7 - 3 = 4$ in [[UnsignedInteger|unsigned]] semantics and equivalently as $7 + (-3) = 4$ in [[TwosComplement|two's-complement]] semantics (the operand bits $\mathtt{0b1100}$ being **read as** $-4$ in two's-complement — the *flip-and-add-one* of $3$ is exactly $-3$ in two's-complement bit semantics, but the *flip alone* gives $-4$; the missing $+1$ is delivered by `CarryIn = 1` on the next step, restoring `0b1100 + 1 = 0b1101 = -3` mathematically).

## Worked Example 2: `0b0111 - 0b1101` (7 − (−3))

```
   Step 1: negate 0b1101 = −3 via two's complement
     flip bits:  0b0010
     add one:    delivered by CarryIn = 1

   Step 2: add operand A and flipped operand B with CarryIn = 1

   carries:    1 1 1 1
               0 1 1 1   (operand A = 7)
             + 0 0 1 0   (flipped operand B = +2 before the +1)
             ---------
               1 0 1 0   (result = 10, no MSB carry-out)
```

- Result: $\mathtt{0b1010} = 10$ ([[UnsignedInteger|unsigned]] reading) — the correct value of $7 - (-3) = 10$.
- The bit pattern $\mathtt{0b1010}$ has [[MostSignificantBit|MSB]] $= 1$ — under a [[TwosComplement|two's-complement]] reading it would mean $-6$, **not** $10$. This worked example anticipates the [[IntegerOverflow|signed-overflow]] story: when the true mathematical result exceeds the representable two's-complement range $[-8, +7]$ for 4 bits, the bit pattern silently aliases to a wrong signed value. The full detection rule is deferred to a subsequent Ch 4 section.

## The Adder-with-Subtract-Mode circuit (implicit)

The chapter's two-step recipe describes a circuit Ch 4.4.1's [[FullAdder|full-adder]] block can implement with **one mode wire** `Subtract`:

| Stage | Wire | When `Subtract = 0` | When `Subtract = 1` |
|---|---|---|---|
| Operand B path | row of `XOR(b_i, Subtract)` | passthrough $b_i$ | flipped $\overline{b_i}$ |
| LSB adder | `CarryIn` | `0` (ordinary addition) | `1` (+1 of two's-complement) |
| Result | `Sum_{N-1..0}` | $A + B$ | $A + (\overline{B} + 1) = A - B$ |

This is the canonical **add/subtract unit** of every introductory [[DigitalLogic|digital-logic]] / [[ComputerArchitecture|computer-architecture]] textbook — *Dive into Systems* presents the recipe before naming the gates or the unit. The full [[ArithmeticLogicUnit|ALU]] generalization (adding logical AND / OR / shift modes alongside add/subtract) is for a later chapter.

## Connections

- [[DiveIntoSystems]] — Ch 4.4.2 is the second of three subsections of [[dis-4-4-arithmetic|Ch 4.4 *Binary Integer Arithmetic*]]; the corpus now stands at **40 chapters**.
- [[SuzanneJMatthews]] / [[TiaNewhall]] / [[KevinCWebb]] — co-authors.
- [[dis-4-4-arithmetic|Ch 4.4]] — parent hub page; supplies the interpretation-invariance framing.
- [[dis-4-4-1-addition|Ch 4.4.1]] — supplies the [[BinaryAddition|adder]] this section reuses and pre-flagged the `CarryIn = 1` hook this section cashes in.
- [[dis-4-3-signed|Ch 4.3]] — supplies the [[TwosComplement|two's-complement]] *flip-and-add-one* negation recipe.
- [[BinarySubtraction]] (new) — the *subtract = add of negation* algorithm this section codifies.
- [[TwosComplement]] — the operand encoding whose flip-and-add-one negation rule makes hardware reuse possible.
- [[BinaryAddition]] / [[Carry]] / [[CarryIn]] — the reused [[dis-4-4-1-addition|Ch 4.4.1]] machinery.
- [[FullAdder]] (mentioned, not new) — the per-bit primitive whose mode-switching with [[XOR|XOR]] gates produces the add/subtract unit.
- [[ArithmeticLogicUnit]] (forward ref) — the [[ComputerArchitecture|architecture]]-level unit this circuit lives inside.
- [[IntegerOverflow]] (forward ref) — Worked Example 2's MSB-as-1 result anticipates the signed-overflow story.

## Contradictions

None — purely additive. Reuses [[dis-4-3-signed|Ch 4.3]]'s [[TwosComplement|two's-complement]] negation recipe and [[dis-4-4-1-addition|Ch 4.4.1]]'s [[BinaryAddition|adder]] machinery without revision. The MSB-carry-out-not-equal-to-overflow caveat is consistent with — and refines — [[dis-4-4-1-addition|Ch 4.4.1]]'s *"hardware simply drops or truncates"* MSB-carry-out rule by noting the truncated bit's **meaning** depends on the addition vs. subtraction mode.
