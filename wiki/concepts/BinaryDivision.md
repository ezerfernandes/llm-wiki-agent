---
title: "Binary Division"
type: concept
tags: [binary, arithmetic, division, algorithm]
sources: [dis-4-4-3-mult-div]
last_updated: 2026-05-17
---

# Binary Division

**Binary division** is the base-$2$ instantiation of the pencil-and-paper **long-division** algorithm — *the grade-school long-division algorithm transferred to base 2 with only the base changing from $10$ to $2$*. Introduced in [[dis-4-4-3-mult-div|Dive into Systems Ch 4.4.3]] as the **third subsection** of [[dis-4-4-arithmetic|Ch 4.4 *Binary Integer Arithmetic*]].

## Algorithm (pencil-and-paper)

Given dividend $A$ and divisor $B$, computing $A \div B$ → quotient $Q$, remainder $R$:

1. Initialize *running remainder* $R \gets 0$, quotient $Q \gets$ empty.
2. For each bit of $A$ from most-significant to least-significant:
   - **Shift** $R$ left by one position and **bring down** the next bit of $A$ into its LSB.
   - **Trial-subtract** $B$ from $R$ (using [[BinarySubtraction|Ch 4.4.2 subtraction]]):
     - If $R \ge B$: subtract → new $R$, append `1` to $Q$.
     - If $R < B$: leave $R$ unchanged, append `0` to $Q$.
3. Final $Q$ is the **truncated integer quotient**; final $R$ is the **integer remainder** (`%` operator).

## Integer-division truncation

> *"The primary thing to keep in mind when dividing integers is that in most languages (for example, C, Python 2, and Java) the fractional portion of the result gets truncated."*

This is the same trap [[dis-1-1-getting-started|Ch 1.1]] flagged at the C-language level — Ch 4.4.3 supplies the **binary-level mechanism**: long division naturally produces an integer quotient and a separate remainder; the fractional part *only appears if* you continue past the binary point (which integer arithmetic doesn't do). The truncation is **structural**, not a rounding choice. See [[IntegerDivision]].

## Worked example: $11 \div 3 = 3$ remainder $2$

Dividend $A = \mathtt{1011}_2$ (11). Divisor $B = \mathtt{11}_2$ (3).

```
            0 0 1 1     ← quotient Q
          ---------
    1 1 ) 1 0 1 1       ← dividend A
            1 1         ← 3 fits into 101 once → quotient bit 1, subtract
          ---------
            1 0 1       ← remainder so far = 10, bring down next bit → 101
            1 1         ← 3 fits into 101 once again → quotient bit 1, subtract
          ---------
              1 0       ← final remainder R = 2 (truncated; not part of integer quotient)
```

Quotient $Q = \mathtt{0011}_2 = 3$; remainder $R = \mathtt{10}_2 = 2$. In C: `11 / 3` → `3`, `11 % 3` → `2`.

## Why it's simpler than decimal

In decimal long-division, deciding *"how many times does the divisor fit into the current running remainder?"* requires guessing a digit in $\{0, 1, \ldots, 9\}$ — often by trial estimation. In binary, the choice is **only between 0 and 1**: either the divisor fits at least once (quotient bit = 1, subtract) or it doesn't (quotient bit = 0, no subtraction). The decision reduces to a **single magnitude comparison** $R \ge B$.

## Hardware reuse with [[BinarySubtraction|Ch 4.4.2 subtraction]]

Each iteration's trial-subtraction uses the **same adder/subtractor** [[dis-4-4-2-subtraction|Ch 4.4.2]] introduced (addition of the two's-complement negation). A hardware divider is essentially a state machine that shifts the remainder, runs the comparator, and selectively subtracts — but the per-iteration arithmetic primitive is the **same N-bit subtractor** Ch 4.4.2 built. The [[dis-4-4-arithmetic|Ch 4.4]] **hardware-reuse theme** continues: addition / subtraction / multiplication / division all share the same N-bit adder core.

## What [[dis-4-4-3-mult-div|Ch 4.4.3]] does NOT cover

The section's *"these methods do not reflect the behavior of modern hardware and are not meant to be comprehensive"* disclaimer applies equally to division:

- **Hardware dividers** — modern ALUs use restoring, non-restoring, or SRT division; pencil-and-paper bit-by-bit long division is conceptual only.
- **The bit-shift power-of-two shortcut** — *"divide by $2^k$ by right-shifting $k$ positions"* (with [[SignExtension|sign extension]] for [[TwosComplement|signed]] operands, i.e. *arithmetic shift right*) is the hardware-friendly fast path for power-of-two divisors. Not covered. See [[BitShift]] (forward reference).
- **Signed division and remainder sign** — C99 specifies *truncation toward zero* for signed division, but the resulting remainder sign convention (`(-7) % 3` = `-1` in C99 / Java, but `2` in Python 3) is a language-level choice not addressed here.
- **Division-by-zero** — the trap behavior (`SIGFPE` on x86, undefined behavior in C) is not discussed.

## Connections

- [[dis-4-4-3-mult-div]] — introducing source.
- [[dis-4-4-arithmetic]] — parent Ch 4.4 hub.
- [[BinarySubtraction]] — used for the per-iteration trial-subtraction step.
- [[BinaryMultiplication]] — sibling operation introduced in the same section.
- [[IntegerDivision]] — the C-language-level concept this supplies the binary mechanism for.
- [[CArithmeticOperators]] — the `/` and `%` operators in C.
- [[BinaryNumber]] — operand encoding.
- [[UnsignedInteger]] — the interpretation Ch 4.4.3 stays in.
- [[BitShift]] — forward reference to the power-of-two shortcut not covered here.
- [[DiveIntoSystems]] — parent textbook.
