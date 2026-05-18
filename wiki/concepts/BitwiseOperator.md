---
title: "Bitwise Operator"
type: concept
tags: [bitwise, c-language, binary, digital-logic, computer-systems]
sources: [dis-4-6-bitwise]
last_updated: 2026-05-17
---

# Bitwise Operator

A **bitwise operator** applies a [[LogicGate|logic-gate]] operation **independently to each bit position** of its operands, producing a same-width result. Per [[dis-4-6-bitwise|Dive into Systems Ch 4.6]], bitwise operators *"directly apply logic gate behavior to bit sequences"* — they are the per-bit instantiation of [[DigitalLogic|digital-logic]] primitives, executing in a single clock cycle with no carry propagation. [[CLanguage|C]] exposes four bit-level boolean operators (`&`, `|`, `^`, `~`) plus the two [[BitShift|shift]] operators (`<<`, `>>`) covered separately.

## The four bit-level boolean operators

| Operator | Name | Arity | Per-bit rule | Truth table |
|---|---|---|---|---|
| `a & b` | [[BitwiseAnd\|Bitwise AND]] | binary | `1` iff **both** bits are `1` | $(0,0)\to 0$, $(0,1)\to 0$, $(1,0)\to 0$, $(1,1)\to 1$ |
| `a | b` | [[BitwiseOr\|Bitwise OR]] | binary | `1` iff **at least one** bit is `1` | $(0,0)\to 0$, $(0,1)\to 1$, $(1,0)\to 1$, $(1,1)\to 1$ |
| `a ^ b` | [[BitwiseXor\|Bitwise XOR]] | binary | `1` iff **exactly one** bit is `1` | $(0,0)\to 0$, $(0,1)\to 1$, $(1,0)\to 1$, $(1,1)\to 0$ |
| `~a` | [[BitwiseNot\|Bitwise NOT]] | unary | flip every bit | $0\to 1$, $1\to 0$ |

## Worked examples (Ch 4.6)

With `x = 26 = 0b011010`, `y = 54 = 0b110110`:

| Expression | Result | Bit pattern |
|---|---|---|
| `x & y` | `18` | `0b010010` |
| `x | y` | `62` | `0b111110` |
| `x ^ y` | `44` | `0b101100` |
| `~x`     | `-27` | `0b…11100101` (all leading bits also flipped) |

The `~x = -27` result reflects [[TwosComplement|two's complement]]: flipping every bit is *almost* negation but **one short** — *"bitwise NOT only flips the bits and doesn't add one"*. Identity: `~x = -x - 1`.

## Canonical idioms

| Goal | Idiom | Why it works |
|---|---|---|
| **Test** bit $i$ | `(x >> i) & 1` or `x & (1u << i)` | Mask isolates bit $i$ |
| **Set** bit $i$ to `1` | `x |= (1u << i)` | OR forces `1` while preserving others |
| **Clear** bit $i$ to `0` | `x &= ~(1u << i)` | Inverted mask keeps everything else |
| **Toggle** bit $i$ | `x ^= (1u << i)` | XOR with `1` flips, with `0` preserves |
| **Mask** a field | `(x >> shift) & ((1u << width) - 1)` | Right-align field, mask off the rest |
| **Pack** two fields | `(a << wa) | b` | Shift one up, OR with the other |
| **Detect difference** | `a ^ b` (zero iff equal) | XOR's annihilation-on-equal property |
| **Check single bit set** | `(x & (x-1)) == 0` | Power-of-two test; `x-1` clears the lowest set bit |

## Bitwise vs. logical operators

[[CLanguage|C]] distinguishes the per-bit family from the truth-value [[LogicalOperator|logical operators]] (`&&`, `||`, `!`):

| Aspect | Bitwise (`&`, `|`, `^`, `~`) | Logical (`&&`, `||`, `!`) |
|---|---|---|
| Operand interpretation | Bit pattern | Boolean (zero = false, non-zero = true) |
| Result | Same-width bit pattern | `0` or `1` |
| Short-circuits | No (always evaluates both operands) | Yes (stops on first decisive operand) |
| Typical use | Bit packing, masks, flags | Control-flow conditions |

*"Programmers often confuse the bitwise `&&` and `||` operators with `&` and `|` operators"* ([[dis-4-6-bitwise|Ch 4.6]]) — the headline category error: `if (flags & MASK_A && flags & MASK_B)` works only because `&` binds tighter than `&&`; mis-parenthesizing into `if (flags & (MASK_A && flags) & MASK_B)` silently does the wrong thing.

## Hardware mapping

| Operator | Logic gate | x86 instruction | ARM instruction |
|---|---|---|---|
| `&` | AND | `AND` | `AND` |
| `|` | OR  | `OR`  | `ORR` |
| `^` | XOR | `XOR` | `EOR` |
| `~` | NOT | `NOT` | `MVN` |

All four execute in **one clock cycle** with no carry propagation — the cheapest operations in the [[InstructionSetArchitecture|ISA]] (vs. multiply / divide / branch).

## See also

- [[BitShift]] — the `<<` / `>>` operator family ([[LogicalRightShift|logical]] / [[ArithmeticRightShift|arithmetic]] right-shift split).
- [[LogicalOperator]] — the `&&` / `||` / `!` truth-value family bitwise operators are routinely confused with.
- [[LogicGate]] — the per-bit hardware primitives bitwise operators map onto.
- [[TwosComplement]] — the encoding that makes `~x = -x - 1`.
- [[BinaryNumber]] — the bit-pattern substrate.
- [[UndefinedBehavior]] — shift-by-≥-width and signed-shift-overflow are UB in C (covered on [[BitShift]]).
- [[dis-4-6-bitwise|Dive into Systems Ch 4.6]] — primary source.
