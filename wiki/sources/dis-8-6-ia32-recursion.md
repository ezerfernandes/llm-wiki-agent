---
title: "Dive into Systems — Ch 8.6 Recursion (IA32)"
type: source
tags: [dive-into-systems, ia32, assembly, recursion, call-stack, stack-frame, 32-bit]
date: 2026-05-17
source_file: https://diveintosystems.org/book/C8-IA32/recursion.html
sources: []
last_updated: 2026-05-17
---

## Summary

Chapter 8.6 of *[[DiveIntoSystems]]* — **sixth leaf** of Ch 8 *32-bit IA32 Assembly* and the **32-bit structural twin** of [[dis-7-6-x86-64-recursion|Ch 7.6]]. Applies the [[dis-8-5-ia32-functions|Ch 8.5]] function-call discipline ([[CallInstruction|`call`]] / [[RetInstruction|`ret`]] / [[LeaveInstruction|`leave`]] + [[CdeclCallingConvention|cdecl]] prologue/epilogue) to **self-referential functions** — proving that [[Recursion|recursion]] needs **no new mechanism**: each recursive [[CallInstruction|`call`]] simply pushes a new [[StackFrame|stack frame]] onto the [[CallStack|call stack]], and the saved-[[FramePointer|`%ebp`]] chain links frames into a stack-growing linked-list that [[LeaveInstruction|`leave`]] / [[RetInstruction|`ret`]] unwinds in reverse order. **Headline 32-vs-64 deltas**: (1) recursive parameter `n` is read from `0x8(%ebp)` per [[CdeclCallingConvention|cdecl]] — *not* from `%edi` per [[SystemVCallingConvention|System V]]; (2) the recursive [[CallInstruction|`call`]] pushes a **4-byte** saved-`%eip` (vs Ch 7.6's 8-byte saved-`%rip`); (3) local-variable allocation uses `sub $0x8, %esp` (8 bytes — IA32 still respects 4-byte alignment but the local-region size is dictated by [[GCC]] codegen, not register width); (4) recursive call to argument re-push pattern: `mov 0x8(%ebp), %eax; sub $1, %eax; push %eax; call sumr` — argument is pushed (not loaded into `%edi`); (5) frame-cleanup after return: `add $0x4, %esp` (caller cleanup per cdecl, vs no-cleanup needed when args were in registers). **Headline rule carries over unchanged**: *"each function call generates a new stack frame"* — recursion adds **no new instruction**, only stack-frame stacking. **85th ingested DIS chapter — sixth leaf of Ch 8.** **No new concept pages** — reuses [[Recursion]], [[CallStack]], [[StackFrame]], [[ExecutionStack]] from [[dis-7-6-x86-64-recursion|Ch 7.6]].

## Key Claims

- **Recursion needs no new instruction — only the [[dis-8-5-ia32-functions|Ch 8.5]] function-call discipline applied self-referentially.** Each recursive [[CallInstruction|`call sumr`]] pushes a new saved-`%eip` (4 bytes) + executes the standard prologue (`push %ebp; mov %esp, %ebp; sub $N, %esp`), producing a new [[StackFrame|stack frame]] for the recursive instance. The [[CallStack|call stack]] therefore grows linearly with recursion depth — **proportional to the longest call chain**, not to the total number of calls.
- **Saved-[[FramePointer|`%ebp`]] linked-list links frames.** The prologue's `push %ebp` saves the **previous** frame's base pointer at `(%ebp)` of the **current** frame — building a singly-linked list of frames backward along the [[ExecutionStack|execution stack]]. [[LeaveInstruction|`leave`]] pops this saved-`%ebp` back into `%ebp` on epilogue, restoring the caller's frame anchor — exactly the unwind step recursion requires.
- **[[CdeclCallingConvention|Cdecl]] parameter re-push.** Each recursive level reads its parameter from `0x8(%ebp)` (its own frame), computes the next argument (e.g., `sub $1, %eax`), and **pushes** it (`push %eax`) before the [[CallInstruction|`call`]] — vs [[dis-7-6-x86-64-recursion|Ch 7.6]]'s `mov %eax, %edi` register-load. Caller cleanup (`add $0x4, %esp`) after return removes the pushed argument.
- **Return-value chaining via [[CalleeSavedRegister|`%eax`]].** Each recursive return lands its value in `%eax`; the caller frame reads it (typically via `add %eax, -0x4(%ebp)` or similar) before its own return. The `%eax` write-then-read pattern chains return values up the unwind path — identical algebra to Ch 7.6, only the register name narrows from `%rax`.
- **Stack growth is the recursion bound.** Because each frame consumes saved-`%eip` (4 bytes) + saved-`%ebp` (4 bytes) + local space (here 8 bytes = 16 bytes total per frame), recursion depth × 16 bytes ≈ stack-space cost. Deep recursion can exhaust the [[CallStack|call stack]] — the underlying mechanism the *stack overflow* error names; the security-payoff [[BufferOverflow|buffer overflow]] discussion of [[dis-8-10-ia32-buffer-overflow|Ch 8.10]] inverts this discipline by **writing past** the buffer to overwrite saved-`%eip`.

## Key Quotes

> "Recursive functions are a special class of functions that call themselves (also known as self-referential functions) to compute a value." — recursion as definitional self-reference, no new mechanism required.

> "Each function call generates a new stack frame" — the [[CallStack|call-stack]] discipline that makes recursion work *for free* given [[dis-8-5-ia32-functions|Ch 8.5]]'s prologue/epilogue.

## Connections

- [[DiveIntoSystems]] — book; **85th ingested chapter**, sixth leaf of Ch 8 *32-bit IA32 Assembly*.
- [[SuzanneJMatthews]] / [[TiaNewhall]] / [[KevinCWebb]] — co-authors.
- [[dis-7-6-x86-64-recursion]] — **structural twin** at [[X86_64|x86-64]] width.
- [[dis-8-5-ia32-functions]] — Ch 8.5; direct predecessor — Ch 8.6 simply applies its [[CallInstruction|`call`]] / [[RetInstruction|`ret`]] / [[LeaveInstruction|`leave`]] + [[CdeclCallingConvention|cdecl]] prologue/epilogue self-referentially.
- [[Recursion]] — the algorithmic pattern Ch 8.6 compiles at IA32 width.
- [[CallStack]] / [[ExecutionStack]] / [[StackFrame]] — the per-recursive-instance activation record stack — *"each function call generates a new stack frame"*.
- [[CdeclCallingConvention]] — parameter-push + caller-cleanup pattern that makes recursion's argument re-staging explicit (vs register-renaming on System V).
- [[CallInstruction]] / [[RetInstruction]] / [[LeaveInstruction]] — reused from [[dis-8-5-ia32-functions|Ch 8.5]]; IA32 mnemonics (no `q` suffix).
- [[StackPointer]] / [[FramePointer]] — `%esp` / `%ebp` invariants the recursive prologue/epilogue manipulates.
- [[IA32]] — the 32-bit ISA.

## Contradictions

None. Ch 8.6 is a **consistent 32-bit re-presentation** of [[dis-7-6-x86-64-recursion|Ch 7.6]] — recursion semantics, frame-stacking discipline, and saved-frame-pointer chain are structurally identical; the [[CdeclCallingConvention|cdecl]] parameter-re-push pattern was already implicit in [[dis-8-5-ia32-functions|Ch 8.5]].
