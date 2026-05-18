---
title: "Dive into Systems — Ch 7.2 Common Instructions (x86-64)"
type: source
tags: [dive-into-systems, x86-64, assembly, instructions, mov, add, sub, push, pop, stack]
date: 2026-05-17
source_file: https://diveintosystems.org/book/C7-x86_64/common.html
---

## Summary

[[SuzanneJMatthews|Matthews]] / [[TiaNewhall|Newhall]] / [[KevinCWebb|Webb]]'s **Ch 7.2** of *[[DiveIntoSystems]]* — the **second leaf** of Ch 7 *x86-64 Assembly*, following [[dis-7-1-x86-64-basics|Ch 7.1]]'s [[CpuRegister|register]] / [[Operand|operand]] / [[X86AddressingMode|addressing-mode]] framing. Introduces the **five most common [[X86_64|x86-64]] instructions** every assembly reader must recognize on sight: the [[X86MovInstruction|data-movement primitive `mov`]], the [[X86ArithmeticInstructions|arithmetic pair `add` / `sub`]], and the [[X86StackInstructions|stack-management pair `push` / `pop`]]. Closes with a step-by-step trace of the `adder2` function from [[dis-7-1-x86-64-basics|Ch 7.1]] showing how the five instructions compose into a complete function prologue / body / epilogue, with register and [[CallStack|call-stack]] state tracked at each step. **Ch 7.2 does not cover `lea`** — load-effective-address is deferred to a later Ch 7 section.

## Key Claims

- **`mov S, D` is the data-movement primitive.** *"Copies a source value into a destination."* The source `S` may be a [[Constant|constant]], [[CpuRegister|register]], or [[MemoryOperand|memory]] operand; the destination `D` may be a register or memory operand (but **not a constant** — restated from [[dis-7-1-x86-64-basics|Ch 7.1]]'s general operand rules). The size suffix (`movb` / `movw` / `movl` / `movq`) selects the [[OperandSize|operand width]] (1 / 2 / 4 / 8 bytes).
- **`add S, D` is the addition primitive.** *"Adds source to destination, storing result in destination."* Semantically `D ← D + S`. Same operand restrictions as `mov`; sets the condition codes in `%eflags` as a side effect.
- **`sub S, D` is the subtraction primitive.** *"Subtracts source from destination, storing result in destination."* Semantically `D ← D − S` (**not** `S − D` — the source-first AT&T order makes this counterintuitive). Same operand restrictions and condition-code side effects as `add`.
- **`push S` writes the source onto the top of the [[CallStack|stack]].** Two-step semantics: *"decrement the stack pointer by 8 bytes, then write the value at the address `%rsp` now points to."* The stack **grows toward lower addresses** on [[X86_64|x86-64]], so push decrements `%rsp`; the 8-byte step matches the 64-bit register width.
- **`pop D` removes the top stack element into a destination.** Inverse of `push`: read 8 bytes at `(%rsp)`, then **increment `%rsp` by 8** — the popped slot is left logically free (no zeroing). Same stack-grows-down convention as push.
- **Worked `adder2` trace.** The 4-instruction `adder2(a) { return a + 2; }` body decomposes into: `push %rbp` (save caller's frame pointer onto the stack) → `mov %rsp, %rbp` (establish new frame) → `mov %edi, -0x4(%rbp)` (spill the first argument `a` from the System V argument register `%rdi` into a local stack slot) → `mov -0x4(%rbp), %eax` (load `a` back into the return-value register `%eax`) → `add $0x2, %eax` (the `+ 2`) → `pop %rbp` (restore the caller's frame pointer) → `retq` (return). The trace illustrates **how `push` / `pop` and `%rbp`-relative addressing keep the [[CallStack|call stack]] balanced** across the function — every push paired with a pop, the stack restored to its entry state before `retq`.
- **Stack discipline is the invariant.** Proper use of `push` / `pop` and frame-pointer management *"restores the call stack to its original state when a function completes"* — the structural contract every well-formed x86-64 function must uphold.

## Key Quotes

> "mov S, D — copies a source value into a destination." — the [[X86MovInstruction|`mov`]] one-line definition.

> "add S, D — adds source to destination, storing result in destination. sub S, D — subtracts source from destination, storing result in destination." — the [[X86ArithmeticInstructions|arithmetic-pair]] semantics.

> "push S — places a copy of the source onto the stack by decrementing the stack pointer by 8 bytes and writing the value." — the [[X86StackInstructions|`push`]] mechanism.

> "pop D — removes the top stack element and places it in the destination, incrementing the stack pointer by 8 bytes." — the [[X86StackInstructions|`pop`]] mechanism.

## Connections

- [[DiveIntoSystems]] — book; **64th ingested chapter**, second leaf of Ch 7 *x86-64 Assembly*.
- [[SuzanneJMatthews]] / [[TiaNewhall]] / [[KevinCWebb]] — authors.
- [[dis-7-1-x86-64-basics]] — direct predecessor; Ch 7.2 reuses Ch 7.1's [[CpuRegister|register]] / [[Operand|operand]] / [[X86AddressingMode|addressing-mode]] vocabulary.
- [[X86_64]] — the ISA whose instruction set Ch 7.2 begins enumerating.
- [[X86MovInstruction]] — new concept: the data-movement primitive `mov`.
- [[X86ArithmeticInstructions]] — new concept: the `add` / `sub` arithmetic pair.
- [[X86StackInstructions]] — new concept: the `push` / `pop` stack-management pair.
- [[CallStack]] / [[StackFrame]] — the data structure `push` / `pop` manipulate; the `adder2` trace makes the frame mechanics concrete.
- [[StackPointer]] — `%rsp`; decremented by `push`, incremented by `pop`.
- [[FramePointer]] — `%rbp`; saved/restored by the function prologue/epilogue.
- [[Operand]] — the three operand types Ch 7.1 named; Ch 7.2 exercises them on real instructions.
- [[OperandSize]] — the `b`/`w`/`l`/`q` suffix that selects per-instruction data width (`addl`, `movq`).
- [[AtAndTSyntax]] — source-first `mov src, dst` order is the convention Ch 7.2 implicitly assumes.

## Contradictions

None. Ch 7.2 is **consistent extension** of [[dis-7-1-x86-64-basics|Ch 7.1]] — the operand-type and operand-size rules Ch 7.1 stated abstractly are applied concretely to `mov` / `add` / `sub` / `push` / `pop`. **Scope note**: the [[LeaInstruction|`lea`]] instruction is **not** introduced here despite being commonly grouped with these primitives in other x86-64 references — it appears in a later Ch 7 section.
