---
title: "Execution Stack"
type: concept
tags: [c-language, runtime, memory, calling-convention]
sources: [dis-1-4-functions]
last_updated: 2026-05-17
---

# Execution Stack

The **execution stack** (a.k.a. the **call stack**) is the LIFO data structure a running [[CLanguage|C]] program uses to track its active [[FunctionCall|function calls]]. Per [[dis-1-4-functions|DIS Ch 1.4]] §1.4.1:

> "The **execution stack** keeps track of the state of active functions in a program."

Each [[FunctionCall|call]] pushes a [[StackFrame|stack frame]] (activation record) onto the top; each [[ReturnStatement|return]] pops it. At any instant the stack is a tower of frames — top frame = currently executing function; bottom frame = [[MainFunction|`main`]] (with the C runtime startup beneath it, in real implementations).

## Invariants

- **LIFO.** A callee always returns before its caller does — that's the structural reason a *stack* (not a queue) is the right shape.
- **Top frame is active.** Only the top frame's [[FunctionParameter|parameters]] and [[LocalVariable|locals]] are in [[FunctionScope|scope]].
- **Recursion works for free.** Ten nested calls to the same [[Function|function]] live in ten distinct [[StackFrame|frames]] — same code, distinct storage.

## Pedagogical placement

[[dis-1-4-functions|Ch 1.4]] introduces the execution stack at the *conceptual* level — frames are little boxes pushed and popped. Later [[DiveIntoSystems]] chapters open up the *concrete* layout: stack growth direction, frame-pointer / stack-pointer registers, the calling convention's register-vs-stack rules for [[FunctionArgument|arguments]] and return values, and the relationship to the rest of the process's address space.

## Hosted vs. bare-metal contrast

In the hosted [[OperatingSystem|OS]] world [[DiveIntoSystems]] assumes, the [[OperatingSystem|OS]] sets up the initial stack for the process. The [[TheEmbeddedRustBook|embedded Rust]] world ([[NoStd|`no_std`]]) instead has a linker script reserve a stack region in RAM and the reset handler load the [[ARMCortexM|Cortex-M]] main-stack pointer at boot — different mechanism, same LIFO discipline.

## Connections

- [[dis-1-4-functions]] — introducing source.
- [[StackFrame]] — the per-call records this stack holds.
- [[FunctionCall]] / [[ReturnStatement]] — push and pop operations.
- [[Function]] / [[FunctionScope]] / [[LocalVariable]] / [[FunctionParameter]] — what the *top* frame governs.
- [[MainFunction]] — the bottom-most user frame.
- [[OperatingSystem]] — sets up the initial stack (hosted-C contrast with [[NoStd]]).
- [[MemoryHierarchy]] — later DIS chapters will place the stack in the broader address space.
- [[ARMCortexM]] — sibling treatment of stack setup in the embedded world.
- [[CLanguage]] / [[DiveIntoSystems]].
