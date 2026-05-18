---
title: "x86-64 `idiv` Instruction"
type: concept
tags: [x86-64, assembly, instruction, arithmetic, division]
sources: [dis-7-3-x86-64-arithmetic]
last_updated: 2026-05-17
---

# `idiv` — Signed Integer Division

The **`idiv S` instruction** is [[X86_64|x86-64]]'s **signed integer division primitive** per [[dis-7-3-x86-64-arithmetic|Ch 7.3]] — **single explicit operand** with two **implicit register operands**:

```
idiv S       # %rax / S → quotient in %rax, remainder in %rdx
```

## Hidden-operand convention

The defining quirk of `idiv` relative to [[X86ArithmeticInstructions|`add`/`sub`]] / [[X86MulInstruction|`imul`]] is the use of fixed registers as implicit operands. Per [[dis-7-3-x86-64-arithmetic|Ch 7.3]]: *"prior to the execution of the `idiv` instruction, it is assumed that register `%rax` contains the dividend."* — `%rax` is **both** the dividend source **and** the quotient destination; `%rdx` receives the remainder. The single explicit operand `S` (the divisor) may be [[Constant|constant]] / [[CpuRegister|register]] / [[MemoryOperand|memory]] per the standard three-type framework.

## Caller responsibility

Because the dividend lives in `%rax` (and on the full 128-bit form, the upper half lives in `%rdx`), the caller must **set up `%rax` before** the `idiv` — typically via [[X86MovInstruction|`mov`]] or by ensuring the prior instruction produced its result there. The pattern conflicts with the otherwise uniform two-explicit-operand structure of x86-64 arithmetic and is a frequent reading hazard in disassembled code: `idiv %rcx` is **not** *"divide `%rcx` by something"* — it is *"divide `%rax` by `%rcx`."*

## Connection to the C `/` and `%` operators

`idiv` is the assembly-level home of the [[IntegerDivision|C integer-division trap]] [[dis-1-1-getting-started|Ch 1.1]] flagged (`11/2 == 5`) and the `%` modulus operator — the same hardware instruction supplies both results in one execution. The [[BinaryDivision|trial-subtraction algorithm]] of [[dis-4-4-3-mult-div|Ch 4.4.3]] is what the hardware implements under the hood.

## Connections

- [[dis-7-3-x86-64-arithmetic]] — **introducing source**.
- [[X86_64]] — the ISA.
- [[X86MulInstruction]] — sibling integer-arithmetic primitive (multiplication).
- [[X86ArithmeticInstructions]] — `add` / `sub` siblings (the two-explicit-operand contrast).
- [[GeneralPurposeRegister]] — `%rax` / `%rdx` are the hidden operands.
- [[BinaryDivision]] — the bit-level trial-subtraction algorithm `idiv` implements.
- [[IntegerDivision]] — the [[CLanguage|C]]-level `/` and `%` operators `idiv` realizes.
