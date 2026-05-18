---
title: "Stack Frame"
type: concept
tags: [c-language, runtime, memory, calling-convention, activation-record]
sources: [dis-1-4-functions]
last_updated: 2026-05-17
---

# Stack Frame

A **stack frame** — also known as an **activation frame** or **activation record** — is the per-call runtime record [[CLanguage|C]] (and most C-family languages) allocates on the [[ExecutionStack|execution stack]] to hold one active [[FunctionCall|function call]]'s state. Per [[dis-1-4-functions|DIS Ch 1.4]] §1.4.1:

> "Each function call creates a new **stack frame** (sometimes called an **activation frame** or **activation record**) containing its parameter and local variable values."

## What's in a frame

At the introductory level [[dis-1-4-functions|Ch 1.4]] introduces, a frame holds:

- The call's [[FunctionParameter|parameter]] values (initialized [[PassByValue|by value]] from the [[FunctionArgument|arguments]]).
- The call's [[LocalVariable|local variables]].

Later [[DiveIntoSystems]] chapters (assembly, calling conventions, [[MemoryHierarchy|memory hierarchy]]) will add: the return address, saved caller-/callee-saved registers, and any temporary space the compiler needs.

## Push on call, pop on return

> "When a function is called, a new stack frame is created for it (pushed on the top of the stack), and space for its local variables and parameters is allocated in the new frame. When a function returns, its stack frame is removed from the stack (popped from the top of the stack), leaving the caller's stack frame on the top of the stack." — [[dis-1-4-functions|DIS Ch 1.4]]

This LIFO discipline is what makes [[FunctionScope|function scope]] mechanical: at any instant, only the **top** frame's names are in scope; all the *suspended* callers' locals sit beneath, intact and inaccessible until their callee returns.

## Why "activation"?

A *function* is a static artifact (one piece of source code). An *activation* is one *dynamic* execution of it. Recursion is the cleanest case where the distinction matters: ten nested calls to the same `max` function are ten activations and ten frames — each with its own `n1`, `n2`, `result`. The frame **is** that activation's storage.

## Later in the wiki

The [[TheEmbeddedRustBook]] corpus already references the same model under [[ARMCortexM|Cortex-M]] calling conventions; [[DiveIntoSystems]] will get there itself when it walks down to assembly and the [[MemoryHierarchy|memory hierarchy]].

## Connections

- [[dis-1-4-functions]] — introducing source (§1.4.1).
- [[ExecutionStack]] — the LIFO substrate the frames live on.
- [[FunctionCall]] / [[ReturnStatement]] — push and pop frames.
- [[Function]] / [[FunctionParameter]] / [[LocalVariable]] — what each frame holds.
- [[PassByValue]] — the rule by which parameter slots are *initialized*.
- [[FunctionScope]] — only the top frame's names are in scope.
- [[MainFunction]] — the *first* frame on the stack at program start.
- [[CLanguage]] / [[DiveIntoSystems]].
