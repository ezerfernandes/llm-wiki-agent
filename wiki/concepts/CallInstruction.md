---
title: "x86-64 `callq` Instruction"
type: concept
tags: [x86-64, assembly, instruction, function-call, control-flow]
sources: [dis-7-5-x86-64-functions]
last_updated: 2026-05-17
---

# `callq` — Function Call

The **`callq` instruction** is [[X86_64|x86-64]]'s **function-call primitive** — a single instruction that bundles two operations atomically: save the return address and transfer control. Per [[dis-7-5-x86-64-functions|Ch 7.5]]:

> "`callq addr` pushes the current value of [[InstructionPointer|`%rip`]] onto the stack and jumps to the function address."

## Semantics

```
callq addr    # push %rip;  %rip ← addr
```

Equivalent to the two-instruction sequence:

```
sub  $0x8, %rsp        # decrement stack pointer (room for return address)
mov  %rip, (%rsp)      # save return address
jmp  addr              # transfer control
```

Exists as a specialized instruction because function call is one of the most common operations in compiled code — and because the save-return-address-then-jump pair must be **atomic** with respect to interrupts.

## The pushed `%rip` value

The `%rip` value pushed by `callq` is the address of the **instruction immediately after** the `callq` itself — i.e., where execution should resume when the callee returns. This is the **return address**, and [[RetInstruction|`retq`]] pops it back into `%rip` to complete the round trip.

## Stack-discipline invariant

Every `callq` must be matched by exactly one [[RetInstruction|`retq`]] (within the called function, possibly along multiple control-flow paths). Violating this discipline — extra pushes left on the stack at return time, missing pops, or a `retq` without a corresponding `callq` — causes the function to return to the wrong address (typically the top of whatever data happens to be at `(%rsp)`), almost always crashing the program or, worse, branching into attacker-controlled data (the foundation of [[BufferOverflow|stack-buffer-overflow]] exploits).

## Relation to other control-flow instructions

`callq` extends the [[X86JumpInstructions|jump family]] from [[dis-7-4-1-x86-64-preliminaries|Ch 7.4.1]] — both modify [[InstructionPointer|`%rip`]] — but `callq` also **saves the old `%rip`** so control can return. Plain `jmp` is one-way; `callq` is round-trip.

## Connections

- [[dis-7-5-x86-64-functions]] — **introducing source**; the `callq` definition and the System V calling-convention frame it fits into.
- [[RetInstruction]] — the inverse instruction; every `callq` is matched by exactly one `retq` on every control path through the callee.
- [[X86StackInstructions]] — the underlying [[X86StackInstructions|`push`]] semantics `callq` specializes against [[StackPointer|`%rsp`]].
- [[X86JumpInstructions]] — sibling control-flow family; `callq` is functionally `push %rip; jmp addr`.
- [[InstructionPointer]] — the `%rip` register `callq` saves and updates.
- [[CallStack]] — the data structure `callq` grows by one return-address slot.
- [[StackFrame]] — the per-call activation record whose construction begins immediately after `callq` (in the callee's prologue).
- [[CallingConvention]] — the contract `callq` participates in; the System V AMD64 convention dictates which registers hold arguments at the moment `callq` executes.
- [[X86_64]] — the ISA `callq` belongs to.
