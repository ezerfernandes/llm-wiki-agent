---
title: "Dive into Systems — Ch 4.6 Bitwise Operators"
type: source
tags: [dive-into-systems, ch4, binary, bitwise, c-language, computer-systems]
date: 2026-05-17
source_file: https://diveintosystems.org/book/C4-Binary/bitwise.html
sources: [dis-4-6-bitwise]
last_updated: 2026-05-17
---

# Dive into Systems — Ch 4.6 *Bitwise Operators*

## Summary

[[SuzanneJMatthews|Matthews]] / [[TiaNewhall|Newhall]] / [[KevinCWebb|Webb]]'s **Ch 4.6** of *[[DiveIntoSystems]]* — the **operator-surface section** that exposes [[CLanguage|C]]'s six [[BitwiseOperator|bitwise operators]] (`&`, `|`, `^`, `~`, `<<`, `>>`) as the per-bit primitives that *directly apply [[LogicGate|logic-gate]] behaviour to bit sequences*. Bridges from Ch 4.1–4.5's value-level [[BinaryRepresentation|binary representation]] and [[BinaryArithmetic|integer arithmetic]] to the **bit-manipulation idioms** systems code uses to pack flags, mask fields, set / clear / toggle / test individual bits, and multiply / divide by powers of two — operations that have no natural expression in higher-level numeric arithmetic.

## Key Claims

- **Bit-level vs. truth-value distinction**: bitwise operators (`&`, `|`, `^`, `~`, `<<`, `>>`) manipulate **individual bits** of their operands; [[LogicalOperator|logical operators]] (`&&`, `||`, `!`) evaluate **truth values** with zero = false and non-zero = true. *"Programmers often confuse the bitwise [[LogicalAnd|`&&`]] and [[LogicalOr|`||`]] operators with [[BitwiseAnd|`&`]] and [[BitwiseOr|`|`]] operators."*
- **Bitwise AND (`&`)** — outputs `1` iff **both** input bits are `1`; truth table $\{(0,0)\to 0, (0,1)\to 0, (1,0)\to 0, (1,1)\to 1\}$. Worked example: `26 & 54 = 18` (`0b011010 & 0b110110 = 0b010010`). Canonical use: **bit masking** — isolate a field by ANDing with a mask that has `1` in the kept positions and `0` elsewhere.
- **Bitwise OR (`|`)** — outputs `1` iff **at least one** input bit is `1`; truth table $\{(0,0)\to 0, (0,1)\to 1, (1,0)\to 1, (1,1)\to 1\}$. Worked example: `26 | 54 = 62` (`0b011010 | 0b110110 = 0b111110`). Canonical use: **setting bits** to `1` while preserving the others.
- **Bitwise XOR (`^`)** — outputs `1` iff **exactly one** input bit is `1`; truth table $\{(0,0)\to 0, (0,1)\to 1, (1,0)\to 1, (1,1)\to 0\}$. Worked example: `26 ^ 54 = 44` (`0b011010 ^ 0b110110 = 0b101100`). Canonical use: **toggling specific bits** (`x ^ mask` flips the bits that are `1` in the mask) and **difference detection** (`a ^ b == 0` iff `a == b`).
- **Bitwise NOT (`~`)** — unary operator inverting every bit (`0`→`1`, `1`→`0`). Worked example: `~26 = -27` because [[TwosComplement|two's complement]] makes bit-flipping equivalent to *flip-without-the-add-one* — *"bitwise NOT only flips the bits and doesn't add one"* — one short of true [[TwosComplement|two's-complement]] negation. Canonical use: **creating inverted masks** for clearing bits (`x & ~mask` clears the bits that are `1` in `mask`).
- **Left shift (`<<`)** — `x << N` moves bits leftward by `N` positions, **zero-filling on the right**, truncating bits shifted past the most-significant position. Worked example: `13 << 3 = 104` (`0b00001101 << 3 = 0b01101000`). **Effect** (absent overflow): multiplication by $2^N$.
- **Right shift (`>>`)** — `x >> N` moves bits rightward by `N` positions; the fill on the **left** depends on the operand's [[CLanguage|C]] type:
  - **[[LogicalRightShift|Logical right shift]]** (unsigned operands): zero-fill — `0b10110011 >> 2 = 0b00101100`.
  - **[[ArithmeticRightShift|Arithmetic right shift]]** (signed operands): replicate the [[SignBit|sign bit]] — `0b10110011 >> 2 = 0b11101100` — to preserve the sign of negative [[TwosComplement|two's-complement]] values. *"The C compiler automatically selects the appropriate shifting variant based on variable declaration."*
  - Comparison example: `unsigned int u_val = 0xFF000000; int s_val = 0xFF000000;` → `u_val >> 12 == 0x000FF000` (logical), `s_val >> 12 == 0xFFFFF000` (arithmetic).
  - **Effect** (logical, unsigned): integer division by $2^N$. For signed values, [[ArithmeticRightShift|arithmetic shift]] approximates floor-division but disagrees with `/` on negative dividends (rounds toward $-\infty$ rather than toward zero).
- **Hardware payoff**: bitwise operators map **one-to-one onto [[LogicGate|logic gates]]** (AND/OR/XOR/NOT) and **wiring topology** (shifts are pure routing — no gates needed); they execute in **one clock cycle** on virtually all ISAs and have **no carry propagation** (unlike addition). The reason they're the cheapest operations in the [[InstructionSetArchitecture|ISA]].
- **C-specific behaviour notes**: shift amount `>=` the operand's bit width is **[[UndefinedBehavior|undefined behavior]] in C** (e.g., `(uint32_t)x << 32` is UB); signed left-shift that overflows the sign bit is also UB; the *type* of the shift result follows the left operand (`x << y` has `x`'s type). The chapter stays at hardware-level mechanics — these C-language pitfalls are wiki-only context.

## Key Quotes

> "Bitwise operators directly apply logic gate behavior to bit sequences." — Ch 4.6, framing the operators as the per-bit instantiation of digital-logic primitives.

> "Programmers often confuse the bitwise `&&` and `||` operators with `&` and `|` operators." — Ch 4.6, naming the canonical category error.

> "Bitwise NOT only flips the bits and doesn't add one." — Ch 4.6, distinguishing `~x` from `-x` under [[TwosComplement|two's complement]].

> "The C compiler automatically selects the appropriate shifting variant based on variable declaration." — Ch 4.6, on the [[LogicalRightShift|logical]] / [[ArithmeticRightShift|arithmetic]] right-shift dispatch by operand type.

## Connections

- [[DiveIntoSystems]] — corpus's **43rd ingested chapter**; advances Ch 4 *Binary and Data Representation* from the [[BinaryArithmetic|integer-arithmetic]] block (4.4 / 4.5) into **bit-manipulation operators** — the surface programmers actually type.
- [[SuzanneJMatthews]] / [[TiaNewhall]] / [[KevinCWebb]] — authors.
- [[BitwiseOperator]] — **new concept page** — the umbrella covering `&` / `|` / `^` / `~` and the bit-test / set / clear / toggle / mask idioms they enable.
- [[BitShift]] — **new concept page** — the `<<` / `>>` family covering [[LogicalRightShift|logical]] vs. [[ArithmeticRightShift|arithmetic]] right shifts and the multiply / divide-by-power-of-two relationship.
- [[CLanguage|C]] — host language whose operator surface this chapter codifies.
- [[LogicGate]] — the per-bit hardware primitives `&` / `|` / `^` / `~` map onto.
- [[BinaryNumber]] — the bit-pattern substrate the operators act on.
- [[TwosComplement]] — the encoding whose [[SignBit|sign-bit]] semantics drive the [[ArithmeticRightShift|arithmetic-right-shift]] rule and the `~x = -x - 1` identity.
- [[SignBit]] — the [[MostSignificantBit|MSB]] whose value the [[ArithmeticRightShift|arithmetic right shift]] replicates.
- [[UnsignedInteger]] — the operand class that triggers [[LogicalRightShift|logical right shift]] in [[CLanguage|C]].
- [[SignedInteger]] — the operand class that triggers [[ArithmeticRightShift|arithmetic right shift]] in [[CLanguage|C]].
- [[LogicalOperator]] — the short-circuiting truth-value operators (`&&`, `||`, `!`) that students confuse with the bitwise family.
- [[UndefinedBehavior]] — the [[CLanguage|C]] category covering shift-by-≥-width and signed-shift-overflow (wiki-only — not in the chapter).
- [[BinaryArithmetic]] — the value-level companion block (Ch 4.4) that bit-level operators sit beside.
- [[IntegerOverflow]] — what happens when left-shift pushes bits past the [[MostSignificantBit|MSB]] (left-shift = multiplication by $2^N$, with the same wrap-around semantics as multiplication).
- [[dis-4-1-bases|Ch 4.1]] — supplies the [[BinaryNumber|binary]] bit-pattern substrate.
- [[dis-4-3-signed|Ch 4.3]] — supplies the [[TwosComplement|two's-complement]] interpretation that drives `~x = -x - 1` and the arithmetic-right-shift sign-replication rule.
- [[dis-4-4-3-mult-div|Ch 4.4.3]] — the chapter that **explicitly defers** the bit-shift power-of-two shortcut for multiplication / division; Ch 4.6 delivers it (left shift multiplies, right shift divides — at single-cycle cost vs. pencil-and-paper long multiplication's per-bit-shift-and-add).
- [[dis-4-5-overflow|Ch 4.5]] — the [[IntegerOverflow|overflow]] rules apply to left-shift identically to multiplication (`x << N` overflows when bits would have to propagate past the MSB).

## Contradictions

- None with existing wiki content. Ch 4.6 **delivers** the [[dis-4-4-3-mult-div|Ch 4.4.3]]-deferred *"bit-shift power-of-two shortcut"* (multiply by $2^k$ = left-shift $k$; divide by $2^k$ = right-shift $k$) that the multiplication-and-division chapter explicitly listed as out of scope.

## Scope Notes

- **Not covered by Ch 4.6**: the [[CLanguage|C]] **[[UndefinedBehavior|UB]]** rules around shifts — shift by an amount `>=` the operand width is UB; left-shift that overflows a signed type is UB. The wiki [[BitShift]] page records this.
- **Not covered**: **rotation** operators (left / right circular shift — wraps bits around rather than discarding) — most CPUs have hardware support (`ROL` / `ROR` on x86, `ROR` on ARM) but standard C exposes no operator; idiomatic `(x << n) | (x >> (W - n))` works only for unsigned types and only when `0 < n < W`.
- **Not covered**: **population count** (`popcount` / hamming weight), **count-leading-zeros** (`clz`), **count-trailing-zeros** (`ctz`), **bit reversal**, **byte swap** — bit-manipulation primitives exposed as hardware instructions (`popcnt`, `lzcnt`, `tzcnt`, `bswap` on x86; `CLZ`, `RBIT`, `REV` on ARM) and compiler intrinsics (`__builtin_popcount`, `__builtin_clz`).
- **Not covered**: **bit-fields** in [[CStruct|`struct`]]s (`unsigned int flag : 1;`) — the C-level abstraction that compiles into bitwise masks and shifts.
- **Not covered**: the historical **XOR-swap idiom** (`a ^= b; b ^= a; a ^= b;`) — works but is slower than the temporary-variable version on modern register renaming; mentioned only as a curiosity in most modern texts.
- **Not covered**: **saturating shifts** (ARM NEON `qshl` — clamp-to-max-instead-of-overflow) — DSP-domain only.
