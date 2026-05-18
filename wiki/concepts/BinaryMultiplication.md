---
title: "Binary Multiplication"
type: concept
tags: [binary, arithmetic, multiplication, algorithm]
sources: [dis-4-4-3-mult-div]
last_updated: 2026-05-17
---

# Binary Multiplication

**Binary multiplication** is the base-$2$ instantiation of the pencil-and-paper **long-multiplication** algorithm — *the decimal long-multiplication algorithm transferred to base 2 with only the base changing from $10$ to $2$*. Introduced in [[dis-4-4-3-mult-div|Dive into Systems Ch 4.4.3]] as the **third subsection** of [[dis-4-4-arithmetic|Ch 4.4 *Binary Integer Arithmetic*]].

## Algorithm (pencil-and-paper)

Given multiplicand $A$ and multiplier $B = (b_{N-1} \ldots b_1 b_0)_2$:

1. For each multiplier bit $b_i$ (from $i = 0$ to $N-1$):
   - If $b_i = 1$: partial product row $i$ = $A$ **shifted left by $i$ positions**.
   - If $b_i = 0$: partial product row $i$ = $0$ (contributes nothing).
2. **Sum all partial-product rows** using [[BinaryAddition|Ch 4.4.1 binary addition]] (column-by-column with [[Carry|carry]] propagation).

The result is $A \times B$.

## Why it's simpler than decimal

In decimal long-multiplication, each multiplier digit is in $\{0, 1, \ldots, 9\}$, requiring a memorized **9 × 9 multiplication table** for each partial product. In binary, each multiplier digit is in $\{0, 1\}$ — every partial-product row is **either the multiplicand itself or zero**. The operation reduces to *select-or-zero, shift, and add*. No multiplication table needed.

## Worked example: $5 \times 3 = 15$

```
        0 1 0 1   (5 = multiplicand A)
      × 0 0 1 1   (3 = multiplier B = b_3 b_2 b_1 b_0)
      ---------
        0 1 0 1   ← b_0 = 1 → A × 1 (no shift)
      0 1 0 1     ← b_1 = 1 → A shifted left 1 = 10
      0 0 0 0     ← b_2 = 0 → 0
    0 0 0 0       ← b_3 = 0 → 0
      ---------
        1 1 1 1   = 15
```

Partial-product sum: $\mathtt{0b0101} + \mathtt{0b1010} = \mathtt{0b1111}$ — five plus ten equals fifteen, computed via [[BinaryAddition|binary addition]].

## What [[dis-4-4-3-mult-div|Ch 4.4.3]] does NOT cover

The section opens with an explicit scope disclaimer: *"these methods do not reflect the behavior of modern hardware and are not meant to be comprehensive."* In particular:

- **Hardware multipliers** — modern ALUs use Booth's algorithm, Wallace trees, or array multipliers; the pencil-and-paper row-by-row approach is conceptual only.
- **The bit-shift power-of-two shortcut** — *"multiply by $2^k$ by left-shifting $k$ positions"* is the hardware-friendly fast path for power-of-two multipliers. Ch 4.4.3 uses left-shift *only as part of the partial-product layout*, never as a standalone optimization. See [[BitShift]] (forward reference).
- **Signed multiplication** — multiplying two [[TwosComplement|two's-complement]] operands requires either sign-extension to double width or a Booth-style sign-handling step; not covered.
- **Overflow rules** — the product of two $N$-bit values can be up to $2N$ bits wide; truncation rules and overflow flags are not addressed.

## Hardware reuse with [[BinaryAddition|Ch 4.4.1 addition]]

The algorithm's final step — summing all partial-product rows — uses the **same [[FullAdder|full-adder]] chain** [[dis-4-4-1-addition|Ch 4.4.1]] introduced for binary addition. A hardware multiplier is conceptually a tree of adders that sum $N$ partial-product rows in parallel; the *pencil-and-paper* version sums them sequentially, but the per-bit-position primitive is identical.

## Connections

- [[dis-4-4-3-mult-div]] — introducing source.
- [[dis-4-4-arithmetic]] — parent Ch 4.4 hub.
- [[BinaryAddition]] — used for partial-product summation.
- [[BinaryDivision]] — sibling operation introduced in the same section.
- [[BinaryNumber]] — operand encoding.
- [[UnsignedInteger]] — the interpretation Ch 4.4.3 stays in.
- [[BitShift]] — forward reference to the power-of-two shortcut not covered here.
- [[CArithmeticOperators]] — the `*` operator in C.
- [[DiveIntoSystems]] — parent textbook.
