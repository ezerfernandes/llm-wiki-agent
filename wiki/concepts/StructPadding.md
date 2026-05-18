---
title: "Struct Padding"
type: concept
tags: [memory-layout, struct, alignment, compiler, c-language]
sources: [dis-7-9-x86-64-structs]
last_updated: 2026-05-17
---

# Struct Padding

**Struct padding** is the [[CCompiler|compiler]]-inserted empty bytes between (or after) [[StructMember|struct fields]] that exist solely to satisfy the [[AlignmentRule|alignment rule]] — *"the compiler adds empty bytes as padding between fields to ensure that each field satisfies its alignment requirements"* ([[dis-7-9-x86-64-structs|Ch 7.9]]). Padding bytes carry no semantic value; their only purpose is to push the next field to an address that is a multiple of its size.

## Concrete example ([[dis-7-9-x86-64-structs|Ch 7.9]])

```c
struct A {
    char  name[63];  // 63 bytes,  offset 0x00
    // 1 padding byte at offset 0x3F
    int   age;       // 4 bytes,   offset 0x40 (4-byte aligned)
};
```

Without the padding byte, `age` would sit at offset `0x3F` — not a multiple of 4, violating the [[X86_64|x86-64]] [[AlignmentRule|alignment rule]] for `int`. With the byte inserted, `age` lands on `0x40` (a 4-byte boundary) and the [[X86MovInstruction|`mov`]] access becomes legal and efficient.

## Why padding exists

The CPU loads data in fixed-size aligned chunks (typically 4 or 8 bytes per memory operation). Misaligned access either (a) costs extra cycles because two aligned loads must be fused, or (b) on stricter ISAs ([[ARM]]) raises a [[SIGBUS|bus error]]. Padding makes every field-access [[X86MovInstruction|`mov`]] a single aligned memory transaction.

## Observable consequences

- [[SizeOf|`sizeof(struct ...)`]] returns the **padded** total, not the sum-of-field-sizes — see [[dis-1-6-structs|Ch 1.6]]'s caveat *"the compiler may insert alignment padding making the actual value larger"*.
- **Field-order rewriting changes struct size.** Largest-fields-first ordering minimizes padding; this is a standard C-systems optimization.
- **Trailing padding** is also inserted at the end of a struct so that the next element in an [[CArray|array of structs]] also starts on the maximum-alignment boundary required by any field.

## Connections

- [[StructLayout]] — the contiguous-declaration-order arrangement that padding fills in.
- [[AlignmentRule]] — the policy that determines where padding is needed.
- [[MemoryAlignment]] — the general hardware principle.
- [[CStruct]] / [[StructMember]] — the source-level aggregates this affects.
- [[SizeOf]] — the operator that reveals the padded total.
- [[CCompiler]] — the agent that inserts the bytes.
- [[X86_64]] — the ISA whose alignment policy drives the rule on this platform.
- [[dis-7-9-x86-64-structs]] — chapter of origin.
- [[dis-1-6-structs]] — source-level previewing of the *"compiler may insert alignment padding"* caveat.
