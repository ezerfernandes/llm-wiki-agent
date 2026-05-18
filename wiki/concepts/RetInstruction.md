---
title: "x86-64 `retq` Instruction"
type: concept
tags: [x86-64, assembly, instruction, function-return, control-flow]
sources: [dis-7-5-x86-64-functions]
last_updated: 2026-05-17
---

# `retq` — Function Return

The **`retq` instruction** is [[X86_64|x86-64]]'s **function-return primitive** — the inverse of [[CallInstruction|`callq`]]. Per [[dis-7-5-x86-64-functions|Ch 7.5]]:

> "`retq` pops the saved return address from the stack back into [[InstructionPointer|`%rip`]]."

## Semantics

```
retq    # %rip ← (%rsp);  %rsp ← %rsp + 8
```

Equivalent to:

```
pop %rip    # (notionally — %rip can't be a destination explicitly)
```

No explicit operand — `retq` always pops `(%rsp)` and uses it as the new `%rip`. The implicit operand is what makes the **stack-discipline invariant** load-bearing.

## Preconditions

`retq` only works correctly when **`%rsp` points to a saved return address at the moment of execution**. Two things must hold:

1. Every value pushed by the function body (locals, callee-saved register spills, intermediate stack arguments to nested calls) must be popped or otherwise removed before `retq` — typically by the [[LeaveInstruction|`leaveq`]] instruction in the function epilogue, which restores `%rsp` to its post-prologue value before `retq` runs.
2. The matching [[CallInstruction|`callq`]] must have pushed a real return address (not been tampered with via, e.g., a [[BufferOverflow|stack buffer overflow]]).

When either precondition fails, `retq` branches to **whatever bytes happen to sit at `(%rsp)`** — typically causing a segmentation fault, or in adversarial settings transferring control to attacker-injected code (ROP / return-into-libc).

## No operand needed

Unlike most [[X86_64|x86-64]] instructions which take explicit source / destination operands, `retq` is **operand-free**: the source is always `(%rsp)`, the destination is always `%rip`, the side effect is always `%rsp += 8`. This makes `retq` and [[CallInstruction|`callq`]] the only two instructions in the ISA that directly read and write `%rip` (every other write to `%rip` goes through the [[X86JumpInstructions|jump family]], which takes an explicit target operand).

## Relation to `leaveq`

In every well-formed function, `retq` is preceded by [[LeaveInstruction|`leaveq`]] (or its longhand equivalent `mov %rbp, %rsp; pop %rbp`), restoring [[StackPointer|`%rsp`]] and [[FramePointer|`%rbp`]] to their caller-frame values. Only then does `retq` find the correct return address at `(%rsp)`.

## Connections

- [[dis-7-5-x86-64-functions]] — **introducing source**; the `retq` definition and its place in the function epilogue.
- [[CallInstruction]] — the inverse instruction; every `retq` consumes a return address pushed by exactly one prior `callq`.
- [[LeaveInstruction]] — the canonical predecessor instruction in the function epilogue; restores `%rsp` so that `retq` finds the return address.
- [[X86StackInstructions]] — the underlying [[X86StackInstructions|`pop`]] semantics `retq` specializes against [[StackPointer|`%rsp`]].
- [[X86JumpInstructions]] — sibling control-flow family; `retq` is functionally `pop %rip` (an indirect jump through the stack top).
- [[InstructionPointer]] — the `%rip` register `retq` restores.
- [[StackFrame]] — the per-call activation record being torn down at the moment `retq` runs (the prior [[LeaveInstruction|`leaveq`]] already dismantled it).
- [[BufferOverflow]] — the canonical failure mode when the saved return address at `(%rsp)` has been corrupted; `retq` then transfers control to attacker-controlled bytes.
- [[X86_64]] — the ISA `retq` belongs to.
