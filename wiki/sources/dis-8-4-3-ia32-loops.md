---
title: "Dive into Systems — Ch 8.4.3 Loops in Assembly (IA32)"
type: source
tags: [dive-into-systems, ia32, assembly, control-flow, loops, while, for, do-while, 32-bit]
date: 2026-05-17
source_file: https://diveintosystems.org/book/C8-IA32/loops.html
---

## Summary

[[SuzanneJMatthews|Matthews]] / [[TiaNewhall|Newhall]] / [[KevinCWebb|Webb]]'s **Ch 8.4.3** of *[[DiveIntoSystems]]* — the **third and final leaf** of [[dis-8-4-ia32-conditional-loops|Ch 8.4]] and the **32-bit structural twin** of [[dis-7-4-3-x86-64-loops|Ch 7.4.3]]. Operationalizes the [[dis-8-4-1-ia32-preliminaries|Ch 8.4.1]] mechanism families ([[X86FlagsRegister|FLAGS]] + [[CmpInstruction|`cmp`]] + [[X86JumpInstructions|conditional jumps]]) into the **canonical compilation pattern** for [[CLanguage|C]]'s [[WhileLoop|`while`]] / [[ForLoop|`for`]] / [[DoWhileLoop|`do`–`while`]] constructs at the [[IA32]] [[AssemblyLanguage|assembly]] surface, via the same `sumUp(int n)` worked example as [[dis-7-4-3-x86-64-loops|Ch 7.4.3]]. **Headline 32-vs-64 deltas**: (1) local variables live in [[FramePointer|`%ebp`]]-relative **negative** stack slots — `total` at `-0x8(%ebp)`, `i` at `-0x4(%ebp)` — vs Ch 7.4.3's compiler-chosen register / `%rbp`-relative slots; (2) parameter `n` is read from the stack at `0x8(%ebp)` (cdecl), not `%edi` (System V); (3) the unconditional `jmp` target is a 32-bit address (`%eip`); (4) the standard prologue saves [[FramePointer|`%ebp`]] and the epilogue uses `leave` + `ret`. The three **jump-to-test pattern rules** carry over **unchanged**: (a) the canonical `while`/`for` pattern is **jump-to-test** — an unconditional `jmp` skips the body, lands at the condition check, and a conditional jump on the **un-negated** loop condition branches **back** to the body — the **inverse** of [[dis-8-4-2-ia32-if-statements|Ch 8.4.2]]'s if-pattern (forward jump on the **negated** condition); (b) `for` and `while` produce **identical assembly** — *"every `for` loop can be represented by a `while` loop"*; (c) `do`–`while` **drops the leading `jmp`** because the body always executes once unconditionally. **83rd ingested DIS chapter — third and final leaf of [[dis-8-4-ia32-conditional-loops|Ch 8.4]], closing the [[ControlFlow|control-flow]] section of Ch 8.** **No new concept pages** — reuses [[AsmLoopPattern]], [[X86JumpInstructions]], [[CmpInstruction]], [[X86FlagsRegister]] from [[dis-7-4-3-x86-64-loops|Ch 7.4.3]] unchanged.

## Key Claims

- **Same `sumUp(int n)` worked example as [[dis-7-4-3-x86-64-loops|Ch 7.4.3]] at IA32 width.** C source byte-identical; only the [[IA32]] assembly form differs — stack-based locals, [[CdeclCallingConvention|cdecl]] parameter passing, and 32-bit register names.
- **Stack-based locals are the headline IA32 delta.** *"Local variables occupy stack positions: `total` at `%ebp-0x8` and `i` at `%ebp-0x4`"* — the IA32 form spills locals to the stack instead of holding them in registers as the [[dis-7-4-3-x86-64-loops|x86-64 -O0 form]] does. Initialization via `movl $0x1, -0x4(%ebp)` and `movl $0x0, -0x8(%ebp)`.
- **Jump-to-test pattern rule unchanged.** *"The first instruction is a direct jump to `<sumUp+32>`, which sets the instruction pointer (`%eip`) to address 0x804842b"* — an unconditional `jmp` lands at the condition check; the body is reached only after the first comparison succeeds. **`jle`** (or analogous signed-`>` consumer) branches **back** to the body when the un-negated `i <= n` holds — the inverse of the [[dis-8-4-2-ia32-if-statements|Ch 8.4.2]] if-pattern.
- **`for` / `while` equivalence carries over.** *"Every `for` loop can be represented by a `while` loop"* — `for (init; cond; step) { body; }` decomposes mechanically to `init; while (cond) { body; step; }` and the [[CCompiler|compiler]] emits **identical IA32 assembly** for both. Same rule as [[dis-7-4-3-x86-64-loops|Ch 7.4.3]].
- **`do`–`while` drops the leading `jmp` — same as x86-64.** Because the body always executes once unconditionally, the test-then-body sequence becomes body-then-test; the unconditional `jmp` to the condition is omitted. Strictly simpler than the `while`/`for` pattern at the assembly surface.
- **Frame discipline closes the function.** *"The `leave` instruction concludes by restoring the caller's stack frame before `ret`"* — same `leave; ret` epilogue pattern as [[dis-7-5-x86-64-functions|Ch 7.5]]'s `leaveq; retq` (just the IA32 mnemonic forms).

## Key Quotes

> "The first instruction is a direct jump to `<sumUp+32>`, which sets the instruction pointer (`%eip`) to address 0x804842b." — the **jump-to-test** pattern at IA32 width, with `%eip` standing in for `%rip`.

> "Every `for` loop can be represented by a `while` loop." — the `for`/`while` equivalence at IA32 width; same rule as [[dis-7-4-3-x86-64-loops|Ch 7.4.3]].

> "The `leave` instruction concludes by restoring the caller's stack frame before `ret`." — the IA32 epilogue pattern (`leave` is just the mnemonic; semantically identical to `leaveq` on x86-64).

## Connections

- [[DiveIntoSystems]] — book; **83rd ingested chapter**, third leaf of Ch 8.4.
- [[SuzanneJMatthews]] / [[TiaNewhall]] / [[KevinCWebb]] — authors.
- [[dis-8-4-ia32-conditional-loops]] — Ch 8.4 hub; direct parent.
- [[dis-8-4-1-ia32-preliminaries]] — Ch 8.4.1; supplies the FLAGS / `cmp` / jump mechanisms.
- [[dis-8-4-2-ia32-if-statements]] — Ch 8.4.2; sibling leaf — the loop pattern is the **inverse** of the if-pattern (back-jump on un-negated condition vs forward-jump on negated condition).
- [[dis-8-1-ia32-basics]] — Ch 8.1; supplies the [[CdeclCallingConvention|cdecl]] / [[FramePointer|`%ebp`]]-frame conventions.
- [[dis-7-4-3-x86-64-loops]] — **structural twin** at x86-64 width.
- [[IA32]] — the 32-bit ISA whose loop-compilation pattern Ch 8.4.3 covers.
- [[AsmLoopPattern]] — reused; same canonical jump-to-test loop compilation pattern covering all three of `while` / `for` / `do`–`while`; IA32 delta: stack-based locals and `%eip`/`%ebp` register names.
- [[X86JumpInstructions]] / [[CmpInstruction]] / [[X86FlagsRegister]] / [[ConditionCode]] — reused; same flag-setting and consumer-mnemonic conventions.
- [[InstructionPointer]] — `%eip` (IA32) vs `%rip` (x86-64).
- [[FramePointer]] — `%ebp` (IA32) vs `%rbp` (x86-64); locals reach via negative offsets `-0x4(%ebp)`, `-0x8(%ebp)`.
- [[CdeclCallingConvention]] — parameter `n` read from `0x8(%ebp)`, not `%edi`.
- [[WhileLoop]] / [[ForLoop]] / [[DoWhileLoop]] — the three [[CLanguage|C]] loop constructs the compilation pattern covers; same trio as [[dis-7-4-3-x86-64-loops|Ch 7.4.3]].
- [[LeaveInstruction]] — `leave` (IA32) vs `leaveq` (x86-64); same `mov %ebp, %esp; pop %ebp` semantics.

## Contradictions

None. Ch 8.4.3 is a **consistent 32-bit re-presentation** of [[dis-7-4-3-x86-64-loops|Ch 7.4.3]] — jump-to-test pattern, `for`/`while` equivalence, `do`–`while` simplification, and `leave`/`ret` frame discipline are structurally identical; only the local-variable storage (stack-based vs register-based at `-O0`), parameter-access mechanism (cdecl `%ebp+N` vs System V `%edi`), and register widths (`%eax`/`%ebp`/`%eip` vs `%rax`/`%rbp`/`%rip`) differ.
