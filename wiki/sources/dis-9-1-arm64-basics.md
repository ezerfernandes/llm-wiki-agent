---
title: "Dive into Systems — Ch 9.1 ARMv8 Assembly Basics"
type: source
tags: [assembly, arm64, arm, aarch64, armv8, isa, risc, load-store, dive-into-systems]
date: 2026-05-17
source_file: https://diveintosystems.org/book/C9-ARM64/basics.html
---

## Summary

Chapter 9.1 *ARMv8 Assembly Basics* is the **first leaf of Ch 9 *64-bit ARM Assembly*** of *[[DiveIntoSystems]]* and the **third-ISA structural sibling** of [[dis-7-1-x86-64-basics|Ch 7.1]] (x86-64) and [[dis-8-1-ia32-basics|Ch 8.1]] (IA32). Unlike Ch 7 → Ch 8, Ch 9 is **not** a structural twin — [[ARM64]] is a **distinct [[RISC]] [[ISA]]**, not an x86 dialect, and the chapter introduces a meaningfully different instruction model: a **[[LoadStoreArchitecture|load/store architecture]]** (memory cannot be operated on directly — data must be moved into registers first), **31 general-purpose 64-bit registers** (`x0`–`x30`) with `w0`–`w30` 32-bit component aliases, dedicated [[StackPointer|`sp`]] / `pc` / `zr` special registers, **destination-first operand order** without [[AtAndTSyntax|AT&T `%`/`#` decoration]] or [[OperandSize|suffix-on-mnemonic]] sizing, and an [[ARM64AddressingMode|addressing-mode family]] (`[xN]` / `[xN, #imm]` / `[xN, xM]` / `[xN, xM, LSL, #s]`) that resembles [[X86AddressingMode|x86-64's]] `disp(base, index, scale)` but uses **bracketed Intel-style syntax** and **explicit shift mnemonic** rather than a numeric scale field. The same `adder2(int a)` worked example from Ch 7.1 / Ch 8.1 returns as the canonical introduction, this time compiled with `aarch64-linux-gnu-gcc` against the [[ARMv8]] ISA — but the resulting three-instruction `adder2` (load → add → store) reveals the load/store discipline.

## Key Claims

- **[[ARM64]] is a distinct [[RISC]] [[ISA]], not a CISC dialect.** Ch 9 is **not** a structural mirror of Ch 7 / Ch 8 — at the **instruction-model level** [[ARM64|ARMv8-A AArch64]] differs from [[X86_64|x86-64]] in load/store discipline, fixed-width 4-byte instruction encoding, larger register file (31 GPRs vs 16), and explicit-shift addressing-mode form.
- **31 general-purpose 64-bit registers (`x0`–`x30`).** Each can hold integer data or a memory address. The compiler chooses register width based on data type — 64-bit `xN` for `long` / pointer, 32-bit `wN` for `int`.
- **Component registers `w0`–`w30` are the low-32-bit aliases.** *"If 32-bit data is stored in component register `w0`, then the upper 32 bits of the register become inaccessible, and are zeroed out."* No `bN` / `hN` further-sub-register hierarchy exists at this chapter's surface — there are only two register widths visible to the programmer.
- **Three architectural special-purpose registers.** [[StackPointer|`sp`]] (stack pointer — top of program stack), `pc` (program counter — next instruction; read-only at the user-mode surface), `zr` (zero register — permanently 0; reading produces 0, writes are discarded).
- **[[LoadStoreArchitecture|Load/store architecture]] — memory operands are confined to load (`ldr`) and store (`str`) instructions.** *"Data cannot be read or written to memory directly; instead, ARM follows a load/store model, which requires data to be operated on in registers."* Arithmetic / logic / shift instructions take **register-or-immediate operands only** — there is no [[X86AddressingMode|x86-64-style]] arbitrary memory operand on `add` / `sub` / `and` / etc.
- **Instruction format: `opcode D, O1, O2` — destination first.** Mirrors [[IntelSyntax|Intel syntax]] order (destination, then sources) rather than [[AtAndTSyntax|AT&T order]] (sources, then destination). No `%` / `$` / suffix decoration — operands are bare register names (`x0` / `w0` / `sp`), immediate constants prefixed with `#` (`#0x2`), or memory forms in brackets (`[sp, #12]`).
- **[[ARM64AddressingMode|Four addressing-mode forms]] for memory operands** (all inside square brackets) — `[xN]` (plain dereference), `[xN, #imm]` (base + signed immediate offset), `[xN, xM]` (base + register index), `[xN, xM, LSL, #s]` (base + register index shifted left by `s` bits). The fourth form is [[ARM64|ARM64]]'s analog of [[ScaledIndexAddressing|x86-64 scaled-index addressing]] — but with an **explicit shift mnemonic** (`LSL`) and **shift amount as a bit count** rather than a `{1,2,4,8}` scale factor.
- **Worked example `adder2(int a) { return a + 2; }`** compiles to three instructions (unoptimized): store `w0` (the parameter `a`) into the stack at `[sp, #12]`, load it back into `w0`, then `add w0, w0, #0x2`. The detour through memory in the unoptimized output operationalizes the load/store rule — *"three instructions required to perform what is a single C operation"* — and motivates compiler optimization.
- **The single arithmetic operation `add w0, w0, #0x2`** demonstrates the canonical three-operand `opcode D, O1, O2` form: destination `w0`, source-1 `w0`, source-2 immediate `#0x2`. This is the **structural opposite** of [[X86_64|x86-64]]'s `add $0x2, %eax` form (AT&T 2-operand, source-then-destination) and operationally distinct from [[IA32|IA32]]'s identical encoding.

## Key Quotes

> "Data cannot be read or written to memory directly; instead, ARM follows a load/store model, which requires data to be operated on in registers." — the **defining ISA-philosophy claim** that separates [[ARM64]] from [[X86_64]] / [[IA32]] at the instruction-model level.

> "If 32-bit data is stored in component register `w0`, then the upper 32 bits of the register become inaccessible, and are zeroed out." — the AArch64 narrowing rule, structurally analogous to the [[X86_64|x86-64]] *write-to-32-bit-zeros-upper-32* convention.

> "ARMv8 provides 31 general-purpose 64-bit registers, named `x0`–`x30`, for storing data." — the register-count headline. **31** is the visible count (not 32) because the slot a 32nd register would occupy is taken by the `zr` zero register at the encoding level.

> "The destination is always a register" — the load/store rule restated at the **non-memory-instruction** surface. Even `ldr` / `str` follow the rule: the destination of `ldr` is a register; the source of `str` is a register. Memory is **never** the destination of computation.

## Connections

- [[DiveIntoSystems]] — the host textbook; this is its **91st ingested chapter** and the **opening leaf of Ch 9 *64-bit ARM Assembly*** — the third and final assembly chapter, after Ch 7 *[[X86_64|x86-64]]* (76 chapters, fully ingested) and Ch 8 *[[IA32]]* (90 chapters, fully ingested).
- [[dis-6-asm-intro]] — the Part III hub that forecast Ch 9; this ingest **resolves** the [[ARM|ARMv8-A]] forward reference at the Ch-9-content surface.
- [[dis-7-1-x86-64-basics]] — **non-twin structural sibling** at the same per-ISA-opening position. Same `adder2` worked example, **structurally distinct** ISA underneath (load/store vs read-modify-write memory operands; 31 GPRs vs 16; destination-first vs source-first; explicit-shift addressing-mode vs scale-factor addressing-mode).
- [[dis-8-1-ia32-basics]] — **non-twin structural sibling** at the same per-ISA-opening position. Same `adder2` worked example, **structurally distinct** ISA underneath (load/store vs read-modify-write; 31 GPRs vs 8; `xN`/`wN` vs `%eXX` letter-substitution subregister scheme).
- [[ARM64]] — **promoted/minted** by this ingest from forward reference to first-class concept page; covers the AArch64 register file + subregister rule + special registers + instruction format at the Ch 9.1 surface.
- [[AArch64Registers]] — **minted** by this ingest; the register-set page (`x0`–`x30`, `w0`–`w30`, `sp`, `pc`, `zr`) and the 64/32-bit narrowing rule.
- [[LoadStoreArchitecture]] — **minted** by this ingest; the ISA-philosophy page distinguishing [[ARM64]] / [[RISCV]] / [[MIPS]] from [[X86_64|x86-64]] / [[IA32]] at the memory-operand-policy level.
- [[ARM64AddressingMode]] — **minted** by this ingest; the four-form table (`[xN]` / `[xN, #imm]` / `[xN, xM]` / `[xN, xM, LSL, #s]`) and the contrast with [[X86AddressingMode|`disp(base, index, scale)`]].
- [[RISC]] — the [[ISA]] family [[ARM64]] belongs to; Ch 9.1 is the wiki's **first detailed in-corpus RISC ISA page** at the user-mode-programmer surface (existing [[ARMCortexM]] is microcontroller-scope, not desktop/server scope).
- [[GeneralPurposeRegister]] — the umbrella concept; this ingest contributes the 31-GPR row to the cross-ISA count comparison.
- [[Operand]] — the same three-type taxonomy applies; ARM64 differs in **which operand types each instruction class accepts** (load/store rule).
- [[IntelSyntax]] — ARM64 syntax is **destination-first** like Intel, but it is not "Intel syntax" — it is its own ARM-defined notation. Operand decoration differs (no `dword ptr [...]` operand-size prefix; no `%`).
- [[AtAndTSyntax]] — the **contrasting** syntax used by [[X86_64]] / [[IA32]] in this book. ARM64 uses **none** of AT&T's `%` register prefix, `$` immediate prefix, or `b`/`w`/`l`/`q` size suffix.
- [[AssemblyLanguage]] — the umbrella concept; ARM64 expands the corpus's [[ISA]]-coverage from CISC-only to CISC + RISC.
- [[CLanguage]] — the source language whose compilation Ch 9.1 traces (`adder2(int a)`).

## Contradictions

None. Ch 9.1 introduces a **structurally distinct [[ISA]]** rather than revising prior claims — it expands the wiki's coverage from x86-family CISC to ARM64 RISC without conflicting with [[dis-7-1-x86-64-basics|Ch 7.1]] or [[dis-8-1-ia32-basics|Ch 8.1]]. The **load/store rule** at first glance appears to contradict the freedom of [[X86AddressingMode|x86-64 memory operands]] on `mov` / `add` / etc. — but Ch 9.1 frames this as an **ISA-design choice** (RISC vs CISC), not an error in the x86 presentation. The two are alternative answers to the *where can memory operands appear?* question, both fully described in the wiki.
