---
title: "Dive into Systems — Ch 7.6 Recursion (x86-64)"
type: source
tags: [dive-into-systems, x86-64, assembly, recursion, call-stack, stack-frame]
date: 2026-05-17
source_file: https://diveintosystems.org/book/C7-x86_64/recursion.html
sources: []
last_updated: 2026-05-17
---

## Summary

Chapter 7.6 of *[[DiveIntoSystems]]* — **sixth leaf** of Ch 7 *x86-64 Assembly* — applies the [[dis-7-5-x86-64-functions|Ch 7.5]] function-call apparatus ([[CallInstruction|`callq`]] / [[RetInstruction|`retq`]] / [[LeaveInstruction|`leaveq`]], [[CallingConvention|System V calling convention]], [[FramePointer|`%rbp`]]-anchored [[StackFrame|stack frames]]) to the **self-invoking** case: [[Recursion|recursion]]. The chapter's single worked example is `sumr`, the recursive sum-from-`n`-down-to-`1` function, traced through its [[X86_64|x86-64]] [[AssemblyLanguage|assembly]] from prologue to recursive `callq` to base-case return. The pedagogical headline: **each recursive invocation gets its own [[StackFrame|stack frame]]** pushed onto the [[CallStack|call stack]] — the same prologue/epilogue mechanism Ch 7.5 introduced, but now applied repeatedly along a single dynamic call chain. The base case (`n <= 0`) returns `0` immediately without further recursion; the recursive case computes `n + sumr(n-1)` by issuing a [[CallInstruction|`callq sumr`]] to itself and adding its `%eax` return to the local `n`.

## Key Claims

- **Recursive calls reuse the [[dis-7-5-x86-64-functions|Ch 7.5]] machinery unchanged.** A recursive function is *not* special at the [[X86_64|x86-64]] [[AssemblyLanguage|assembly]] level — the same [[CallInstruction|`callq <function>`]] instruction the compiler emits for a call to *any* function is the instruction emitted for a call to *the function itself*. The book demonstrates this on `sumr` — the single recursive `callq 0x400551 <sumr>` instruction at the heart of the function body is **structurally identical** to any other `callq`. The [[CallingConvention|calling convention]] (`%edi` as the 1st parameter, `%eax` as the return) applies on every recursive invocation just as on the outermost one.
- **Each recursive invocation gets its own [[StackFrame|stack frame]].** The canonical Ch 7.5 prologue — `push %rbp; mov %rsp, %rbp; sub $0x10, %rsp` (16 bytes of local-variable space) — fires on **every** entry to `sumr`. Each frame holds its own copy of the parameter `n` (spilled from `%edi` to the local stack slot) and its own slot for the recursive return value. Recursive depth $d$ ⇒ exactly $d$ live `sumr` frames stacked along the [[CallStack|call stack]] at the deepest point — every frame waiting on its inner `callq` to return before its own `add` + `leaveq` + `retq` can fire.
- **Base case vs recursive case is realized as a [[CmpInstruction|`cmp`]] + conditional jump.** The `sumr` body opens with a comparison `cmp $0x0, -0x4(%rbp)` against the spilled `n`, followed by a [[X86JumpInstructions|`jg`]] (signed-greater) to the recursive branch — the standard [[AsmIfThenElse|Ch 7.4.2]] if-pattern with the **negated** condition (the *"jumps when condition is **not** true"* rule). On `n <= 0` (the base case) execution falls through to `mov $0x0, %eax; leaveq; retq` — return 0 and unwind one frame. On `n > 0` execution jumps to the recursive case: load `n` into `%edi`, decrement it (`sub $0x1, %edi`), `callq sumr`, then `add -0x4(%rbp), %eax` to fold the just-returned `sumr(n-1)` into the local `n`, and `leaveq; retq` to return to the *caller* (which is itself another `sumr` invocation — except at the outermost call where the caller is `main` or wherever `sumr` was originally invoked).
- **The [[CallStack|call stack]] grows linearly with recursion depth — this is the **stack-depth cost** of recursion.** Calling `sumr(5)` produces six stacked `sumr` frames at the deepest point (one each for `n = 5, 4, 3, 2, 1, 0`); calling `sumr(1000)` produces 1001 frames. The textbook does **not** name [[TailRecursion|tail-call optimization]] (or any other recursion-elimination transform) — the `sumr` example is **not** tail-recursive (the `add -0x4(%rbp), %eax` happens *after* the recursive call returns, so the recursive `callq` is **not** in tail position), and the chapter scope is the unoptimized recursive realization.
- **Recursive return-value flow is `%eax` ↔ `%eax`.** The recursive `callq sumr` deposits the inner call's return into `%eax` per the [[CallingConvention|calling convention]]. The caller frame then issues `add -0x4(%rbp), %eax` (its own `n`) to combine the inner result with its own parameter — `%eax` is both the inner return and the running accumulator. The final `leaveq; retq` unwinds the current frame and propagates the now-combined `%eax` up to its own caller, where the same `add` pattern repeats one level higher.

## Key Quotes

> "Each recursive call generates a new stack frame." — the headline rule the chapter is built around; the [[CallStack|call stack]] grows by exactly one [[StackFrame|frame]] per invocation, regardless of whether the call is to a *different* function or to *the same* function recursively.

> "return n + sumr(n-1)" — the C-level recursive case of `sumr`; the [[X86_64|x86-64]] [[AssemblyLanguage|assembly]] realizes this as `callq sumr` + `add -0x4(%rbp), %eax`, with the `add` happening **after** the recursive call returns — placing the recursive `callq` outside tail position.

## Connections

- [[DiveIntoSystems]] — parent textbook; this is the **71st ingested chapter** and the **sixth leaf** of Ch 7 *x86-64 Assembly*.
- [[dis-7-5-x86-64-functions]] — immediate predecessor and **direct dependency**; Ch 7.5 introduced the function-call apparatus ([[CallInstruction|`callq`]] / [[RetInstruction|`retq`]] / [[LeaveInstruction|`leaveq`]], [[CallingConvention|System V calling convention]], [[FramePointer|`%rbp`]]-anchored frames). Ch 7.6 reuses every piece unchanged — recursion is a **dynamic property** of the call chain (the same function appears multiple times on the stack), not a separate instruction-set feature.
- [[dis-7-4-2-x86-64-if-statements]] — Ch 7.4.2's [[AsmIfThenElse|if-pattern]] is the mechanism for the base-case test in `sumr` — [[CmpInstruction|`cmp`]] + [[X86JumpInstructions|conditional jump]] on the negated condition. The base case is structurally a standard if-statement compiled the standard way.
- [[Recursion]] — the [[ComputerScience|CS]] concept Ch 7.6 operationalizes at the [[X86_64|x86-64]] [[AssemblyLanguage|assembly]] level. Ch 7.6 **promotes** [[Recursion]] from forward-reference to first-class concept page.
- [[CallStack]] — the LIFO of [[StackFrame|stack frames]] recursion grows linearly with depth. Ch 7.6 **promotes** [[CallStack]] from forward-reference (used by Ch 7.2 / 7.5 / and elsewhere) to first-class page.
- [[StackFrame]] — each recursive invocation pushes one. Ch 7.6 supplies the **recursive-depth-equals-frame-count** observation that makes [[StackFrame]] concrete at runtime scale.
- [[FramePointer]] / [[StackPointer]] — `%rbp` is re-anchored on every recursive entry; the chain of saved-`%rbp` values forms a backward link across all live recursive frames (the basis for [[GDB|debugger]] `backtrace` showing `sumr` repeated $d$ times).
- [[CallInstruction]] — the recursive `callq sumr` is structurally identical to any other `callq`; recursion is a **caller property**, not a callee property.
- [[X86_64]] — the ISA; Ch 7.6 adds no new instructions, just a new **pattern** for the existing function-call family.
- [[dis-1-4-functions]] — the [[CLanguage|C]]-level treatment of functions, parameters, and the [[ExecutionStack|execution stack]]; Ch 1.4 mentions stack frames at the source level, Ch 7.6 = the assembly-side realization in the recursive case.

## Subsections (leaf coverage)

Ch 7.6 is a **single-page section** like Ch 7.5, not a hub. The wiki ingest mints **one new concept page** and promotes **two forward references**:

- **New**: [[Recursion]] (promoted from forward-reference) — the function-calls-itself pattern operationalized at the [[X86_64|x86-64]] assembly level.
- **Promoted from forward reference**: [[CallStack]] — referenced repeatedly across [[dis-7-2-x86-64-common|Ch 7.2]] / [[dis-7-5-x86-64-functions|Ch 7.5]] / [[StackPointer]] / [[X86StackInstructions]] / etc., now a first-class page that names the LIFO of frames the prior chapters were already manipulating.

## Scope Notes

- **No [[TailRecursion|tail-call optimization]] / tail-recursion treatment.** The chapter scope is unoptimized recursion; `sumr` is **not** in tail form (the `add` after the recursive `callq` keeps the recursive call out of tail position), and the chapter does not introduce the concept of rewriting recursion as iteration to bound stack depth. Wiki-flagged but **not** covered by Ch 7.6.
- **No stack-overflow / recursion-depth-limit discussion.** The chapter notes that each recursive call adds a frame, but does not address what happens when the [[CallStack|stack]] runs out (e.g., the `SIGSEGV` from hitting the stack guard page on Linux). Wiki-flagged but **not** covered.
- **No mutual recursion / indirect recursion.** Only direct self-recursion (`sumr` → `sumr`) is shown.

## Contradictions

None. Ch 7.6 **extends** the Ch 7.5 function-call treatment by demonstrating it under self-call — adds an example/pattern rather than revising the underlying mechanism. Every claim Ch 7.5 made about [[CallInstruction|`callq`]], [[RetInstruction|`retq`]], [[LeaveInstruction|`leaveq`]], the [[CallingConvention|System V convention]], and the [[FramePointer|`%rbp`]]-anchored frame discipline remains intact in Ch 7.6.
