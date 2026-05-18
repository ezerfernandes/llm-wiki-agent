---
title: "Dive into Systems — Ch 8.5 Functions in Assembly (IA32)"
type: source
tags: [dive-into-systems, ia32, assembly, functions, calling-convention, stack-frame, cdecl, 32-bit]
date: 2026-05-17
source_file: https://diveintosystems.org/book/C8-IA32/functions.html
sources: []
last_updated: 2026-05-17
---

## Summary

Chapter 8.5 of *[[DiveIntoSystems]]* — **fifth leaf** of Ch 8 *32-bit IA32 Assembly* and the **32-bit structural twin** of [[dis-7-5-x86-64-functions|Ch 7.5]]. Re-presents the function-call instruction family — [[CallInstruction|`call`]] / [[RetInstruction|`ret`]] / [[LeaveInstruction|`leave`]] — and the [[CallStack|call-stack]] / [[StackFrame|stack-frame]] discipline at [[IA32]] width under the [[CdeclCallingConvention|cdecl]] [[CallingConvention|calling convention]]. **Headline 32-vs-64 deltas**: (1) **all parameters pushed on the stack** — IA32 cdecl has *no* six-argument-register fast path (vs Ch 7.5's System V `%rdi`/`%rsi`/`%rdx`/`%rcx`/`%r8`/`%r9`); callee reads the i-th parameter at `(%ebp+8+4*(i-1))` — **first** parameter at `8(%ebp)`, **second** at `12(%ebp)`, **third** at `16(%ebp)`, etc.; (2) **return value in [[CalleeSavedRegister|`%eax`]]** (or `%edx:%eax` for 64-bit returns) — not `%rax`; (3) stack-frame anchors are [[StackPointer|`%esp`]] (top) and [[FramePointer|`%ebp`]] (frame base) — not `%rsp` / `%rbp`; (4) instruction mnemonics drop the `q` suffix: `call` (not `callq`), `ret` (not `retq`), `leave` (not `leaveq`); (5) [[CallInstruction|`call`]] pushes a 4-byte saved-[[InstructionPointer|`%eip`]] (not 8-byte saved-`%rip`); the [[ExecutionStack|stack]] therefore grows by 4 bytes per call (not 8). **Headline rules carry over unchanged**: the prologue/epilogue pattern (`push %ebp; mov %esp, %ebp; sub $N, %esp` then `leave; ret`), the saved-frame-pointer linked-list along the [[CallStack|call stack]], and the [[CallerSavedRegister|caller-saved]] (`%eax`/`%ecx`/`%edx`) vs [[CalleeSavedRegister|callee-saved]] (`%ebx`/`%esi`/`%edi`/`%ebp`) partition (already minted by [[dis-8-1-ia32-basics|Ch 8.1]]'s [[CdeclCallingConvention]] page). **84th ingested DIS chapter — fifth leaf of Ch 8.** **No new concept pages** — reuses [[CallInstruction]] / [[RetInstruction]] / [[LeaveInstruction]] / [[CallingConvention]] / [[CdeclCallingConvention]] / [[StackPointer]] / [[FramePointer]] / [[CallerSavedRegister]] / [[CalleeSavedRegister]] from [[dis-7-5-x86-64-functions|Ch 7.5]] and [[dis-8-1-ia32-basics|Ch 8.1]].

## Key Claims

- **Two new instructions, same control-flow algebra.** [[CallInstruction|`call addr`]] *"saves the current value of [[InstructionPointer|`%eip`]] on the stack to represent the return address"* and jumps to `addr`; [[RetInstruction|`ret`]] *"restores the value of [[InstructionPointer|`%eip`]] to the value saved on the stack, ensuring that the program resumes execution at the program address specified in the caller function."* Same atomic *jump+save* / *pop+jump* semantics as Ch 7.5's `callq` / `retq` — narrowed to 4-byte saved-`%eip` per IA32 width.
- **[[CdeclCallingConvention|Cdecl]] parameter passing: stack only, positive `%ebp` offsets.** First parameter at `%ebp+8`, second at `%ebp+12`, n-th at `%ebp + 8 + 4*(n-1)`. The fixed `+8` offset accounts for the saved-`%ebp` (4 bytes at `(%ebp)`) and the saved-`%eip` (4 bytes at `4(%ebp)`) the [[CallInstruction|`call`]] + prologue laid down. **No register-based argument fast path** — this is the single biggest pedagogical contrast against [[dis-7-5-x86-64-functions|Ch 7.5]]'s System V six-argument-register convention.
- **Return value in [[CalleeSavedRegister|`%eax`]].** Caller retrieves the return value from `%eax` after the [[CallInstruction|`call`]] returns. 64-bit returns use the `%edx:%eax` pair (high half in `%edx`, low half in `%eax`) — the same pair that [[dis-8-3-ia32-arithmetic|Ch 8.3]] established for [[X86MulInstruction|`mul` / `imul`]] and [[X86DivInstruction|`idiv` / `div`]] dividend / product handling.
- **Canonical prologue / epilogue pattern (32-bit width).** Prologue: `push %ebp` (save caller's frame pointer); `mov %esp, %ebp` (establish new frame base — `%ebp` now points at saved-`%ebp` slot); `sub $N, %esp` (allocate `N` bytes of local-variable space). Epilogue: [[LeaveInstruction|`leave`]] (equivalent to `mov %ebp, %esp; pop %ebp` — restores both pointers in one op); [[RetInstruction|`ret`]] (pops saved-`%eip` back into [[InstructionPointer|`%eip`]]). The `leave; ret` pair undoes everything the prologue did, restoring the caller's frame intact.
- **Caller-cleanup of arguments.** Per [[CdeclCallingConvention|cdecl]], the **caller** removes pushed arguments from the stack after [[RetInstruction|`ret`]] returns — typically via `add $N, %esp` where `N` is the total argument size — vs Windows stdcall's callee-cleanup. Caller cleanup is what makes cdecl naturally variadic-compatible ([[Printf|`printf`]], [[Scanf|`scanf`]]).

## Key Quotes

> "When the caller function executes the `call` instruction, the current value of `%eip` is saved on the stack to represent the return address." — the [[CallInstruction|`call`]] semantics: *save+jump* atomically, 4-byte saved-`%eip` (vs 8-byte saved-`%rip` per [[dis-7-5-x86-64-functions|Ch 7.5]]).

> "The `ret` instruction restores the value of `%eip` to the value saved on the stack, ensuring that the program resumes execution at the program address specified in the caller function." — the [[RetInstruction|`ret`]] semantics: *pop+jump* atomically.

## Connections

- [[DiveIntoSystems]] — book; **84th ingested chapter**, fifth leaf of Ch 8 *32-bit IA32 Assembly*.
- [[SuzanneJMatthews]] / [[TiaNewhall]] / [[KevinCWebb]] — co-authors.
- [[dis-7-5-x86-64-functions]] — **structural twin** at [[X86_64|x86-64]] width; same prologue/epilogue + call/ret pair; differs in parameter-passing (registers vs stack), return-register width (`%rax` vs `%eax`), and mnemonic suffixes (`callq`/`retq`/`leaveq` vs `call`/`ret`/`leave`).
- [[dis-8-4-3-ia32-loops]] — Ch 8.4.3; direct predecessor (closes the [[ControlFlow|control-flow]] section that Ch 8.5 builds on by adding the structured call/return pair).
- [[dis-8-1-ia32-basics]] — Ch 8.1; minted the [[CdeclCallingConvention]] page Ch 8.5 now operationalizes via [[CallInstruction|`call`]] / [[RetInstruction|`ret`]] / [[LeaveInstruction|`leave`]].
- [[CallInstruction]] / [[RetInstruction]] / [[LeaveInstruction]] — reused unchanged from [[dis-7-5-x86-64-functions|Ch 7.5]]; the IA32 forms drop the `q` suffix and save/restore a 4-byte `%eip` rather than 8-byte `%rip`.
- [[CdeclCallingConvention]] — the IA32 ABI Ch 8.5 operationalizes: stack-only args, caller cleanup, return in `%eax` / `%edx:%eax`.
- [[CallingConvention]] — umbrella concept; Ch 8.5 = the IA32 instance.
- [[StackPointer]] (`%esp`) / [[FramePointer]] (`%ebp`) — the two register-pair invariants Ch 8.5's prologue establishes and epilogue restores.
- [[CallerSavedRegister]] (`%eax`/`%ecx`/`%edx`) / [[CalleeSavedRegister]] (`%ebx`/`%esi`/`%edi`/`%ebp`) — the IA32 partition (minted on the [[CdeclCallingConvention]] page in Ch 8.1).
- [[CallStack]] / [[ExecutionStack]] / [[StackFrame]] — the per-call activation-record discipline Ch 8.5 builds frame-by-frame, 4 bytes (saved-`%eip`) + 4 bytes (saved-`%ebp`) + local-variable space per frame.
- [[InstructionPointer]] (`%eip`) — the 32-bit instruction pointer [[CallInstruction|`call`]] saves and [[RetInstruction|`ret`]] restores.
- [[IA32]] — the 32-bit ISA; Ch 8.5 adds the function-call instruction family + cdecl operationalization to its catalog.
- [[AssemblyLanguage]] / [[AtAndTSyntax]] — Ch 8.5 stays in [[AtAndTSyntax|AT&T source-then-destination order]].

## Contradictions

None. Ch 8.5 is a **consistent 32-bit re-presentation** of [[dis-7-5-x86-64-functions|Ch 7.5]] — the call/return instruction pair, prologue/epilogue pattern, and frame-pointer linked-list discipline are structurally identical; the calling-convention divergence (stack-only args, `%eax` return, no register fast path) was already documented on the [[CdeclCallingConvention]] page minted by [[dis-8-1-ia32-basics|Ch 8.1]].
