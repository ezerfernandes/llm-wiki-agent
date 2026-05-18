---
title: "x86-64 mov Instruction"
type: concept
tags: [x86-64, assembly, instruction, data-movement, mov]
sources: [dis-7-2-x86-64-common, dis-7-1-x86-64-basics]
last_updated: 2026-05-17
---

# `mov` — Data Movement

The **`mov` instruction** is [[X86_64|x86-64]]'s data-movement primitive — *"copies a source value into a destination"* per [[dis-7-2-x86-64-common|Ch 7.2]]. Two-operand form, [[AtAndTSyntax|AT&T order]] source-first:

```
mov S, D    # D ← S
```

## Operand combinations

The source `S` may be any of the three [[Operand|operand types]] from [[dis-7-1-x86-64-basics|Ch 7.1]] — [[Constant|constant / immediate]], [[CpuRegister|register]], or [[MemoryOperand|memory]]. The destination `D` may be **register or memory only** — `mov` cannot write to a constant (the general operand rule from Ch 7.1). The further [[dis-7-1-x86-64-basics|Ch 7.1]] constraint also applies: **at most one memory operand per instruction** — memory-to-memory moves are illegal and must be split into two `mov`s through a register.

## Size variants — `movb` / `movw` / `movl` / `movq`

Per the [[OperandSize|operand-size suffix]] table — `movb` (1 byte), `movw` (2 bytes), `movl` (4 bytes), `movq` (8 bytes). Selects which sub-register width the move operates on:

- `movq $0x10, %rax` — 64-bit immediate-to-register.
- `movl %edi, -0x4(%rbp)` — 32-bit register-to-stack-slot (the canonical *"spill argument to local"* idiom from the [[dis-7-2-x86-64-common|Ch 7.2]] `adder2` trace).
- `movl -0x4(%rbp), %eax` — 32-bit stack-slot-to-register (the *"reload local"* idiom).

## Use cases

The dominant instruction in any compiled function — every load, store, register copy, argument spill, return-value setup, and stack-slot save uses `mov`. In the [[dis-7-2-x86-64-common|Ch 7.2 `adder2` trace]], four of seven body instructions are `mov`s: prologue frame setup (`mov %rsp, %rbp`), argument spill (`mov %edi, -0x4(%rbp)`), local reload (`mov -0x4(%rbp), %eax`), and an implicit return-value setup. The remaining three instructions ([[X86ArithmeticInstructions|`add`]] / [[X86StackInstructions|`pop`]] / `retq`) handle the actual computation and control flow.

## Connections

- [[dis-7-2-x86-64-common]] — **introducing source**; the `mov` definition and the `adder2` trace.
- [[dis-7-1-x86-64-basics]] — operand-type and operand-size rules that constrain `mov`.
- [[X86_64]] — the ISA `mov` belongs to.
- [[Operand]] — the constant / register / memory taxonomy `mov` exercises.
- [[OperandSize]] — the `b` / `w` / `l` / `q` suffix selecting `mov`'s data width.
- [[X86ArithmeticInstructions]] — sibling primitives (`add` / `sub`) sharing the same operand structure.
- [[X86StackInstructions]] — `push` / `pop` are specialized stack-targeted `mov`s.
- [[AtAndTSyntax]] — the source-first ordering convention.
- [[CpuRegister]] / [[MemoryOperand]] — the operand kinds `mov` shuttles data between.
