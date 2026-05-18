---
title: "Dive into Systems — Ch 8.1 IA32 Assembly Basics"
type: source
tags: [dive-into-systems, ia32, x86, assembly, isa, registers, att-syntax, addressing-modes, 32-bit]
date: 2026-05-17
source_file: https://diveintosystems.org/book/C8-IA32/basics.html
---

## Summary

[[SuzanneJMatthews|Matthews]] / [[TiaNewhall|Newhall]] / [[KevinCWebb|Webb]]'s **Ch 8.1** of *[[DiveIntoSystems]]* — **opens Ch 8 *32-bit IA32 Assembly***, the **32-bit sibling of [[dis-7-1-x86-64-basics|Ch 7.1]]**. Re-runs the same `adder2` walkthrough — from [[CLanguage|C]] to [[AssemblyLanguage|assembly]] in [[AtAndTSyntax|AT&T syntax]] — but now compiled with `gcc -m32` against the [[IA32|32-bit IA32]] [[ISA]]. Headline 32-vs-64 deltas: (1) **eight** [[GeneralPurposeRegister|GPRs]] instead of 16 — `%eax`, `%ebx`, `%ecx`, `%edx`, `%edi`, `%esi`, `%esp`, `%ebp` (no `%r8`–`%r15`); (2) **letter-substitution subregisters only** — `%eax` (32) → `%ax` (16) → `%al`/`%ah` (8) — no suffix-style names since there are no new `%r8`–`%r15` registers to suffix; (3) **stack-based parameter passing** — IA32 has **no** [[SystemVCallingConvention|System V six-argument-register convention]]; all function arguments are passed on the stack (cdecl); (4) **`l` suffix is the default integer width** (32 bits) — `q` (64-bit) and the `s`/`d` float suffixes mostly out of play. The [[Operand|operand-type]] taxonomy, [[X86AddressingMode|`disp(base, index, scale)` addressing modes]], and source-then-destination instruction order are **structurally identical** to [[dis-7-1-x86-64-basics|Ch 7.1]].

## Key Claims

- **Eight 32-bit general-purpose registers.** *"There are eight 32-bit registers for data storage: `%eax`, `%ebx`, `%ecx`, `%edx`, `%edi`, `%esi`, `%esp`, and `%ebp`."* The first six are general-purpose; `%esp` is the [[StackPointer|stack pointer]] (top of stack) and `%ebp` the [[FramePointer|frame pointer]] (current [[StackFrame|stack frame]] base) — *"the last two are compiler-reserved"*. Plus `%eip` as the [[InstructionPointer|instruction pointer]] — *"programs cannot write directly to it"* (same read-only rule [[dis-7-1-x86-64-basics|Ch 7.1]]'s `%rip` carries).
- **Subregister naming uses letter substitution only.** `%eax` (32 bits) → `%ax` (low 16) → `%al`/`%ah` (low/high byte of `%ax`). For the first four registers (`%eax`/`%ebx`/`%ecx`/`%edx`) the byte split into `%aX`/`%aH` is available; `%edi` / `%esi` / `%esp` / `%ebp` expose only the 16-bit low form (`%di`/`%si`/`%sp`/`%bp`). **No suffix-style names** (no `%eaxd` etc.) — that scheme only exists in [[X86_64|x86-64]] for the new `%r8`–`%r15` registers IA32 doesn't have. The byte-level access *"facilitates operations like bitwise shifts requiring single-byte operands"*.
- **IA32 has no register-based [[CallingConvention|calling convention]].** Unlike [[dis-7-1-x86-64-basics|Ch 7.1]]'s [[SystemVCallingConvention|System V AMD64 ABI]] (first six args in `%rdi` / `%rsi` / `%rdx` / `%rcx` / `%r8` / `%r9`), the IA32 [[CdeclCallingConvention|cdecl convention]] passes **all** function arguments on the stack — accessed inside the callee as `8(%ebp)`, `12(%ebp)`, `16(%ebp)`, ... (positive offsets above the saved `%ebp`). Return value still in `%eax`. The first-six-args-in-registers rule [[dis-7-1-x86-64-basics|Ch 7.1]] introduced **does not apply** here — Ch 8.1 introduces this delta but the worked example deferred to later Ch 8 sections (Ch 8.5 *Functions*).
- **Instruction structure and operand types identical to [[X86_64|x86-64]].** [[AtAndTSyntax|AT&T order]] (`mov src, dst`), three [[Operand|operand types]] — **constant** prefixed `$` (e.g., `$0x2`), **register** prefixed `%` (e.g., `%eax`), **memory** as an addressing-mode expression. Same two structural constraints: constants cannot be destinations; *"memory forms cannot serve both as the source and destination operand in a single instruction."* The operand `0x8(%ebp)` *"loosely translates to 'add 0x8 to the value in register `%ebp`, and then perform a memory lookup'"* — the canonical pattern for accessing the first stack-passed parameter.
- **[[X86AddressingMode|Memory addressing modes]] match Ch 7.1's six-form table** — `(%eax)` (indirect), `0x8(%eax)` (displacement + base), `(%eax, %ecx)` (base + index), `0x800(,%edx,4)` (displacement + scaled index, no base), and the full `disp(base, index, scale)` form. *"Scale factors: 1, 2, 4, or 8"* — same [[CPrimitiveType|primitive-type byte-width]] set.
- **[[OperandSize|Size suffixes]] collapse to `b` / `w` / `l`.** Three suffixes: `b` = 1 byte (`char`), `w` = 2 bytes (`short`), `l` = 4 bytes (`int` / `long` — *"long is 4 bytes on IA32, despite the name"*). The 64-bit `q` suffix has no application in IA32 since there are no 64-bit registers. Float suffixes (`s` / `d`) exist but are out of scope for Ch 8's integer-arithmetic walkthrough. *"The compiler automatically selects appropriate suffixes during translation"* — same compiler-driven discipline as Ch 7.
- **Compilation pipeline is `gcc -m32 -S simpleops.c`.** The `-m32` flag forces IA32 emission on any modern 64-bit host. *"Examples use unoptimized compilation (`gcc -m32` without `-O` flags), producing seemingly redundant instructions"* — *"the compiler is not 'smart' — it simply follows a series of rules"*. Optimization passes deferred to later chapters.

## Key Quotes

> "There are eight 32-bit registers for data storage: `%eax`, `%ebx`, `%ecx`, `%edx`, `%edi`, `%esi`, `%esp`, and `%ebp`." — the canonical IA32 [[GeneralPurposeRegister|GPR]] set, **half the [[X86_64|x86-64]] count**.

> "Memory forms cannot serve both as the source and destination operand in a single instruction." — same [[Operand|operand]] constraint Ch 7.1 stated; carries over unchanged from [[X86_64|x86-64]] because it is a feature of the underlying [[CISC]] [[ISA]] family, not the register width.

> "The compiler is not 'smart' — it simply follows a series of rules to translate human-readable code into machine language." — Ch 8.1's recap of the unoptimized-output rationale, anchoring the visible redundancy in subsequent traces.

## Connections

- [[DiveIntoSystems]] — book; **77th ingested chapter**, **first leaf of Ch 8 *32-bit IA32 Assembly***. Mirrors [[dis-7-1-x86-64-basics|Ch 7.1]] for the 32-bit ISA.
- [[SuzanneJMatthews]] / [[TiaNewhall]] / [[KevinCWebb]] — authors.
- [[dis-7-1-x86-64-basics|Ch 7.1]] — **direct structural twin**: same `adder2` walkthrough, same [[AtAndTSyntax|AT&T syntax]], same operand / addressing-mode / suffix vocabulary; Ch 8.1 differs only in register width, register count, and calling convention.
- [[dis-6-asm-intro|Ch 6]] — Part III hub forecasting both Ch 7 (x86-64) and Ch 8 (IA32) as the two x86 dialects.
- [[dis-2-9-7-c-to-assembly|Ch 2.9.7]] — **the corpus's first IA32 sighting** via `gcc -m32 -S`; Ch 8.1 now supplies the architectural reference Ch 2.9.7's worked example anchored against.
- [[IA32]] — **the concept page Ch 8.1 expands** from the [[dis-2-9-7-c-to-assembly|Ch 2.9.7]] introduction to the full register-set / addressing-mode / suffix surface.
- [[X86_64]] — the 64-bit sibling — Ch 8.1's structural twin and the explicit comparison target.
- [[GeneralPurposeRegister]] — the IA32 GPR set is a strict subset of the [[X86_64|x86-64]] GPRs (the lower 32 bits of `%rax`–`%rsi`, no `%r8`–`%r15`).
- [[AtAndTSyntax]] — the [[AssemblyLanguage|assembly]] syntax dialect — unchanged from Ch 7.1.
- [[OperandSize]] — the suffix family — `b` / `w` / `l` apply; `q` does not (no 64-bit registers).
- [[X86AddressingMode]] — the `disp(base, index, scale)` template — unchanged.
- [[Operand]] — the three operand types — unchanged.
- [[StackPointer]] / [[FramePointer]] — `%esp` / `%ebp` are the IA32 names of the same architectural roles `%rsp` / `%rbp` play in [[X86_64|x86-64]].
- [[InstructionPointer]] — `%eip` is the IA32 form of `%rip`; same read-only rule.
- [[CallingConvention]] — IA32 [[CdeclCallingConvention|cdecl]] is **stack-only**; the [[SystemVCallingConvention|System V x86-64 ABI]]'s six argument registers do **not** apply.
- [[GCC]] — `gcc -m32` flag targets IA32 from a 64-bit host.

## Contradictions

None. Ch 8.1 **reuses** the operand / addressing-mode / suffix / instruction-structure framings Ch 7.1 established, narrowing them where appropriate to the 32-bit register width and stack-based calling convention. The [[IA32]] concept page's existing claims (32-bit register width, eight GPRs, `%ebp`-relative frame addressing, *"calling convention: most args on stack"*) are **confirmed and extended** by Ch 8.1's architectural reference.
