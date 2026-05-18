---
title: "Call Stack"
type: concept
tags: [call-stack, stack, stack-frame, execution-stack, runtime, assembly]
sources: [dis-7-6-x86-64-recursion, dis-7-5-x86-64-functions, dis-7-2-x86-64-common, dis-1-4-functions]
last_updated: 2026-05-17
---

# Call Stack

The **call stack** is the LIFO (last-in-first-out) sequence of [[StackFrame|stack frames]] representing every currently-active [[Function|function]] invocation along a single thread of execution. Each `callq` instruction grows the stack by exactly one frame; each `retq` shrinks it by exactly one. The stack's invariants — frame layout, growth direction, register conventions — are dictated by the [[CallingConvention|calling convention]] of the underlying [[ISA]].

## Promoted from Forward Reference

[[CallStack]] was a long-standing forward reference used by [[dis-7-2-x86-64-common|Ch 7.2]] (where the `adder2` trace tracked call-stack state at each step), by [[dis-7-5-x86-64-functions|Ch 7.5]] (where [[CallInstruction|`callq`]] / [[RetInstruction|`retq`]] / [[LeaveInstruction|`leaveq`]] were introduced as the instructions that manipulate it), and by adjacent concept pages ([[StackPointer]], [[X86StackInstructions]], [[CallInstruction]]). [[dis-7-6-x86-64-recursion|Ch 7.6]] is the chapter whose [[Recursion|recursive]] `sumr` example makes the call stack's dynamic growth most concrete — recursion depth $d$ ⇒ $d + 1$ live frames stacked — promoting CallStack to a first-class concept page.

## Synonym

**Execution stack** ([[ExecutionStack]]) is a synonym used by [[dis-1-4-functions|Ch 1.4]] / Ch 1.4.1 of *[[DiveIntoSystems]]* at the source-level introduction. *"Call stack"* and *"execution stack"* refer to the same runtime data structure; the wiki distinguishes them only by the level of abstraction at which the term is introduced (source-level C → "execution stack"; assembly-level x86-64 → "call stack").

## Structure (per [[dis-7-5-x86-64-functions|Ch 7.5]] + [[dis-7-6-x86-64-recursion|Ch 7.6]])

On [[X86_64|x86-64]] under the [[CallingConvention|System V AMD64 calling convention]]:

- **Grows downward.** [[StackPointer|`%rsp`]] decreases as frames are pushed; the stack occupies a high-address region of the process's virtual memory and grows toward lower addresses (toward the heap, which grows upward).
- **Frames bracketed by [[StackPointer|`%rsp`]] and [[FramePointer|`%rbp`]].** The current frame occupies the range `[%rsp, %rbp]`. `%rsp` always points to the top of the stack (lowest address); `%rbp` points to the base of the current frame (the saved-`%rbp` slot of the caller).
- **Backward-linked frame chain.** Each frame stores the **saved [[FramePointer|`%rbp`]]** of the caller at `(%rbp)` — so the chain of frames forms a backward singly-linked list along the stack. Debuggers walk this chain to render `backtrace`.
- **Return addresses interleaved.** Each [[CallInstruction|`callq`]] pushes a return address ([[InstructionPointer|`%rip`]]) onto the stack before the callee's prologue runs; the saved-`%rbp` slot sits immediately below it in the new frame. [[RetInstruction|`retq`]] pops the return address back into `%rip`; [[LeaveInstruction|`leaveq`]] restores the saved `%rbp` before `retq` fires.

## Growth Patterns

- **Linear-call chain** (`main → f → g → h`): the call stack holds exactly 4 frames at the deepest point; each call shifts the chain one frame deeper, each return one frame shallower.
- **Recursive call chain** (per [[dis-7-6-x86-64-recursion|Ch 7.6]]): `sumr(5)` causes the call stack to hold 6 `sumr` frames at the deepest point — the same function appears multiple times on the stack, each with its own copy of parameters and locals. Depth scales linearly with input size; this is the **structural memory cost** of [[Recursion|recursive]] algorithms.
- **Tail-call elimination** (forward reference, not in [[dis-7-6-x86-64-recursion|Ch 7.6]]): when a recursive call is in **tail position**, an optimizing compiler can replace the `callq` with a `jmp` that reuses the current frame instead of allocating a new one — collapsing the linear-depth chain to constant depth.

## Failure Mode

When the call stack grows beyond its allocated region (typically 1 MiB to 8 MiB per thread on Linux), the next push crosses the **stack guard page** and the OS raises a [[StackOverflow|stack overflow]] (SIGSEGV on Linux). Unbounded [[Recursion|recursion]] without a base case is the canonical cause; deep but bounded recursion on tight stacks (e.g., embedded systems) is another. Not named directly by [[dis-7-6-x86-64-recursion|Ch 7.6]] but implicit in the *"each recursive call generates a new stack frame"* observation.

## Security Relevance

The call stack is the substrate of classical control-flow-hijacking attacks. [[BufferOverflow|Stack-buffer-overflow]] exploits overwrite the saved return address ([[RetInstruction|`retq`]]'s source) and/or the saved-[[FramePointer|`%rbp`]] slot, redirecting control to attacker-chosen code on `retq`. Stack canaries, [[ASLR|address-space layout randomization]], non-executable stack pages, and [[CFI|control-flow integrity]] are the modern mitigations. Not covered by [[dis-7-6-x86-64-recursion|Ch 7.6]] but referenced from adjacent pages.

## Connections

- [[dis-7-6-x86-64-recursion]] — the chapter that promotes [[CallStack]] from forward-reference to first-class page via the recursive `sumr` example.
- [[dis-7-5-x86-64-functions]] — introduces the instructions that manipulate the call stack ([[CallInstruction|`callq`]] / [[RetInstruction|`retq`]] / [[LeaveInstruction|`leaveq`]]) and the [[CallingConvention|System V convention]] governing frame layout.
- [[dis-7-2-x86-64-common]] — first DIS chapter to track call-stack state at each instruction step (the `adder2` trace).
- [[dis-1-4-functions]] — source-level introduction of the **execution stack** (the synonym at the [[CLanguage|C]]-level abstraction).
- [[ExecutionStack]] — synonym; same data structure, different abstraction-level naming.
- [[StackFrame]] — the per-call activation record the call stack is a sequence of.
- [[StackPointer]] — `%rsp`, always points to the top of the call stack.
- [[FramePointer]] — `%rbp`, points to the base of the current frame; chain of saved-`%rbp` values links frames.
- [[CallInstruction]] / [[RetInstruction]] / [[LeaveInstruction]] — the [[X86_64|x86-64]] instructions that grow / shrink / unwind the call stack.
- [[X86StackInstructions]] — `push` / `pop`, the underlying primitives `callq` / `retq` specialize.
- [[CallingConvention]] — the [[CallingConvention|System V AMD64]] ABI that dictates frame layout.
- [[Recursion]] — the runtime pattern whose stack-depth cost the call stack realizes.
- [[StackFrame]] — the unit the call stack is composed of.
- [[InstructionPointer]] — the `%rip` register whose values are pushed onto / popped from the call stack as return addresses.
- [[BufferOverflow]] — the classical exploit class that corrupts the call stack's saved return addresses.
