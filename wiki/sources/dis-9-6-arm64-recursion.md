---
title: "Dive into Systems — Ch 9.6 Recursion (ARM64)"
type: source
tags: [book, dive-into-systems, arm64, armv8, assembly, recursion, stack-frame]
date: 2026-05-17
source_file: https://diveintosystems.org/book/C9-ARM64/recursion.html
sources: []
last_updated: 2026-05-17
---

## Summary

**Sixth leaf** of Ch 9 *64-bit ARM Assembly* of *[[DiveIntoSystems]]* — **non-twin structural sibling** of [[dis-7-6-x86-64-recursion|Ch 7.6]] / [[dis-8-6-ia32-recursion|Ch 8.6]]. Applies the [[dis-9-5-arm64-functions|Ch 9.5]] [[ARM64BranchAndLink|`bl`]] / [[ARM64Ret|`ret`]] + [[ARM64CallingConvention|AAPCS64]] prologue/epilogue self-referentially to the recursive case via the `sumr` worked example. **No new instructions, no new concept pages** — recursion is a *dynamic-call-chain pattern* on top of the existing 9.5 mechanism. **Headline [[ARM64]]-distinctive note**: because the [[LinkRegister|link register `x30`]] is a **single register**, every recursive function **must** save `x30` to its own stack frame in the [[ARM64FunctionPrologue|prologue]] via `stp x29, x30, [sp, #-32]!` — otherwise the nested `bl sumr` would overwrite the outer call's return address. [[X86_64|x86]] / [[IA32]] don't need this discipline because [[CallInstruction|`callq` / `call`]] already push the return address onto the stack implicitly.

## Key Claims

- **Each recursive call creates a new stack frame.** *"Recursive functions are a special class of functions that call themselves to compute a value"* — recursion depth $d$ ⇒ $d + 1$ live `sumr` frames stacked on the call stack at the deepest point. Same headline rule as [[dis-7-6-x86-64-recursion|Ch 7.6]] / [[dis-8-6-ia32-recursion|Ch 8.6]] — no new instructions needed.
- **The [[LinkRegister|`x30`]]-save discipline is mandatory for recursive (and non-leaf) functions.** Because `x30` is a **single register**, the [[ARM64BranchAndLink|`bl sumr`]] inside the recursive call would overwrite the outer caller's return address. The [[ARM64FunctionPrologue|prologue]] `stp x29, x30, [sp, #-32]!` saves both [[FramePointer|`x29`]] and `x30` to the new frame; the epilogue `ldp x29, x30, [sp], #32` restores them. **Leaf functions** (no nested `bl`) can skip the `x30` save — an [[ARM64]]-specific optimization with no [[X86_64|x86]] equivalent.
- **Parameter and local storage on the stack frame.** Function parameters and locals are spilled to the stack frame slots (typically at `[sp, #offset]` from frame base) rather than held exclusively in registers — allowing nested calls to preserve argument values across recursive invocations. The standard unoptimized pattern: store parameter from `x0` to a stack slot on entry, reload before use.
- **Base case terminates recursion via [[ARM64ConditionalBranch|`b.cond`]].** Recursive functions require an explicit base case; in `sumr`, when `n <= 0` the function returns 0 without calling itself — realized as a standard [[dis-9-4-2-arm64-if-statements|Ch 9.4.2]] [[IfStatement|`if`]]-compilation pattern ([[ARM64Cmp|`cmp`]] + [[ARM64ConditionalBranch|`b.le`]] on the negated condition).
- **Prologue/epilogue symmetry.** The pre-indexed `stp x29, x30, [sp, #-32]!` prologue and post-indexed `ldp x29, x30, [sp], #32` epilogue are **structural mirrors** — together they allocate/deallocate the frame **and** save/restore fp+lr in two instructions total. Frame size 32 bytes (vs the 16-byte minimum from [[dis-9-2-arm64-common|Ch 9.2]]'s `adder2`) reflects the extra parameter / local-variable slots `sumr` needs.
- **Sequential computation stacking on unwind.** Multiple recursive calls create a "stack" of pending computations that resolve sequentially as frames unwind during the return phase — the [[CallStack|call stack]]'s LIFO structure made visible at the [[ARM64]] surface. Return values chain through [[ARM64Ret|`x0`]] on each `ret`.

## Key Quotes

> "Recursive functions are a special class of functions that call themselves to compute a value." — the operative definition of recursion at the [[CLanguage|C]] / [[ARM64]] surface.

> "Each recursive call creates new stack frames for each function call." — the headline rule: **recursion stacks frames**, no new instruction required.

## Connections

- [[DiveIntoSystems]] — parent textbook; this is the **99th ingested chapter** / **sixth leaf of Ch 9**.
- [[dis-9-5-arm64-functions]] — immediate predecessor; supplied the [[ARM64BranchAndLink|`bl`]] / [[ARM64Ret|`ret`]] + [[ARM64CallingConvention|AAPCS64]] + [[ARM64FunctionPrologue|prologue/epilogue]] mechanism the recursive `sumr` example self-references.
- [[dis-7-6-x86-64-recursion]] / [[dis-8-6-ia32-recursion]] — structural siblings; same recursive-frame-stacking pattern. **Headline [[ARM64]]-specific delta**: explicit `x30` save in prologue (no equivalent on [[X86_64|x86]] where [[CallInstruction|`callq`]] pushes return address automatically).
- [[LinkRegister]] — central concept; `x30`-save is mandatory for non-leaf functions.
- [[ARM64FunctionPrologue]] — the `stp x29, x30, [sp, #-N]!` / `ldp x29, x30, [sp], #N` pair; the recursive case demonstrates *why* the prologue exists.
- [[Recursion]] / [[CallStack]] / [[StackFrame]] / [[ExecutionStack]] — umbrella concepts; reused from [[dis-7-6-x86-64-recursion|Ch 7.6]].
- [[TailRecursion]] — scope omission (same as Ch 7.6 / Ch 8.6); not covered.

## Contradictions

None. Ch 9.6 **operationalizes** [[Recursion]] at the [[ARM64]] surface — no new instructions, no revised claims. The `x30`-save requirement is an **[[ARM64]]-specific consequence** of the [[LinkRegister|single-register return address]] design — complements rather than contradicts [[X86_64|x86]]'s stack-resident return-address model.
