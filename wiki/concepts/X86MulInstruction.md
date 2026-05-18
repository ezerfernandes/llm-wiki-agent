---
title: "x86-64 `imul` Instruction"
type: concept
tags: [x86-64, assembly, instruction, arithmetic, multiplication]
sources: [dis-7-3-x86-64-arithmetic]
last_updated: 2026-05-17
---

# `imul` — Signed Integer Multiplication

The **`imul S, D` instruction** is [[X86_64|x86-64]]'s **signed integer multiplication primitive** per [[dis-7-3-x86-64-arithmetic|Ch 7.3]] — two-operand, [[AtAndTSyntax|AT&T order]] source-first:

```
imul S, D    # D ← S × D    (truncated to 64 bits on overflow)
```

## Operand structure

Same three-type operand framework as [[X86MovInstruction|`mov`]] and [[X86ArithmeticInstructions|`add` / `sub`]] — `S` may be [[Constant|constant]] / [[CpuRegister|register]] / [[MemoryOperand|memory]]; `D` is register or memory; destination is also a source. The [[dis-7-1-x86-64-basics|Ch 7.1]] *at-most-one-memory-operand* rule applies. Implicit [[OperandSize|operand-size]] suffix (`imulq`, `imull`, etc.) selects the width.

## Overflow semantics

Per [[dis-7-3-x86-64-arithmetic|Ch 7.3]]: *"truncates the result to 64 bits in the case of overflow"* — the full product of two 64-bit operands is up to 128 bits, but the two-operand `imul S, D` form keeps only the **low 64 bits**. Multiplication is the [[BinaryMultiplication|partial-product summation]] algorithm of [[dis-4-4-3-mult-div|Ch 4.4.3]] implemented in hardware; sign is handled implicitly by the `i` (integer / signed) prefix. The matching unsigned form `mul` is out of [[dis-7-3-x86-64-arithmetic|Ch 7.3]]'s scope.

## Compiler strength-reduction

When the multiplier is a **power of two**, compilers typically replace `imul` with a [[X86ShiftInstructions|left shift]] — per [[dis-7-3-x86-64-arithmetic|Ch 7.3]]: *"to compute `77 * 4`, most compilers will translate this operation to `77 << 2` to avoid the use of an `imul` instruction"* — `shl` executes in fewer cycles than `imul` on most microarchitectures. The [[BitShift|shift-as-multiply]] [[CompilerOptimization|strength-reduction]] is the canonical assembly-level instantiation of the [[dis-4-6-bitwise|Ch 4.6]] C-level `x << k == x * (1<<k)` identity.

## Connections

- [[dis-7-3-x86-64-arithmetic]] — **introducing source**.
- [[X86_64]] — the ISA the instruction belongs to.
- [[X86DivInstruction]] — sibling integer-arithmetic primitive (division).
- [[X86ArithmeticInstructions]] — `add` / `sub` siblings with same operand structure.
- [[X86ShiftInstructions]] — power-of-two `imul` is typically lowered to `shl`.
- [[BinaryMultiplication]] — the bit-level partial-product algorithm `imul` implements.
- [[CompilerOptimization]] — the *imul → shl* power-of-two strength-reduction move.
- [[IntegerOverflow]] — the truncate-to-64-bits semantic.
