---
title: "Struct Layout"
type: concept
tags: [memory-layout, struct, c-language, x86-64, compiler]
sources: [dis-7-9-x86-64-structs]
last_updated: 2026-05-17
---

# Struct Layout

The **struct layout** is the arrangement of a [[CStruct|C struct]]'s [[StructMember|fields]] in memory: fields are stored **contiguously** and **in declaration order**, with the [[CCompiler|compiler]] free to insert [[StructPadding|padding bytes]] between (and after) fields to satisfy the platform's [[AlignmentRule|alignment rule]]. Each field has a fixed compile-time **offset** from the struct's base address, which the compiler uses to emit `disp(%base)` [[X86AddressingMode|addressing-mode]] accesses in [[X86_64|x86-64]] [[AssemblyLanguage|assembly]].

## Canonical example ([[dis-7-9-x86-64-structs|Ch 7.9]])

```c
struct studentT {
    char name[64];   // offset 0x00,  64 bytes
    int  age;        // offset 0x40,   4 bytes
    int  grad_yr;    // offset 0x44,   4 bytes
    float gpa;       // offset 0x48,   4 bytes
};
```

Assembly access pattern (struct base in `%rax`):

```asm
mov %edx, 0x44(%rax)   ; studentT.grad_yr = edx
```

The `0x44` displacement is the compile-time offset of `grad_yr`; no runtime offset computation is needed (contrast with [[AsmArrayAccess|array access]] which uses [[ScaledIndexAddressing|scaled-index addressing]] for runtime indices).

## Why declaration order matters

Because the compiler inserts [[StructPadding|padding]] to satisfy [[AlignmentRule|alignment]], the **size** of a struct depends on field order. Replacing `char name[64]` with `char name[63]` forces the compiler to insert **one padding byte** before `age` so the `int` lands on a 4-byte boundary. Reordering fields from largest-to-smallest typically minimizes total padding — a well-known C optimization that the [[StructLayout|struct-layout]] rule makes observable via [[SizeOf|`sizeof`]].

## Connections

- [[CStruct]] — the C-source aggregate whose layout this concept describes.
- [[StructMember]] — the individual field accessed via fixed offset.
- [[StructPadding]] — the empty bytes the compiler inserts to satisfy alignment.
- [[AlignmentRule]] — the policy that drives where padding goes.
- [[MemoryAlignment]] — the general principle behind the rule.
- [[X86_64]] / [[AssemblyLanguage]] / [[X86MovInstruction]] / [[X86AddressingMode]] — the surface at which the layout becomes observable.
- [[SizeOf]] — reveals the padded total size.
- [[dis-7-9-x86-64-structs]] — chapter of origin.
- [[dis-1-6-structs]] — source-level struct introduction.
