---
title: "Binary Subtraction"
type: concept
tags: [binary, arithmetic, subtraction, twos-complement, computer-systems, digital-logic]
sources: [dis-4-4-arithmetic, dis-4-4-2-subtraction]
last_updated: 2026-05-17
---

# Binary Subtraction

**Binary subtraction** is the base-$2$ subtraction operation $A - B$ implemented as **addition of the [[TwosComplement|two's-complement]] negation** $A + (-B)$. Per [[dis-4-4-2-subtraction|Dive into Systems Ch 4.4.2]], no dedicated subtractor hardware is required — the existing [[BinaryAddition|binary adder]] from [[dis-4-4-1-addition|Ch 4.4.1]] handles subtraction by **flipping the bits of $B$** and **injecting `1` into the [[CarryIn|`CarryIn`]] of the least-significant-bit adder**. The headline quote: *"subtracting $7 - 3$ is equivalent to expressing the operation as $7 + (-3)$."*

## Algorithm

To compute $A - B$ on $N$-bit operands:

1. **Negate $B$ via [[TwosComplement|two's complement]]** — *"flip all the bits and add one"*. The bit-flip is one row of [[XOR|XOR]] gates; the *add one* is folded into the addition.
2. **Add $A + \overline{B}$ with [[CarryIn|`CarryIn`]] = 1** on the LSB adder. The injected $1$ delivers the *add one* of the two's-complement negation at zero extra hardware cost.
3. **Truncate any MSB carry-out** — the residual $N$ bits are the result. (Whether that carry-out indicates overflow is **not automatic** — its meaning differs between addition and subtraction modes; the full [[IntegerOverflow|overflow]] rule is deferred to a later Ch 4 section.)

## Worked example 1: $7 - 3$

Both operands fit in 4 bits: $7 = \mathtt{0b0111}$, $3 = \mathtt{0b0011}$.

- Flip $3$: $\mathtt{0b1100}$.
- Add $\mathtt{0b0111} + \mathtt{0b1100}$ with `CarryIn = 1` → $\mathtt{0b10100}$.
- Truncate MSB carry-out → $\mathtt{0b0100} = 4$. **Correct**.

## Worked example 2: $7 - (-3)$

$7 = \mathtt{0b0111}$, $-3 = \mathtt{0b1101}$ ([[TwosComplement|two's complement]]).

- Flip $-3$: $\mathtt{0b0010}$.
- Add $\mathtt{0b0111} + \mathtt{0b0010}$ with `CarryIn = 1` → $\mathtt{0b1010} = 10$. **Correct** ([[UnsignedInteger|unsigned]] reading); the all-four-sign-combinations claim is verified on the negative-subtrahend case.

## Hardware: the add/subtract unit

The chapter's recipe maps to a single mode wire `Subtract` controlling **two** existing adder inputs:

| Stage | Wire | `Subtract = 0` (add) | `Subtract = 1` (subtract) |
|---|---|---|---|
| Operand B path | `XOR(b_i, Subtract)` per bit | passthrough $b_i$ | flipped $\overline{b_i}$ |
| LSB adder | `CarryIn` | `0` | `1` |
| Result | `Sum_{N-1..0}` | $A + B$ | $A + (\overline{B} + 1) = A - B$ |

This is the canonical **add/subtract unit** the [[FullAdder|full-adder]] chain becomes when wrapped with one [[XOR|XOR]]-gate row plus the `CarryIn = 1` wire — *Dive into Systems* presents the recipe in plain prose before naming the gates or the unit. The [[ArithmeticLogicUnit|ALU]] generalization (adding AND / OR / shift modes alongside add/subtract) is deferred to a later chapter.

## Why this matters

- **Zero extra arithmetic hardware**: subtraction reuses the adder, paying only an [[XOR|XOR]]-gate row and one wire flip — a major architectural payoff of [[dis-4-3-signed|Ch 4.3]]'s [[TwosComplement|two's-complement]] encoding choice.
- **Sign-combination universality**: the same circuit handles $A - B$ for **all four sign combinations** (`+ − +`, `+ − −`, `− − +`, `− − −`) without special-case logic, by reapplying the [[dis-4-4-arithmetic|Ch 4.4]] **interpretation-invariance** principle to the subtraction case.
- **Cashes in [[dis-4-4-1-addition|Ch 4.4.1]]'s `CarryIn` hook**: [[CarryIn|`CarryIn`]] existed as an architectural input on every [[FullAdder|full-adder]] *because of* subtraction; this chapter delivers on that promise. The implicit `0` of ordinary addition becomes the mode-switching `Subtract` signal here.
- **MSB carry-out semantics shift**: in subtraction mode, the MSB carry-out **does not automatically signal overflow** the way it does in addition mode — its interpretation depends on operand sign combinations; the full [[IntegerOverflow|overflow]]-detection rule is deferred.

## See also

- [[BinaryAddition]] — the reused adder algorithm; this concept page's dual operation.
- [[Carry]] / [[CarryIn]] / [[CarryOut]] — the chained-bit propagation signal; [[CarryIn]] of the LSB carries the subtraction mode bit.
- [[TwosComplement]] — the *flip-all-bits-and-add-one* negation recipe that makes hardware reuse possible.
- [[FullAdder]] — the per-bit primitive the add/subtract unit chains.
- [[ArithmeticLogicUnit]] — the architecture-level unit that contains the add/subtract circuit alongside logical / shift modes.
- [[IntegerOverflow]] — the overflow story Worked Example 2's MSB-as-1 result anticipates.
- [[BinaryArithmetic]] — the umbrella concept (addition / subtraction / multiplication / division).
- [[dis-4-4-arithmetic|Dive into Systems Ch 4.4]] / [[dis-4-4-2-subtraction|Ch 4.4.2]] — primary source.
