---
title: "Dive into Systems — Ch 4.4.3 Multiplication and Division"
type: source
tags: [textbook, computer-systems, binary, arithmetic, multiplication, division]
date: 2026-05-17
source_file: https://diveintosystems.org/book/C4-Binary/arithmetic_mult_div.html
---

## Summary

Section 4.4.3 of [[DiveIntoSystems]] — the **third and final subsection** of [[dis-4-4-arithmetic|Ch 4.4 *Binary Integer Arithmetic*]] — transfers the **pencil-and-paper** [[BinaryMultiplication|long-multiplication]] and [[BinaryDivision|long-division]] algorithms from decimal to base 2. The pedagogical thesis is unchanged from [[dis-4-4-1-addition|Ch 4.4.1]] and [[dis-4-4-2-subtraction|Ch 4.4.2]] — decimal place-value arithmetic algorithms transfer directly to [[BinaryNumber|binary]], only the base $B$ changes from $10$ to $2$. The section is **deliberately scoped to manual calculation**: it opens with the disclaimer *"these methods do not reflect the behavior of modern hardware and are not meant to be comprehensive"*, and consequently does **not** cover the hardware bit-shift shortcuts (left-shift = ×2, right-shift = ÷2) that real ALUs and compilers use for power-of-two operands. The headline payoff is **algorithm transfer**, not hardware realism.

## Key Claims

- **Binary multiplication = the pencil-and-paper long-multiplication algorithm in base 2.** *"To perform multiplication in binary, recall the common pencil-and-paper strategy of considering one digit at a time and adding the results."* Per-digit partial-product rows are summed using [[BinaryAddition|Ch 4.4.1 binary addition]].
- **Each multiplier bit produces a shifted copy of the multiplicand.** Worked example $\mathtt{0b0101} \times \mathtt{0b0011}$ (5 × 3): multiplying by $d_0 = 1$ produces partial product $\mathtt{0b0101}$ (5); multiplying by $d_1 = 1$ and **shifting left one position** produces partial product $\mathtt{0b1010}$ (10); the $d_2 = 0$ and $d_3 = 0$ rows contribute zero; final sum $\mathtt{0b0101} + \mathtt{0b1010} = \mathtt{0b1111}$ = 15. The shift is described as *part of the per-digit partial-product layout*, not as a standalone "multiply by 2" shortcut.
- **Binary multiplication is operationally simpler than decimal long-multiplication** because each multiplier digit is restricted to $\{0,1\}$ — every partial-product row is either *the multiplicand* (digit = 1) or *zero* (digit = 0). No per-digit multiplication table is needed; the operation reduces to *select-and-shift-then-add*.
- **[[IntegerDivision|Integer division]] truncates the fractional part** — restated explicitly: *"The primary thing to keep in mind when dividing integers is that in most languages (for example, C, Python 2, and Java) the fractional portion of the result gets truncated."* The connection to [[dis-1-1-getting-started|Ch 1.1]]'s integer-division trap is made explicit.
- **Binary division = the grade-school long-division algorithm in base 2.** Worked example $\mathtt{1011}_2 \div \mathtt{11}_2$ (11 ÷ 3): 11 doesn't fit into the first two bits; 11 fits into the first three bits (101) **once**, leaving remainder 10; the next bit shifts in giving 101 again; 11 fits **once** more; final quotient $\mathtt{0011}_2$ = 3 with remainder 2 (truncated).
- **The `%` operator delivers the integer remainder.** Example: $11 \% 3 = 2$. Paired with `/` it gives the quotient-and-remainder pair, completing the [[CArithmeticOperators|C arithmetic-operator]] surface area for integer division.
- **Explicit hardware-scope disclaimer.** The section ends without covering: (a) modern hardware multipliers (Booth's algorithm, Wallace trees, etc.); (b) bit-shift power-of-two shortcuts; (c) signed-multiplication / signed-division special cases; (d) overflow detection rules — all deferred or left out of scope.

## Key Quotes

> "To perform multiplication in binary, recall the common pencil-and-paper strategy of considering one digit at a time and adding the results."

> "These methods do not reflect the behavior of modern hardware and are not meant to be comprehensive."

> "The primary thing to keep in mind when dividing integers is that in most languages (for example, C, Python 2, and Java) the fractional portion of the result gets truncated."

## Worked Examples

### Multiplication: $5 \times 3 = 15$ in 4-bit binary

```
        0 1 0 1   (5 = multiplicand)
      × 0 0 1 1   (3 = multiplier)
      ---------
        0 1 0 1   ← d_0 = 1 →    5 × 1 = 5
      0 1 0 1     ← d_1 = 1 →    5 × 2 = 10 (shifted left 1)
      0 0 0 0     ← d_2 = 0 →    0
    0 0 0 0       ← d_3 = 0 →    0
      ---------
        1 1 1 1   = 15
```

### Division: $11 \div 3 = 3$ remainder $2$ in binary

```
            0 0 1 1     ← quotient
          ---------
    1 1 ) 1 0 1 1
            1 1         ← 3 fits into 101 once → quotient bit 1
          ---------
            1 0 1       ← remainder so far: 10, bring down next bit → 101
            1 1         ← 3 fits into 101 once again → quotient bit 1
          ---------
              1 0       ← final remainder 2 (truncated)
```

In C: `11 / 3` → `3`; `11 % 3` → `2`.

## Connections

- [[DiveIntoSystems]] — parent textbook; this is **the third (and final) subsection of [[dis-4-4-arithmetic|Ch 4.4]]** inside **Ch 4 *Binary and Data Representation***; **closes the [[BinaryArithmetic|binary integer arithmetic]] block** (Addition / Subtraction / Multiplication & Division).
- [[SuzanneJMatthews]] / [[TiaNewhall]] / [[KevinCWebb]] — authors.
- [[dis-4-4-arithmetic]] — parent hub page; this subsection completes the three-subsection block.
- [[dis-4-4-1-addition]] — multiplication's **per-digit partial products are summed using Ch 4.4.1's [[BinaryAddition|binary-addition]] algorithm**.
- [[dis-4-4-2-subtraction]] — division's **trial-subtraction step uses Ch 4.4.2's [[BinarySubtraction|binary-subtraction]] mechanism** (subtracting the divisor from the running remainder).
- [[BinaryMultiplication]] — the new concept page introduced here.
- [[BinaryDivision]] — the new concept page introduced here.
- [[IntegerDivision]] — already in the wiki from [[dis-1-1-getting-started|Ch 1.1]]; Ch 4.4.3 supplies the **base-2 algorithm** for the operation Ch 1.1 introduced at the C-language level.
- [[CArithmeticOperators]] — `/` and `%` operators; Ch 4.4.3 explicates the **binary-level mechanism** behind C's `/` and `%` for integer types.
- [[BinaryNumber]] / [[UnsignedInteger]] / [[TwosComplement]] — operand encodings; Ch 4.4.3 stays in the unsigned interpretation but notes the [[dis-4-4-arithmetic|Ch 4.4]] interpretation-invariance principle continues to apply for the underlying bit-pattern arithmetic (though signed multiplication / division have additional sign-handling not covered here).
- [[dis-4-1-bases]] / [[dis-4-2-conversion]] / [[dis-4-3-signed]] — prior Ch 4 subsections supplying the [[PositionalNotation|place-value]] framework and signed/unsigned bit-pattern semantics.
- [[BitShift]] — **explicitly NOT covered** by Ch 4.4.3 as a multiplication-by-2 / division-by-2 shortcut. The section uses left-shift only as part of the partial-product layout in long-multiplication, not as a standalone optimization. Forward reference for a future hardware-realistic treatment.

## Contradictions

None. Purely additive — Ch 4.4.3 instantiates [[dis-4-4-arithmetic|Ch 4.4]]'s base-transfer thesis on the multiplication and division algorithms, reusing the [[BinaryAddition|Ch 4.4.1 adder]] for partial-product summation and the [[BinarySubtraction|Ch 4.4.2 subtractor]] for the trial-subtraction step inside long division.
