---
title: "x86-64 Single-Operand Arithmetic (`neg` / `inc` / `dec`)"
type: concept
tags: [x86-64, assembly, instruction, arithmetic, negation, increment, decrement]
sources: [dis-7-3-x86-64-arithmetic]
last_updated: 2026-05-17
---

# `neg` / `inc` / `dec` — Single-Operand Arithmetic

Per [[dis-7-3-x86-64-arithmetic|Ch 7.3]], [[X86_64|x86-64]] supplies three **single-operand arithmetic instructions** that complement the two-operand [[X86ArithmeticInstructions|`add` / `sub`]] family — read-modify-write transformations applied in place to the destination operand:

```
neg D    # D ← -D    (two's-complement negation)
inc D    # D ← D + 1 (increment)
dec D    # D ← D - 1 (decrement)
```

## `neg` — full two's-complement negation

`neg D` writes the [[TwosComplement|two's-complement]] negation of `D` back into `D`. Implements the *flip all the bits and add one* recipe [[dis-4-3-signed|Ch 4.3]] codified — the **full** negation, not the bit-flip alone. The wiki's central distinction (carried to the assembly level by [[dis-7-3-x86-64-arithmetic|Ch 7.3]]): `neg` ≠ [[X86BitwiseInstructions|`not`]] — *"the `not` instruction flips the bits but does not add 1"* — so `~x = -x - 1` at the bit-pattern level (the [[BitwiseNot|`~` identity]] from [[dis-4-6-bitwise|Ch 4.6]]).

## `inc` / `dec` — specialized add/sub-by-one

`inc D` and `dec D` are encoding shortcuts for `add $1, D` and `sub $1, D` — same semantics, more compact instruction encoding. Used pervasively for [[ForLoop|loop counters]] and [[PointerArithmetic|pointer]] step. They are functionally redundant with `add` / `sub` but exist for the same reason `push` / `pop` exist as separate instructions from `mov` + `sub`/`add` against [[StackPointer|`%rsp`]]: ubiquity in compiled code justifies a dedicated short encoding.

## Operand structure

`D` may be [[CpuRegister|register]] or [[MemoryOperand|memory]] (never a [[Constant|constant]] — these are read-modify-write). [[OperandSize|Operand-size suffix]] (`negq`, `incl`, `decw`, ...) selects width. Like all x86 read-modify-write arithmetic, condition codes in `%eflags` are updated implicitly.

## Connections

- [[dis-7-3-x86-64-arithmetic]] — **introducing source**.
- [[X86_64]] — the ISA.
- [[X86ArithmeticInstructions]] — the two-operand `add` / `sub` siblings; `inc` / `dec` are specialized one-operand forms.
- [[X86BitwiseInstructions]] — `not` (bit-flip only) is the *off-by-one* contrast that defines `neg`.
- [[TwosComplement]] — the encoding `neg` realizes via *flip-and-add-one*.
- [[dis-4-3-signed]] — the bit-pattern-level derivation of the negation recipe.
- [[IncrementOperator]] — [[CLanguage|C]]'s `++` / `--`, which compilers typically lower to `inc` / `dec`.
