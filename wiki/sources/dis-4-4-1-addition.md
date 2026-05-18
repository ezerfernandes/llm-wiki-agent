---
title: "Dive into Systems — Ch 4.4.1 Addition"
type: source
tags: [dive-into-systems, binary, arithmetic, addition, computer-systems]
date: 2026-05-17
source_file: https://diveintosystems.org/book/C4-Binary/arithmetic_addition.html
sources: [dis-4-4-1-addition]
last_updated: 2026-05-17
---

## Summary

**Ch 4.4.1 *Addition*** is the first subsection of [[dis-4-4-arithmetic|Ch 4.4 *Binary Integer Arithmetic*]] of *[[DiveIntoSystems]]* by [[SuzanneJMatthews|Matthews]] / [[TiaNewhall|Newhall]] / [[KevinCWebb|Webb]]. It instantiates the chapter's headline thesis — *decimal place-value arithmetic transfers directly to base 2* — by walking the **column-by-column [[BinaryAddition|binary addition]] algorithm** from the least-significant digit to the most-significant digit, with [[Carry|carries]] propagating leftward. The headline observation is that since the only multi-bit elementary sum is $1 + 1 = \mathtt{0b10}$, every binary column produces at most a **one-bit carry** into the next position — making binary addition operationally simpler than decimal (where the carry can be any digit $0$–$9$, here only $0$ or $1$). The chapter introduces the **[[FullAdder|full-adder]] truth table** (eight rows over `DigitA` × `DigitB` × `CarryIn` → `Sum` + `CarryOut`) as the per-bit primitive that hardware implements, and names the [[CarryOut|carry-out]] from the [[MostSignificantBit|MSB]] as the bit *"the hardware simply drops or truncates"* — the silent overflow that motivates [[Ch 4.4 *Binary Integer Arithmetic*|dis-4-4-arithmetic]]'s [[BinaryArithmetic|interpretation-invariance]] claim and the eventual [[IntegerOverflow|overflow-detection]] story.

## Key Claims

- **Place-value transfer**: binary addition uses the same column-by-column low-order-to-high-order algorithm as decimal — only the base changes from $10$ to $2$.
- **One-bit carry**: because the only multi-bit elementary sum is $1 + 1 = \mathtt{0b10}$, every column produces at most a single bit of [[Carry|carry]] into the next position. This is strictly simpler than decimal arithmetic.
- **Eight-row full-adder truth table**: a single bit-position adder takes three inputs (`DigitA`, `DigitB`, `CarryIn`) and produces two outputs (`Sum`, `CarryOut`) — eight rows total.
- **Worked example** $\mathtt{0b0010} + \mathtt{0b1011} = \mathtt{0b1101}$: position 1's $1 + 1$ generates a [[Carry|carry]] of `1` into position 2; the result `0b1101` is **simultaneously** $13$ when interpreted as [[UnsignedInteger|unsigned]] and $-3$ when interpreted as [[TwosComplement|two's complement]] — the per-[[dis-4-4-arithmetic|Ch 4.4]] interpretation-invariance principle made concrete.
- **[[CarryOut|Carry-out]] from the MSB is truncated**: when the addition produces a carry beyond the most-significant bit, *"the hardware simply drops or truncates"* that bit. The result is the lower $N$ bits only — silently incorrect when overflow actually occurs.
- **[[CarryIn|Carry-in]] is implicit zero** for standard addition: the rightmost bit position has no predecessor, so multibit adders wire its `CarryIn` to `0`. The architectural reason this input *exists* at all (rather than being hard-wired to zero) is the [[BinarySubtraction|subtraction]] use case — *"this feature becomes critical for subtraction implementations"* — foreshadowing [[Ch 4.4.2|dis-4-4-2-subtraction]]'s **flip-and-add-one** recipe ([[TwosComplement|two's complement]] negation = bit-flip + add 1; the *add 1* is delivered by setting `CarryIn = 1` on a single adder, costing no extra hardware).

## Key Quotes

> "When we look at single-bit addition, there are eight possible combinations of inputs and outputs to consider." — the [[FullAdder|full-adder]] truth-table framing.

> "the hardware simply drops or truncates" — on the MSB [[CarryOut|carry-out]] bit (the silent-overflow root cause).

> "this feature becomes critical for subtraction implementations" — on why `CarryIn` exists as an input despite being implicit zero during standard addition.

## The Full-Adder Truth Table

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

`Sum` is the XOR of all three inputs; `CarryOut` is the majority of all three inputs — the canonical [[FullAdder|full-adder]] equations every CS architecture text uses, here introduced before the names *full adder*, XOR, or majority are spoken.

## Worked Example: `0b0010 + 0b1011`

```
   carries:  0 1 0 0
             0 0 1 0
           + 1 0 1 1
           ---------
             1 1 0 1
```

- Position 0: $0 + 1 + 0 = 1$ → write `1`, `CarryOut = 0`.
- Position 1: $1 + 1 + 0 = \mathtt{0b10}$ → write `0`, `CarryOut = 1` (the only column that carries).
- Position 2: $0 + 0 + 1 = 1$ → write `1`, `CarryOut = 0`.
- Position 3: $0 + 1 + 0 = 1$ → write `1`, `CarryOut = 0` (no MSB carry-out — no overflow).

Result `0b1101` interprets as **13** when read as [[UnsignedInteger|unsigned]] (per [[dis-4-1-bases|Ch 4.1]]) or **−3** when read as [[TwosComplement|two's complement]] (per [[dis-4-3-signed|Ch 4.3]] — MSB has negative weight $-8$, so $-8 + 4 + 0 + 1 = -3$). Both interpretations are *correct* — the addition arithmetic is identical; only the post-hoc reading of the bit pattern differs. This is the per-[[dis-4-4-arithmetic|Ch 4.4]] **interpretation-invariance** principle made concrete on one worked example.

## Connections

- [[DiveIntoSystems]] — Ch 4.4.1 is the first of three subsections of [[dis-4-4-arithmetic|Ch 4.4 *Binary Integer Arithmetic*]]; the corpus now stands at **39 chapters**.
- [[SuzanneJMatthews]] / [[TiaNewhall]] / [[KevinCWebb]] — co-authors.
- [[dis-4-4-arithmetic|Ch 4.4]] — parent hub page; supplies the interpretation-invariance framing.
- [[dis-4-3-signed|Ch 4.3]] — supplies the [[TwosComplement|two's complement]] reading of `0b1101` as `-3`.
- [[dis-4-1-bases|Ch 4.1]] — supplies the [[UnsignedInteger|unsigned]] reading of `0b1101` as `13`.
- [[BinaryAddition]] (new) — the column-by-column algorithm this section codifies.
- [[Carry]] (new) — the one-bit propagation mechanism.
- [[FullAdder]] (mentioned, not new) — the per-bit hardware primitive whose truth table is presented; the full-adder concept is implicit (a future [[ArithmeticLogicUnit|ALU]] / [[DigitalLogic|digital-logic]] section will name it explicitly).
- [[CarryOut]] / [[CarryIn]] — the two carry signals named in the chapter; treated as facets of the unified [[Carry]] concept page rather than separate pages.
- [[BinaryNumber]] / [[UnsignedInteger]] / [[TwosComplement]] — the operand-interpretation lattice.
- [[BinarySubtraction]] (forward ref to [[dis-4-4-2-subtraction|Ch 4.4.2]]) — the reason `CarryIn` exists as an input.
- [[IntegerOverflow]] (forward ref) — the named consequence of truncating the MSB [[CarryOut|carry-out]]; subsequent Ch 4 sections will formalize.

## Contradictions

None — purely additive. The interpretation-invariance principle from [[dis-4-4-arithmetic|Ch 4.4]] is here made concrete on the `0b1101` worked example, and the MSB-carry-out-truncation rule is consistent with [[dis-4-3-signed|Ch 4.3]]'s [[TwosComplement|two's-complement]] arithmetic.
