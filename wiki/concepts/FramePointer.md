---
title: "Frame Pointer (`%rbp`)"
type: concept
tags: [x86-64, assembly, register, stack, stack-frame, calling-convention]
sources: [dis-7-5-x86-64-functions, dis-7-2-x86-64-common, dis-7-1-x86-64-basics]
last_updated: 2026-05-17
---

# Frame Pointer (`%rbp`)

The **frame pointer** `%rbp` is the [[X86_64|x86-64]] special-purpose register that **points to the base of the current [[StackFrame|stack frame]]**. Per [[dis-7-5-x86-64-functions|Ch 7.5]]:

> "The frame pointer (`%rbp`) points to the base of the current stack frame."

Promoted from forward reference to first-class page with the Ch 7.5 ingest — was first flagged in [[dis-7-2-x86-64-common|Ch 7.2]]'s [[X86StackInstructions|stack-instruction]] coverage.

## Invariant

For the lifetime of a function compiled **with a frame pointer**, `%rbp` is **established once at function entry and held constant** until the epilogue. Unlike [[StackPointer|`%rsp`]] (which moves with every push/pop), `%rbp` provides a **stable anchor** for accessing local variables and parameters via fixed offsets — `-8(%rbp)`, `-16(%rbp)`, etc. for locals; `16(%rbp)` and beyond for stack-passed arguments.

## Establishment in the prologue

The canonical [[X86_64|x86-64]] function prologue establishes `%rbp` in two instructions:

```
push %rbp          # save caller's frame pointer
mov  %rsp, %rbp    # establish new frame base
```

After these two instructions:
- `(%rbp)` holds the **saved caller's `%rbp`** (forms a backward chain of frames along the [[ExecutionStack|execution stack]]).
- `8(%rbp)` holds the **return address** (pushed by the caller's [[CallInstruction|`callq`]]).
- `16(%rbp)` and beyond hold **stack-passed arguments** (the 7th-and-later parameters under the System V [[CallingConvention|calling convention]]).
- `-8(%rbp)`, `-16(%rbp)`, ... hold **local variables** (allocated below `%rbp` by `sub $N, %rsp`).

## Teardown in the epilogue

The function epilogue restores `%rbp` via [[LeaveInstruction|`leaveq`]] (or its longhand `mov %rbp, %rsp; pop %rbp`). After `leaveq`, `%rbp` holds the caller's frame pointer again and `%rsp` points to the saved return address — ready for [[RetInstruction|`retq`]].

## The frame chain

Walking the linked list of saved-`%rbp` values yields the **call stack trace** — `(%rbp)` is the caller's `%rbp`, `((%rbp))` is the caller's caller's `%rbp`, and so on until you hit the entry frame. Debuggers like [[GDB]] use this chain to implement `backtrace` / `info stack` — when the chain is intact, stack-walking is mechanical; when frame pointers are omitted (see below), the debugger must use DWARF unwind info instead.

## Frame-pointer omission (`-fomit-frame-pointer`)

Modern compilers with `-O1` or higher often **omit `%rbp` entirely** as an optimization — local variables and arguments are accessed via `%rsp` directly, freeing `%rbp` for general use as a 17th general-purpose register. Trade-offs:

- **Pros**: one extra register available for the register allocator; smaller code (no prologue/epilogue `%rbp` save+restore); slightly faster (two fewer instructions per function).
- **Cons**: harder to walk the stack in a debugger (must rely on DWARF unwind info instead of the frame chain); some profilers / sampling tools have degraded accuracy without it.

This is why production binaries are often built with `-fno-omit-frame-pointer` despite the optimization — debuggability wins over micro-optimization.

## Callee-saved status

`%rbp` is [[CalleeSavedRegister|callee-saved]] under the System V [[CallingConvention|calling convention]] — the `push %rbp` at function entry **is** the save, and the corresponding `pop %rbp` (via [[LeaveInstruction|`leaveq`]]) at exit is the restore. Functions that omit the frame pointer still preserve `%rbp` (because the convention requires it) — they just don't use it for frame anchoring.

## Connections

- [[dis-7-5-x86-64-functions]] — **introducing source** (promoting source for the first-class page); defines the `%rbp` invariant and its role in the canonical prologue/epilogue.
- [[dis-7-2-x86-64-common]] — first introduced `%rbp` via the `adder2` `push %rbp` / `pop %rbp` pair; flagged for later promotion.
- [[dis-7-1-x86-64-basics]] — names `%rbp` as one of the three special-purpose registers alongside [[StackPointer|`%rsp`]] and [[InstructionPointer|`%rip`]].
- [[StackPointer]] — the partner register `%rsp`; together `[%rsp, %rbp]` brackets the current [[StackFrame|stack frame]].
- [[StackFrame]] — the per-function activation record `%rbp` anchors the base of.
- [[LeaveInstruction]] — restores `%rbp` from the stack in the function epilogue.
- [[CallInstruction]] / [[RetInstruction]] — `%rbp` is **not** touched by `callq` / `retq` themselves; the prologue/epilogue handle the save/restore.
- [[CalleeSavedRegister]] — the ownership class `%rbp` belongs to under System V.
- [[CallingConvention]] — the convention under which `%rbp` is callee-saved.
- [[GDB]] — uses the saved-`%rbp` chain to implement `backtrace`.
- [[GeneralPurposeRegister]] — `%rbp` is one of the 16 GPRs; its frame-pointer role is a software convention, not a hardware constraint.
- [[X86_64]] — the ISA.
