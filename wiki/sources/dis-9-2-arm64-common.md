---
title: "Dive into Systems — Ch 9.2 Common ARMv8 Instructions"
type: source
tags: [assembly, arm64, aarch64, armv8, isa, risc, load-store, ldr, str, mov, ldp, stp, dive-into-systems]
date: 2026-05-17
source_file: https://diveintosystems.org/book/C9-ARM64/common.html
---

## Summary

Chapter 9.2 *Common Instructions* is the **second leaf of Ch 9 *64-bit ARM Assembly*** of *[[DiveIntoSystems]]* and the **third-ISA structural sibling** of [[dis-7-2-x86-64-common|Ch 7.2]] (x86-64) and [[dis-8-2-ia32-common|Ch 8.2]] (IA32). It introduces the **data-movement primitives** of [[ARM64]]: [[ARM64DataMovement|`mov` (register-to-register)]], [[ARM64DataMovement|`ldr` (memory → register, *load*)]], and [[ARM64DataMovement|`str` (register → memory, *store*)]] — the **only three instructions** that touch memory per the [[LoadStoreArchitecture|load/store rule]] from [[dis-9-1-arm64-basics|Ch 9.1]] — plus the **pair extensions** `ldp` (load pair) and `stp` (store pair), each capable of moving **two consecutive 64-bit values** in one instruction, with **pre-indexed** (`[xN, #imm]!`) and **post-indexed** (`[xN], #imm`) addressing-mode forms that fold pointer-update into the load/store itself. The same `adder2` worked example from [[dis-9-1-arm64-basics|Ch 9.1]] returns, this time presented with full annotation of the [[ARM64AddressingMode|`[sp, #12]` stack-slot access]]. The headline structural delta from [[X86_64|x86-64]] / [[IA32]] is **two-fold**: (1) memory operands appear *only* on `ldr` / `str` / `ldp` / `stp` (never on `add` / `sub` / `and` / etc.), and (2) the **pair** instructions `ldp` / `stp` have no [[CISC]] analog — they are an [[ARM64]]-specific optimization for prologue / epilogue stack-frame setup and teardown.

## Key Claims

- **[[ARM64]] data movement is split into five instructions**: [[ARM64DataMovement|`mov D, S`]] (register-to-register or immediate-to-register; **no memory operand**), [[ARM64DataMovement|`ldr D, [addr]`]] (memory → register; **only direction memory may be a source for non-memory targets**), [[ARM64DataMovement|`str S, [addr]`]] (register → memory; **only direction memory may be a destination**), and the pair forms [[ARM64DataMovement|`ldp` / `stp`]] for two consecutive 64-bit registers.
- **`mov D, S` does *not* touch memory.** *"Copies value of S into D."* This is the structural opposite of [[X86MovInstruction|x86-64 `mov`]], which freely accepts a memory operand on either source or destination — on [[ARM64]] that case requires the dedicated [[ARM64DataMovement|`ldr`]] / [[ARM64DataMovement|`str`]] instructions.
- **`ldr D, [addr]` loads memory into a register.** *"Loads the value in memory into register D."* The bracketed `[addr]` operand uses one of the four [[ARM64AddressingMode|addressing-mode forms]] from [[dis-9-1-arm64-basics|Ch 9.1]] (`[xN]` / `[xN, #imm]` / `[xN, xM]` / `[xN, xM, LSL, #s]`). Destination width selects the load width — `ldr w0, [...]` is 4 bytes, `ldr x0, [...]` is 8 bytes.
- **`str S, [addr]` stores a register to memory.** *"Stores S into memory location *(addr)."* Note the **operand-order inversion** relative to [[X86_64|x86-64]]'s [[X86MovInstruction|`movq %rax, (%rbx)`]]: on [[ARM64]] the **register source comes first**, the **memory operand second**, in keeping with the destination-first / source-second pattern (here the destination is memory and is in second-operand position — the only [[ARM64]] instruction class where this happens at the surface, because `str` semantically swaps "destination" from the syntactic-second-operand to the **memory side**).
- **`ldp` and `stp` operate on register *pairs*.** [[ARM64DataMovement|`ldp D1, D2, [addr]`]] loads **two consecutive 64-bit values** from memory into `D1` and `D2`; [[ARM64DataMovement|`stp S1, S2, [addr]`]] stores **two consecutive 64-bit values** to memory. The implicit offset between the pair members is **8 bytes** (one 64-bit word). No [[X86_64|x86-64]] / [[IA32]] equivalent exists.
- **Three indexing variants on the bracketed operand**: plain `[xN, #imm]` (effective address = base + offset; **base unchanged**), pre-indexed `[xN, #imm]!` (effective address = base + offset; **base register updated to that address** *before* the access), post-indexed `[xN], #imm` (effective address = base alone; **base register updated** to base + offset *after* the access). The two indexed forms are used by compilers to fold the typical [[StackFrame|stack-frame]] prologue / epilogue `sp` adjustment into the same instruction that saves / restores [[CalleeSaved|callee-saved]] registers.
- **Typical prologue / epilogue idiom** uses the pair-plus-pre-index pattern: `stp x29, x30, [sp, #-16]!` saves the frame pointer + link register **and** advances `sp` by `-16` in one instruction; `ldp x29, x30, [sp], #16` reverses both at function return. This is **one instruction** doing what [[X86_64|x86-64]] would express as a `sub $16, %rsp` + two `mov` instructions (three instructions total) — a concrete instance of the [[RISC]] design philosophy of *more uniform instructions, fewer of them total* being **violated favorably** by these special-purpose composite ops, which exist precisely to lower the prologue/epilogue cost the [[LoadStoreArchitecture|load/store rule]] would otherwise impose.
- **`adder2` worked example revisited** with full annotation: `str w0, [sp, #12]` stores the parameter `a` at `sp + 12`, `ldr w0, [sp, #12]` reloads it, `add w0, w0, #0x2` adds the immediate constant 2. The unoptimized three-instruction expansion of `return a + 2` is the **load/store discipline made visible** — the parameter cannot stay in `w0` across the spill/reload because the unoptimized compiler does not keep live values in registers across statement boundaries.

## Key Quotes

> "Loads the value in memory into register D." — the canonical statement of the **load direction** at the heart of the [[LoadStoreArchitecture|load/store architecture]].

> "Stores S into memory location *(addr)." — the canonical statement of the **store direction**. Together with `ldr`, these are the *only* paths between register and memory.

> "Copies value of S into D." — `mov`'s definition makes explicit that **memory is not involved**. Distinct from [[X86MovInstruction|x86 `mov`]].

## Connections

- [[DiveIntoSystems]] — the host textbook; this is its **92nd ingested chapter** and the **second leaf of Ch 9 *64-bit ARM Assembly***.
- [[dis-9-1-arm64-basics]] — **prior sibling at Ch 9.1**; established the [[ARM64]] register file, operand-syntax conventions, and [[ARM64AddressingMode|four addressing-mode forms]] that Ch 9.2 operationalizes via concrete `ldr` / `str` examples.
- [[dis-7-2-x86-64-common]] — **non-twin structural sibling at the same per-ISA-leaf position**. Same five-instructions-treated approach, **structurally distinct** ISA underneath: x86-64's `mov` collapses what [[ARM64]] splits into `mov`/`ldr`/`str`; x86-64 has no `ldp`/`stp` pair extension.
- [[dis-8-2-ia32-common]] — **non-twin structural sibling at Ch 8.2** (IA32 32-bit). Same observations.
- [[ARM64DataMovement]] — **minted** by this ingest; the concept page covering `mov` / `ldr` / `str` / `ldp` / `stp` and the pre-/post-indexed addressing variants.
- [[ARM64]] — promoted concept; this ingest contributes the data-movement-instruction table.
- [[LoadStoreArchitecture]] — restated and operationalized; Ch 9.2 is where the load/store rule **manifests at the instruction surface** as three dedicated instructions.
- [[ARM64AddressingMode]] — extended; the **pre-indexed (`!`) and post-indexed forms** are introduced here as variants of the [[dis-9-1-arm64-basics|Ch 9.1]] base + offset addressing mode.
- [[StackFrame]] — the canonical use case for `stp ..., [sp, #-N]!` / `ldp ..., [sp], #N` pair-plus-indexed prologue / epilogue idiom.
- [[StackPointer]] — `sp` is the canonical base register inside the bracketed operand.
- [[X86MovInstruction]] — contrasting [[CISC]] instruction; collapses `mov` / `ldr` / `str` into one mnemonic with memory operands accepted on either side.
- [[X86StackInstructions]] — contrasting [[CISC]] stack-management story (`push` / `pop` macros over `sp`); [[ARM64]] uses `stp` / `ldp` plus indexed addressing instead.
- [[AssemblyLanguage]] — umbrella concept.

## Contradictions

None. Ch 9.2 **specifies** the [[LoadStoreArchitecture|load/store rule]] from [[dis-9-1-arm64-basics|Ch 9.1]] at the instruction surface — `mov` is **register-only**, `ldr` and `str` are **the only memory-touching instructions**, and the pair / indexed variants are [[ARM64]]-specific extensions with no [[CISC]] equivalent. Consistent with [[dis-9-1-arm64-basics|Ch 9.1]]'s ISA-philosophy framing.
