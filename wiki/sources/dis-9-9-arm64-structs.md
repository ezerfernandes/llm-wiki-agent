---
title: "Dive into Systems — Ch 9.9 Structs in Assembly (ARM64)"
type: source
tags: [book, dive-into-systems, arm64, armv8, assembly, structs, alignment]
date: 2026-05-17
source_file: https://diveintosystems.org/book/C9-ARM64/structs.html
sources: []
last_updated: 2026-05-17
---

## Summary

**Ninth leaf** of Ch 9 *64-bit ARM Assembly* of *[[DiveIntoSystems]]* — **non-twin structural sibling** of [[dis-7-9-x86-64-structs|Ch 7.9]] / [[dis-8-9-ia32-structs|Ch 8.9]]. Compiles the [[CLanguage|C]] [[CStruct|struct]] aggregate at the [[ARM64|AArch64]] [[AssemblyLanguage|assembly]] surface: fields stored **contiguously in declaration order**; each [[StructMember|member]] has a fixed compile-time offset and is accessed via the **second [[ARM64AddressingMode|addressing-mode form]]** `[xN, #imm]` (base + signed immediate offset — `str w1, [x0, #64]` writes a 4-byte field 64 bytes past struct base). **Same [[AlignmentRule|alignment]] / [[StructPadding|padding]] policy as [[X86_64|x86-64]]** (full 8-byte alignment for 8-byte types — unlike [[IA32]]'s 4-byte cap from [[dis-8-9-ia32-structs|Ch 8.9]]). Floating-point fields use `sN` / `dN` registers — preview of the [[ARM64]] SIMD/FP register file. **No new concept pages** — reuses [[StructLayout]] / [[StructPadding]] / [[AlignmentRule]] / [[CStruct]] / [[MemoryAlignment]] / [[ARM64AddressingMode]].

## Key Claims

- **Contiguous declaration-order layout.** *"Each field is stored contiguously next to one another in memory in the order in which they are declared"* — same source-level rule as [[dis-7-9-x86-64-structs|Ch 7.9]] / [[dis-8-9-ia32-structs|Ch 8.9]]. Struct base address + per-field compile-time offset = field address. Layout is **declaration-order-dependent** — reordering fields changes the total `sizeof(struct)` via [[StructPadding|padding]] consequences.
- **Displacement addressing — `[xN, #imm]`.** Assembly code accesses struct fields using the [[ARM64AddressingMode|base + immediate-offset]] form, where the offset matches the field's byte position within the struct. Example: `str w1, [x0, #64]` writes a 4-byte `int` field at offset 64 from the struct base `x0`. Same role as [[X86_64|x86]]'s `mov %edx, 0x44(%rax)`.
- **8-byte alignment rule (full 64-bit policy).** *"4-byte types must align to multiples of 4, while 8-byte types must align to multiples of 8"* — same [[AlignmentRule|alignment policy]] as [[X86_64|x86-64]] [[dis-7-9-x86-64-structs|Ch 7.9]] (unlike [[IA32]]'s 4-byte cap from [[dis-8-9-ia32-structs|Ch 8.9]]). Pointers and `long` / `double` get 8-byte alignment — a structural consequence of [[ARM64]]'s 64-bit-native register file.
- **Compiler-inserted padding.** *"The compiler adds empty bytes as 'padding' between fields to ensure that each field satisfies its alignment requirements"* — padding bytes are inserted automatically between fields to satisfy alignment, even though they don't correspond to declared fields. Field reordering can minimize waste — same optimization opportunity as [[dis-7-9-x86-64-structs|Ch 7.9]].
- **Field offsets depend on cumulative size + padding.** The offset to each field is **not** merely a sum of declared sizes — it's the cumulative size of previous fields **plus any alignment padding** inserted between them. Observable via [[SizeOf|`sizeof`]] and the assembly-level displacement constants.
- **Register selection by data type.** Assembly instructions use different registers based on field type: `w` registers for 32-bit integers (`int`, `unsigned`), `x` registers for 64-bit pointers / `long`, **`s` registers for `float`** and **`d` registers for `double`** (the [[ARM64]] SIMD/FP register file, **separate** from the [[AArch64Registers|`x0`–`x30` GPR file]] — preview of vector instructions covered in later material).

## Key Quotes

> "Each field is stored contiguously next to one another in memory in the order in which they are declared." — the [[StructLayout]] invariant at the [[CLanguage|C]] / [[ARM64]] surface.

> "The compiler adds empty bytes as 'padding' between fields to ensure that each field satisfies its alignment requirements." — the [[StructPadding|padding-insertion]] mechanism that makes struct size declaration-order-dependent.

## Connections

- [[DiveIntoSystems]] — parent textbook; this is the **102nd ingested chapter** / **ninth leaf of Ch 9**.
- [[dis-9-8-arm64-matrices]] — immediate predecessor; closed aggregate-array access. Ch 9.9 pivots to the aggregate-record case.
- [[dis-9-1-arm64-basics]] — supplied the second [[ARM64AddressingMode|addressing-mode form]] `[xN, #imm]` (base + immediate) that struct field access uses.
- [[dis-7-9-x86-64-structs]] / [[dis-8-9-ia32-structs]] — structural siblings; same contiguous-declaration-order layout. **Headline alignment delta**: [[ARM64]] matches [[X86_64|x86-64]]'s 8-byte alignment for 8-byte types (unlike [[IA32]]'s 4-byte cap).
- [[StructLayout]] / [[StructPadding]] / [[AlignmentRule]] / [[CStruct]] / [[MemoryAlignment]] / [[StructMember]] — reused concept pages.
- [[dis-1-6-structs]] / [[dis-2-7-structs]] — original [[CLanguage|C]]-level struct introduction; Ch 9.9 operationalizes the *"compiler may insert alignment padding"* caveat at the [[ARM64]] assembly surface.

## Contradictions

None. Ch 9.9 **operationalizes** [[CStruct]] at the [[ARM64]] surface using existing concept machinery. The full 8-byte alignment for 8-byte types matches [[X86_64|x86-64]] — no contradiction with the [[IA32]]-specific 4-byte cap.
