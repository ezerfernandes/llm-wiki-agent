---
title: "Dive into Systems — Ch 9.8 Matrices in Assembly (ARM64)"
type: source
tags: [book, dive-into-systems, arm64, armv8, assembly, matrices, multidimensional-array]
date: 2026-05-17
source_file: https://diveintosystems.org/book/C9-ARM64/matrices.html
sources: []
last_updated: 2026-05-17
---

## Summary

**Eighth leaf** of Ch 9 *64-bit ARM Assembly* of *[[DiveIntoSystems]]* — **non-twin structural sibling** of [[dis-7-8-x86-64-matrices|Ch 7.8]] / [[dis-8-8-ia32-matrices|Ch 8.8]]. Extends [[dis-9-7-arm64-arrays|Ch 9.7]]'s 1-D [[CArray|array]]-compilation pattern to 2-D [[MultidimensionalArray|matrices]] at the [[ARM64|AArch64]] [[AssemblyLanguage|assembly]] surface. Walks both [[CLanguage|C]] [[MultidimensionalArray|2-D-array]] layouts: **contiguous** (statically declared `int M1[4][3]` or single-`malloc` `int *M` — all rows contiguous in [[RowMajorOrder|row-major order]]) where element `M[i][j]` collapses to a **single linear offset** `(i*cols + j) * sizeof(T)` using the [[ARM64AddressingMode|fourth addressing-mode form]] with `LSL, #2`; and **[[ArrayOfArrays|noncontiguous array-of-arrays]]** (`int **M3`) requiring a **two-stage pointer chase**: scale-8 multiply + `ldr` to fetch row pointer, then scale-4 multiply + `ldr` for the element. **No new concept pages** — reuses [[MultidimensionalArray]] / [[RowMajorOrder]] / [[ArrayOfArrays]] / [[AsmArrayAccess]] / [[ScaledIndexAddressing]] / [[ARM64AddressingMode]].

## Key Claims

- **Row-major layout — contiguous matrices.** *"For some matrix called `matrix`, `matrix+i*cols` is equivalent to `&matrix[i]`"* — statically allocated matrices store all rows contiguously in memory, enabling predictable address calculations using the formula `M + i*cols + j`. Same [[RowMajorOrder|row-major]] invariant as [[dis-7-8-x86-64-matrices|Ch 7.8]] / [[dis-8-8-ia32-matrices|Ch 8.8]] — layout is [[CLanguage|C]]-language-level, not ISA-dependent.
- **2-D indexing formula reduces to a single linear offset.** Element access requires computing `(cols * i + j) * element_size` to determine the byte offset from the base address — one [[ARM64Cmp|multiply]] / [[ARM64ShiftInstructions|shift]] + one [[ARM64ArithmeticInstructions|add]] + one [[ARM64DataMovement|`ldr`]]. The [[ARM64AddressingMode|`[xN, xM, LSL, #2]`]] scaled-index form absorbs the `* 4` scaling into the load itself.
- **Pointer arithmetic differs by layout — noncontiguous matrices.** *"Each pointer contains the address of a separate contiguous array, which corresponds to a separate row in the matrix"* — [[ArrayOfArrays|array-of-arrays]] (`int **`) requires **two dereference operations**: first to retrieve the row pointer (scale-8 multiply since pointers are 64-bit on [[ARM64]] — `LSL, #3`), then to access the element inside the row (scale-4 multiply — `LSL, #2`).
- **Size-based scaling — `LSL, #2` vs `LSL, #3`.** The compiler automatically scales indices by data type size: multiplying row indices by **8** for pointer arrays (64-bit pointers — `LSL, #3`) and by **4** for integer arrays (32-bit `int` — `LSL, #2`). Same source-level layout choice (contiguous vs array-of-arrays) is **observable at the [[ARM64]] assembly surface** — contiguous = one memory load per element; noncontiguous = two memory loads + worse cache behavior.
- **Nested loop structure carries over from [[dis-9-4-3-arm64-loops|Ch 9.4.3]].** Assembly implements matrix traversal with outer loops controlling row iteration and inner loops handling column access — standard `cmp` + [[ARM64ConditionalBranch|`b.cond`]] backward-branching shape, applied twice. No new control-flow primitives.
- **Register allocation — `w` for values, `x` for addresses.** Local variables on the stack frame; `w` registers used for 32-bit `int` operations, `x` registers for 64-bit address calculations — same register-width discipline as [[dis-9-7-arm64-arrays|Ch 9.7]].

## Key Quotes

> "For some matrix called `matrix`, `matrix+i*cols` is equivalent to `&matrix[i]`." — the [[RowMajorOrder|row-major]] linear-offset identity for contiguous matrices.

> "Each pointer contains the address of a separate contiguous array, which corresponds to a separate row in the matrix." — the [[ArrayOfArrays|array-of-arrays]] layout structure that forces two-stage dereference.

## Connections

- [[DiveIntoSystems]] — parent textbook; this is the **101st ingested chapter** / **eighth leaf of Ch 9**.
- [[dis-9-7-arm64-arrays]] — immediate predecessor; the 1-D base case Ch 9.8 extends to 2-D. Same [[ARM64AddressingMode|`[xN, xM, LSL, #s]`]] scaled-index form, two-axis composition.
- [[dis-9-4-3-arm64-loops]] — supplied the [[ARM64ConditionalBranch|`b.cond`]] backward-branch loop pattern used twice (nested) for matrix traversal.
- [[dis-7-8-x86-64-matrices]] / [[dis-8-8-ia32-matrices]] — structural siblings; same [[RowMajorOrder|row-major]] layout and contiguous-vs-array-of-arrays split, different scale-encoding surface.
- [[MultidimensionalArray]] / [[RowMajorOrder]] / [[ArrayOfArrays]] / [[AsmArrayAccess]] / [[ScaledIndexAddressing]] — reused concept pages.
- [[dis-2-5-arrays]] — original [[CLanguage|C]]-level distinction between contiguous and array-of-arrays layouts; Ch 9.8 makes it observable at the assembly surface.

## Contradictions

None. Ch 9.8 **extends** the 1-D array-access pattern to 2-D — adds composition rather than revises. The [[RowMajorOrder|row-major]] layout is a [[CLanguage|C]]-language invariant unchanged by ISA.
