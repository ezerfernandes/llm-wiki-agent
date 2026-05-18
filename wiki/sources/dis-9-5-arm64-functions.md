---
title: "Dive into Systems — Ch 9.5 Functions in Assembly (ARM64)"
type: source
tags: [book, dive-into-systems, arm64, armv8, assembly, functions, calling-convention, aapcs64, stack-frame]
date: 2026-05-17
source_file: https://diveintosystems.org/book/C9-ARM64/functions.html
sources: []
last_updated: 2026-05-17
---

## Summary

**Fifth leaf** of Ch 9 *64-bit ARM Assembly* of *[[DiveIntoSystems]]* — **non-twin structural sibling** of [[dis-7-5-x86-64-functions|Ch 7.5]] / [[dis-8-5-ia32-functions|Ch 8.5]]. Closes the per-ISA tour of the function-call mechanism at the [[ARM64|AArch64]] [[AssemblyLanguage|assembly]] surface. Adds **two new control-flow instructions** — [[ARM64BranchAndLink|`bl`]] (branch-and-link) / [[ARM64Ret|`ret`]] — and operationalizes the **[[ARM64CallingConvention|AAPCS64 calling convention]]**: first eight arguments in `x0`–`x7` (vs [[SystemVCallingConvention|System V]]'s six in `%rdi`–`%r9` and [[CdeclCallingConvention|cdecl]]'s zero), return value in `x0`, the **[[LinkRegister|link register `x30`]]** holds the return address (vs [[X86_64|x86]]'s stack-only return address), [[FramePointer|`x29`]] as frame pointer, [[StackPointer|`sp`]] always 16-byte aligned. **No `push`/`pop` instructions** — the [[ARM64FunctionPrologue|prologue/epilogue idiom]] uses the [[ARM64DataMovement|pre-/post-indexed `stp` / `ldp`]] pair from [[dis-9-2-arm64-common|Ch 9.2]] instead.

## Key Claims

- **Two new control-flow instructions complete the function-call family.** [[ARM64BranchAndLink|`bl addr`]] *"sets `x30 = pc + 4` and sets `pc = addr`"* — atomically saves the post-call return address into the [[LinkRegister|link register `x30`]] and transfers control to the callee. [[ARM64Ret|`ret`]] *"sets `pc = x30`"* — the inverse operation. Unlike [[X86_64|x86-64]]'s [[CallInstruction|`callq`]] / [[RetInstruction|`retq`]] (which push/pop the return address against the stack), [[ARM64]]'s `bl`/`ret` use a **dedicated register** — eliminating a memory access for **leaf functions** (no nested calls) at the cost of an explicit save when the callee makes further calls.
- **AAPCS64 calling convention — eight argument registers, return in `x0`.** *"The first eight parameters to a function are stored in registers `x0`…​`x7`"*; additional parameters spill to the stack. Return value lives in [[ARM64Ret|`x0`]] (or `w0` for 32-bit returns). Doubles [[SystemVCallingConvention|System V]]'s six-register fast path and fully eliminates [[CdeclCallingConvention|cdecl]]'s stack-only argument passing — the [[RISC]] design tradeoff for the larger [[AArch64Registers|31-GPR]] register file.
- **Frame pointer `x29` + link register `x30` bracket the stack frame.** [[FramePointer|`x29`]] *"maintains the base pointer of the current stack frame"*; [[StackPointer|`sp`]] points to the top of the stack (grows toward lower addresses). The standard [[ARM64FunctionPrologue|prologue]] saves both via the **canonical pair-store idiom** `stp x29, x30, [sp, #-N]!` (pre-indexed — decrement `sp` by `N`, then store fp+lr; one instruction) and the **canonical epilogue** `ldp x29, x30, [sp], #N` (post-indexed — load fp+lr, then increment `sp` by `N`).
- **No `push` / `pop` instructions — pre-/post-indexed `stp` / `ldp` replace them.** [[ARM64]] has **no dedicated stack-manipulation mnemonic family** (in contrast to [[X86StackInstructions|x86 `push` / `pop`]] which adjust `%rsp` by 8 / 4 implicitly). Stack growth and shrinkage are expressed through the [[ARM64AddressingMode|pre-indexed]] (`[sp, #-N]!`) and [[ARM64AddressingMode|post-indexed]] (`[sp], #N`) addressing-mode forms on [[ARM64DataMovement|`stp` / `ldp`]] / `str` / `ldr` — the [[LoadStoreArchitecture|load/store rule]] applied to stack discipline.
- **Stack-grown-down + `sp` 16-byte alignment.** The stack grows toward lower addresses (same convention as [[X86_64|x86-64]] / [[IA32]]); [[StackPointer|`sp`]] must remain 16-byte aligned at every function-call boundary (AAPCS64 ABI constraint — frames are typically allocated in 16-byte multiples even when the live data would fit in 8 or 12 bytes).
- **Uninitialized stack reads return garbage.** Loading from an uninitialized stack slot retrieves whatever bytes previously occupied that memory — the assembly-surface mechanism behind C's *"uninitialized variable"* class of bug. Same warning as [[dis-7-5-x86-64-functions|Ch 7.5]] / [[dis-8-5-ia32-functions|Ch 8.5]].

## Key Quotes

> "Sets `x30 = pc + 4` and sets `pc = addr`." — the [[ARM64BranchAndLink|`bl`]] semantics: **save next instruction's address into [[LinkRegister|`x30`]] + jump to `addr`** atomically.

> "The first eight parameters to a function are stored in registers `x0`…​`x7`." — the [[ARM64CallingConvention|AAPCS64]] argument-passing rule (doubles [[SystemVCallingConvention|System V]]'s register fast-path width).

## Connections

- [[DiveIntoSystems]] — parent textbook; this is the **98th ingested chapter** / **fifth leaf of Ch 9**.
- [[dis-9-4-arm64-conditional-loops]] / [[dis-9-4-3-arm64-loops]] — immediate predecessor; closed [[ARM64]] control-flow at the jump-instruction level. Ch 9.5 adds the **structured branch-and-link / return pair** on top.
- [[dis-9-2-arm64-common]] — Ch 9.2 introduced [[ARM64DataMovement|`ldp` / `stp` with pre-/post-indexed addressing]] and previewed the canonical `stp x29, x30, [sp, #-16]!` prologue idiom; Ch 9.5 formalizes it.
- [[dis-7-5-x86-64-functions]] / [[dis-8-5-ia32-functions]] — structural siblings; same calling-convention slot at the [[X86_64|x86-64]] / [[IA32]] level. **Headline cross-ISA deltas**: (1) [[LinkRegister|`x30`]] holds return address in a register (vs [[X86_64|x86]]'s stack-only); (2) 8 argument registers (vs 6 / 0); (3) `stp`/`ldp` pair replaces `push`/`pop`.
- [[ARM64CallingConvention]] / [[ARM64FunctionPrologue]] / [[LinkRegister]] — the three new concept pages this chapter mints.
- [[CallingConvention]] — umbrella concept; AAPCS64 is the [[ARM64]] variant.
- [[StackFrame]] / [[FramePointer]] / [[StackPointer]] — bracket the active frame; the [[ARM64]] realizations use `x29` / `sp`.

## Contradictions

None. Ch 9.5 **extends** the Ch 9 instruction-family tour with the function-call category. The [[LinkRegister|`x30`-as-return-address]] discipline is an **alternative ISA-design answer** to [[X86_64|x86]]'s stack-resident return address — distinct mechanism, same conceptual role.
