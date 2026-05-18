---
title: "Callee-Saved Register"
type: concept
tags: [x86-64, assembly, register, calling-convention, abi]
sources: [dis-7-5-x86-64-functions]
last_updated: 2026-05-17
---

# Callee-Saved Register

A **callee-saved register** (a.k.a. *non-volatile* / *preserved* register) is one whose value the **callee** is responsible for preserving across a [[CallInstruction|`callq`]] boundary. If the callee uses one, it must save the old value at function entry and restore it at function exit. Per [[dis-7-5-x86-64-functions|Ch 7.5]]: the other half of the register-preservation partition that the System V [[CallingConvention|calling convention]] imposes on the 16 [[GeneralPurposeRegister|GPRs]].

## The System V x86-64 callee-saved set

Seven registers are callee-saved under System V AMD64:

| Register | Role |
|---|---|
| `%rbx` | general-purpose (no convention role) |
| `%rbp` | frame pointer |
| `%r12` | general-purpose |
| `%r13` | general-purpose |
| `%r14` | general-purpose |
| `%r15` | general-purpose |
| `%rsp` | stack pointer (implicitly preserved — function must restore by `retq`) |

The 5 "no-convention-role" registers (`%rbx`, `%r12`–`%r15`) are the **register allocator's home for long-lived variables** — values that must survive function calls without per-call save/restore overhead.

## The contract from each side

**Callee's view**: *"If I want to use any callee-saved register, I must first `push` (or `mov` into another callee-saved slot) the old value at function entry, and `pop` (or `mov` back) at function exit. The caller is relying on these surviving unchanged."*

**Caller's view**: *"I can leave values in these registers across a call and they'll still be there when control returns. No need to spill."*

## The prologue/epilogue pattern

Functions that use callee-saved registers typically save them via [[X86StackInstructions|`push`]] in the prologue and restore via [[X86StackInstructions|`pop`]] in the epilogue:

```
# Prologue
push %rbp              # callee-saved (frame pointer)
mov  %rsp, %rbp
push %rbx              # callee-saved (because we'll clobber it)
push %r12              # callee-saved (because we'll clobber it)
sub  $N, %rsp

# ... function body uses %rbx, %r12 freely ...

# Epilogue
add  $N, %rsp
pop  %r12              # restore in reverse order
pop  %rbx
pop  %rbp              # (or leaveq for the %rbp pair)
retq
```

The **reverse-order pop** matches the LIFO discipline of the stack — last pushed = first popped.

## When to choose callee-saved (compiler perspective)

A register allocator picks callee-saved for variables whose **live range crosses one or more function calls**. The trade-off versus [[CallerSavedRegister|caller-saved]] registers:

- **Caller-saved**: cheap if no calls cross the live range; expensive (per-call save/restore) if calls do.
- **Callee-saved**: one save+restore at function entry/exit no matter how many times the value is read; cheap for variables read frequently across multiple calls.

The break-even is roughly *"2+ calls in the live range"* — fewer than that, and caller-saved wins.

## `%rsp` is special

`%rsp` is technically callee-saved — every function must restore `%rsp` to its entry value before [[RetInstruction|`retq`]], or the return will branch to garbage. But the mechanism is **not** save+restore via push/pop — it's the [[LeaveInstruction|`leaveq`]] instruction (or the explicit `add $N, %rsp`) that returns `%rsp` to its entry value. So `%rsp` is *callee-preserved* but not *callee-saved-via-push*.

## Connections

- [[dis-7-5-x86-64-functions]] — **introducing source**; defines the callee-saved partition under the System V calling convention.
- [[CallerSavedRegister]] — the **other half** of the register-preservation partition.
- [[CallingConvention]] — the convention that defines the caller-saved / callee-saved split.
- [[CallInstruction]] — the boundary across which the callee-saved promise applies.
- [[GeneralPurposeRegister]] — the 16-register inventory the convention partitions.
- [[X86StackInstructions]] — the [[X86StackInstructions|`push`]] / [[X86StackInstructions|`pop`]] pair used to save and restore callee-saved registers.
- [[FramePointer]] — `%rbp` is callee-saved; its save+restore is the canonical example.
- [[StackPointer]] — `%rsp` is implicitly callee-preserved (restored by [[LeaveInstruction|`leaveq`]] rather than push/pop).
- [[StackFrame]] — where callee-saved register spills live during the function's lifetime.
- [[X86_64]] — the ISA whose System V convention defines this partition.
