---
title: "Dive into Systems — Ch 7.9 Structs in Assembly (x86-64)"
type: source
tags: [dive-into-systems, x86-64, assembly, structs, memory-layout, alignment, padding]
date: 2026-05-17
source_file: https://diveintosystems.org/book/C7-x86_64/structs.html
---

## Summary

**Ninth leaf** of Ch 7 *x86-64 Assembly* of [[DiveIntoSystems]]. Shows how the [[CLanguage|C]] [[CStruct|struct]] aggregate type compiles to [[X86_64|x86-64]] [[AssemblyLanguage|assembly]] — fields are stored contiguously in declaration order, accessed via fixed `disp(%base)` offsets from the struct's base address, and the compiler may insert **padding bytes** between fields to satisfy the x86-64 **alignment policy** that requires each data type to reside at an address that is a multiple of its size. The chapter operationalizes the [[StructLayout|struct-layout]] / [[StructPadding|padding]] / [[AlignmentRule|alignment-rule]] machinery that [[dis-1-6-structs|Ch 1.6]] and [[dis-2-7-structs|Ch 2.7]] previewed at the source level.

## Key Claims

- **Contiguous declaration-order layout.** Fields of a `struct` are stored contiguously in memory in the order declared. For `struct studentT { char name[64]; int age; int grad_yr; float gpa; }`, the layout is `name` at offset `0x0` (64 bytes), `age` at `0x40` (4 bytes), `grad_yr` at `0x44` (4 bytes), `gpa` at `0x48` (4 bytes).
- **Offset-based field access.** Assembly accesses a [[StructMember|struct member]] via a constant displacement off the struct's base register: `mov %edx, 0x44(%rax)` writes `grad_yr` 68 bytes past the struct base in `%rax`. The compiler precomputes every field's offset at translation time.
- **x86-64 alignment policy.** *"x64's alignment policy requires that two-byte data types (i.e., `short`) reside at a two-byte-aligned address, four-byte data types (i.e., `int`, `float`, and `unsigned`) reside at four-byte-aligned addresses, and larger data types (`long`, `double`, and pointer data) reside at eight-byte-aligned addresses."* — each primitive type must sit at an address that is a multiple of its size.
- **Compiler-inserted padding.** *"The compiler adds empty bytes as **padding** between fields to ensure that each field satisfies its alignment requirements."* If `char name[63]` (63 bytes) were declared instead of `char name[64]`, the compiler would insert **one padding byte** before the next `int` field so `age` lands on a 4-byte boundary.
- **Field reordering changes struct size.** Because padding depends on field order, swapping the declaration order of differently-sized fields can change the total `sizeof(struct ...)` — a [[CCompiler|compiler]]-observable consequence of the source-level field order that [[dis-1-6-structs|Ch 1.6]] flagged as *"the compiler may insert alignment padding making the actual value larger"*.

## Key Quotes

> *"x64's alignment policy requires that two-byte data types (i.e., `short`) reside at a two-byte-aligned address, four-byte data types (i.e., `int`, `float`, and `unsigned`) reside at four-byte-aligned addresses, and larger data types (`long`, `double`, and pointer data) reside at eight-byte-aligned addresses."* — the [[AlignmentRule|alignment rule]] formalized.

> *"The compiler adds empty bytes as **padding** between fields to ensure that each field satisfies its alignment requirements."* — the [[StructPadding|padding]] mechanism that makes [[StructLayout|struct layout]] non-trivially dependent on field order.

> Assembly example: `mov %edx, 0x44(%rax)` — stores `grad_yr` (an `int`) at displacement `0x44` (68 bytes) from the struct base address in `%rax`. The displacement is the field's compile-time offset, not a runtime computation.

## Connections

- [[DiveIntoSystems]] — host book; **74th ingested chapter**, ninth leaf of Ch 7 *x86-64 Assembly*.
- [[X86_64]] — the ISA whose alignment policy this chapter codifies.
- [[AssemblyLanguage]] — the surface at which struct access manifests as `disp(%base)`.
- [[CStruct]] — the source-level [[CLanguage|C]] aggregate whose compilation this chapter explains; previously introduced at [[dis-1-6-structs|Ch 1.6]] and extended at [[dis-2-7-structs|Ch 2.7]].
- [[StructMember]] — accessed via fixed compile-time offset from the struct base.
- [[StructLayout]] — *new*: the contiguous-declaration-order arrangement of fields in memory.
- [[StructPadding]] — *new*: compiler-inserted empty bytes between fields to satisfy alignment.
- [[AlignmentRule]] — *new*: the size-equals-alignment policy for x86-64 primitive types.
- [[MemoryAlignment]] — *new*: the general principle that data items reside at addresses that are multiples of their size.
- [[X86MovInstruction]] — the `mov` instruction used for offset-based field access (`mov %edx, 0x44(%rax)`).
- [[X86AddressingMode]] — the `disp(base)` addressing mode that encodes the field offset.
- [[SizeOf]] — `sizeof(struct ...)` reports the padded total, not the sum-of-field-sizes.
- [[CCompiler]] — inserts padding and computes offsets at compile time.
- [[dis-1-6-structs]] — first introduction of structs at the C-source level.
- [[dis-2-7-structs]] — extends structs with pointer-to-struct and dynamic allocation.
- [[dis-7-1-x86-64-basics]] — supplies the `disp(base)` addressing-mode vocabulary.
- [[dis-7-7-x86-64-arrays]] — the sibling 1-D-array compilation pattern; structs use **fixed compile-time offsets**, arrays use **runtime scaled-index addressing**.

## Contradictions

- None. Ch 7.9 **operationalizes** the source-level struct semantics from [[dis-1-6-structs|Ch 1.6]] and [[dis-2-7-structs|Ch 2.7]] at the assembly surface — concretizes the *"the compiler may insert alignment padding"* caveat into a specific size-equals-alignment rule for x86-64. Adds mechanism rather than revising claims.
