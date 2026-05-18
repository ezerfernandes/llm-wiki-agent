---
title: "Dive into Systems — Ch 8.9 Structs in Assembly (IA32)"
type: source
tags: [dive-into-systems, ia32, assembly, struct, alignment, padding, 32-bit]
date: 2026-05-17
source_file: https://diveintosystems.org/book/C8-IA32/structs.html
sources: []
last_updated: 2026-05-17
---

## Summary

Chapter 8.9 of *[[DiveIntoSystems]]* — **ninth leaf** of Ch 8 *32-bit IA32 Assembly* and the **32-bit structural twin** of [[dis-7-9-x86-64-structs|Ch 7.9]]. Shows how the [[CLanguage|C]] [[CStruct|struct]] composite type compiles at [[IA32]] width: fields stored **contiguously in declaration order**, accessed via **fixed byte-offsets** added to the struct's base address (e.g., `s->age` at offset 64, `s->grad_yr` at offset 68). **Headline 32-vs-64 deltas** from [[dis-7-9-x86-64-structs|Ch 7.9]]: (1) IA32's [[AlignmentRule|alignment policy]] caps at **4-byte** boundaries — *"two-byte data types reside at a two-byte-aligned address whereas four-byte data types reside at four-byte-aligned addresses"* — vs Ch 7.9's 8-byte alignment for `double` / `long long` / pointer; (2) [[StructPadding|padding]] is therefore typically smaller — a `struct { char c; int x; }` wastes 3 bytes in both ISAs, but `struct { int x; double d; }` wastes 0 bytes on IA32 (`double` fits at offset 4 with no padding since IA32 caps alignment at 4) vs 4 bytes on x86-64 (where `double` must align to 8); (3) pointer fields are 4 bytes wide and 4-byte-aligned (vs 8/8 on x86-64); (4) base-pointer arithmetic uses 32-bit registers and the [[X86AddressingMode|`disp(base)` addressing mode]] for fixed-offset field access. **Headline rules carry over unchanged**: (a) fields lay out in declaration order; (b) compiler inserts padding to satisfy alignment; (c) **field reordering minimizes padding** — moving large/aligned fields first (or to the end) groups together to reduce inter-field padding; (d) the struct's overall size is rounded up to the largest field's alignment so adjacent struct elements in an array stay properly aligned. **88th ingested DIS chapter — ninth leaf of Ch 8.** **No new concept pages** — reuses [[StructLayout]], [[StructPadding]], [[AlignmentRule]], [[CStruct]] from [[dis-7-9-x86-64-structs|Ch 7.9]].

## Key Claims

- **Contiguous declaration-order storage.** *"The fields are stored contiguously next to one another in memory in the order in which they are declared"* — same invariant as Ch 7.9, independent of register width.
- **Field access via fixed byte offsets from struct base.** The compiler computes `&s->field = s + offsetof(field)` at compile time and emits `disp(base_reg)` operands — e.g., `mov 0x40(%eax), %edx` to load the `age` field at offset 64. No runtime computation needed (the [[ScaledIndexAddressing|scaled-index]] machinery is only needed for variable-indexed arrays, not fixed-offset struct fields).
- **IA32 [[AlignmentRule|alignment policy]] caps at 4 bytes.** *"IA32's alignment policy requires that two-byte data types reside at a two-byte-aligned address whereas four-byte data types reside at four-byte-aligned addresses"* — `char` at any byte, `short` at 2-aligned, `int` / `float` / pointer / `long` at 4-aligned. **No 8-byte alignment requirement** even for `double` or `long long` (vs Ch 7.9's 8-byte alignment for these types on x86-64).
- **[[StructPadding|Compiler-inserted padding]] satisfies alignment.** Between a `char` field and a following `int` field, the compiler inserts up to 3 padding bytes to push the `int` to a 4-aligned offset. The padding bytes don't correspond to declared fields — they exist solely to satisfy the [[AlignmentRule|alignment requirement]].
- **Field reordering minimizes wasted space.** *"Moving large fields to the struct's end can minimize padding waste by grouping aligned fields together"* — declaration order affects sizeof(struct), so layout-aware field ordering is a legitimate space-optimization knob.

## Key Quotes

> "The fields are stored contiguously next to one another in memory in the order in which they are declared." — the contiguity invariant.

> "IA32's alignment policy requires that two-byte data types reside at a two-byte-aligned address whereas four-byte data types reside at four-byte-aligned addresses." — the IA32-specific 4-byte alignment cap (vs x86-64's 8-byte cap).

## Connections

- [[DiveIntoSystems]] — book; **88th ingested chapter**, ninth leaf of Ch 8 *32-bit IA32 Assembly*.
- [[SuzanneJMatthews]] / [[TiaNewhall]] / [[KevinCWebb]] — co-authors.
- [[dis-7-9-x86-64-structs]] — **structural twin** at [[X86_64|x86-64]] width; identical declaration-order + padding + offsetof semantics, only the alignment cap differs (4 bytes here vs 8 bytes on x86-64 for `double`/`long long`/pointer).
- [[dis-8-8-ia32-matrices]] — Ch 8.8; direct predecessor.
- [[CStruct]] — the [[CLanguage|C]] composite type compiled.
- [[StructLayout]] — the declaration-order + offset rules.
- [[StructPadding]] — the alignment-driven inter-field gaps.
- [[AlignmentRule]] — the IA32 4-byte cap (vs x86-64 8-byte cap).
- [[X86AddressingMode]] — `disp(base)` for fixed-offset field access.
- [[CdeclCallingConvention]] — struct-pointer parameter at `0x8(%ebp)`.
- [[IA32]] — the 32-bit ISA.

## Contradictions

None. Ch 8.9 is a **consistent 32-bit re-presentation** of [[dis-7-9-x86-64-structs|Ch 7.9]] — the contiguity-plus-padding-plus-offset-access discipline is structurally identical; the alignment cap narrows from 8 bytes to 4 bytes, which **reduces** typical struct padding on IA32 compared to x86-64 (a rare case where IA32 is the more space-efficient ISA at the per-struct level).
