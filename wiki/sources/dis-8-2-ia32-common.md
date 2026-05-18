---
title: "Dive into Systems — Ch 8.2 Common Instructions (IA32)"
type: source
tags: [dive-into-systems, ia32, assembly, instructions, mov, add, sub, push, pop, stack, 32-bit]
date: 2026-05-17
source_file: https://diveintosystems.org/book/C8-IA32/common.html
---

## Summary

[[SuzanneJMatthews|Matthews]] / [[TiaNewhall|Newhall]] / [[KevinCWebb|Webb]]'s **Ch 8.2** of *[[DiveIntoSystems]]* — the **second leaf** of Ch 8 *32-bit IA32 Assembly* and the **32-bit structural twin** of [[dis-7-2-x86-64-common|Ch 7.2]]. Re-presents the same five common instructions — [[X86MovInstruction|`mov`]], the [[X86ArithmeticInstructions|`add` / `sub`]] arithmetic pair, and the [[X86StackInstructions|`push` / `pop`]] stack pair — but at the **32-bit IA32 register width**. **Headline 32-vs-64 deltas**: (1) instructions implicitly operate on **4-byte (`l`) operands** by default — the `q` 64-bit suffix has no IA32 application; (2) the [[StackPointer|stack pointer]] is **`%esp`** and the [[FramePointer|frame pointer]] is **`%ebp`** (not `%rsp` / `%rbp`); (3) [[X86StackInstructions|`push` / `pop`]] adjust `%esp` by **4 bytes** (not 8) — matching the 32-bit register width; (4) function return value lives in **`%eax`** (not `%rax`). The stack-grows-down convention, [[AtAndTSyntax|source-then-destination AT&T order]], operand-type rules ([[Constant|constant]] / [[CpuRegister|register]] / [[MemoryOperand|memory]]; no constant destination, ≤ one memory operand), and instruction semantics (`mov S, D` = `D ← S`; `add S, D` = `D ← D + S`; `sub S, D` = `D ← D − S`) are **structurally identical** to [[dis-7-2-x86-64-common|Ch 7.2]]. **78th ingested chapter — second leaf of Ch 8.** **No new concept pages** — reuses [[X86MovInstruction]], [[X86ArithmeticInstructions]], [[X86StackInstructions]] from [[dis-7-2-x86-64-common|Ch 7.2]]; the IA32-specific machinery ([[IA32]] register set, [[CdeclCallingConvention|cdecl]]) already lives on the [[dis-8-1-ia32-basics|Ch 8.1]] / [[IA32]] pages.

## Key Claims

- **The same five instructions [[dis-7-2-x86-64-common|Ch 7.2]] introduced apply at IA32 width.** [[X86MovInstruction|`mov S, D`]] / [[X86ArithmeticInstructions|`add S, D`]] / [[X86ArithmeticInstructions|`sub S, D`]] / [[X86StackInstructions|`push S`]] / [[X86StackInstructions|`pop D`]] — same operand rules, same semantics; the only delta is the **operand width** (32 bits / 4 bytes default).
- **`l` is the default integer suffix on IA32.** Where [[dis-7-2-x86-64-common|Ch 7.2]] showed `movq` / `addq` etc. as the canonical 8-byte forms, Ch 8.2 examples use the implicit 4-byte form (no `q` variant exists on IA32 — the 64-bit width has no register to land in).
- **[[StackPointer|`%esp`]] is the IA32 stack pointer; [[FramePointer|`%ebp`]] the frame pointer.** The [[CallStack|call-stack]] discipline from [[dis-7-2-x86-64-common|Ch 7.2]] is identical in shape but uses these 32-bit names.
- **[[X86StackInstructions|`push` / `pop`]] adjust [[StackPointer|`%esp`]] by 4 bytes**, not 8 — matching the 32-bit register width. *"`push` and `pop` instructions require only one operand apiece."*
- **The execution stack grows toward lower addresses on IA32**, as on [[X86_64|x86-64]]: *"On IA32 systems, the execution stack grows toward lower addresses."* — restating the [[dis-7-2-x86-64-common|Ch 7.2]] convention at IA32 width.
- **[[CdeclCallingConvention|cdecl]] return-value rule: `%eax` holds the function return value.** *"By convention, the register `%eax` always contains the return value (if one exists)."* — the IA32 mirror of x86-64's `%rax` rule.

## Key Quotes

> "On IA32 systems, the execution stack grows toward lower addresses." — stack-grows-down at IA32 width.

> "Notice that while the three instructions require two operands, the `push` and `pop` instructions require only one operand apiece." — the operand-arity split (`mov` / `add` / `sub` are two-operand; `push` / `pop` are one-operand).

> "By convention, the register `%eax` always contains the return value (if one exists)." — the IA32 [[CdeclCallingConvention|cdecl]] return-value rule.

## Connections

- [[DiveIntoSystems]] — book; **78th ingested chapter**, second leaf of Ch 8 *32-bit IA32 Assembly*.
- [[SuzanneJMatthews]] / [[TiaNewhall]] / [[KevinCWebb]] — authors.
- [[dis-8-1-ia32-basics]] — direct predecessor; Ch 8.2 reuses Ch 8.1's [[IA32]] register set ([[GeneralPurposeRegister|8 GPRs]] — `%eax` / `%ebx` / `%ecx` / `%edx` / `%edi` / `%esi` / `%esp` / `%ebp`), [[CdeclCallingConvention|cdecl]], and operand-type rules.
- [[dis-7-2-x86-64-common]] — **structural twin**; Ch 8.2 re-presents the same five instructions at IA32 width.
- [[IA32]] — the 32-bit ISA whose instruction set Ch 8.2 enumerates.
- [[X86MovInstruction]] — reused: the data-movement primitive `mov`.
- [[X86ArithmeticInstructions]] — reused: the `add` / `sub` pair.
- [[X86StackInstructions]] — reused: the `push` / `pop` pair (adjusts [[StackPointer|`%esp`]] by 4 bytes on IA32 vs 8 on [[X86_64|x86-64]]).
- [[StackPointer]] — `%esp` on IA32 (vs `%rsp` on x86-64).
- [[FramePointer]] — `%ebp` on IA32 (vs `%rbp` on x86-64).
- [[CallStack]] / [[StackFrame]] — the data structure `push` / `pop` manipulate.
- [[CdeclCallingConvention]] — return value lives in `%eax`.
- [[OperandSize]] — `l` (4-byte) is the IA32 default; `q` does not apply.
- [[AtAndTSyntax]] — source-first `mov src, dst` order, same as Ch 7.2.

## Contradictions

None. Ch 8.2 is a **consistent 32-bit re-presentation** of [[dis-7-2-x86-64-common|Ch 7.2]] — instruction semantics, operand rules, and stack-discipline invariants are identical; only the register width (32 vs 64), default suffix (`l` vs `q`), stack step (4 vs 8 bytes), and stack/frame/return-register names (`%esp` / `%ebp` / `%eax` vs `%rsp` / `%rbp` / `%rax`) differ.
