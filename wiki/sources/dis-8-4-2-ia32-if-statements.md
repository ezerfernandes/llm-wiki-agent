---
title: "Dive into Systems — Ch 8.4.2 If Statements in Assembly (IA32)"
type: source
tags: [dive-into-systems, ia32, assembly, control-flow, if-else, conditional, cmov, 32-bit]
date: 2026-05-17
source_file: https://diveintosystems.org/book/C8-IA32/if_statements.html
---

## Summary

[[SuzanneJMatthews|Matthews]] / [[TiaNewhall|Newhall]] / [[KevinCWebb|Webb]]'s **Ch 8.4.2** of *[[DiveIntoSystems]]* — the **second leaf** of [[dis-8-4-ia32-conditional-loops|Ch 8.4]] and the **32-bit structural twin** of [[dis-7-4-2-x86-64-if-statements|Ch 7.4.2]]. Operationalizes the [[dis-8-4-1-ia32-preliminaries|Ch 8.4.1]] mechanism families ([[X86FlagsRegister|FLAGS]] + [[CmpInstruction|`cmp`]] + [[X86JumpInstructions|conditional jumps]]) into the **canonical compilation pattern** for [[CLanguage|C]]'s [[IfStatement|`if`]] / [[ElseStatement|`else`]] construct via the same `getSmallest(int x, int y)` worked example as [[dis-7-4-2-x86-64-if-statements|Ch 7.4.2]] — traced through both **unoptimized (branch-based)** and **`-O1`-optimized (branch-free, [[X86ConditionalMove|`cmov`]]-based)** [[IA32]] assembly. **Headline 32-vs-64 deltas**: (1) parameters are read from the stack via [[FramePointer|`%ebp`]]-anchored offsets (`mov 0x8(%ebp), %eax`; `cmp 0xc(%ebp), %eax`) per the [[CdeclCallingConvention|cdecl calling convention]] — **not** from `%edi`/`%esi` like the [[SystemVCallingConvention|System V]] x86-64 form; (2) return value lives in `%eax` (not `%rax`); (3) the [[X86ConditionalMove|`cmovle`]] form is `cmovle 0x8(%ebp), %eax` — moves a 32-bit stack-memory operand into a 32-bit register, vs Ch 7.4.2's register-to-register `cmovle %edi, %eax`. The two **branch-pattern rules** carry over unchanged: (a) the branch-based form jumps on the **negated** source condition — *"a 'jump' (to the `else`) occurs when conditions are not true"* — the `jle` fires precisely when `x ≤ y`, falling through to the then-branch when the source `x > y` holds; (b) the `-O1` substitution to [[X86ConditionalMove|`cmov`]] **eliminates** the [[ControlHazard|control hazard]] / [[BranchPrediction|branch-prediction]] dependency at the cost of pre-evaluating both arms. **82nd ingested DIS chapter — second leaf of Ch 8.4.** **No new concept pages** — reuses [[X86ConditionalMove]], [[AsmIfThenElse]], [[BranchInstruction]], [[CmpInstruction]], [[X86JumpInstructions]] from [[dis-7-4-2-x86-64-if-statements|Ch 7.4.2]] unchanged.

## Key Claims

- **Same `getSmallest` worked example as [[dis-7-4-2-x86-64-if-statements|Ch 7.4.2]] at IA32 width.** The C source is byte-identical; only the [[IA32]] assembly form differs — stack-based parameter access and 32-bit register names.
- **Stack-based parameter access is the headline IA32 delta.** *"`mov 0x8(%ebp),%eax`"* loads parameter `x` from the stack (offset 8 from [[FramePointer|`%ebp`]]); *"`cmp 0xc(%ebp),%eax`"* compares against parameter `y` at offset 12 — per the [[CdeclCallingConvention|cdecl convention]] from [[dis-8-1-ia32-basics|Ch 8.1]]. Contrast with [[dis-7-4-2-x86-64-if-statements|Ch 7.4.2]]'s `%edi` / `%esi` register-passed parameters.
- **Branch-pattern rule unchanged: jump on the negated condition.** *"Compilers translating code into assembly designate a jump when a condition is true. Contrast this behavior with the structure of an `if` statement, where a 'jump' (to the `else`) occurs when conditions are not true"* — the [[X86JumpInstructions|`jle`]] in the IA32 trace fires when `x ≤ y` (the negation of `x > y`), falling through to the then-branch when the source condition holds. Same as [[dis-7-4-2-x86-64-if-statements|Ch 7.4.2]].
- **`-O1` substitutes [[X86ConditionalMove|`cmovle`]] for the branch — same as x86-64.** The optimizer rewrites the explicit if/else as a ternary-equivalent `cmovle 0x8(%ebp), %eax` — a single conditional move that **eliminates the branch** and the [[ControlHazard|control hazard]] / [[BranchPrediction|branch-prediction]] dependency, at the cost of pre-evaluating both arms. Same structural reasoning as on x86-64; the only delta is the IA32 stack-memory source operand vs x86-64's register source.
- **Branch-free safety constraint identical.** As on x86-64, [[X86ConditionalMove|`cmov`]] cannot be used when one arm has side effects or could fault (e.g. [[NullPointerSafety|null-pointer dereference]]) — the compiler falls back to the branch-based form when pre-evaluation is unsafe.

## Key Quotes

> "Compilers translating code into assembly designate a jump when a condition is true. Contrast this behavior with the structure of an `if` statement, where a 'jump' (to the `else`) occurs when conditions are not true." — the jump-on-negated-condition rule at IA32 width.

> "`mov 0x8(%ebp),%eax` — load first parameter (x); `cmp 0xc(%ebp),%eax` — compare with second parameter (y); `jle 0x8048421` — 'jump if less-than-or-equal' (the *negated* condition x > y)." — the stack-based parameter access pattern that distinguishes the IA32 form from [[dis-7-4-2-x86-64-if-statements|Ch 7.4.2]].

> "`cmovle 0x8(%ebp),%eax` — 'move x to %eax only if x ≤ y.'" — the branch-free [[X86ConditionalMove|`cmov`]] form, with the IA32-specific stack-memory source operand.

## Connections

- [[DiveIntoSystems]] — book; **82nd ingested chapter**, second leaf of Ch 8.4.
- [[SuzanneJMatthews]] / [[TiaNewhall]] / [[KevinCWebb]] — authors.
- [[dis-8-4-ia32-conditional-loops]] — Ch 8.4 hub; direct parent.
- [[dis-8-4-1-ia32-preliminaries]] — Ch 8.4.1; supplies the FLAGS / `cmp` / jump mechanisms Ch 8.4.2 operationalizes.
- [[dis-8-1-ia32-basics]] — Ch 8.1; supplies the [[CdeclCallingConvention|cdecl]] stack-parameter convention the if-pattern reads from.
- [[dis-7-4-2-x86-64-if-statements]] — **structural twin** at x86-64 width.
- [[IA32]] — the 32-bit ISA whose if-compilation pattern Ch 8.4.2 covers.
- [[AsmIfThenElse]] — reused; same jump-on-negated-condition compilation pattern, stack-based parameter access is the IA32 delta.
- [[X86ConditionalMove]] — reused; same branch-elimination role; IA32 form uses stack-memory source operands.
- [[BranchInstruction]] — reused; same role as the unifying concept above the jump family and `cmov`.
- [[CmpInstruction]] / [[X86JumpInstructions]] — reused; same flag-setting and consumer-mnemonic conventions.
- [[CdeclCallingConvention]] — operationalized here; stack-based parameter access via `%ebp+8` / `%ebp+12` / ... is the headline IA32 delta vs the System V form.
- [[FramePointer]] — `%ebp` (IA32) vs `%rbp` (x86-64); the anchor for stack-based parameter access.
- [[ControlHazard]] / [[BranchPrediction]] — what `cmov` substitution eliminates, same as on x86-64.
- [[NullPointerSafety]] — the safety constraint that prevents `cmov` substitution when one arm could fault.
- [[CompilerOptimization]] — the `-O1` substitution from branch to `cmov`.

## Contradictions

None. Ch 8.4.2 is a **consistent 32-bit re-presentation** of [[dis-7-4-2-x86-64-if-statements|Ch 7.4.2]] — branch-pattern rule, `cmov`-substitution rule, and safety constraints are structurally identical; only the parameter-access mechanism (stack-based [[CdeclCallingConvention|cdecl]] via `%ebp+N` vs register-based [[SystemVCallingConvention|System V]] `%edi`/`%esi`), register widths (`%eax` vs `%rax`), and `cmov` operand form (stack-memory vs register) differ.
