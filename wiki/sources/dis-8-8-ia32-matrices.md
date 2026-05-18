---
title: "Dive into Systems — Ch 8.8 Matrices in Assembly (IA32)"
type: source
tags: [dive-into-systems, ia32, assembly, matrices, multidim-array, row-major, 32-bit]
date: 2026-05-17
source_file: https://diveintosystems.org/book/C8-IA32/matrices.html
sources: []
last_updated: 2026-05-17
---

## Summary

Chapter 8.8 of *[[DiveIntoSystems]]* — **eighth leaf** of Ch 8 *32-bit IA32 Assembly* and the **32-bit structural twin** of [[dis-7-8-x86-64-matrices|Ch 7.8]]. Extends [[dis-8-7-ia32-arrays|Ch 8.7]]'s [[AsmArrayAccess|scaled-index]] [[CArray|array]] compilation to **2-D [[MultidimensionalArray|matrices]]**, exposing the same fundamental split as Ch 7.8: (a) **contiguous** matrices — statically declared `int M1[4][3]` or single-`malloc` `int *M2 = malloc(4*3*sizeof(int))` — store all elements in one flat block, indexed by `(i*cols + j) * 4` from the base pointer; (b) **non-contiguous** [[ArrayOfArrays|array-of-arrays]] — `int **M3` with per-row `malloc` — requires **two-stage dereferencing**: first load `M3[i]` row-pointer via `(M3, i, 4)`, then offset within that row via `(M3[i], j, 4)`. **Headline 32-vs-64 deltas**: (1) base pointer and row pointers are **4 bytes** (vs 8 bytes on Ch 7.8) — the second-stage dereference uses `(row_ptr, %ecx, 4)` because IA32 pointer width = 4 = `int` width = unified scale factor (a small simplification vs Ch 7.8 where pointers were 8 bytes and ints 4 bytes); (2) row-stride multiply uses `imul $0xc, %eax, %eax` (12 = 3·4) — the same byte stride as Ch 7.8 (cols × sizeof(int)), only the operands are 32-bit; (3) the array-base pointer comes from `0x8(%ebp)` per [[CdeclCallingConvention|cdecl]] — not from `%rdi` per [[SystemVCallingConvention|System V]]; (4) [[X86ShiftInstructions|`shl`]] / [[X86MulInstruction|`imul`]] / [[LeaInstruction|`leal`]] do the scaled-multiply. **Headline rules carry over unchanged**: (a) [[RowMajorOrder|row-major]] memory layout for contiguous matrices; (b) `M[i][j]` notation **only works** for `int M[ROWS][COLS]` and `int **M` (array-of-arrays) — *not* for single-`malloc` flat matrices where manual `M[i*cols+j]` indexing is mandatory; (c) the contiguous vs non-contiguous trade-off — one-`malloc` is memory-efficient and cache-friendly but loses bracket-notation; array-of-arrays gives bracket-notation back at the cost of pointer-table indirection and non-contiguous rows. **87th ingested DIS chapter — eighth leaf of Ch 8.** **No new concept pages** — reuses [[MultidimensionalArray]], [[RowMajorOrder]], [[ArrayOfArrays]], [[AsmArrayAccess]], [[ScaledIndexAddressing]] from [[dis-7-8-x86-64-matrices|Ch 7.8]].

## Key Claims

- **Statically declared matrices use [[RowMajorOrder|row-major]] contiguous layout.** All rows lay out sequentially in one memory block — `M1[0][0], M1[0][1], M1[0][2], M1[1][0], ...` — enabling efficient sequential access and a single offset computation `base + (i*cols + j) * sizeof(elem)`.
- **Element access requires index scaling by element size.** *"Element access requires multiplying the computed index by the data type size (4 bytes for integers) to calculate correct byte offsets"* — the same byte-addressability requirement as Ch 8.7, lifted to 2-D.
- **Contiguous vs non-contiguous trade-off.** Memory-efficient single-`malloc` matrices use one offset computation `(i*cols + j) * 4` but **lose `M[i][j]` bracket notation** — *"Element (i, j) cannot be accessed using the `M[i][j]` notation"*; programmer must hand-write `M[i*cols + j]`. [[ArrayOfArrays|Array-of-arrays]] (`int **M`) restores bracket-notation at the cost of non-contiguous rows and pointer-table indirection.
- **Non-contiguous matrices require two-stage dereferencing.** First offset `(matrix, i, 4)` loads the row pointer (4 bytes — IA32 pointer width); second offset `(row_ptr, j, 4)` loads the element. *"The individual arrays are not contiguous with one another"* — each row's memory location is independent (separately `malloc`'d).
- **Scaling instructions: [[X86ShiftInstructions|`shl`]] / [[X86MulInstruction|`imul`]] / [[LeaInstruction|`leal`]].** The compiler uses `shl $2` (left-shift by 2 = ×4) for power-of-2 strides, `imul $0xc, %eax` (×12) for the row stride of a 3-column int matrix, and `leal` to combine base+index+scale arithmetic in one instruction without dereferencing.

## Key Quotes

> "Element (i, j) cannot be accessed using the `M[i][j]` notation" — for memory-efficient single-`malloc` matrices; manual `M[i*cols + j]` scaled-indexing is mandatory.

> "The individual arrays are not contiguous with one another" — in [[ArrayOfArrays|array-of-arrays]] implementations, contrasting with the unified memory layout of static allocation.

## Connections

- [[DiveIntoSystems]] — book; **87th ingested chapter**, eighth leaf of Ch 8 *32-bit IA32 Assembly*.
- [[SuzanneJMatthews]] / [[TiaNewhall]] / [[KevinCWebb]] — co-authors.
- [[dis-7-8-x86-64-matrices]] — **structural twin** at [[X86_64|x86-64]] width.
- [[dis-8-7-ia32-arrays]] — Ch 8.7; direct predecessor (1-D array compilation Ch 8.8 extends to 2-D).
- [[MultidimensionalArray]] — the [[CLanguage|C]] construct Ch 8.8 compiles.
- [[RowMajorOrder]] — the contiguous-matrix memory layout.
- [[ArrayOfArrays]] — the non-contiguous `int **M` layout.
- [[AsmArrayAccess]] / [[ScaledIndexAddressing]] — the underlying compilation idiom from [[dis-8-7-ia32-arrays|Ch 8.7]], lifted to 2-D.
- [[LeaInstruction]] — `leal` for base+index+scale arithmetic.
- [[X86ShiftInstructions]] — `shl` strength-reduction for power-of-2 strides.
- [[X86MulInstruction]] — `imul` for non-power-of-2 row strides.
- [[CdeclCallingConvention]] — matrix base passed at `0x8(%ebp)`.
- [[IA32]] — the 32-bit ISA.

## Contradictions

None. Ch 8.8 is a **consistent 32-bit re-presentation** of [[dis-7-8-x86-64-matrices|Ch 7.8]] — the contiguous-vs-array-of-arrays split, row-major layout, and two-stage dereferencing discipline are structurally identical; pointer width narrows from 8 bytes to 4 bytes (with the side-effect that pointer-stride and int-stride coincide at IA32 width).
