---
title: "Stack Pointer (`%rsp`)"
type: concept
tags: [x86-64, assembly, register, stack, calling-convention]
sources: [dis-7-5-x86-64-functions, dis-7-2-x86-64-common, dis-7-1-x86-64-basics]
last_updated: 2026-05-17
---

# Stack Pointer (`%rsp`)

The **stack pointer** `%rsp` is the [[X86_64|x86-64]] special-purpose register that **always points to the top of the [[CallStack|call stack]]**. Per [[dis-7-5-x86-64-functions|Ch 7.5]]:

> "The stack pointer (`%rsp`) always points to the top of the stack."

Promoted from forward reference to first-class page with the Ch 7.5 ingest — was first flagged in [[dis-7-2-x86-64-common|Ch 7.2]]'s [[X86StackInstructions|stack-instruction]] coverage.

## Invariant

At any well-formed point in program execution, `(%rsp)` is the most-recently-pushed value on the [[ExecutionStack|execution stack]]. Every instruction that touches the stack maintains this invariant:

- [[X86StackInstructions|`push S`]] — *decrements* `%rsp` by 8, then writes `S` to `(%rsp)`.
- [[X86StackInstructions|`pop D`]] — reads `(%rsp)` into `D`, then *increments* `%rsp` by 8.
- [[CallInstruction|`callq addr`]] — pushes the return address, decrementing `%rsp` by 8.
- [[RetInstruction|`retq`]] — pops the return address, incrementing `%rsp` by 8.
- [[LeaveInstruction|`leaveq`]] — restores `%rsp` from [[FramePointer|`%rbp`]] as part of the function epilogue.

## Stack-grows-down convention

[[X86_64|x86-64]] stacks **grow toward lower memory addresses** — so *push* is *decrement-then-write* and *pop* is *read-then-increment*. The "top" of the stack is at the **lowest** address occupied by stack data; the "bottom" is the high address where the OS originally placed the [[StackSection|stack segment]].

## Width and the 8-byte step

`%rsp` is a 64-bit register and every push/pop moves 8 bytes — the [[OperandSize|`q` size suffix]] is implicit for stack ops. Sub-register names exist (`%esp` for 32-bit, `%sp` for 16-bit, `%spl` for 8-bit) but are rarely used in 64-bit code.

## 16-byte alignment requirement

The **System V AMD64 ABI** requires `%rsp` to be **16-byte aligned at the moment of [[CallInstruction|`callq`]]** — so that after the 8-byte return address is pushed, the callee sees `%rsp` aligned to `8 mod 16` at function entry. Compilers maintain this with extra `sub $8, %rsp` padding in function prologues when local-variable allocation would otherwise mis-align the stack. Violating this constraint causes mysterious crashes on SSE / AVX instructions which require 16-byte-aligned operands.

## Relation to `%rbp`

`%rsp` (the top of the stack) and [[FramePointer|`%rbp`]] (the base of the current [[StackFrame|stack frame]]) bracket the **current function's local-variable area**. `%rsp` moves around as the function pushes intermediate values; `%rbp` stays fixed for the function's lifetime, providing a stable anchor for variable references that are immune to `%rsp` motion.

## Callee-saved status

`%rsp` is implicitly [[CalleeSavedRegister|callee-saved]] — the function must restore `%rsp` to its entry-value before [[RetInstruction|`retq`]], or the return will branch to garbage. The [[LeaveInstruction|`leaveq`]] instruction handles this restoration mechanically.

## Connections

- [[dis-7-5-x86-64-functions]] — **introducing source** (promoting source for the first-class page); defines the `%rsp` invariant and its role in the calling convention.
- [[dis-7-2-x86-64-common]] — first introduced `%rsp` as the [[X86StackInstructions|`push` / `pop`]] target; flagged for later promotion.
- [[dis-7-1-x86-64-basics]] — names `%rsp` as one of the three special-purpose registers alongside [[FramePointer|`%rbp`]] and [[InstructionPointer|`%rip`]].
- [[FramePointer]] — the partner register `%rbp`; together `[%rsp, %rbp]` brackets the current [[StackFrame|stack frame]].
- [[X86StackInstructions]] — the instructions whose entire purpose is adjusting `%rsp`.
- [[CallInstruction]] / [[RetInstruction]] — the function-call instructions that adjust `%rsp` by 8 each.
- [[LeaveInstruction]] — restores `%rsp` from `%rbp` in the function epilogue.
- [[CallStack]] / [[ExecutionStack]] — the data structure `%rsp` points to the top of.
- [[StackFrame]] — the per-function activation record `%rsp` and `%rbp` bracket.
- [[StackSection]] — the [[ProcessMemory|process-memory]] region the stack lives in.
- [[GeneralPurposeRegister]] — `%rsp` is technically one of the 16 GPRs but its dedicated role makes it special-purpose in practice.
- [[X86_64]] — the ISA.
- [[CallingConvention]] — the System V AMD64 ABI that mandates `%rsp` 16-byte alignment at call sites.
