---
title: "Dive into Systems — Ch 7.5 Functions in Assembly (x86-64)"
type: source
tags: [dive-into-systems, x86-64, assembly, functions, calling-convention, stack-frame]
date: 2026-05-17
source_file: https://diveintosystems.org/book/C7-x86_64/functions.html
sources: []
last_updated: 2026-05-17
---

## Summary

Chapter 7.5 of *[[DiveIntoSystems]]* — **fifth leaf** of Ch 7 *x86-64 Assembly* — closes the per-ISA tour by adding **the function-call instruction family** on top of the [[dis-7-1-x86-64-basics|register / operand]] / [[dis-7-2-x86-64-common|data-movement / stack]] / [[dis-7-3-x86-64-arithmetic|arithmetic]] / [[dis-7-4-x86-64-conditional-loops|control-flow]] surface assembled by 7.1–7.4. Operationalizes the **System V AMD64 [[CallingConvention|calling convention]]** at the [[X86_64|x86-64]] [[AssemblyLanguage|assembly]] level: two new control-flow instructions ([[CallInstruction|`callq`]] / [[RetInstruction|`retq`]]) that push and pop the saved return address against the [[CallStack|call stack]]; the **six argument registers** (`%rdi` / `%rsi` / `%rdx` / `%rcx` / `%r8` / `%r9` for the first six parameters, stack for the rest); `%rax` as the return-value register; and the [[CallerSavedRegister|caller-saved]] vs [[CalleeSavedRegister|callee-saved]] partition that determines which side of a call boundary owns the preservation of each register.

## Key Claims

- **Two new instructions complete the [[ControlFlow|control-flow]] family.** [[CallInstruction|`callq addr`]] *"pushes the current value of [[InstructionPointer|`%rip`]] onto the stack and jumps to the function address"* — atomically saving the return address and transferring control. [[RetInstruction|`retq`]] *"pops the saved return address from the stack back into `%rip`"* — the inverse operation. Together they extend Ch 7.4's `%rip`-modification primitive (conditional + unconditional jumps) with a **structured pair** that also manages the return-address stack discipline.
- **Two register-pair invariants govern stack-frame management.** [[StackPointer|`%rsp`]] *"always points to the top of the stack"* — adjusted by every [[X86StackInstructions|`push` / `pop`]] and by every [[CallInstruction|`callq`]] / [[RetInstruction|`retq`]]. [[FramePointer|`%rbp`]] *"points to the base of the current stack frame"* — established once at function entry and held constant for the function's lifetime, providing a **stable anchor** for local-variable and parameter offsets even as `%rsp` moves around. Together they bracket the current [[StackFrame|stack frame]] — `[%rsp, %rbp]` is the frame, with the **saved `%rbp`** at `(%rbp)` linking to the caller's frame (a singly-linked-list of frames along the [[ExecutionStack|execution stack]]).
- **System V calling convention — registers 1–6, stack for the rest.** First six arguments go in `%rdi` / `%rsi` / `%rdx` / `%rcx` / `%r8` / `%r9` (the order matters — `%rdi` is always the first parameter, never the second); seventh-and-beyond *"are successively loaded into the call stack based on their size"*. Return value is in `%rax` (or a sub-register — `%eax` for 32-bit returns, `%ax` for 16-bit, `%al` for 8-bit per the [[OperandSize|operand-size]] suffix table from [[dis-7-1-x86-64-basics|Ch 7.1]]).
- **Canonical function prologue / epilogue pattern.** Prologue (function entry): `push %rbp` (save caller's frame pointer onto stack); `mov %rsp, %rbp` (establish new frame base — `%rbp` now points to the saved-`%rbp` slot); `sub $N, %rsp` (allocate `N` bytes of local-variable space, only if needed). Epilogue (function exit): [[LeaveInstruction|`leaveq`]] (the dedicated bundled instruction — *"equivalent to `mov %rbp, %rsp` then `pop %rbp`"* — restores both pointers in one op); [[RetInstruction|`retq`]] (pop saved `%rip` back into `%rip`). The leaveq+retq pair undoes everything the prologue did, restoring the caller's frame intact.
- **[[CallerSavedRegister|Caller-saved]] vs [[CalleeSavedRegister|callee-saved]] partition.** The 16 [[GeneralPurposeRegister|GPRs]] split into two ownership classes across a [[CallInstruction|`callq`]] boundary. **Caller-saved** (`%rax`, `%rcx`, `%rdx`, `%rsi`, `%rdi`, `%r8`–`%r11`) — the **caller** must spill any of these values it wants to keep across the call, because the callee is free to overwrite them. **Callee-saved** (`%rbx`, `%rbp`, `%r12`–`%r15`, plus `%rsp` implicitly) — if the **callee** uses any of these, it must save the old value at function entry and restore it at function exit (typically via `push`/`pop` in prologue/epilogue). The convention is a **contract** every well-formed function must follow — violating it corrupts the caller's state in subtle, hard-to-debug ways.

## Key Quotes

> "The stack pointer (`%rsp`) always points to the top of the stack." — the **`%rsp` invariant** every push/pop/call/ret must preserve.

> "The frame pointer (`%rbp`) points to the base of the current stack frame." — the **`%rbp` invariant** the function prologue establishes and the epilogue tears down.

> "`callq addr` pushes the current value of [[InstructionPointer|`%rip`]] onto the stack and jumps to the function address." — the [[CallInstruction|`callq`]] semantics: *jump + save* atomically.

> "`retq` pops the saved return address from the stack back into [[InstructionPointer|`%rip`]]." — the [[RetInstruction|`retq`]] semantics: *pop + jump* atomically.

> "`leaveq` is equivalent to `mov %rbp, %rsp` then `pop %rbp`." — the [[LeaveInstruction|`leaveq`]] shortcut that bundles the standard epilogue pointer-restoration into one instruction.

> "The first six parameters are passed in registers `%rdi`, `%rsi`, `%rdx`, `%rcx`, `%r8`, and `%r9`. Additional parameters are successively loaded into the call stack based on their size." — the System V six-argument-register rule.

## Connections

- [[DiveIntoSystems]] — parent textbook; this is the **70th ingested chapter** and the **fifth leaf** of Ch 7 *x86-64 Assembly*.
- [[dis-7-4-x86-64-conditional-loops]] — immediate predecessor (and its three subsections [[dis-7-4-1-x86-64-preliminaries|7.4.1]] / [[dis-7-4-2-x86-64-if-statements|7.4.2]] / [[dis-7-4-3-x86-64-loops|7.4.3]]); Ch 7.4 added the **conditional / unconditional jump** control-flow primitives. Ch 7.5 adds the **structured call/return pair** on top.
- [[dis-7-2-x86-64-common]] — Ch 7.2 introduced [[X86StackInstructions|`push` / `pop`]] against [[StackPointer|`%rsp`]]; Ch 7.5 builds on this primitive — [[CallInstruction|`callq`]] is functionally `push %rip; jmp addr` and [[RetInstruction|`retq`]] is functionally `pop %rip`. The `adder2` trace in Ch 7.2 was already using the prologue/epilogue pattern Ch 7.5 now names and formalizes.
- [[dis-7-1-x86-64-basics]] — the [[GeneralPurposeRegister|16 GPR]] inventory Ch 7.5 partitions into caller-saved vs callee-saved; the [[OperandSize|operand-size]] suffix table that governs `%rax` / `%eax` / `%ax` / `%al` return-value width.
- [[dis-1-4-functions]] — the **C-level original** of the constructs Ch 7.5 compiles down. Ch 1.4 introduces functions / parameters / [[ReturnStatement|`return`]] / the [[ExecutionStack|execution stack]] / [[StackFrame|stack frames]] at the source level; Ch 7.5 = the assembly-side complement.
- [[StackFrame]] — the per-call activation record Ch 7.5's prologue builds and the epilogue tears down. Ch 7.5 supplies its `%rbp`-anchored x86-64 realization.
- [[ExecutionStack]] — the LIFO of stack frames that Ch 7.5's [[CallInstruction|`callq`]] grows and [[RetInstruction|`retq`]] shrinks; saved-`%rbp` values link the frames into a backward chain.
- [[CallStack]] — synonym for [[ExecutionStack]] at this level.
- [[InstructionPointer]] — the `%rip` register [[CallInstruction|`callq`]] saves and [[RetInstruction|`retq`]] restores; the same register Ch 7.4's jump family modifies, now manipulated via the structured call/return pair.
- [[X86_64]] — the ISA; Ch 7.5 adds the function-call instruction family + the System V calling convention to its wiki-cataloged surface.

## Subsections (leaf coverage)

Ch 7.5 is a **single-page section**, not a hub. The wiki ingest mints **six new concept pages** plus promotes two forward references:

- **New**: [[CallInstruction]] ([[CallInstruction|`callq`]]), [[RetInstruction]] ([[RetInstruction|`retq`]]), [[LeaveInstruction]] ([[LeaveInstruction|`leaveq`]]), [[CallingConvention]] (System V AMD64), [[CallerSavedRegister]], [[CalleeSavedRegister]].
- **Promoted from forward reference**: [[StackPointer]] (`%rsp`), [[FramePointer]] (`%rbp`) — first flagged in [[dis-7-2-x86-64-common|Ch 7.2]]'s log entry, now first-class pages.

## Contradictions

None. Ch 7.5 **extends** the Ch 7 instruction-family tour with the function-call category — adds rather than revises. The prologue/epilogue pattern Ch 7.2's `adder2` trace exhibited is the same pattern Ch 7.5 formalizes; the [[X86StackInstructions|`push` / `pop`]] pair Ch 7.2 introduced remains the underlying primitive [[CallInstruction|`callq`]] / [[RetInstruction|`retq`]] specialize.
