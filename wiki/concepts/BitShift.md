---
title: "Bit Shift"
type: concept
tags: [bitwise, shift, c-language, binary, digital-logic, computer-systems]
sources: [dis-4-6-bitwise, dis-4-4-3-mult-div]
last_updated: 2026-05-17
---

# Bit Shift

A **bit shift** moves every bit in an $N$-bit value left or right by some number of positions, **discarding** bits that fall off one end and **filling** the vacated positions on the other end. Per [[dis-4-6-bitwise|Dive into Systems Ch 4.6]], [[CLanguage|C]] exposes two shift operators — `<<` (left shift) and `>>` (right shift) — and the right-shift behaviour **splits into two variants** ([[LogicalRightShift|logical]] vs. [[ArithmeticRightShift|arithmetic]]) depending on whether the operand is [[UnsignedInteger|unsigned]] or signed.

This concept page also delivers the [[BitShift|bit-shift]] **power-of-two shortcut for multiplication and division** that [[dis-4-4-3-mult-div|Ch 4.4.3]] **explicitly listed as out of scope**.

## Left shift (`<<`)

`x << N` moves all bits leftward by $N$ positions; the rightmost $N$ positions are **zero-filled**, the leftmost $N$ bits are **truncated**.

| Operand bits | Operation | Result bits |
|---|---|---|
| `0b00001101` (13) | `<< 3` | `0b01101000` (104) |

**Effect** (absent overflow): multiplication by $2^N$ — `x << N == x * (1 << N)`. The delivery on [[dis-4-4-3-mult-div|Ch 4.4.3]]'s deferred *power-of-two shortcut*: instead of the pencil-and-paper long-multiplication that chapter taught, `x * 16` compiles to `x << 4` (one cycle, no carry propagation) vs. the multi-cycle shift-and-add core a hardware multiplier runs.

**Overflow**: bits shifted past the [[MostSignificantBit|MSB]] are lost — `(uint8_t)0x80 << 1 == 0x00`. Same wrap-around semantics as multiplication ([[dis-4-5-overflow|Ch 4.5]]'s [[IntegerOverflow|overflow]] rules apply).

## Right shift (`>>`) — the logical / arithmetic split

`x >> N` moves all bits rightward by $N$ positions; the leftmost $N$ positions are filled — but **what they're filled with depends on the operand type**:

### [[LogicalRightShift|Logical right shift]] (unsigned operands)

Zero-fill the high-order positions. Used for [[UnsignedInteger|unsigned]] types.

| Operand | Operation | Result |
|---|---|---|
| `0b10110011` (179) | `>> 2` | `0b00101100` (44) |
| `0xFF000000` (`unsigned`) | `>> 12` | `0x000FF000` |

**Effect**: integer division by $2^N$ (floor), since the discarded low bits are the remainder — `(unsigned)x >> N == x / (1u << N)`.

### [[ArithmeticRightShift|Arithmetic right shift]] (signed operands)

Replicate the [[SignBit|sign bit]] (the [[MostSignificantBit|MSB]]) into the high-order positions — preserves the sign of negative [[TwosComplement|two's-complement]] values.

| Operand | Operation | Result |
|---|---|---|
| `0b10110011` (signed, −77) | `>> 2` | `0b11101100` (−20) |
| `0xFF000000` (`signed int`, negative) | `>> 12` | `0xFFFFF000` |

**Effect**: floor-division by $2^N$ — disagrees with C's `/` operator on negative dividends (arithmetic shift rounds toward $-\infty$; `/` rounds toward zero). Example: `(-1) >> 1 == -1` (floor), but `(-1) / 2 == 0` (truncate).

### Dispatch (C)

*"The C compiler automatically selects the appropriate shifting variant based on variable declaration."* ([[dis-4-6-bitwise|Ch 4.6]]). The type of the **left operand** governs:

```c
unsigned int u_val = 0xFF000000;
int          s_val = 0xFF000000;
printf("%08X\n", u_val >> 12);  // 000FF000  (logical)
printf("%08X\n", s_val >> 12);  // FFFFF000  (arithmetic)
```

## Power-of-two arithmetic shortcuts

| Decimal operation | Bit-shift equivalent | Cost |
|---|---|---|
| `x * 2`     | `x << 1`  | 1 cycle, no carry propagation |
| `x * 16`    | `x << 4`  | 1 cycle |
| `x * 1024`  | `x << 10` | 1 cycle |
| `x / 2`  (unsigned, floor) | `x >> 1`  | 1 cycle |
| `x / 256` (unsigned, floor) | `x >> 8`  | 1 cycle |
| `x % (1<<N)` (unsigned)     | `x & ((1<<N) - 1)` | 1 cycle (mask, not shift) |

Modern compilers perform **strength reduction** automatically — `x * 8` compiles to `shl 3` without programmer intervention. The pattern survives in hand-tuned code mostly for: (a) hot-path arithmetic on platforms with slow `MUL` / `DIV` (embedded MCUs, [[ARMCortexM|Cortex-M0]] has no hardware divide); (b) modular arithmetic with power-of-two moduli; (c) bit-field manipulation alongside [[BitwiseOperator|bitwise AND/OR]].

## C undefined-behaviour pitfalls

[[CLanguage|C]] imposes strict rules on shift operands; violations are [[UndefinedBehavior|UB]]:

| Pitfall | Example | Why |
|---|---|---|
| **Shift ≥ operand width** | `(uint32_t)x << 32` | UB — *"the behavior is undefined if the right operand is negative, or greater than or equal to the width of the promoted left operand"* (C standard) |
| **Negative shift amount** | `x << -1` | UB |
| **Signed left shift past sign bit** | `(int)0x40000000 << 1` | UB in C (the result would change sign) |
| **Right-shift of signed negative** | `(-1) >> 1` | Implementation-defined pre-C++20 (logical or arithmetic) — most compilers do arithmetic |

The chapter stays at hardware mechanics — these UB rules are wiki-only context but **load-bearing in real code**.

## Hardware mapping

| Operator | x86 instruction | ARM instruction | Notes |
|---|---|---|---|
| `<<`  | `SHL` / `SAL` | `LSL` | Shifts in zeros from the right |
| `>>` (unsigned, [[LogicalRightShift\|logical]]) | `SHR` | `LSR` | Shifts in zeros from the left |
| `>>` (signed, [[ArithmeticRightShift\|arithmetic]]) | `SAR` | `ASR` | Sign-extends from the left |

Single-cycle on virtually every ISA since the 1970s — implemented as a **barrel shifter** (a switch network, no gates beyond multiplexers). [[ARM]] additionally embeds free shifts into the second operand of most data-processing instructions (`ADD r0, r1, r2, LSL #3` is one cycle).

## See also

- [[BitwiseOperator]] — the boolean bit-level family (`&` / `|` / `^` / `~`).
- [[LogicalRightShift]] — the zero-fill right-shift variant for unsigned operands.
- [[ArithmeticRightShift]] — the sign-replicating right-shift variant for signed operands.
- [[TwosComplement]] — the encoding whose [[SignBit|sign-bit]] semantics drive the arithmetic-shift rule.
- [[SignBit]] — the bit replicated by arithmetic right shift.
- [[IntegerOverflow]] — left-shift overflow follows the same rules as multiplication.
- [[UndefinedBehavior]] — shift-by-≥-width and signed-shift-overflow are UB in C.
- [[BinaryMultiplication]] / [[BinaryDivision]] — the long-form algorithms shifts replace for power-of-two operands.
- [[dis-4-6-bitwise|Dive into Systems Ch 4.6]] — primary source.
- [[dis-4-4-3-mult-div|Dive into Systems Ch 4.4.3]] — the chapter that flagged the bit-shift shortcut as out of scope; Ch 4.6 delivers it.
