---
title: "Dive into Systems — Ch 7.1 Diving into Assembly: Basics (x86-64)"
type: source
tags: [dive-into-systems, x86-64, assembly, isa, registers, operands, att-syntax, addressing-modes]
date: 2026-05-17
source_file: https://diveintosystems.org/book/C7-x86_64/basics.html
---

## Summary

[[SuzanneJMatthews|Matthews]] / [[TiaNewhall|Newhall]] / [[KevinCWebb|Webb]]'s **Ch 7.1** of *[[DiveIntoSystems]]* — **opens Ch 7 *x86-64 Assembly*** of Part III, the first ISA-specific chapter after the [[dis-6-asm-intro|Ch 6]] hub. Walks the reader from a one-line C function (`adder2`) to its [[X86_64|x86-64]] [[AssemblyLanguage|assembly]] form in [[AtAndTSyntax|AT&T syntax]], anchoring four sub-topics: (1) the 16 [[GeneralPurposeRegister|general-purpose registers]] (`%rax`–`%rdx`, `%rdi`, `%rsi`, `%r8`–`%r15`) plus three special-purpose (`%rsp`, `%rbp`, `%rip`); (2) the **subregister naming scheme** that exposes each register's lower 32 / 16 / 8 bits under distinct names; (3) instruction structure (opcode + source-then-destination operands); (4) the three [[Operand|operand types]] (constant, register, memory) with [[X86AddressingMode|memory addressing modes]] up to displacement + base + scaled-index; and (5) the [[OperandSize|operand-size]] suffix table (`b` / `w` / `l` / `q` plus `s` / `d` for floats) that selects the data-width variant of each instruction.

## Key Claims

- **A register is "a word-sized storage unit located directly on the CPU."** The [[X86_64|x86-64]] [[ISA]] provides **16 [[GeneralPurposeRegister|general-purpose 64-bit registers]]** for integer / pointer data — `%rax`, `%rbx`, `%rcx`, `%rdx`, `%rdi`, `%rsi`, and `%r8`–`%r15` — plus the special-purpose `%rsp` (stack pointer), `%rbp` (frame/base pointer), and `%rip` (instruction pointer, read-only — *"cannot be written directly"*).
- **System V calling convention surfaces here.** *"Compilers typically store the first six parameters in registers `%rdi`, `%rsi`, `%rdx`, `%rcx`, `%r8` and `%r9`, respectively. Register `%rax` stores the return value from a function."* — the first explicit naming of the function-argument register order in the [[DiveIntoSystems]] corpus.
- **The subregister naming scheme exposes each register's lower bytes under distinct names.** First eight registers use a **letter-substitution** scheme: `%rax` (64) → `%eax` (low 32) → `%ax` (low 16) → `%al` (low 8) / `%ah` (next-higher 8). The new registers `%r8`–`%r15` use a **suffix** scheme: `%r8` (64) → `%r8d` (low 32) → `%r8w` (low 16) → `%r8b` (low 8). Compiler convention: *"the 64-bit registers when dealing with 64-bit values (e.g., pointers or `long` types) and the 32-bit component registers when dealing with 32-bit types (e.g., `int`)."*
- **Instruction structure is opcode + operands, source-then-destination ([[AtAndTSyntax|AT&T order]]).** Each instruction names an operation and zero or more operands; when two operands appear they read **left-to-right as `mov src, dst`** — the opposite of [[IntelSyntax|Intel syntax]]'s `mov dst, src`.
- **Three [[Operand|operand types]].** (1) **Constant / immediate** — prefixed `$` (e.g. `$0x2`); (2) **register** — name prefixed `%` (e.g. `%rsp`); (3) **memory** — an addressing-mode expression that dereferences an address in RAM. The constraint: *"constant forms cannot serve as destination operands"* and *"memory forms cannot serve as both the source and destination operand in a single instruction."*
- **[[X86AddressingMode|Memory addressing modes]] in [[AtAndTSyntax|AT&T syntax]]** follow the `disp(base, index, scale)` template — six concrete forms covered: `(%rax)` (indirect), `0x8(%rax)` (displacement + base), `(%rax, %rcx)` (base + index), `0x4(%rax, %rcx)` (displacement + base + index), `0x800(,%rdx,4)` (displacement + scaled index, no base), `(%rax, %rdx, 8)` (base + scaled index). **Scaling factors are restricted to 1, 2, 4, or 8** — the [[CPrimitiveType|primitive-type]] byte widths.
- **The [[OperandSize|operand-size]] suffix selects the data width.** *"Common and arithmetic instructions have a suffix that indicates the size (associated with the type) of the data being operated on."* Six suffixes: `b` (1 byte, `char`), `w` (2 bytes, `short`), `l` (4 bytes, `int` / `unsigned`), `s` (4 bytes, `float`), `q` (8 bytes, `long` / pointers), `d` (8 bytes, `double`). The suffix selects which sub-register variant the instruction reads/writes — `addl $0x2, %eax` is a 32-bit add on the 32-bit subregister; the `q` variant would write all 64 bits.

## Key Quotes

> "A register is a word-sized storage unit located directly on the CPU." — anchors the [[CpuRegister|register]] definition for the entire Ch 7 sequence.

> "The compiler typically uses the 64-bit registers when dealing with 64-bit values (e.g., pointers or long types) and the 32-bit component registers when dealing with 32-bit types (e.g., int)." — the **subregister selection rule** linking [[CPrimitiveType|C type width]] to register-name choice.

> "Common and arithmetic instructions have a suffix that indicates the size (associated with the type) of the data being operated on." — the [[OperandSize|operand-size]] mechanism in one sentence.

> "Scaling factors can be one of 1, 2, 4, or 8." — the only legal values for the scale field in `disp(base, index, scale)` — the [[CPrimitiveType|byte widths of primitive C types]].

## Connections

- [[DiveIntoSystems]] — book; **63rd ingested chapter**, **first ISA-specific section** of Part III after the [[dis-6-asm-intro|Ch 6]] hub.
- [[SuzanneJMatthews]] / [[TiaNewhall]] / [[KevinCWebb]] — authors.
- [[dis-6-asm-intro]] — direct predecessor; Ch 7 opens the [[X86_64|x86-64]] dialect Ch 6 forecast.
- [[dis-2-9-7-c-to-assembly|Ch 2.9.7]] — first appearance of [[AssemblyLanguage|assembly]] in the corpus (via [[IA32]] and `gcc -S`); Ch 7.1 generalizes that experience to 64-bit and to the full operand-syntax surface.
- [[dis-3-5-gdb-assembly|Ch 3.5]] — the [[GDB]] register names (`%rax`, `%rbx`, `%rip`, `%eflags`) Ch 7.1 now defines architecturally.
- [[X86_64]] — promoted from forward-reference stub to **first-class [[ISA]] page**.
- [[GeneralPurposeRegister]] — new concept: the 16 GPRs (`%rax`–`%r15`) and their subregister names.
- [[AtAndTSyntax]] — new concept: AT&T assembly syntax conventions (`%` / `$` prefixes, `mov src, dst` order, `disp(base, index, scale)` memory form).
- [[IntelSyntax]] — new concept: contrasting Intel syntax (`mov dst, src`, no prefixes, `[base + index*scale + disp]`).
- [[OperandSize]] — new concept: the `b` / `w` / `l` / `s` / `q` / `d` suffix table.
- [[X86AddressingMode]] — new concept: the six memory-operand forms.
- [[Operand]] — new concept: the three operand types (constant / register / memory).
- [[CpuRegister]] — Ch 7.1 supplies the canonical *"word-sized storage unit on the CPU"* definition the wiki already used.
- [[InstructionPointer]] — `%rip` named here as the read-only program counter.
- [[IA32]] — the 32-bit predecessor whose registers (`%eax`, `%ebp`, `%esp`, `%eip`) Ch 7.1 retroactively explains as **sub-registers** of the x86-64 64-bit registers.
- [[ARM]] / [[RISCV]] — sibling ISAs Ch 8 and Ch 9 will cover; same operand-structure framing, different register set and syntax.
- [[ISA]] — the architecture-software contract; Ch 7.1 instantiates it concretely for x86-64.

## Contradictions

None. Ch 7.1's framings are consistent with the wiki's existing [[CpuRegister]], [[AssemblyLanguage]], [[ISA]], and [[InstructionPointer]] coverage — it **supplies the canonical x86-64 register set and operand syntax** that prior pages referenced abstractly.
