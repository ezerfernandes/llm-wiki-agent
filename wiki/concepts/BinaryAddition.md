---
title: "Binary Addition"
type: concept
tags: [binary, arithmetic, addition, computer-systems, digital-logic]
sources: [dis-4-4-arithmetic, dis-4-4-1-addition]
last_updated: 2026-05-17
---

# Binary Addition

**Binary addition** is the base-$2$ instantiation of place-value column addition. Per [[dis-4-4-1-addition|Dive into Systems Ch 4.4.1]], the algorithm is **identical to decimal long addition** — only the base changes from $10$ to $2$. Operands are aligned at the least-significant bit, columns are summed low-order to high-order, and a one-bit [[Carry|carry]] propagates leftward whenever a column sum reaches $2$ or $3$.

## Per-column rule

Because each binary digit is $0$ or $1$, the elementary column sum `DigitA + DigitB + CarryIn` takes values in $\{0, 1, 2, 3\}$:

| Column sum | `Sum` bit | `CarryOut` |
|---|---|---|
| 0 | 0 | 0 |
| 1 | 1 | 0 |
| 2 | 0 | 1 |
| 3 | 1 | 1 |

This is the [[FullAdder|full-adder]] truth table compressed into a four-row form. The eight-row form ([[dis-4-4-1-addition|Ch 4.4.1]]'s presentation) enumerates the three input bits explicitly:

| `DigitA` | `DigitB` | `CarryIn` | `Sum` | `CarryOut` |
|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 1 | 0 |
| 0 | 1 | 0 | 1 | 0 |
| 0 | 1 | 1 | 0 | 1 |
| 1 | 0 | 0 | 1 | 0 |
| 1 | 0 | 1 | 0 | 1 |
| 1 | 1 | 0 | 0 | 1 |
| 1 | 1 | 1 | 1 | 1 |

Algebraically: `Sum = DigitA XOR DigitB XOR CarryIn`, `CarryOut = majority(DigitA, DigitB, CarryIn)`.

## Worked example: `0b0010 + 0b1011`

Position 1 generates the only carry ($1 + 1 = \mathtt{0b10}$), which propagates into position 2. Result: `0b1101` — which reads as **13** ([[UnsignedInteger|unsigned]]) or **−3** ([[TwosComplement|two's complement]]) depending on the choice of operand interpretation. This worked example is [[dis-4-4-1-addition|Ch 4.4.1]]'s concrete instantiation of the [[dis-4-4-arithmetic|Ch 4.4]] **interpretation-invariance** principle.

## Hardware consequences

- **Unified [[ArithmeticLogicUnit|ALU]]**: the same $N$-bit adder serves both [[UnsignedInteger|unsigned]] and [[TwosComplement|two's-complement]] operands; the bit-level steps are identical and only the post-hoc interpretation differs.
- **MSB [[CarryOut|carry-out]] is truncated**: the result is the lower $N$ bits only — silently incorrect when overflow occurs. The hardware *"simply drops or truncates"* the extra bit (per [[dis-4-4-1-addition|Ch 4.4.1]]).
- **[[CarryIn|Carry-in]] = 0 for standard addition**: but the input exists architecturally because [[BinarySubtraction|subtraction]] sets it to $1$ to deliver the *add one* half of [[TwosComplement|two's complement]]'s *flip-and-add-one* negation recipe (preview of [[dis-4-4-2-subtraction|Ch 4.4.2]]).

## Why binary addition is easier than decimal

In decimal, the carry can be any digit $0$–$9$, requiring a $10 \times 10 + 1$-row column sum table. In binary, the carry is exactly $0$ or $1$, and the [[FullAdder|full-adder]] truth table is only $2^3 = 8$ rows — small enough to memorize and small enough to build out of a handful of [[LogicGate|logic gates]].

## See also

- [[Carry]] — the bit-position-to-next-bit-position propagation mechanism this algorithm relies on.
- [[FullAdder]] — the per-bit hardware primitive (named in subsequent [[DigitalLogic|digital-logic]] chapters).
- [[BinarySubtraction]] — the dual operation, implemented as addition of the [[TwosComplement|two's-complement]] negation.
- [[IntegerOverflow]] — what happens when the MSB [[CarryOut|carry-out]] is truncated and the true result didn't fit in $N$ bits.
- [[BinaryArithmetic]] — the umbrella concept (addition / subtraction / multiplication / division).
- [[dis-4-4-arithmetic|Dive into Systems Ch 4.4]] / [[dis-4-4-1-addition|Ch 4.4.1]] — primary source.
